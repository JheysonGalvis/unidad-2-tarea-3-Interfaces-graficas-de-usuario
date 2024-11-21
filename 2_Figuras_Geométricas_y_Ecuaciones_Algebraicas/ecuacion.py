import tkinter as tk
from tkinter import ttk

# Crear ventana principal
window = tk.Tk()
window.title("Cálculo de Ecuación")
window.geometry("300x200")  # Tamaño de la ventana

# Función para calcular Z
def calcular_z():
    try:
        # Obtener valores de X y Y desde los Spinboxes
        x = int(spin_x.get())
        y = int(spin_y.get())
        
        # Calcular Z = ((2X + 3Y)^2) / 5
        z = ((2 * x + 3 * y) ** 2) / 5
        
        # Mostrar el resultado en el campo de texto
        resultado_z.config(state="normal")  # Habilitar edición temporal
        resultado_z.delete(0, tk.END)      # Borrar el contenido actual
        resultado_z.insert(0, f"{z:.2f}")  # Insertar el resultado formateado
        resultado_z.config(state="readonly")  # Volver a ponerlo como solo lectura
    except ValueError:
        resultado_z.config(state="normal")
        resultado_z.delete(0, tk.END)
        resultado_z.insert(0, "Error")
        resultado_z.config(state="readonly")

# Crear un marco para la sección de la ecuación
frame = ttk.LabelFrame(window, text="Ecuación")
frame.pack(padx=10, pady=10, fill="both", expand=True)

# Crear etiquetas y Spinboxes para X e Y
label_x = ttk.Label(frame, text="X=")
label_x.grid(row=0, column=0, padx=5, pady=5, sticky="w")
spin_x = ttk.Spinbox(frame, from_=0, to=100, width=5)
spin_x.grid(row=0, column=1, padx=5, pady=5)

label_y = ttk.Label(frame, text="Y=")
label_y.grid(row=1, column=0, padx=5, pady=5, sticky="w")
spin_y = ttk.Spinbox(frame, from_=0, to=100, width=5)
spin_y.grid(row=1, column=1, padx=5, pady=5)

# Mostrar la ecuación
label_ecuacion = ttk.Label(frame, text="Z = (2X + 3Y)^2 / 5")
label_ecuacion.grid(row=2, column=0, columnspan=2, pady=5)

# Crear el campo para mostrar Z (resultado)
label_z = ttk.Label(frame, text="Z=")
label_z.grid(row=3, column=0, padx=5, pady=5, sticky="w")
resultado_z = ttk.Entry(frame, width=10, state="readonly")  # Campo solo lectura
resultado_z.grid(row=3, column=1, padx=5, pady=5)

# Botón para calcular Z
boton_calcular = ttk.Button(frame, text="Calcular", command=calcular_z)
boton_calcular.grid(row=4, column=0, columnspan=2, pady=10)

# Iniciar el bucle principal de la aplicación
window.mainloop()
