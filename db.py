import sqlite3;
from datetime import datetime;
import parking;
import administracion as admin;


########################################
# Usuarios

def insertUsuario(id, nombre, email, contrasena, matriculacoche):
    sql = "insert into 'usuarios' ( 'id', 'nombre', 'email', 'contrasena', 'matriculacoche') " \
          "VALUES (?, ?, ?, ?, ?);";
    parameters = (id,
                  nombre,
                  email,
                  contrasena,
                  matriculacoche);
    __manageTable__(sql, parameters);

def updateUsuarioMatriculaCoche(id, matriculacoche):
    sql = "update 'usuarios' set matriculacoche=:0 where id=:1;";
    parameters = (matriculacoche, id);
    __manageTable__(sql, parameters);

def updateUsuarioContrasena(id, contrasena):
    sql = "update 'usuarios' set contrasena=:0 where id=:1;";
    parameters = (contrasena, id);
    __manageTable__(sql, parameters);

def deleteUsuario(id):
    sql = "delete from 'usuarios' where id='{0}';".format(id)
    __manageTable__(sql);

def getUsuario(id):
    sql = "select * from 'usuarios' where id='{0}';".format(id)
    result = __queryTable__(sql);
    list = __buildUsers__(result);
    if not list:
        return None;
    return list[0];

def queryAllUsuarios():
    sql = "select * from 'usuarios';";
    result = __queryTable__(sql);
    return __buildUsers__(result);

########################################
# Estacionamientos

def getEstacionamientoDesde(inicio):
    sql = 'select * from estacionamiento where entrada > ?;';
    parametros = (inicio,);
    result = __queryTable__(sql, parametros);
    list = __buildEstacionamientos__(result);
    return list;

def getPlazasOcupadasYMatricula():
    sql = "select plaza, matricula from estacionamiento where salida is NULL;";
    result = __queryTable__(sql);
    ocupadas = [];
    for r in result:
        ocupadas.append((int(r[0]), r[1]));
    return ocupadas;

def getPlazasOcupadas():
    sql = "select plaza from estacionamiento where salida is NULL;";
    result = __queryTable__(sql);
    ocupadas = [];
    for r in result:
        ocupadas.append(int(r[0]));
    return ocupadas;

def queryEstacionamientoActual(matricula):
    sql = "select * from estacionamiento where matricula = '{0}' and salida is NULL;".format(matricula);
    result = __queryTable__(sql);
    list = __buildEstacionamientos__(result);
    if not list:
        return None;
    return list[0];

def updateEstacionamiento(estacionamiento):
    sql = "update 'estacionamiento' set plaza=:1, matricula=:2, entrada=:3, salida=:4, coste=:5 where pk=:6;";
    parameters = (estacionamiento.plaza,
                  estacionamiento.matricula,
                  estacionamiento.horaEntrada,
                  estacionamiento.horaSalida,
                  estacionamiento.coste,
                  estacionamiento.pk);
    __manageTable__(sql, parameters);

def insertEstacionamiento(plaza, matricula):
    sql = "insert into 'estacionamiento' ( 'plaza', 'matricula', 'entrada', 'salida', 'coste') " \
          "VALUES (?, ?, ?, ?, ?);";
    parameters = (plaza,
                  matricula,
                  datetime.now(),
                  None,
                  None);
    __manageTable__(sql, parameters);

def queryAllEstacionamientos():
    sql = "select * from estacionamiento;";
    result = __queryTable__(sql);
    return __buildEstacionamientos__(result);


def __manageTable__ (query, parameters=()):
    con = sqlite3.connect("parking.db");
    c = con.cursor();
    c.execute(query, parameters);
    con.commit();
    c.close();
    con.close();


def __queryTable__ (query, parameters=()):
    con = sqlite3.connect("parking.db", detect_types=sqlite3.PARSE_DECLTYPES);
    c = con.cursor();
    c.execute(query, parameters);
    result = c.fetchall();
    c.close();
    con.close();
    return result;


def __buildUsers__ (result):
    list = [];
    for r in result:
        list.append(admin.usuario(r[0], r[1], r[2], r[3], r[4]));
    return list;


def __buildEstacionamientos__ (result):
    list = [];
    for r in result:
        list.append(parking.estacionamiento(r[0], r[1], r[2], r[3], r[4], r[5]));
    return list;
