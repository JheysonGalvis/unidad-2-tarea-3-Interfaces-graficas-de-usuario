import tkinter as tk
from tkinter import ttk
from math import factorial  # Importar para calcular el factorial

# Crear ventana principal
window = tk.Tk()
window.title("Factorial y Conjuntos")
window.geometry("500x400")  # Ajustar el tamaño de la ventana

### Funcionalidad Factorial ###
def calcular_factorial():
    try:
        # Obtener número seleccionado del Combobox
        numero = int(combo_factorial.get())
        # Calcular el factorial
        resultado = factorial(numero)
        # Mostrar el resultado
        entrada_resultado_factorial.config(state="normal")
        entrada_resultado_factorial.delete(0, tk.END)
        entrada_resultado_factorial.insert(0, resultado)
        entrada_resultado_factorial.config(state="readonly")
    except ValueError:
        entrada_resultado_factorial.config(state="normal")
        entrada_resultado_factorial.delete(0, tk.END)
        entrada_resultado_factorial.insert(0, "Error")
        entrada_resultado_factorial.config(state="readonly")

### Funcionalidad Conjuntos ###
# Agregar elementos a los conjuntos
def agregar_a_conjunto(lista, entrada):
    elemento = entrada.get()
    if elemento:
        lista.insert(tk.END, elemento)
        entrada.delete(0, tk.END)

# Eliminar elementos seleccionados de los conjuntos
def eliminar_de_conjunto(lista):
    seleccionado = lista.curselection()
    if seleccionado:
        lista.delete(seleccionado)

# Calcular la unión o intersección
def calcular_conjuntos():
    # Obtener elementos de las listas
    conjunto_a = set(lista_a.get(0, tk.END))
    conjunto_b = set(lista_b.get(0, tk.END))

    # Verificar opción seleccionada
    if opcion_union.get():
        resultado = conjunto_a | conjunto_b  # Unión
    else:
        resultado = conjunto_a & conjunto_b  # Intersección

    # Mostrar el resultado
    lista_resultado.delete(0, tk.END)
    for item in resultado:
        lista_resultado.insert(tk.END, item)

### Interfaz de Factorial ###
frame_factorial = ttk.LabelFrame(window, text="Factorial")
frame_factorial.pack(padx=10, pady=10, fill="x")

# Combobox para seleccionar un número
ttk.Label(frame_factorial, text="Elija un Número").pack(anchor="w", padx=10, pady=5)
combo_factorial = ttk.Combobox(frame_factorial, values=list(range(1, 11)), state="readonly", width=10)
combo_factorial.pack(padx=10, pady=5)

# Botón para calcular el factorial
boton_calcular_factorial = ttk.Button(frame_factorial, text="Calcular", command=calcular_factorial)
boton_calcular_factorial.pack(pady=5)

# Entrada para mostrar el resultado
entrada_resultado_factorial = ttk.Entry(frame_factorial, state="readonly", width=20)
entrada_resultado_factorial.pack(padx=10, pady=5)

### Interfaz de Conjuntos ###
frame_conjuntos = ttk.LabelFrame(window, text="Conjuntos")
frame_conjuntos.pack(padx=10, pady=10, fill="both", expand=True)

# Conjunto A
frame_a = ttk.LabelFrame(frame_conjuntos, text="Conjunto A")
frame_a.grid(row=0, column=0, padx=5, pady=5)

entrada_a = ttk.Entry(frame_a, width=15)
entrada_a.pack(padx=5, pady=5)
ttk.Button(frame_a, text="Añadir", command=lambda: agregar_a_conjunto(lista_a, entrada_a)).pack(padx=5, pady=5)
ttk.Button(frame_a, text="Eliminar seleccionado", command=lambda: eliminar_de_conjunto(lista_a)).pack(padx=5, pady=5)

lista_a = tk.Listbox(frame_a, height=6)
lista_a.pack(padx=5, pady=5)

# Conjunto B
frame_b = ttk.LabelFrame(frame_conjuntos, text="Conjunto B")
frame_b.grid(row=0, column=1, padx=5, pady=5)

entrada_b = ttk.Entry(frame_b, width=15)
entrada_b.pack(padx=5, pady=5)
ttk.Button(frame_b, text="Añadir", command=lambda: agregar_a_conjunto(lista_b, entrada_b)).pack(padx=5, pady=5)
ttk.Button(frame_b, text="Eliminar seleccionado", command=lambda: eliminar_de_conjunto(lista_b)).pack(padx=5, pady=5)

lista_b = tk.Listbox(frame_b, height=6)
lista_b.pack(padx=5, pady=5)

# Opciones de operación
opciones_frame = ttk.Frame(frame_conjuntos)
opciones_frame.grid(row=1, column=0, columnspan=2, pady=10)

opcion_union = tk.BooleanVar(value=True)  # Valor por defecto es Unión
ttk.Radiobutton(opciones_frame, text="Unión", variable=opcion_union, value=True).pack(side="left", padx=10)
ttk.Radiobutton(opciones_frame, text="Intersección", variable=opcion_union, value=False).pack(side="left", padx=10)

# Resultado de la operación
lista_resultado = tk.Listbox(frame_conjuntos, height=6)
lista_resultado.grid(row=2, column=0, columnspan=2, pady=10)

ttk.Button(frame_conjuntos, text="Calcular", command=calcular_conjuntos).grid(row=3, column=0, columnspan=2, pady=10)

# Iniciar la aplicación
window.mainloop()
