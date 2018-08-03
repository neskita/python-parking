

def mainMenu():
    print("[0] Soy un admin user")
    print("[1] Soy un usuario del parking")
    return __getSeleccion("Por favor, elija que tipo de usuario es: ");


def __getSeleccion(mensaje, maxLimit):
    while(True):
        try:
            value = int(input(mensaje));
            if value > maxLimit:
                raise ValueError('Seleccion fuera de margen');
            return value;
        except:
            print("Seleccion no valida. Por favor intentelo de nuevo")


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