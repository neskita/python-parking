import parking;
from random import randint;
from time import sleep
from datetime import datetime;
import db;

#
# est = parking.estacionamiento(pk=48, plaza=randint(0,100), matricula=22, horaEntrada=datetime.now(), horaSalida=datetime.now(), coste = 33)
# db.update(est)

matricula = "matricula" + str(randint(0,1000));
parking.aparcar(matricula);
sleep(2);
estacionamiento = parking.sacarCoche(matricula);
print(estacionamiento.coste);

"http://data.fixer.io/api/latest?access_key=b96a72bed66245c7dff0d19efb83b1ee"
