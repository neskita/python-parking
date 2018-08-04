

def mainMenu():
    print("[0] Soy un admin user")
    print("[1] Soy un usuario del parking")
    print("[2] Salir")
    return __getSeleccion("Por favor, elija una opcion: ", 2);


def userMenu():
    print("[0] Crear un usuario Nuevo")
    print("[1] Aparcar un coche en el parking")
    print("[2] Sacar un coche del parking")
    print("[3] Log out")
    return __getSeleccion("Por favor, que accion desea realizar? ", 3);


def userAdmin():
    print("[0] Mostrar todos los usuarios")
    print("[1] Dar de baja un usuario")
    print("[2] Revisar el uso de las plazas")
    print("[3] Ver el importe total del día, semana o mes")
    print("[4] Log out")
    return __getSeleccion("Por favor, que accion desea realizar? ", 4);


def userAdminUsoPlazas():
    print("[0] Imprimir Mapa de las Plazas")
    print("[1] Lista de Plazas usadas y Matriculas")
    print("[2] Salir")
    return __getSeleccion("Por favor, que accion desea realizar? ", 2);


def userAdminImportes():
    print("[0] Ver total del dia")
    print("[1] Ver total de la semana")
    print("[2] Ver total del mes")
    print("[3] Salir")
    return __getSeleccion("Por favor, que accion desea realizar? ", 3);


def __getSeleccion(mensaje, maxLimit):
    while True:
        try:
            value = int(input(mensaje));
            if value > maxLimit:
                raise ValueError('Seleccion fuera de margen');
            return value;
        except:
            print("Seleccion no valida. Por favor intentelo de nuevo")

def validateIntInput(mensaje):
    while True:
        try:
            value = int(input(mensaje));
            return value;
        except:
            print("Por favor Inserte un valor numerico....");

def imprimirPlazasLibres(disponibles):
    for x in range(0, 10):
        linePlazas = '';
        lineEstados = '';
        for y in range(0, 10):
            plaza = (x * 10 + y);
            plazaStr = '{:5s}'.format("(" + str(plaza) + ")");
            linePlazas = linePlazas + plazaStr;
            lineEstados = lineEstados + ("  O  " if plaza in disponibles else "  X  ");
        print(linePlazas);
        print(lineEstados);
        print();

def imprimirPlazasOcupadasYCoches(ocupadas):
    print("Plaza --> Matricula Coche")
    for tupla in ocupadas:
        print ("(" + str(tupla[0]) + ")  -->  " + tupla[1]);


def imprimirListaUsuarios(usuarios):
    if not usuarios:
        return;
    for usuario in usuarios:
        print(usuario);

def inputDataUsuario():
    return validateIntInput("Introduzca el ID: "),\
           input("Introduzca el nombre: "),\
           input("Introduzca el email: "),\
           input("Introduzca la contrasena: "),\
           input("Introduzca la matricula del coche");

def menuForeignCurrency():
    return input("Especifique otra moneda si quiere mostrar el imorte en moneda extranjera: ");