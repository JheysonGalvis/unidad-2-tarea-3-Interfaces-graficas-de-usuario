import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar #ojo debes instalar tkcalendar con pip

# Crear la ventana principal
window = tk.Tk()
window.title("Cálculo de Días Transcurridos")
window.geometry("400x300")

# Función para calcular los días entre dos fechas
def calcular_dias():
    # Obtener las fechas seleccionadas
    fecha_inicial = calendario_inicial.get_date()
    fecha_final = calendario_final.get_date()

    # Convertir las fechas a formato datetime
    from datetime import datetime
    f_inicial = datetime.strptime(fecha_inicial, "%d/%m/%Y")
    f_final = datetime.strptime(fecha_final, "%d/%m/%Y")

    # Calcular la diferencia en días
    dias = (f_final - f_inicial).days
    # Mostrar el resultado en el campo de entrada
    resultado_var.set(dias)

# Crear un contenedor para las fechas
frame_fechas = ttk.LabelFrame(window, text="Días Transcurridos", padding=10)
frame_fechas.pack(pady=10, padx=10, fill="x")

# Fecha inicial
ttk.Label(frame_fechas, text="F. Inicial").grid(row=0, column=0, padx=5, pady=5)
calendario_inicial = Calendar(frame_fechas, date_pattern="dd/mm/yyyy")
calendario_inicial.grid(row=1, column=0, padx=5)

# Fecha final
ttk.Label(frame_fechas, text="F. Final").grid(row=0, column=1, padx=5, pady=5)
calendario_final = Calendar(frame_fechas, date_pattern="dd/mm/yyyy")
calendario_final.grid(row=1, column=1, padx=5)

# Botón para calcular
boton_calcular = ttk.Button(window, text="Calcular Días", command=calcular_dias)
boton_calcular.pack(pady=10)

# Resultado
ttk.Label(window, text="Días Transcurridos").pack(pady=5)
resultado_var = tk.StringVar()
resultado_entry = ttk.Entry(window, textvariable=resultado_var, state="readonly", width=15)
resultado_entry.pack()

# Iniciar la ventana principal
window.mainloop()
