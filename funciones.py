import json
import tablib
from datetime import datetime, timedelta

libros = []
socios = []
prestamos = []

#funciones de agregar libro
#se abre el archivo en modo r lectura
with open('libros.json', 'r') as f:
    libros = json.load(f)

def agregar_libro():
    id_libro = 0
    id_libro = len(libros) + 1
    titulo = input("Ingrese el título del libro: ")
    autor = input("Ingrese el autor del libro: ")
    editorial = input("Ingrese la editorial del libro: ")
    anio = input("Ingrese el año de publicacion del libro: ")
    genero = input("Ingrese el genero del libro: ")
    disponibilidad = True
    libros_dict = {
        "id_libro": id_libro,
        "titulo": titulo,
        "autor": autor,
        "editorial": editorial,
        "anio": anio,
        "genero": genero,
        "disponibilidad":disponibilidad
    }
    # se añade el libro al la lista de libros
    libros.append(libros_dict)
    #se abre el archivo en modo w escritura
    with open('libros.json','w', encoding='utf-8') as f:
        json.dump(libros, f, indent=4)


#funciones de busqueda
#define la función buscar_libro que recibe dos parametros de busqueda
def buscar_libro(campo, valor):
    # Busca un libro en la lista de libros por un campo específico
    for libro in libros:
        if libro[campo] == valor:
            for clave, valor in libro.items():
                print(f"{clave}: {valor}")
            return  # Sale de la función si encuentra el libro
        
    print("No se encontró el libro")

def editar_libro(id_libro, campo, nuevo_valor):
    libro_encontrado = False
    for libro in libros:
        if libro["id_libro"] == int(id_libro):
            libro[campo] = nuevo_valor
            libro_encontrado = True
            break

    if not libro_encontrado:
        print("Libro no encontrado.")
    else:
        with open('libros.json', 'w', encoding='utf-8') as f:
            json.dump(libros, f, indent=4)
        print("Libro modificado exitosamente.")

def eliminar_libro(id_libro):
    for libro in libros:
        if libro["id_libro"] == int(id_libro):
            libros.remove(libro)
            with open('libros.json','w', encoding='utf-8') as f:
                json.dump(libros, f, indent=4)
            print("Libro eliminado con exito!")
        else:
            print("Libro no encontrado.")



#funciones socios
with open('socios.json', 'r') as f:
    socios = json.load(f)

def agregar_socio():
    id_socio = 0
    id_socio = len(socios) + 1 
    nombre = input("Ingrese el nombre del socio: ")
    apellido = input("Ingrese el apellido del socio: ")
    dni = input("Ingrese el dni del socio: ")
    fecha_nacimiento = input("Ingrese fecha de nacimiento: ")
    telefono = input("Ingrese el telefono del socio: ")
    direccion = input("Ingrese la direccion del socio: ")
    email = input("Ingrese el email del socio: ")
    socios_dict = {"id_socio": id_socio,
                   "nombre": nombre, 
                   "apellido": apellido, 
                   "dni": dni, 
                   "fecha_nacimiento": fecha_nacimiento,
                   "telefono": telefono, 
                   "direccion": direccion, 
                   "email": email
                   }
    socios.append(socios_dict)
    with open('socios.json','w', encoding='utf-8') as f:
        json.dump(socios, f, indent=4)


def editar_socio(id_socio, campo, nuevo_valor):
    socio_encontrado = False
    for socio in socios:
        if socio["id_socio"] == int(id_socio):
            socio[campo] = nuevo_valor
            socio_encontrado = True
            break  # Salimos del bucle una vez que encontramos el socio

    #si se encuentra el socio, se establece socio_encontrado en True y se realiza el cambio.
    if socio_encontrado:
        with open('socios.json', 'w', encoding='utf-8') as f:
            json.dump(socios, f, indent=4)
    print("Socio modificado exitosamente.")
        

def eliminar_socio(id_socio):
    for socio in socios:
        if socio["id_socio"] == int(id_socio):
            socios.remove(socio)
            with open('socios.json','w', encoding='utf-8') as f:
                json.dump(socios, f, indent=4)
            print("Socio eliminado exitosamente.")
        else:
            print("Socio no encontrado.")



#funciones prestamos
def veificar_disponibilidad():
    id_libro = input("Ingrese el ID del libro que quieres prestar: ")
    for libro in libros:
        if libro["id_libro"] == int(id_libro):
            if libro["disponibilidad"] == True:
                agregar_prestamo(id_libro)
                break
            else:
                print("El libro no está disponible para préstamo.")
                break
    else:
        print("Libro no encontrado.")

def agregar_prestamo(id_libro):
    with open('prestamos.json', 'r') as f:
        prestamos = json.load(f)
    id_prestamo = 0
    id_prestamo = len(prestamos) + 1 
    id_socio = input("ingrese el id del socio: ")
    for socio in socios:
        if socio["id_socio"] == int(id_socio):
            id_socio = socio["id_socio"]
            socio_encontrado = True
            break
    if socio_encontrado:    
        fecha_prestamo = input("Ingrese la fecha de préstamo (AAAA-MM-DD): ")
        fecha_prestamo_obj = datetime.strptime(fecha_prestamo, "%Y-%m-%d") 
        fecha_devolucion = fecha_prestamo_obj + timedelta(weeks=2)
        costo = input("Ingrese el costo del libro: ")
        estado_prestamo = True
        nuevo_prestamo = {"id_prestamo" : id_prestamo,
                        "id_socio": id_socio,
                        "id_libro": id_libro,
                        "fecha_prestamo": fecha_prestamo,
                        "Costo": costo,
                        "fecha_devolucion": fecha_devolucion,
                        "estado_prestamo": estado_prestamo}
        prestamos.append(nuevo_prestamo)
        # Guardar los préstamos actualizados en el archivo
        with open('prestamos.json', 'w') as f:
            json.dump(prestamos, f, indent=4, default=str)
        print("Préstamo registrado exitosamente.")
        print("Nuevo préstamo agregado:")
        for clave, valor in nuevo_prestamo.items():
            print(f"{clave}: {valor}")
    if not socio_encontrado:
        print("Socio no encontrado")
        return

def devolucion_libro():
    #se cargan los datos de los archivos JSON
    with open('prestamos.json', 'r') as f:
        prestamos = json.load(f)
    with open('libros.json', 'r') as f:
        libros = json.load(f)
    
    # Solicitar el ID del préstamo
    id_prestamo = int(input("Ingrese el ID del préstamo: "))
    prestamo_encontrado = False
    
    # Buscar el préstamo por el ID
    for prestamo in prestamos:
        if prestamo["id_prestamo"] == id_prestamo:
            prestamo_encontrado = True
            
            #se erifica si el préstamo ya está marcado como devuelto
            if not prestamo["estado_prestamo"]:
                print("El préstamo ya ha sido devuelto.")
                return
            
            #se actualiza el estado del préstamo a devuelto
            prestamo["estado_prestamo"] = False
            
            # Buscar el libro correspondiente y actualizar su disponibilidad
            libro_encontrado = False
            for libro in libros:
                if libro["id_libro"] == prestamo["id_libro"]:
                    libro_encontrado = True
                    # Verificar si el libro ya está disponible
                    if libro["disponibilidad"]:
                        print("El libro ya está disponible. No es necesario devolverlo.")
                        return
                    
                    libro["disponibilidad"] = True
                    break
            
            if not libro_encontrado:
                print("El libro correspondiente al préstamo no se encontró en la base de datos.")
                return
            
            #Se guardan los cambios en el archivo de préstamos
            with open('prestamos.json', 'w') as f:
                json.dump(prestamos, f, indent=4)
            #se guardan los cambios en el archivo de libros
            with open('libros.json', 'w') as f:
                json.dump(libros, f, indent=4)
            
            print("Libro devuelto exitosamente.")
            break
    
    if not prestamo_encontrado:
        print("Préstamo no encontrado. Intente nuevamente.")

def reporte_prestamo_socio():
    with open('prestamos.json', 'r') as f:
        prestamos = json.load(f)
    data = tablib.Dataset()
    data.headers = ['ID Prestamo', 'ID Socio', 'ID Libro', 'Fecha Prestamo', 'Fecha Devolucion', 'Estado']
    for prestamo in prestamos:
        data.append((prestamo['id_prestamo'], prestamo['id_socio'], prestamo['id_libro'], prestamo['fecha_prestamo'], prestamo['fecha_devolucion'], prestamo['estado']))

    # Generar reporte por socio

    prestamos_por_socio = {}
    for prestamo in prestamos:
        if prestamo['id_socio'] not in prestamos_por_socio:
            prestamos_por_socio[prestamo['id_socio']] = []
        prestamos_por_socio[prestamo['id_socio']].append(prestamo)

    # Crear un dataset para cada socio
    for socio, prestamos_socio in prestamos_por_socio.items():
        data_socio = tablib.Dataset()
        # ... (llenar el dataset con los préstamos del socio)
        data_socio.export('csv', f'reporte_socio_{socio}.csv')
        print("Reportes generados con éxito.")
