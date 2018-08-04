import db;

USUARIO_ADMIN = 'ROOT';
PASS_ADMIN = 'ROOT';

class usuario():
    def __init__(self, id, nombre, email, contrasena, matriculacoche):
        self.id = id;
        self.nombre = nombre;
        self.email = email;
        self.contrasena = contrasena;
        self.matriculacoche = matriculacoche;

    def __str__(self):
        return "id [{0}] nombre [{1}] email [{2}] contrasena [{3}] matricula [{4}]".format(self.id, self.nombre, self.email, self.contrasena, self.matriculacoche)

def getMatriculaDeUsuario(userId):
    user = db.getUsuario(userId)
    return user.matriculacoche;


def logar(usuario, contrasena):
    if usuario == USUARIO_ADMIN:
        if contrasena == PASS_ADMIN:
            return USUARIO_ADMIN, True;
    return logarUsuario(usuario, contrasena);

def logarUsuario(usuario, contrasena):
    usr = db.getUsuario(usuario);
    if usr is None:
        return None, False;
    if usr.contrasena.upper() == contrasena:
        return usr.id, False;

    return None, False;

def altaUsuario(id, nombre, email, contrasena, matriculacoche):
    try:
        db.insertUsuario(id, nombre, email, contrasena, matriculacoche);
    except Exception as ex:
        print("Ha habido un problema dando de alta al usuario" + str(ex));

def bajaUsuario(id):
    try:
        db.deleteUsuario(id);
    except Exception as ex:
        print("Ha habido un problema dando de baja al usuario [" + id + "]" + str(ex));


def queryUsuarios():
    try:
        return db.queryAllUsuarios();
    except Exception as ex:
        print("Ha habido un problema seleccionando todos los usuarios" + str(ex));