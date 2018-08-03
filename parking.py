from datetime import date, datetime, timedelta;
from random import randint;
import db;

class estacionamiento():

    def __init__(self, pk, plaza, matricula, horaEntrada, horaSalida, coste = None): #se podria aplicar una tarifa inicial
        self.pk = pk;
        self.plaza = plaza;
        self.matricula = matricula;
        self.horaEntrada = horaEntrada;
        self.horaSalida = horaSalida;
        self.coste = coste;


    def salir(self):
        self.horaSalida = datetime.now();
        return self.__calcularCoste();


    def __calcularCoste(self):
        timedelta = self.horaSalida - self.horaEntrada;
        totalSecs = timedelta.days * 86400 + timedelta.seconds;
        minutes = divmod(totalSecs, 60)[0]
        hours = divmod(minutes, 60) [0]
        if minutes < 20:
            self.coste = 1;
        elif minutes < 60:
            self.coste = 1.50;
        elif minutes < 24:
            self.coste = 1.5 * hours;
        else:
            self.coste = 15 * timedelta.days;
        return self.coste;


def sacarCoche(matricula):
    estacionamiento = db.queryEstacionamiento(matricula);
    if estacionamiento is None:
        return None;
    estacionamiento.salir();
    db.updateEstacionamiento(estacionamiento);
    return estacionamiento;

def aparcar(matricula):
    plazas = getPlazasDisponibles();
    if not plazas:
        return None;
    aparcar(matricula, plazas[randint(0,len(plazas)-1)]);

def aparcar(matricula, plaza=None):
    resultado = db.queryEstacionamiento(matricula);
    if resultado is None:
        disponibles = getPlazasDisponibles();

        if not disponibles:
            return None;

        if plaza is None:
            plaza = disponibles[randint(0,len(disponibles)-1)];

        if plaza not in disponibles:
            return None;

        return db.insertEstacionamiento(plaza, matricula);
    raise ValueError('Este coche ya esta aparcado. Necesita salir antes de volver a entrar.')

def getPlazasOcupadasYMatricula():
    return db.getPlazasOcupadasYMatricula();

def getPlazasDisponibles():
    ocupadas = db.getPlazasOcupadas();
    disponibles = [ i for i in range(0,100) if i not in ocupadas]
    return disponibles;


def verImporteMes():
    firstDayMonth = date.today().replace(day=1);
    return verImporteDesde(firstDayMonth)


def verImporteSemana():
    firstDayWeek = date.today() - timedelta(days=date.today().weekday());
    return verImporteDesde(firstDayWeek);

def verImporteHoy():
    return verImporteDesde(date.today());


def verImporteDesde(beginningDate):
    estacionamientos = db.getEstacionamientoDesde(beginningDate);
    return __sumarImportesCoste(estacionamientos);


def __sumarImportesCoste(estacionamientos):
    return sum([x.coste for x in estacionamientos if x.coste is not None]);

