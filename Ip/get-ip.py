import socket as sc
import tkinter as tk


# ip
hostname = sc.gethostname()
ip = sc.gethostbyname(hostname)

# tkinter
ventana = tk.Tk()
ventana.geometry("400x400")


label1 = tk.Label(ventana, text=ip)
label2 = tk.Label(ventana, text=hostname + ":")

label2.pack()
label1.pack()

ventana.mainloop()
