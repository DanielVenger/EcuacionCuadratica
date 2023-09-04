#AVILA MEJIA DANIEL SAID 5CV4
"""ESTE PROGRAMA GENERA LA SOLUCIONES DE UNA ECUACION DE SEGUNDO GRADO 
ASI COMO LA GRAFICA Y OBTENCION DE RESULTADOS, TODO CON UNA SENCIILA INTERFAZ GRAFICA """

import math
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import Entry, Label, Button, messagebox, Toplevel

def resolver(a, b, c):
    # Primero igualamos a cero los valores no ingresados
    if a is None:
        a = 0
    if b is None:
        b = 0
    if c is None:
        c = 0

    # Hacemos la verificacion algrebraica
    if a == 0:
        if b == 0:
            if c == 0:
                return "La ecuación tiene infinitas soluciones"
            else:
                return "La ecuación no tiene solución"
        else:
            x = -c / b
            return f"La solución de la ecuación lineal es x = {x}"
    else:
        discriminante = b**2 - 4 * a * c
        if discriminante > 0:
            x1 = (-b + math.sqrt(discriminante)) / (2 * a)
            x2 = (-b - math.sqrt(discriminante)) / (2 * a)
            return f"Las soluciones son x1 = {x1} y x2 = {x2}", discriminante
        elif discriminante == 0:
            x = -b / (2 * a)
            return f"La única solución x = {x}", discriminante
        else:
            return "La ecuación no tiene soluciones reales", discriminante

def graficar(a, b, c):
    # Aqui se crea el grafico de la ecuacion generada
    discriminante = resolver(a, b, c)[1]
    if discriminante >= 0:
        x = np.linspace(-10, 10, 400)
        y = a * x**2 + b * x + c

        plt.figure(figsize=(8, 6))
        plt.plot(x, y, label=f'{a}x^2 + {b}x + {c} = 0')
        plt.axhline(0, color='black', linewidth=0.5)
        plt.axvline(0, color='black', linewidth=0.5)
        plt.grid(color='gray', linestyle='--', linewidth=0.5)
        plt.legend()
        plt.title("Gráfico de la ecuación cuadrática")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.show()

def flotante(valor):
    try:
        return float(valor)
    except ValueError:
        return None

def calcgraf():
    a = flotante(a_entry.get())
    b = flotante(b_entry.get())
    c = flotante(c_entry.get())

    if a is None or b is None or c is None:
        messagebox.showerror("Error", "Ingrese valores numéricos válidos para a, b y c")
        return

    solucion, discriminante = resolver(a, b, c)
    resultado(solucion, discriminante)

def resultado(solucion, discriminante):
    # Crear una ventana emergente para mostrar los resultados y el gráfico
    ventana_resultados = Toplevel(ventana)
    ventana_resultados.title("Resultados")

    # Mostrar los valores de x y el gráfico
    label_x = Label(ventana_resultados, text="Resultados:")
    label_x.pack()

    resultado_label = Label(ventana_resultados, text=solucion)
    resultado_label.pack()

    if discriminante >= 0:
        graficar(float(a_entry.get()), float(b_entry.get()), float(c_entry.get()))

# Crear la ventana principal de la interfaz gráfica
ventana = tk.Tk()
ventana.title("Calculadora de Ecuación Cuadrática")

# Crear etiquetas y campos de entrada
a_label = Label(ventana, text="Valor de a:")
a_label.pack()
a_entry = Entry(ventana)
a_entry.pack()

b_label = Label(ventana, text="Valor de b:")
b_label.pack()
b_entry = Entry(ventana)
b_entry.pack()

c_label = Label(ventana, text="Valor de c:")
c_label.pack()
c_entry = Entry(ventana)
c_entry.pack()

# Botón para calcular y graficar
calcular_button = Button(ventana, text="Calcular y Graficar", command=calcgraf)
calcular_button.pack()

# Iniciar la aplicación
ventana.mainloop()
