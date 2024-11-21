import tkinter as tk
from tkinter import messagebox  # Para mostrar mensajes emergentes

# Función para verificar la respuesta seleccionada
def verificar_respuesta():
    respuesta = seleccion.get()  # Obtiene la respuesta seleccionada
    if respuesta == "Pirámides de Egipto":
        messagebox.showinfo("Información", "¡Correcto!")  # Mensaje emergente de correcto
    else:
        messagebox.showerror("Información", "Incorrecto.")  # Mensaje emergente de incorrecto

# Ventana principal
window = tk.Tk()
window.title("Trivia")
window.geometry("400x300")  # Tamaño de la ventana

# Imagen
from PIL import Image, ImageTk  # Para manejar imágenes
imagen = Image.open("piramides.jpg")  # Reemplazar con la ruta de la imagen
imagen = imagen.resize((150, 100), Image.Resampling.LANCZOS)  # Ajustar tamaño
imagen_tk = ImageTk.PhotoImage(imagen)

label_imagen = tk.Label(window, image=imagen_tk)
label_imagen.pack(pady=10)

# Pregunta
pregunta = tk.Label(window, text="Una de las 7 maravillas del mundo antiguo:", font=("Arial", 12))
pregunta.pack(pady=10)

# Opciones
seleccion = tk.StringVar(value="")  # Variable para almacenar la opción seleccionada

opcion1 = tk.Radiobutton(window, text="Pirámides de Egipto", variable=seleccion, value="Pirámides de Egipto", font=("Arial", 10))
opcion1.pack(anchor="w")

opcion2 = tk.Radiobutton(window, text="Torre Eiffel", variable=seleccion, value="Torre Eiffel", font=("Arial", 10))
opcion2.pack(anchor="w")

opcion3 = tk.Radiobutton(window, text="caño cristales", variable=seleccion, value="caño cristales", font=("Arial", 10))
opcion3.pack(anchor="w")

# Botón para verificar
boton_verificar = tk.Button(window, text="Verificar", command=verificar_respuesta)
boton_verificar.pack(pady=20)

# Iniciar la aplicación
window.mainloop()
