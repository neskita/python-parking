import currency
import parking;
from gui import imprimirPlazasLibres, imprimirPlazasOcupadasYCoches;
from random import randint;
from time import sleep
import db;

matricula = "matricula" + str(randint(0,100));
# parking.aparcar(matricula);
#sleep(2);
#estacionamiento = parking.sacarCoche(matricula);
#print(estacionamiento.coste);

#
# dolares = currency.getExchangeRate('USD');
# print(dolares)
#
# print(parking.verImporteHoy());
# print(parking.verImporteSemana());
# print(parking.verImporteMes());
#
# imprimirPlazasLibres(parking.getPlazasDisponibles())
# imprimirPlazasOcupadasYCoches(parking.getPlazasOcupadasYMatricula())

# i = randint(0,1000);
# db.insertUsuario(i, "nombre" + str(i), "email" + str(i), "contrasena" + str(i), matricula);
# usuario = db.getUsuario(i)
# print(usuario)
# db.updateUsuarioContrasena(i, "contrasenanueva" + str(i));
# usuario = db.getUsuario(i)
# print(usuario)
# db.updateUsuarioMatriculaCoche(i, "nuevamatricula" + str(i));
# usuario = db.getUsuario(i)
# print(usuario)

