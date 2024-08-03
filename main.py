import funciones
import reportes


#menu pricipal
def menu_principal():
    while True:
        print("                       **************************")
        print("                       ***** MENÚ PRINCIPAL *****")
        print("                       **************************")
        print("  ")
        print("                     ............     ............")
        print("               '...'             ',.,'            ',..,")    
        print("             ,' ,'      ~~~~       :       ~~~~    ', ',")
        print("           ,' ,'  ~~~~~~   ~~~~~   :   ~~~~~~  ~~~~~  ', ',")
        print("         ,' ,'       ~~~~~~~       :      ~~~~~~~~~~    ', ',")
        print("       ,' ,' ~~~~~~~~ ~~~~  ~~~~~  :  ~~~~~  ~~~  ~~~~~~   ', ',")
        print("     ,' ,'.......................  :  .......................', ',")
        print("   ,' ,'                         ',:,'                          ', ',")
        print(" ,'  '........................     '     .........................'  ',")
        print("  ''''''''''''''''''''''''''''';''''''';''''''''''''''''''''''''''''''")
        print(" ")
        print("                             1. Libros")
        print("                             2. Socios")
        print("                             3. Prestamos y devoluciones")
        print("                             4. Reportes")
        print("                             5. Salir")
        print(" ")
        opcion = input("                        Seleccione una opción (1-5): ")

        if opcion == "1":
            menu_libros()
        elif opcion == "2":
            menu_socios()
        elif opcion == "3":
            menu_prestamos_devoluciones()
        elif opcion == "4":
            menu_reportes()
        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

def menu_libros():
    while True:
        print("1. Agregar libro")
        print("2. Buscar libro")
        print("3. Editar libro")
        print("4. Eliminar libro")
        print("5. Volver al menú principal")
        opcion = input("Seleccione una opción (1-3): ")

        if opcion == "1":
            funciones.agregar_libro(id_libro)
            print("Libro agregado con éxito...")
        elif opcion == "2":
            print("Seleccione el criterio de búsqueda:")
            print("     a. Por título")
            print("     b. Por autor")
            print("     c. Por género")
            print("     d. Por editorial")
            opcion_busqueda = input("   Ingrese una opción: ")

            if opcion_busqueda == "a":
                campo = "titulo"
                valor = input("Ingrese el titulo del libro: ")
            elif opcion_busqueda == "b":
                campo = "autor"
                valor = input("Ingrese el autor del libro: ")
            elif opcion_busqueda == "c":
                campo = "genero"
                valor = input("Ingrese el género del libro: ")
            elif opcion_busqueda == "d":
                campo = "editorial"
                valor = input("Ingrese la editorial del libro: ")
            else:
                print("Opción inválida.")
                continue
            funciones.buscar_libro(campo, valor)
        elif opcion == "3":
            id_libro = input("Ingrese el ID del libro a editar: ")
            print("Seleccione el criterio a modificar:")
            print("     1. título")
            print("     2. autor")
            print("     3. año")
            print("     4. editorial")
            print("     5. género")
            print("     6. volver")
            opcion_busqueda = input("   Ingrese una opción: ")

            if opcion_busqueda == "1":
                campo = "titulo"
                nuevo_valor = input("Ingrese el nuevo titulo del libro: ")
            elif opcion_busqueda == "2":
                campo = "autor"
                nuevo_valor = input("Ingrese el nuevo autor del libro: ")
            elif opcion_busqueda == "3":
                campo = "anio"
                nuevo_valor = input("Ingrese el nuevo año: ")
            elif opcion_busqueda == "4":
                campo = "editorial"
                nuevo_valor = input("Ingrese la nueva editorial del libro: ")
            elif opcion_busqueda == "5":
                campo = "genero"
                nuevo_valor = input("Ingrese el nuevo género del libro: ")
            elif opcion_busqueda == "6":
                break
            else:
                print("Opción inválida.")
                continue
            funciones.editar_libro(id_libro, campo, nuevo_valor)
        elif opcion == "4":
            id_libro = input("Ingrese el ID del libro a eliminar: ")
            funciones.eliminar_libro(id_libro)
        elif opcion == "5":
            break
        else:
            print("Opción inválida. Intente nuevamente.")


def menu_socios():
    while True:
        print("1. Agregar socio")
        print("2. Editar socio")
        print("3. Eliminar socio")
        print("4. Volver al menú principal")
        opcion = input("Seleccione una opción (1-4): ")

        if opcion == "1":
            funciones.agregar_socio()
            print("Socio agregado con éxito...")
        elif opcion == "2":
            print("Seleccione el criterio de búsqueda:")
            print("     1. modificar nombre")
            print("     2. modificar apellido")
            print("     3. modificar DNI")
            print("     4. modificar telefono")
            print("     5. modificar direccion")
            print("     6. modificar correo")
            print("     7. modificar fecha de nacimiento")
            print("     8. volver al menú anterior")
            opcion_busqueda = input("   Ingrese una opción: ")

            if opcion_busqueda == "1":
                campo = "nombre"
                valor = input("Ingrese el nombre modificado: ")
            elif opcion_busqueda == "2":
                campo = "apellido"
                valor = input("Ingrese el nuevo apellido: ")
            elif opcion_busqueda == "3":
                campo = "dni"
                valor = input("Ingrese el nuevo DNI: ")
            elif opcion_busqueda == "4":
                campo = "telefono"
                valor = input("Ingrese el nuevo telefono: ")
            elif opcion_busqueda == "5":
                campo = "direccion"
                valor = input("Ingrese la nueva direccion: ")
            elif opcion_busqueda == "6":
                campo = "correo"
                valor = input("Ingrese el nuevo correo: ")
            elif opcion_busqueda == "7":
                campo = "fecha_nacimiento"
                valor = input("Ingrese la nueva fecha de nacimiento: ")
            elif opcion_busqueda == "8":
                break
            else:
                print("Opción inválida.")
                continue
            id_socio = input("Ingrese el ID del socio a editar: ")
            funciones.editar_socio(id_socio,campo,valor)
        elif opcion == "3":
            id_socio = input("Ingrese el ID del socio a eliminar: ")
            funciones.eliminar_socio(id_socio)
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Intente nuevamente.")

def menu_prestamos_devoluciones():
    while True:
        print("1. Prestamos")
        print("2. Devoluciones")
        print("3. Volver al menú principal")
        opcion = input("Seleccione una opción (1-3): ")

        if opcion == "1":
            funciones.veificar_disponibilidad()
        elif opcion == "2":
            funciones.devolucion_libro()
        elif opcion == "3":
            break
        else:
            print("Opción no válida. Intente nuevamente.")


def menu_reportes():
    socios = reportes.cargar_datos('socios.json')
    libros = reportes.cargar_datos('libros.json')

    while True:
        print("1. Generar reporte de préstamos")
        print("2. Generar reporte de devoluciones")
        print("3. Regresar al menú principal")
        opcion = input("Seleccione una opción (1-3): ")

        if opcion == "1":
            print("1. Reporte de préstamos por socio")
            print("2. Reporte de préstamos por libro")
            print("3. Reporte de préstamos por rango de fechas")
            print("4. Volver...")
            opcion_reporte = input("Seleccione una opción (1-4): ")
            
            if opcion_reporte == "1":
                prestamos = reportes.cargar_datos('prestamos.json')
                reportes.generar_reporte(prestamos, socios, libros, 'socio')
            elif opcion_reporte == "2":
                prestamos = reportes.cargar_datos('prestamos.json')
                reportes.generar_reporte(prestamos, socios, libros, 'libro')
            elif opcion_reporte == "3":
                prestamos = reportes.cargar_datos('prestamos.json')
                reportes.generar_reporte(prestamos, socios, libros, 'fecha')
            elif opcion_reporte == "4":
                continue
        elif opcion == "2":
            print("1. Reporte de devoluciones por socio")
            print("2. Reporte de devoluciones por libro")
            print("3. Reporte de devoluciones por rango de fechas")
            print("4. Volver...")
            opcion_reporte = input("Seleccione una opción (1-4): ")

            if opcion_reporte == "1":
                devoluciones = reportes.cargar_datos('prestamos.json')
                reportes.generar_reporte(devoluciones, socios, libros, 'socio')
            elif opcion_reporte == "2":
                devoluciones = reportes.cargar_datos('prestamos.json')
                reportes.generar_reporte(devoluciones, socios, libros, 'libro')
            elif opcion_reporte == "3":
                devoluciones = reportes.cargar_datos('prestamos.json')
                reportes.generar_reporte(devoluciones, socios, libros, 'fecha')
            elif opcion_reporte == "4":
                continue
        elif opcion == "3":
            break
        else:
            print("Opción inválida. Intente nuevamente.")

 
menu_principal()
menu_libros()
menu_socios()
menu_prestamos_devoluciones()
menu_reportes()
'''  
            print("1. reporte de préstamos por socio")
            print("2. reporte de préstamos por libro")
            print("3. reporte de préstamos por rango de fechas:") 
            print("4. volver...")
            opcion_reporte = input("Seleccione una opción (1-3): ")
            if opcion_reporte == "1":
                funciones.reporte_prestamos_socio()
            elif opcion_reporte == "2":
                funciones.reporte_prestamos_libro()
            elif opcion_reporte == "3":
                funciones.reporte_prestamos_fecha()
            elif opcion_reporte == "4":
                break
'''