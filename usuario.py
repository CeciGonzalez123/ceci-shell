import getpass
import os
import shutil
import crypt
from re import split

def cmdAddUser():
	if os.getuid() == 0:
		usuario = input("Nombre de usuario: ")
		#contrasena = input("Ingrese la contrasena: ")
		while True:
			contrasena = getpass.getpass("contrasena: ")
			contrasena2 = getpass.getpass("vuelva a ingresar la contrasena: ")
			if contrasena == contrasena2:
				break
		
		ip = input("Ingrese su ip: ")
		print("Introduzca el nuevo valor, o presione INTRO para el predeterminado")
		nombre = input("Nombre completo :")
		nrotel= input("Numero de Telefono :")
		otro= input("Otro[] :")
		print("Ingrese su horario de trabajo : ")
		id = assignid()

		while True:
			horario_de_entrada = input("Ingrese horario entrada(formato 00:00): ")
			if validar_horario(horario_de_entrada):
				break
			else:
				print("respete el formato: 00:00")
		while True:
			horario_de_salida = input("Ingrese horario salida(formato 00:00): ")
			if validar_horario(horario_de_salida):
				break
			else:
				print("respete el formato: 00:00")
		mensaje = usuario + " " + ip + " " + horario_de_entrada + " " + horario_de_salida
		print(mensaje)
		info = input("confirme los datos agregados [Y/N]: ")
		if info == "Y" or info == "y":
			try:
				usuario_file = usuario + ":x:" + id + ":" + id + ":"  
				other =  nombre + "," + nrotel + "," + otro + ":" 
				home_bash = "/home/" + usuario + ":/bin/bash" + "\n"
				string = usuario_file + other + home_bash
				archivo = open("/etc/passwd", "a") 
				archivo.writelines(string) #Se agrega el nuevo usuario en la ruta /etc/passwd
				archivo.close()
				grupo = usuario +":x:" + id +":" + "\n"
				archivo2 = open("/etc/group", "a")
				archivo2.writelines(grupo) #Se le asigna un grupo al nuevo usuario en la ruta /etc/group
				archivo2.close()
				shutil.copytree("/etc/skel", "/home/" + usuario)
				usuario_file = usuario + ":" + crypt.crypt(contrasena2,crypt.mksalt(crypt.METHOD_SHA512)) + ":18944:0:99999:7:::\n"
				with open("/etc/shadow", "a") as file:
					file.write(usuario_file)
					file.close()
				mensaje = "adduser: se agrego el usuario " + usuario
				print(mensaje)
				msj=usuario + ' ' + ip + ' ' + horario_de_entrada + ' ' + horario_de_salida

			except:
				mensaje = "Error al agregar usuario"
				print(mensaje)
		else:
			mensaje = "adduser: se cancelo el registro de usuario"
			print(mensaje)
	else:
		mensaje = "adduser: solo root puede agregar usuarios"
		print(mensaje)

def assignid():
	with open("/etc/passwd") as file: #Se accede al archivo donde se encuentran los usuarios
			for line in file:
				pass
			last_line = line #Se guarda la id del ultimo usuario

	idchar = split("\D+", last_line)
	id = int(idchar[1])
	flag=0
	file = open("/etc/passwd", "r")
	while flag == 0:
		id = id +1 #Se le suma 1 a la id del usuario anterior para obtener una nueva id unica
		id = str(id)
		if id in file:
			flag = 0
		else:
			flag=1
	file.close()
	return id
