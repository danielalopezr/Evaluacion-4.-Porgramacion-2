from classes.Handlers import Handler
import os
#Funcion para limpiar la pantalla dependiendo del sistema operativo
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def main():
    handler = Handler()
    opcion = 0;
    while(opcion != "x" and opcion != "X"):
        clear()
        print("|| Sistema de ventas de Flacco y Asociados C.A. ||".upper())
        head = "| {:<25} |".format("Opcion")
        print("-"*len(head))
        print(head)
        print("-"*len(head))
        print("| {:<25} |".format("1. Listar productos"))
        print("| {:<25} |".format("2. Listar por categoria"))
        print("| {:<25} |".format("3. Crear producto"))
        print("| {:<25} |".format("4. Crear categoria"))
        print("| {:<25} |".format("5. Editar producto"))
        print("| {:<25} |".format("6. Vender"))
        print("| {:<25} |".format("7. Divisa"))
        print("| {:<25} |".format("8. Total de ventas"))
        print("| {:<25} |".format("9. Productos agotados"))
        print("| {:<25} |".format("10. Producto más barato"))
        print("| {:<25} |".format("11. Producto más caro"))
        print("-"*len(head))
        opcion = input("Seleccione una opción, x para salir: ")
        try:
            opcion = int(opcion)
            if opcion == 1:
                handler.listar()
            elif opcion == 2:
                handler.listar_tag()
            elif opcion == 3:
                handler.crear_producto()
            elif opcion == 4:
                handler.crear_tag()
            elif opcion == 5:
                handler.editar_producto()
            elif opcion == 6:
                handler.vender()
            elif opcion == 7:
                handler.editar_tasa()
            elif opcion == 8:
                handler.total_ventas()
            elif opcion == 9:
                handler.productos_agotados()
            elif opcion == 10:
                handler.producto_mas_barato()
            elif opcion == 11:
                handler.producto_mas_caro()
        except ValueError:
            pass
        
        

if __name__ == "__main__":
    main()
