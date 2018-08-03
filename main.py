import gui;
import administracion as admin;

seleccion = gui.mainMenu();
seleccion = input("Por favor, elija que tipo de usuario es");
usuario = input("Por favor inserte el id de usuario: ");
contrasena = input("Por favor inserte la contrasena: ")
if seleccion == 0:
    id, admin = admin.logarUsuarioAdmin(usuario, contrasena);
if seleccion == 1:
    id, admin = admin.logarUsuario(usuario, contrasena)

//TODO while not authenticated

while True:
    seleccion = gui.userMenu();
    // add both users flow