from tkinter import *
from tkinter import ttk

#Definir ventana
ventana = Tk()
ventana.title('Proyecto Tkinter | Master en Python')
#ventana.geometry("500x500")
ventana.minsize(500, 500)
ventana.resizable(0,0)

#Pantallas
def home():
    home_label.config(
        fg="white",
        bg="black",
        font=('Arial', 30),
        padx=210,
        pady=20
    )
    home_label.grid(row=0, column=0)
    products_box.grid(row=2)
    
    #Listar Productos
    '''
    for product in products:
        if len(product) == 3:
            product.append("added")
            Label(products_box, text=product[0]).grid()
            Label(products_box, text=product[1]).grid()
            Label(products_box, text=product[2]).grid()
            Label(products_box, text="------------").grid()'''
            
    for product in products:
            if len(product) == 3:
                products.remove(product)
                products_box.insert("", 0, text=product[0], values = (product[1]))
               
    add_label.grid_remove()
    add_frame.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()
    
    return True

def add():
    add_label.config(
        fg="white",
        bg="black",
        font=('Arial', 30),
        padx=100,
        pady=20
    )
    add_label.grid(row=0, column=0, columnspan=19)
    
    #campos del formulario
    add_frame.grid(row=1)
    add_name_label.grid(row=1, column=0, padx=5, pady=5, sticky=E)
    add_name_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)
    
    add_price_label.grid(row=2, column=0, padx=5, pady=5, sticky=E)
    add_price_entry.grid(row=2, column=1, padx=5, pady=5, sticky=W)
    
    add_descripcion_label.grid(row=3, column=0, padx=5, pady=5, sticky=NW)
    add_descripcion_entry.grid(row=3, column=1, padx=5, pady=5, sticky=W)
    add_descripcion_entry.config(
        width=20,
        height=3,
        font=("Consolas", 12),
        padx=15,
        pady=15
    )
    
    add_separador.grid(row=4)
    
    boton.grid(row=5, column=1, sticky=E)
    boton.config(
        pady=5,
        padx=15,
        fg="white",
        bg="green",
        font=('Arial', 10)
    )
    
    home_label.grid_remove()
    products_box.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()
    
    return True

def info():
    info_label.config(
        fg="white",
        bg="black",
        font=('Arial', 30),
        padx=150,
        pady=20
    )
    info_label.grid(row=0, column=0)
    
    add_label.grid_remove()
    products_box.grid_remove()
    add_frame.grid_remove()
    home_label.grid_remove()
    data_label.grid_remove()
    
    return True

def add_product():
    products.append([
        name_data.get(),
        price_data.get(),
        add_descripcion_entry.get("1.0", "end-1c")
    ])
    
    name_data.set("")
    price_data.set("")
    add_descripcion_entry.delete("1.0", END)
    
    home()
    
    print(products)

#variables
products = []
name_data = StringVar()
price_data = StringVar()
    
data_label = Label(ventana, text="Creado por Orlin Diaz")
data_label.grid(row=1, column=0)

#Definir campos de pantallas(INICIO)
home_label = Label(ventana, text="Inicio")
#products_box = Frame(ventana, width=250)

#Label(products_box).grid(row=0)
Label(ventana).grid(row=1)
products_box = ttk.Treeview(height=12, columns=2)
products_box.grid(row=1, column=0, columnspan=2)
products_box.heading("#0", text="Producto", anchor=W)
products_box.heading("#1", text="Precio", anchor=W)

#Definir campos de pantallas(AGREGAR)
add_label = Label(ventana, text="Agregar Producto")

#Definir campos de pantallas(INFORMACION)
info_label = Label(ventana, text="Informacion")

#Campos del formulario
add_frame = Frame(ventana)

add_name_label = Label(add_frame, text="Nombre: ")
add_name_entry = Entry(add_frame, textvariable=name_data)

add_price_label = Label(add_frame, text="Precio: ")
add_price_entry = Entry(add_frame, textvariable=price_data)

add_descripcion_label = Label(add_frame, text="Descripcion: ")
add_descripcion_entry = Text(add_frame)

add_separador = Label(add_frame)

boton = Button(add_frame, text="Guardar", command=add_product)

#Llamar la funcion
home()

#Menu superior
menu_superior = Menu(ventana)
menu_superior.add_command(label="Inicio", command=home)
menu_superior.add_command(label="Agregar", command=add)
menu_superior.add_command(label="Informacion", command=info)
menu_superior.add_command(label="Salir", command=ventana.quit)

#Cargar menu
ventana.config(menu=menu_superior)

#Cargar ventana
ventana.mainloop()