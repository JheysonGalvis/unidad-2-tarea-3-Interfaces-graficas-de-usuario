import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Para manejar imágenes en Tkinter

# Función para verificar la respuesta
def verificar_respuesta():
    # Verifica si la opción seleccionada es "Sí"
    if opcion.get() == "Sí":
        messagebox.showinfo("Información", "Correcto.")  # Mensaje informativo
    else:
        messagebox.showerror("Información", "Incorrecto.")  # Mensaje de error

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Identificación de Pasiflora")  # Título de la ventana
ventana.geometry("400x300")  # Tamaño de la ventana

# Cargar la imagen
ruta_imagen = "pasiflora_flor_pasion.jpg"  # Cambia esto por la ruta de tu imagen
imagen_original = Image.open(ruta_imagen)
imagen_redimensionada = imagen_original.resize((150, 150))  # Ajustar tamaño de la imagen
imagen = ImageTk.PhotoImage(imagen_redimensionada)

# Crear un marco (frame) para organizar los widgets
frame = tk.Frame(ventana)
frame.pack(pady=10)

# Mostrar la imagen
label_imagen = tk.Label(frame, image=imagen)
label_imagen.pack()

# Pregunta
pregunta = tk.Label(frame, text="La imagen corresponde a una pasiflora:")
pregunta.pack(pady=5)

# Variables para opciones
opcion = tk.StringVar(value="")  # Variable para almacenar la respuesta

# Botones de opción (Radiobuttons)
radio_si = tk.Radiobutton(frame, text="Sí", variable=opcion, value="Sí")
radio_si.pack()
radio_no = tk.Radiobutton(frame, text="No", variable=opcion, value="No")
radio_no.pack()

# Botón para verificar la respuesta
boton_verificar = tk.Button(frame, text="Verificar", command=verificar_respuesta)
boton_verificar.pack(pady=10)

# Iniciar el bucle principal de la interfaz
ventana.mainloop()
