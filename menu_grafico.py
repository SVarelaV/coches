from tkinter import *
from tkinter import messagebox
from coches import Coches
from coche import Coche

# Crear la ventana principal
ventana = Tk()
ventana.title("Gestión de Coches")
ventana.geometry("400x300")
ventana.config(bg="pink1")

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

# Función para mostrar lista de coches
def mostrar_coches():
    lista_coches = gestor_coches.lista_coches
    if not lista_coches:
        messagebox.showinfo("Lista de Coches", "No hay coches registrados.")
    else:
        print("Lista de Coches:")
        for coche in lista_coches:
            print(f"Matrícula: {coche.matricula}, Marca: {coche.marca}, Modelo: {coche.modelo}, Color: {coche.color}")

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


# Cargar el icono de los botones
icono_agregar = PhotoImage(file="iconos/icono_agregar.png").subsample(20, 20)
icono_mostrar = PhotoImage(file="iconos/icono_mostrar.png").subsample(20, 20)
icono_eliminar = PhotoImage(file="iconos/icono_eliminar.png").subsample(20, 20)
icono_buscar = PhotoImage(file="iconos/icono_buscar.png").subsample(20, 20)


# Frame para agrupar los botones
frame_botones = Frame(ventana, bg="pink1")
frame_botones.grid(row=0, column=0, columnspan=4, pady=(10, 20))

# Botón Agregar
frame_agregar = Frame(frame_botones, bg="pink1")
Label(frame_agregar, text="Agregar Coche", font=("Arial", 10), bg="pink1").pack()
boton_agregar = Button(frame_agregar, image=icono_agregar, command=agregar_coche, borderwidth=1)
boton_agregar.pack()
frame_agregar.pack(side=LEFT, expand=True, padx=10)

# Botón Mostrar
frame_mostrar = Frame(frame_botones, bg="pink1")
Label(frame_mostrar, text="Mostrar Coches", font=("Arial", 10), bg="pink1").pack()
boton_mostrar = Button(frame_mostrar, image=icono_mostrar, command=mostrar_coches, borderwidth=1)
boton_mostrar.pack()
frame_mostrar.pack(side=LEFT, expand=True, padx=10)

# Botón Eliminar
frame_eliminar = Frame(frame_botones, bg="pink1")
Label(frame_eliminar, text="Eliminar Coche", font=("Arial", 10), bg="pink1").pack()
boton_eliminar = Button(frame_eliminar, image=icono_eliminar, command=eliminar_coche, borderwidth=1)
boton_eliminar.pack()
frame_eliminar.pack(side=LEFT, expand=True, padx=10) 

# Botón Buscar
frame_buscar = Frame(frame_botones, bg="pink1")
Label(frame_buscar, text="Buscar Coche", font=("Arial", 10), bg="pink1").pack()
boton_buscar = Button(frame_buscar, image=icono_buscar, command=buscar_coche, borderwidth=1)
boton_buscar.pack()
frame_buscar.pack(side=LEFT, expand=True, padx=10)

# Frame para agrupar las etiquetas y campos de entrada
frame_campos = Frame(ventana, bg="pink1")
frame_campos.grid(row=1, column=0, columnspan=4, pady=(10, 0))

# Etiquetas y campos de entrada dentro del nuevo Frame
Label(frame_campos, text="Matrícula:", font=("Arial", 15), bg="pink1").grid(row=0, column=0, padx=10, pady=5, sticky="e")
entrada_matricula = Entry(frame_campos, font=("Arial", 15))
entrada_matricula.grid(row=0, column=1, padx=10, pady=5)

Label(frame_campos, text="Marca:", font=("Arial", 15), bg="pink1").grid(row=1, column=0, padx=10, pady=5, sticky="e")
entrada_marca = Entry(frame_campos, font=("Arial", 15))
entrada_marca.grid(row=1, column=1, padx=10, pady=5)

Label(frame_campos, text="Modelo:", font=("Arial", 15), bg="pink1").grid(row=2, column=0, padx=10, pady=5, sticky="e")
entrada_modelo = Entry(frame_campos, font=("Arial", 15))
entrada_modelo.grid(row=2, column=1, padx=10, pady=5)

Label(frame_campos, text="Color:", font=("Arial", 15), bg="pink1").grid(row=3, column=0, padx=10, pady=5, sticky="e")
entrada_color = Entry(frame_campos, font=("Arial", 15))
entrada_color.grid(row=3, column=1, padx=10, pady=5)


# Iniciar el bucle principal de la ventana
ventana.mainloop()