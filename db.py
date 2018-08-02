import sqlite3;
from datetime import datetime;
import parking;


def getPlazasOcupadas():
    sql = "select plaza from estacionamiento where salida is NULL;";
    result = __queryTable__(sql);
    ocupadas = [];
    for r in result:
        ocupadas.append(int(r[0]));
    return ocupadas;


def query(matricula):
    sql = "select * from estacionamiento where matricula = '{0}';".format(matricula);
    result = __queryTable__(sql);
    list = __buildEstacionamientos__(result);
    if not list:
        return None;
    return list[0];

def update(estacionamiento):
    sql = "update 'estacionamiento' set plaza=:1, matricula=:2, entrada=:3, salida=:4, coste=:5 where pk=:6;";
    parameters = (estacionamiento.plaza,
                  estacionamiento.matricula,
                  estacionamiento.horaEntrada,
                  estacionamiento.horaSalida,
                  estacionamiento.coste,
                  estacionamiento.pk);
    __manageTable__(sql, parameters);

def insert(plaza, matricula):
    sql = "insert into 'estacionamiento' ( 'plaza', 'matricula', 'entrada', 'salida', 'coste') " \
          "VALUES (?, ?, ?, ?, ?);";
    parameters = (plaza,
                  matricula,
                  datetime.now(),
                  None,
                  None);
    __manageTable__(sql, parameters);

def queryAll():
    sql = "select * from estacionamiento;";
    result = __queryTable__(sql);
    return __buildEstacionamientos__(result);


def __manageTable__ (query, parameters):
    con = sqlite3.connect("parking.db");
    c = con.cursor();
    c.execute(query, parameters);
    con.commit();
    c.close();
    con.close();


def __queryTable__ (query):
    con = sqlite3.connect("parking.db", detect_types=sqlite3.PARSE_DECLTYPES);
    c = con.cursor();
    c.execute(query);
    result = c.fetchall();
    c.close();
    con.close();
    return result;


def __buildEstacionamientos__ (result):
    list = [];
    for r in result:
        list.append(parking.estacionamiento(r[0], r[1], r[2], r[3], r[4]));
    return list;
