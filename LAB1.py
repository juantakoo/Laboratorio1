directorio = []

mensajes = {
    "bienvenida": "Bienvenido al directorio telefónico",
    "nombre": "Digite el nombre completo (nombre y apellido): ",
    "telefono": "Digite el teléfono celular: ",
    "cumpleanos": "Digite la fecha de cumpleaños (DD/MM): ",
    "correo": "Digite el correo electrónico: ",
    "despedida": "Gracias por usar el directorio telefónico. ¡Hasta luego!",
    "opcion_invalida": "Opción no válida. Intente de nuevo.",
    "telefono_invalido": "❌ El teléfono debe contener solo números.",
    "telefono_existente": "❌ Este teléfono ya está registrado.",
    "fecha_invalida": "❌ Formato de fecha inválido. Use DD/MM.",
    "correo_invalido": "❌ Correo electrónico inválido. Formato: usuario@dominio.com"
}

def menu():
    while True:
        print("\n" + "="*15 + " MENÚ " + "="*15)
        print("1. 📝 Agregar nuevo registro")
        print("2. 🔍 Buscar persona por teléfono")
        print("3. 🗑️  Borrar registro")
        print("4. 🚪 Salir")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            agregar_registro()
        elif opcion == "2":
            buscar_persona()
        elif opcion == "3":
            borrar_registro()
        elif opcion == "4":
            print("\n" + mensajes["despedida"])
            break
        else:
            print(mensajes["opcion_invalida"])

def validar_fecha(fecha):
    if len(fecha) != 5 or fecha[2] != '/':
        return False
    try:
        dia, mes = map(int, fecha.split('/'))
        return 1 <= dia <= 31 and 1 <= mes <= 12
    except ValueError:
        return False

def validar_correo(correo):
    return '@' in correo and '.' in correo.split('@')[-1] and len(correo.split('@')) == 2

def agregar_registro():
    print("\n" + "="*15 + " NUEVO REGISTRO " + "="*15)
    
    # Validar nombre
    nombre = input(mensajes["nombre"]).strip().title()
    while not nombre.replace(' ', '').isalpha():
        print("❌ Nombre inválido. Solo letras y espacios.")
        nombre = input(mensajes["nombre"]).strip().title()
    
    # Validar teléfono
    while True:
        telefono = input(mensajes["telefono"]).strip()
        if not telefono.isdigit() or len(telefono) < 7:
            print(mensajes["telefono_invalido"])
            continue
        if any(p["telefono"] == telefono for p in directorio):
            print(mensajes["telefono_existente"])
            return
        break
    
    # Validar fecha
    while True:
        cumpleanos = input(mensajes["cumpleanos"]).strip()
        if validar_fecha(cumpleanos):
            break
        print(mensajes["fecha_invalida"])
    
    # Validar correo
    while True:
        correo = input(mensajes["correo"]).strip().lower()
        if validar_correo(correo):
            break
        print(mensajes["correo_invalido"])
    
    directorio.append({
        "nombre": nombre,
        "telefono": telefono,
        "cumpleanos": cumpleanos,
        "correo": correo
    })
    print("\n✅ Registro agregado exitosamente!")

def buscar_persona():
    print("\n" + "="*15 + " BUSCAR " + "="*15)
    telefono = input("Teléfono a buscar: ").strip()
    
    if not telefono.isdigit():
        print(mensajes["telefono_invalido"])
        return
    
    encontrado = False
    for persona in directorio:
        if persona["telefono"] == telefono:
            print("\n🔍 Resultado de búsqueda:")
            print(f"  Nombre:      {persona['nombre']}")
            print(f"  Teléfono:    {persona['telefono']}")
            print(f"  Cumpleaños:  {persona['cumpleanos']}")
            print(f"  Correo:      {persona['correo']}")
            encontrado = True
            break
    
    if not encontrado:
        print("\n❌ No se encontraron registros con ese teléfono.")

def borrar_registro():
    print("\n" + "="*15 + " BORRAR " + "="*15)
    telefono = input("Teléfono a borrar: ").strip()
    
    if not telefono.isdigit():
        print(mensajes["telefono_invalido"])
        return
    
    for i, persona in enumerate(directorio):
        if persona["telefono"] == telefono:
            confirmacion = input(f"¿Borrar a {persona['nombre']}? (S/N): ").upper()
            if confirmacion == "S":
                del directorio[i]
                print("\n✅ Registro borrado exitosamente!")
            else:
                print("\n❌ Operación cancelada.")
            return
    
    print("\n❌ No se encontraron registros con ese teléfono.")

if __name__ == "__main__":
    print("\n" + "="*15 + " " + mensajes["bienvenida"] + " " + "="*15)
    menu()
