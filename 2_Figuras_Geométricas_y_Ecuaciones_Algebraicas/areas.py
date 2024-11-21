# Importamos la biblioteca tkinter para la interfaz
import tkinter as tk
from tkinter import ttk  # Para usar widgets más avanzados

# Función para calcular el área según la figura seleccionada
def calcular_area():
    figura = figura_seleccionada.get()  # Obtenemos la figura seleccionada
    try:
        if figura == "Círculo":
            radio = float(entry_radio.get())
            area = 3.1416 * (radio ** 2)
        elif figura == "Triángulo":
            base = float(entry_base.get())
            altura = float(entry_altura.get())
            area = (base * altura) / 2
        elif figura == "Cuadrado":
            lado = float(entry_lado.get())
            area = lado ** 2
        elif figura == "Rectángulo":
            base = float(entry_base.get())
            altura = float(entry_altura.get())
            area = base * altura
        else:
            area = "Figura no válida"
        # Mostramos el resultado
        resultado.set(f"El área es: {area:.2f}")
    except ValueError:
        resultado.set("Error: Verifica los datos ingresados")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Cálculo de Áreas")

# Variable para seleccionar la figura
figura_seleccionada = tk.StringVar(value="Círculo")

# Crear un frame para organizar los elementos
frame = ttk.Frame(ventana, padding=20)
frame.grid(row=0, column=0)

# Radio buttons para seleccionar la figura
ttk.Label(frame, text="Figuras:").grid(row=0, column=0, sticky="w")
figuras = ["Círculo", "Triángulo", "Cuadrado", "Rectángulo"]
for i, figura in enumerate(figuras):
    ttk.Radiobutton(frame, text=figura, value=figura, variable=figura_seleccionada).grid(row=i+1, column=0, sticky="w")

# Entradas para los datos
ttk.Label(frame, text="Radio:").grid(row=0, column=1, sticky="e")
entry_radio = ttk.Entry(frame, width=10)
entry_radio.grid(row=0, column=2)

ttk.Label(frame, text="Base:").grid(row=1, column=1, sticky="e")
entry_base = ttk.Entry(frame, width=10)
entry_base.grid(row=1, column=2)

ttk.Label(frame, text="Altura:").grid(row=2, column=1, sticky="e")
entry_altura = ttk.Entry(frame, width=10)
entry_altura.grid(row=2, column=2)

ttk.Label(frame, text="Lado:").grid(row=3, column=1, sticky="e")
entry_lado = ttk.Entry(frame, width=10)
entry_lado.grid(row=3, column=2)

# Variable para mostrar el resultado
resultado = tk.StringVar()
ttk.Label(frame, textvariable=resultado).grid(row=5, column=0, columnspan=3)

# Botón para calcular el área
ttk.Button(frame, text="Calcular", command=calcular_area).grid(row=4, column=0, columnspan=3)

# Ejecutar el bucle principal
ventana.mainloop()
