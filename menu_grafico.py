from tkinter import *
from tkinter import messagebox
from coches import Coches
from coche import Coche

# Crear la ventana principal
ventana = Tk()
ventana.title("Gestión de Coches")
ventana.geometry("500x300")
ventana.resizable(False, False)
ventana.config(bg="pink1")

# Cargar el icono de los botones
icono_agregar = PhotoImage(file="icono_agregar.png").subsample(20, 20)
icono_mostrar = PhotoImage(file="icono_mostrar.png").subsample(20, 20)
icono_eliminar = PhotoImage(file="icono_eliminar.png").subsample(20, 20)
icono_buscar = PhotoImage(file="icono_buscar.png").subsample(20, 20)

# Crear una instancia de la clase Coches
gestor_coches = Coches()

# Función para añadir un coche
def agregar_coche():
    matricula = entrada_matricula.get()
    marca = entrada_marca.get()
    modelo = entrada_modelo.get()
    color = entrada_color.get()

    if not matricula or not marca or not modelo or not color:
        messagebox.showerror("Error", "Por favor, completa todos los campos.")
        return
    else:
        nuevo_coche = Coche(matricula, marca, modelo, color)
        gestor_coches.agregar_coche(nuevo_coche)
        messagebox.showinfo("Éxito", f'Coche {matricula} añadido correctamente.')
        entrada_matricula.delete(0, END)
        entrada_marca.delete(0, END)
        entrada_modelo.delete(0, END)
        entrada_color.delete(0, END)

# Función para mostrar coches
def mostrar_coches():
    lista_coches = gestor_coches.lista_coches
    if not lista_coches:
        messagebox.showinfo("Información", "No hay coches registrados.")
    else:
        ventana_mostrar = Toplevel(ventana)  # Nueva ventana
        ventana_mostrar.title("Lista de Coches")
        text_area = Text(ventana_mostrar, wrap=WORD, width=40, height=10, font=("Courier New", 10))
        text_area.pack(padx=10, pady=10)
        for coche in lista_coches:
            text_area.insert(END, f"Matrícula: {coche.matricula}, Marca: {coche.marca}, Modelo: {coche.modelo}, Color: {coche.color}\n")
        text_area.configure(state='disabled') # Hace el Text de solo lectura

# Función para eliminar un coche con confirmación
def eliminar_coche():
    matricula = entrada_matricula.get()
    if not matricula:
        messagebox.showerror("Error", "Por favor, ingresa la matrícula del coche a eliminar.")
        return

    coche = gestor_coches.buscar_coche(matricula)
    if coche:
        # Confirmar la eliminación
        confirmar = messagebox.askyesno("Confirmar eliminación", f"¿Estás seguro de que deseas eliminar el coche con matrícula {matricula}?")
        if confirmar:
            gestor_coches.eliminar_coche(matricula)
            messagebox.showinfo("Éxito", f"Coche con matrícula {matricula} eliminado correctamente.")
            entrada_matricula.delete(0, END)
        else:
            messagebox.showinfo("Cancelado", "La eliminación del coche ha sido cancelada.")
    else:
        messagebox.showerror("Error", f"No se encontró un coche con matrícula {matricula}.")

# Función para buscar un coche por matrícula
def buscar_coche():
    matricula = entrada_matricula.get()
    if not matricula:
        messagebox.showerror("Error", "Por favor, ingresa la matrícula del coche a buscar.")
        return

    coche = gestor_coches.buscar_coche(matricula)
    if coche:
        messagebox.showinfo("Coche Encontrado", f"Matrícula: {coche.matricula}\nMarca: {coche.marca}\nModelo: {coche.modelo}\nColor: {coche.color}")
    else:
        messagebox.showerror("Error", f"No se encontró un coche con matrícula {matricula}.")


# Botones y etiquetas
boton_agregar = Button(ventana, image=icono_agregar, command=agregar_coche, borderwidth=5)
boton_agregar.grid(row=0, column=0, pady=(10, 0), padx=15)
Label(ventana, text="Agregar Coche", font=("Arial", 10), bg="pink1").grid(row=1, column=0, pady=(10, 0))

boton_mostrar = Button(ventana, image=icono_mostrar, command=mostrar_coches, borderwidth=5)
boton_mostrar.grid(row=0, column=1, pady=(10, 0), padx=15)
Label(ventana, text="Mostrar Coches", font=("Arial", 10), bg="pink1").grid(row=1, column=1, pady=(10, 0))

boton_eliminar = Button(ventana, image=icono_eliminar, command=eliminar_coche, borderwidth=5)
boton_eliminar.grid(row=0, column=2, pady=(10, 0), padx=15)
Label(ventana, text="Eliminar Coche", font=("Arial", 10), bg="pink1").grid(row=1, column=2, pady=(10, 0))

boton_buscar = Button(ventana, image=icono_buscar, command=buscar_coche, borderwidth=5)
boton_buscar.grid(row=0, column=3, pady=(10, 0), padx=15)
Label(ventana, text="Buscar Coche", font=("Arial", 10), bg="pink1").grid(row=1, column=3, pady=(10, 0))


# Etiquetas y campos de entrada
Label(ventana, text="Matrícula:", font=("Arial", 12), bg="pink1").grid(row=2, column=0, padx=10, pady=5, sticky="e")
entrada_matricula = Entry(ventana, font=("Arial", 12))
entrada_matricula.grid(row=2, column=1, padx=10, pady=5)

Label(ventana, text="Marca:", font=("Arial", 12), bg="pink1").grid(row=3, column=0, padx=10, pady=5, sticky="e")
entrada_marca = Entry(ventana, font=("Arial", 12))
entrada_marca.grid(row=3, column=1, padx=10, pady=5)

Label(ventana, text="Modelo:", font=("Arial", 12), bg="pink1").grid(row=4, column=0, padx=10, pady=5, sticky="e")
entrada_modelo = Entry(ventana, font=("Arial", 12))
entrada_modelo.grid(row=4, column=1, padx=10, pady=5)

Label(ventana, text="Color:", font=("Arial", 12), bg="pink1").grid(row=5, column=0, padx=10, pady=5, sticky="e")
entrada_color = Entry(ventana, font=("Arial", 12))
entrada_color.grid(row=5, column=1, padx=10, pady=5)


# Iniciar el bucle principal de la ventana
ventana.mainloop()