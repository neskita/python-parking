import sys;
import gui;
import administracion as admin;
import parking;
import currency;

loggedUser = (); #id, admin

def registerUser():
    seleccion = gui.mainMenu();

    if seleccion == 2:
        sys.exit(0)

    usuario = input("Por favor inserte el id de usuario: ");
    contrasena = input("Por favor inserte la contrasena: ")
    if seleccion == 0:
        loggedUser = admin.logarUsuarioAdmin(usuario, contrasena);
    if seleccion == 1:
        loggedUser = admin.logarUsuario(usuario, contrasena)

    return loggedUser;

while True:
    loggedUser = registerUser();

    while True:
        if loggedUser[1]:
            #Admin User
            seleccion = gui.userAdmin();

            # "[0] Mostrar todos los usuarios"
            if seleccion == 0:
                gui.imprimirListaUsuarios(admin.queryUsuarios());

            # "[1] Dar de baja un usuario"
            if seleccion == 1:
                admin.bajaUsuario(gui.validateIntInput("Inserte el id del usuario a dar de baja: "));

            # "[2] Revisar el uso de las plazas"
            #       "[0] Imprimir Mapa de las Plazas"
            #       "[1] Lista de Plazas usadas y Matriculas"
            #       "[2] Salir"
            if seleccion == 2:
                plazasSeleccion = gui.userAdminUsoPlazas()
                if plazasSeleccion == 0:
                    gui.imprimirPlazasLibres(parking.getPlazasDisponibles());
                if plazasSeleccion == 1:
                    gui.imprimirPlazasOcupadasYCoches(parking.getPlazasOcupadasYMatricula());

            # "[3] Ver el importe total del día, semana o mes"
            #       "[0] Ver total del dia"
            #       "[1] Ver total de la semana"
            #       "[2] Ver total del mes"
            if seleccion == 3:
                importesSeleccion = gui.userAdminImportes();
                if importesSeleccion == 0:
                    print("El importe recaudado hoy es: " + str(parking.verImporteHoy()) + "€");
                if importesSeleccion == 1:
                    print("El importe recaudado esta semana es: " + str(parking.verImporteSemana()) + "€");
                if importesSeleccion == 1:
                    print("El importe recaudado este mes es: " + str(parking.verImporteMes()) + "€");

            # "[4] Log out"
            if seleccion == 4:
                loggedUser = ();
                break;
        else:
            # Parking User
            seleccion = gui.userMenu();

            #"[0] Crear un usuario Nuevo"
            if seleccion == 0:
                admin.altaUsuario(gui.inputDataUsuario());

            #"[1] Aparcar coche en el parking"
            if seleccion == 1:
                coste = parking.aparcarMiCoche(loggedUser[0]);
                crr = gui.menuForeignCurrency();
                exchangeValue = currency.getExchangeRate(crr);
                total = coste * exchangeValue;
                print("El coste a pagar por el estacionamiento es: ", str(total), currency);

            #"[2] Sacar coche del parking"
            if seleccion == 2:
                parking.sacarMiCoche(loggedUser[1]);

            #"[3] Log out"
            if seleccion == 3:
                loggedUser = ();
                break;
