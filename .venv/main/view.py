import tkinter as tk
from 0 g[import USB
from tkinter import messagebox
from PIL import Image, ImageTk

usb = USB()
connectieon = False
data = []

def show_voltage():
    print("Puerto: " + usb.getCOM())
    data = usb.sendData(usb.getCOM())
    if "Conexion Primero" in data:
        messagebox.showinfo("Error", data)
    else:
        label_vol.config(text="Tensión Registrada de: " + data + "v")

def show_message():
    global connection
    if not connection:
        COM = usb.find_port()
        if "COM" in COM:
            connection = True
            label_text.config(text="Conectado a " + COM)
            messagebox.showinfo("Exitosa", "OK")
        else:
            label_text.config(text=COM)
    else:
        messagebox.showinfo("Error", "La conexión ya fue establecida.")

root = tk.Tk()
root.title("UART Message")

for i in range(20):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

image = Image.open(r"image\img.png")
photo = ImageTk.PhotoImage(image)
# label_image = tk.Label(root, image=photo)
# label_image.image = photo
# label_image.grid(row=0, column=0, columnspan=2, padx=1, pady=1, sticky="nsew")

label_text = tk.Label(root, text="Sin Conexión")
label_text.grid(row=1, column=0, columnspan=10, padx=20, pady=20, sticky="nsew")

label_vol = tk.Label(root, text="")
label_vol.grid(row=2, column=0, columnspan=10, padx=20, pady=20, sticky="nsew")

button_connect = tk.Button(root, text="Conectar", command=show_message)
button_connect.grid(row=3, column=0, columnspan=5, padx=20, pady=20, sticky="nsew")

button_voltage = tk.Button(root, text="Mostrar Tensión", command=show_voltage)
button_voltage.grid(row=3, column=6, columnspan=5, padx=20, pady=20, sticky="nsew")

root.mainloop()
