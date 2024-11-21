import tkinter as tk
from tkinter import ttk

# Crear ventana principal
window = tk.Tk()
window.title("Conversor de Temperatura")
window.geometry("400x200")  # Tamaño de la ventana

# Función para convertir temperaturas
def convertir_temperatura(value):
    try:
        # Obtener el valor actual del slider (Celsius)
        celsius = float(value)

        # Convertir a Fahrenheit y Kelvin
        fahrenheit = (celsius * 9/5) + 32
        kelvin = celsius + 273.15

        # Mostrar resultados en las entradas de texto
        fahrenheit_entry.delete(0, tk.END)
        fahrenheit_entry.insert(0, f"{fahrenheit:.2f}")

        kelvin_entry.delete(0, tk.END)
        kelvin_entry.insert(0, f"{kelvin:.2f}")
    except ValueError:
        pass  # Manejo básico de errores por si ocurre un problema

# Crear un contenedor (Frame) para organizar los widgets
frame = ttk.Frame(window, padding=10)
frame.grid(row=0, column=0, sticky="NSEW")

# Etiqueta del slider
slider_label = ttk.Label(frame, text="Celsius")
slider_label.grid(row=0, column=0, padx=10, pady=5)

# Slider para Celsius
celsius_slider = ttk.Scale(
    frame, from_=-100, to=100, orient="vertical", command=convertir_temperatura
)
celsius_slider.set(0)  # Valor inicial del slider
celsius_slider.grid(row=1, column=0, padx=10)

# Entrada para Fahrenheit
fahrenheit_label = ttk.Label(frame, text="Fahrenheit")
fahrenheit_label.grid(row=0, column=1, padx=10)

fahrenheit_entry = ttk.Entry(frame, width=10)
fahrenheit_entry.grid(row=1, column=1, padx=10)

# Entrada para Kelvin
kelvin_label = ttk.Label(frame, text="Kelvin")
kelvin_label.grid(row=0, column=2, padx=10)

kelvin_entry = ttk.Entry(frame, width=10)
kelvin_entry.grid(row=1, column=2, padx=10)

# Iniciar el bucle principal de la ventana
window.mainloop()
