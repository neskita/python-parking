import currency
import parking;
from random import randint;
from time import sleep

matricula = "matricula" + str(randint(0,1000));
parking.aparcar(matricula);
sleep(2);
estacionamiento = parking.sacarCoche(matricula);
print(estacionamiento.coste);


dolares = currency.getExchangeRate('USD');
print(dolares)

print(parking.verImporteHoy());
print(parking.verImporteSemana());
print(parking.verImporteMes());