from datetime import  datetime
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
    estacionamiento = db.query(matricula);
    if estacionamiento is None:
        return None;
    estacionamiento.salir();
    db.update(estacionamiento);
    return estacionamiento;

def aparcar(matricula):
    resultado = db.query(matricula);
    if resultado is None:
        plazas = getPlazasDisponibles();
        if not plazas:
            return None;
        return db.insert(plazas[0], matricula);
    raise ValueError('Este coche ya esta aparcado. Necesita salir antes de volver a entrar.')

def getPlazasDisponibles():
    ocupadas = db.getPlazasOcupadas();
    disponibles = [ i for i in range(0,100) if i not in ocupadas]
    return disponibles;
