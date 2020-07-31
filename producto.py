#Clase encargada del manejo e productos
class Producto(object):
    #Atributos de la clase
    codigo = ""
    nombre = ""
    descripcion = ""
    tag = ""
    precio = 0
    existencia = 0

    #Constructor de la clase
    def __init__(self, codigo, nombre, descripcion, tag, precio, existencia):
        self.codigo = codigo
        self.nombre = nombre
        self.description = descripcion
        self.tag = tag
        self.precio = precio
        self.existencia = existencia
    
    #convertidor de divisas por producto
    def price_in_bs(self,rate):
        if rate == 0: return
        return float(self.precio) * rate
    
    #Funcion para escribir el producto en el archivo
    def write(self):
        existe = False
        contenido = list()
        pos = 0
        with open("./archivos/productos.txt",'r') as archivo:
            for linea in archivo:
                columnas = linea.split(';')
                if(columnas[0] == self.codigo):
                    existe = True
                pos += 1

        if(existe == False):
            with open("./archivos/productos.txt",'a') as archivo:
                archivo.write("\n{0};{1};{2};{3};{4};{5}".format(
                    self.codigo, 
                    self.nombre, 
                    self.description, 
                    self.tag, 
                    self.precio, 
                    self.existencia
                ))
        else:
            with open('./archivos/productos.txt', 'r') as archivo:
                contenido = archivo.readlines()
                print(pos)
                contenido[pos-1] = "{0};{1};{2};{3};{4};{5}".format(
                    self.codigo, 
                    self.nombre, 
                    self.description, 
                    self.tag, 
                    self.precio, 
                    self.existencia
                );
            with open('./archivos/productos.txt', 'w') as archivo:
                print(contenido)
                archivo.write(''.join(contenido))
        
