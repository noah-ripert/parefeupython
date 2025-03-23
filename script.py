import psutil
import os
import tkinter as tk
from tkinter import messagebox
from plyer import notification
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Fonctionnalités
def list_connections():
    connections = psutil.net_connections(kind='inet')
    return [(conn.pid, conn.laddr, conn.raddr, conn.status) for conn in connections]

def block_ip(ip):
    command = f"netsh advfirewall firewall add rule name=\"Block {ip}\" dir=in action=block remoteip={ip}"
    os.system(command)

def alert_user(message):
    notification.notify(title='Alerte Sécurité', message=message, timeout=10)

def send_email(subject, body):
    sender_email = "ton_email@gmail.com"
    receiver_email = "destinataire_email@example.com"
    password = "ton_mot_de_passe_email"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.close()
        print("Email envoyé avec succès!")
    except Exception as e:
        print(f"Erreur lors de l'envoi de l'email : {e}")

def check_blacklist():
    blacklist = ["192.168.1.100", "10.0.0.1"]
    connections = psutil.net_connections(kind='inet')
    for conn in connections:
        if conn.raddr and conn.raddr[0] in blacklist:
            print(f"Alerte : Connexion suspecte venant de {conn.raddr[0]}")
            block_ip(conn.raddr[0])
            alert_user(f"Connexion suspecte détectée et bloquée : {conn.raddr[0]}")
            send_email("Alerte Sécurité", f"Connexion suspecte venant de {conn.raddr[0]} bloquée.")

# Interface graphique
def update_connections():
    connections = list_connections()
    listbox.delete(0, tk.END)
    for conn in connections:
        listbox.insert(tk.END, f"{conn[1]} -> {conn[2]} ({conn[3]})")

def block_selected_ip():
    selected = listbox.get(tk.ACTIVE)
    if selected:
        ip = selected.split('->')[1].split()[0]
        block_ip(ip)
        messagebox.showinfo("Blocage", f"IP {ip} bloquée.")
        update_connections()

root = tk.Tk()
root.title("Pare-feu Personnel")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

listbox = tk.Listbox(frame, width=80, height=20)
listbox.pack()

button_update = tk.Button(frame, text="Mettre à jour les connexions", command=update_connections)
button_update.pack(pady=5)

button_block = tk.Button(frame, text="Bloquer l'IP sélectionnée", command=block_selected_ip)
button_block.pack(pady=5)

root.mainloop()
