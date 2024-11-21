import tkinter as tk
from tkinter import ttk

# Crear la ventana principal
window = tk.Tk()
window.title("Conversor de Monedas")  # Título de la ventana
window.geometry("400x200")  # Tamaño de la ventana (ancho x alto)

# Función para realizar la conversión
def convertir_moneda():
    try:
        # Obtener valores de las entradas de texto
        trm = float(trm_entry.get())  # Tasa representativa de mercado
        colombianos = float(cop_entry.get())  # Monto en pesos colombianos

        # Realizar la conversión
        resultado = colombianos / trm

        # Mostrar el resultado en la entrada de texto "resultado_entry"
        resultado_entry.delete(0, tk.END)
        resultado_entry.insert(0, f"{resultado:.2f}")  # Formato con dos decimales
    except ValueError:
        resultado_entry.delete(0, tk.END)
        resultado_entry.insert(0, "Error")  # Si ocurre un error (como dejar campos vacíos)

# Crear un contenedor para organizar los elementos
frame = ttk.Frame(window, padding=10)
frame.grid(row=0, column=0, sticky="NSEW")

# Etiqueta y entrada para la TRM (Tasa Representativa de Mercado)
ttk.Label(frame, text="Tasa Representativa").grid(row=0, column=0, padx=5, pady=5, sticky="W")
trm_entry = ttk.Entry(frame, width=20)
trm_entry.grid(row=0, column=1, padx=5, pady=5)

# Etiqueta y entrada para el monto en pesos colombianos
ttk.Label(frame, text="$ Colombianos").grid(row=1, column=0, padx=5, pady=5, sticky="W")
cop_entry = ttk.Entry(frame, width=20)
cop_entry.grid(row=1, column=1, padx=5, pady=5)

# Menú desplegable para elegir la moneda (opcional)
ttk.Label(frame, text="Elija la Moneda").grid(row=2, column=0, padx=5, pady=5, sticky="W")
moneda_combobox = ttk.Combobox(frame, values=["Dólar", "Euro", "Libra Esterlina"])
moneda_combobox.grid(row=2, column=1, padx=5, pady=5)
moneda_combobox.current(0)  # Selección inicial

# Etiqueta y entrada para el resultado de la conversión
ttk.Label(frame, text="Resultado:").grid(row=3, column=0, padx=5, pady=5, sticky="W")
resultado_entry = ttk.Entry(frame, width=20)
resultado_entry.grid(row=3, column=1, padx=5, pady=5)

# Botón para realizar la conversión
convertir_button = ttk.Button(frame, text="Convertir", command=convertir_moneda)
convertir_button.grid(row=4, column=0, columnspan=2, pady=10)

# Ejecutar la ventana principal
window.mainloop()
