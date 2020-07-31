from classes.Producto import Producto
from classes.Salidas import salidas
from classes.Tasa import Tasa
from classes.Tag import tag
import os
import datetime
class Handler(object):
    #globales
    productos = list()
    salidas = list()
    tags = list()
    tasa = Tasa('1')
    codigos = []
    def __init__(self):
        self.getproductos()
        self.getsalidas()
        self.gettags()

    #Funcion para limpiar la pantalla dependiendo del sistema operativo
    def clear(self):
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

    #Funcion para listar todos los productos
    def listar(self):
        self.clear() #Limpio
        #Armo la tabla
        titles = "| {:<10} | {:<15} | {:<20} | {:<15} | {:<12} | {:<12}|".format("Codigo", "Nombre", "Descripcion", "tag", "Precio", "Cantidad")
        print("-"*len(titles))
        print(titles)
        print("-"*len(titles))
        for product in self.productos:
            print("| {:<10} | {:<15} | {:<20} | {:<15} | {:<12} | {:<12}".format(
                    product.codigo, 
                    product.nombre, 
                    product.description,
                    product.tag,
                    product.precio,
                    product.existencia
                ))
        print("-"*len(titles))
        input("Presione cualquier tecla para volver...")

    #Funcion para listar por tag
    def listar_tag(self):
        opcion = 0
        while opcion != "x":
            cont = 1
            self.clear()
            #Pinto todas las tags disponibles
            print("--------------Seleccione la tag a revisar------------------\n\n")
            for cat in self.tags:
                print("{0}. {1}".format(cont, cat.nombre))
                cont +=1
            opcion = input("Eliga una opcion, x para salir: ")
            if(opcion!="x"):  
                #mando a pintar la tabla
                self.dibujar_lista(int(opcion))
                input("Presione cualquier tecla para volver...")

    #Funcion para pintar las listas de productos por tag
    def dibujar_lista(self,pos):
        self.clear()
        cat = self.tags[pos - 1].id
        titles = "| {:<10} | {:<15} | {:<20} | {:<15} | {:<12} | {:<12}|".format("Codigo", "Nombre", "Descripcion", "tag", "Precio", "Cantidad")
        print("-"*len(titles))
        print(titles)
        print("-"*len(titles))
        for product in self.productos:
            if product.tag == cat:
                print("| {:<10} | {:<15} | {:<20} | {:<15} | {:<12} | {:<12}".format(
                        product.codigo, 
                        product.nombre, 
                        product.description,
                        product.tag,
                        product.precio,
                        product.existencia
                    ))
        print("-"*len(titles))
        
    # Funcion para crear una tag
    def crear_tag(self):
        print("--------------Crea otra tag------------------\n\n")
        nombre = input("Nombre: ")
        cat = tag(nombre, None)
        self.tags.append(cat)
        cat.write()
        self.clear()
        print("--------------tag creada------------------\n\n")
        print("Presiona una tecla para regresar...")


    #Funcion para crear producto
    def crear_producto(self):
        self.clear()
        print("--------------Introduzca los datos del nuevo producto------------------\n\n")
        codigo = input("Codigo: ")
        nombre = input("Nombre: ")
        desc = input("Descripcion: ")
        tag = input("tag: ")
        precio = input("Precio: ")
        cantidad = input("Cantidad inicial: ")
        
        #valido que el codigo no este usado ya
        if (codigo in self.codigos):
            self.clear()
            print("XXXXXX El codigo de producto ya esta en uso XXXXXX\n\n")
            input()
            crear_producto()
        #Valido que no esten vacios algunos campos
        elif (codigo == '') or (nombre == '') or (desc == '') or (tag == ''):
            self.clear()
            print("XXXXXX Algun dato esta vacio completelo por favor XXXXXX\n\n")
            input()
            crear_producto()
        else:
            #Guardo el producto
            newProduct = Producto(codigo,nombre,desc,tag,precio,cantidad)
            newProduct.write()
            self.productos.append(newProduct)
            self.clear()
            print("--------------Producto creado correctamente------------------\n\n")
            input("Presione cualquier tecla para volver...")

    #Editar producto
    def editar_producto(self):
        self.clear()
        print("--------------Introduzca el codigo del producto a editar------------------\n\n")
        codigo = input("Codigo: ")
        #Verifico que exista el codigo al que quieren modificar
        if not codigo in self.codigos:
            self.clear()
            print("XXXXXX El codigo no corresponde con ninguno, vuelva a intentar XXXXXX\n\n")
            editar_producto()
        else:
            #Mustro el producto
            index = codigos.index(codigo)
            print("--------------Editando producto------------------\n\n")
            titles = "| {:<10} | {:<15} | {:<20} | {:<15} | {:<12} | {:<12}|".format("Codigo", "Nombre", "Descripcion", "tag", "Precio", "Cantidad")
            print("-"*len(titles))
            print(titles)
            print("-"*len(titles))
            print("| {:<10} | {:<15} | {:<20} | {:<15} | {:<12} | {:<12}".format(
                self.productos[index].codigo, 
                self.productos[index].nombre, 
                self.productos[index].description,
                self.productos[index].tag,
                self.productos[index].precio,
                self.productos[index].existencia
            ))
            print("-"*len(titles)+"\n")
            nombre = input("Nombre: ")
            desc = input("Descripcion: ")
            tag = input("tag: ")
            precio = input("Precio: ")
            cantidad = input("Cantidad: ")

            #Guardo los datos introducidos
            if nombre != "": self.productos[index].nombre = nombre
            if desc != "": self.productos[index].descripcion = desc
            if tag != "": self.productos[index].tag = tag
            if precio != "": self.productos[index].precio = precio
            if cantidad != "": self.productos[index].existencia = cantidad

            self.productos[index].write()
            print("--------------Producto editado------------------\n\n")
            print("Presiona una tecla para regresar...")

    #Vender un producto
    def vender(self):
        self.clear()
        print("--------------Introduzca el codigo del producto a vender------------------\n\n")
        codigo = input("Codigo: ")
        #Verifico que el producto a vender este en la base de datos
        if not codigo in self.codigos:
            self.clear()
            print("XXXXXX El codigo no corresponde con ninguno, vuelva a intentar XXXXXX\n\n")
            vender()
        else:
            #Muestro el producto
            index = self.codigos.index(codigo)
            print("--------------Editando producto------------------\n\n")
            titles = "| {:<10} | {:<15} | {:<20} | {:<15} | {:<12} | {:<12}|".format("Codigo", "Nombre", "Descripcion", "tag", "Precio", "Cantidad")
            print("-"*len(titles))
            print(titles)
            print("-"*len(titles))
            print("| {:<10} | {:<15} | {:<20} | {:<15} | {:<12} | {:<12}|".format(
                self.productos[index].codigo, 
                self.productos[index].nombre, 
                self.productos[index].description,
                self.productos[index].tag,
                self.productos[index].precio,
                self.productos[index].existencia
            ))
            print("-"*len(titles)+"\n")
            cantidad = float(input("Cantidad a vender: "))
            #Verifico que la cantidad este
            if cantidad > float(self.productos[index].existencia):
                self.clear()
                print("XXXXXX El codigo no corresponde con ninguno, vuelva a intentar XXXXXX\n\n")
                vender()
            else:
                #Muestro la factura
                self.clear()
                titles = "| {:<10} | {:<15} | {:<20} | {:<20} | {:<20}|".format("Total Bs.","Total $", "Codigo", "Fecha", "Cantidad")
                print("-"*len(titles))
                print(titles)
                print("-"*len(titles))
                date = datetime.datetime.now()
                print("| {:<10} | {:<15} | {:<20} | {:<20} | {:<20}|".format(
                    self.productos[index].price_in_bs(float(tasa.tasa)), 
                    self.productos[index].precio, 
                    self.productos[index].codigo,
                    date.strftime('%x'),
                    cantidad
                ))
                print("-"*len(titles))
                aceptado = input("Presione x para cancelar o cualquier tecla para aceptar...  ")
                #Guardo la venta
                if aceptado != "x" and aceptado != "X":
                    self.productos[index].existencia = float(productos[index].existencia) - cantidad
                    self.productos[index].write()
                    venta = salidas(
                        self.productos[index].price_in_bs(float(tasa.tasa)), 
                        self.productos[index].precio, 
                        self.productos[index].codigo,
                        datetime.datetime.now(),
                        cantidad
                    )
                    venta.write()
                    self.salidas.append(venta)
                    self.clear()
                    print("--------------Venta realizada exitosamente------------------\n\n")
                    input("Presione cualquier tecla para volver...")
    
    #Funcion para mostrar las estadisticas
    def estadisticas(self):
        opcion = 0
        while opcion != 5:
            self.clear()
            print("--------------Estadisticas------------------\n\n")
            print("1. Total en salidas  2. Productos agotados 3. Producto mas costoso 4.Producto mas economico 5. Volver\n")
            opcion = int(input("Eliga una opcion: "))
            if opcion == 1:
                self.total_salidas()
            elif opcion == 2:
                self.productos_agotados()
            elif opcion == 3:
                self.producto_mas_caro()
            elif opcion == 4:
                self.producto_mas_barato()

    #Mostrar el total en dolares y bolivares
    def total_salidas(self):
        self.clear()
        total_dolares = 0
        total_bolivares = 0
        for venta in self.salidas:
            total_bolivares += float(venta.total_bolivares)
            total_dolares += float(venta.total_dolares)
        titles = "| {:<10} | {:<15}|".format("Total Bolivares.","Total Dolares")
        print("-"*len(titles))
        print(titles)
        print("-"*len(titles))
        print("| {:<16} | {:<15}|".format(total_bolivares, total_dolares))
        print("-"*len(titles))
        input("Presiona cualquier tecla...")

    #Mostrar productos en existencia 0
    def productos_agotados(self):
        titles = "| {:<10} | {:<15} | {:<20} | {:<15} | {:<12} | {:<12}|".format("Codigo", "Nombre", "Descripcion", "tag", "Precio", "Cantidad")
        print("-"*len(titles))
        print(titles)
        print("-"*len(titles))
        for product in self.productos:
            if float(product.existencia) <= 0:
                print("| {:<10} | {:<15} | {:<20} | {:<15} | {:<12} | {:<12}".format(
                    product.codigo, 
                    product.nombre, 
                    product.description,
                    product.tag,
                    product.precio,
                    product.existencia
                ))
        print("-"*len(titles))
        input("Presiona cualquier tecla...")

    #Mostrar producto mas economico
    def producto_mas_barato(self):
        mas_barato = self.productos[0]
        for producto in self.productos:
            if float(producto.precio) < float(mas_barato.precio):
                mas_barato = producto

        titles = "| {:<10} | {:<15} | {:<20} | {:<15} | {:<12} | {:<12}|".format("Codigo", "Nombre", "Descripcion", "tag", "Precio", "Cantidad")
        print("-"*len(titles))
        print(titles)
        print("-"*len(titles))
        print("| {:<10} | {:<15} | {:<20} | {:<15} | {:<12} | {:<12}".format(
            mas_barato.codigo, 
            mas_barato.nombre, 
            mas_barato.description,
            mas_barato.tag,
            mas_barato.precio,
            mas_barato.existencia
        ))
        print("-"*len(titles)+"\n")
        input("Presiona cualquier tecla...")

    #Mostrar producto mas caro
    def producto_mas_caro(self):
        mas_caro = self.productos[0]
        for producto in self.productos:
            if float(producto.precio) > float(mas_caro.precio):
                mas_caro = producto

        titles = "| {:<10} | {:<15} | {:<20} | {:<15} | {:<12} | {:<12}|".format("Codigo", "Nombre", "Descripcion", "tag", "Precio", "Cantidad")
        print("-"*len(titles))
        print(titles)
        print("-"*len(titles))
        print("| {:<10} | {:<15} | {:<20} | {:<15} | {:<12} | {:<12}".format(
            mas_caro.codigo, 
            mas_caro.nombre, 
            mas_caro.description,
            mas_caro.tag,
            mas_caro.precio,
            mas_caro.existencia
        ))
        print("-"*len(titles)+"\n")
        input("Presiona cualquier tecla...")

    #Cambiar la tasa de la divisa
    def editar_tasa(self):
        self.clear()
        print("La tasa actual es: " + tasa.tasa)
        new_tasa = input("Defina una nueva tasa: ")
        if new_tasa == "" or float(new_tasa) <= 0:
            print("XXXXXX La tasa es invalida, vuelva a intentarlo XXXXXX\n")
            input()
            editar_tasa()
        else:
            self.tasa.tasa = new_tasa
            self.tasa.write()

    ## Funciones para setear las variables globales
    def getproductos(self):
        with open('./archivos/productos.txt', 'r') as archivo:
            for line in archivo:
                row = line.split(';')
                self.productos.append(Producto(row[0],row[1],row[2],row[3],row[4],row[5].split('\n')[0]))
                self.codigos.append(row[0])

    def getsalidas(self):
        with open('./archivos/salidas.txt', 'r+') as archivo:
            for line in archivo:
                row = line.split(';')
                self.salidas.append(salidas(row[0],row[1],row[2],row[3],row[4].split('\n')[0]))

    def setTasa(self):
        with open("./archivos/tasa.txt", 'r+') as archivo:
            line = archivo.readline()
            self.tasa.tasa = line

    def gettags(self):
        with open('./archivos/tags.txt', 'r') as archivo:
            for line in archivo:
                row = line.split(';')
                self.tags.append(tag(row[1].split('\n')[0], row[0]))
