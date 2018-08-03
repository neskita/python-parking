
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