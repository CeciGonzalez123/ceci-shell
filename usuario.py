import getpass
import os
import socket
import time
from re import split
import crypt
import util
import logger

def crea_usuario(username):
	""""
	Crear usuario y solicita clave, nombre, hora de entrada y hora de salida
	"""
	
	# Verifica si usuario existe
	if util.existe_usuario(username):
		util.respuesta(f"{username} ya existe", "error")
		return True

	# Generar id de usuario
	uid = util.generar_id()

	# Crer perfil de usuario
	perfil = "/home/" + username 
	if(os.path.exists("/home/" + username) == 0):
		os.mkdir(perfil,int('755',8))

	# Solicitar clave
	password = solicitar_clave()

	# Solicitar informacion personal
	fullname=input("Fullname: ")
	ip = str(socket.gethostbyname(socket.gethostname()))
	entrada=input("Hora de Entrada HH:MM: ")
	entrada=entrada.replace(":","")
	salida=input("Hora de Salida HH:MM: ")
	salida=salida.replace(":","")
	epoch = int(time.time())

	# Agregar informacion en archivos en shadow
	info = f"{username}:{password}:{epoch}:0:99999:7:::\n"
	util.agregar_informacion("/etc/shadow", info)

	# Agregar informacion en archivos en passwd
	info = f"{username}:x:{uid}:{uid}:{fullname},{ip},{entrada},{salida}:{perfil}:/bin/bash\n"
	util.agregar_informacion("/etc/passwd", info)

	# Agregar informacion en archivos en group
	info = f"{username}:x:{uid}:\n"
	util.agregar_informacion("/etc/group", info)

	util.respuesta(f"Usuario {username} creado con exito")
	logger.log(f"Creado usuario {username}", "sistema")

def cambiar_clave(username):
	"""
	Realiza cambio de clave del usuario indicado y pide nueva clave y confirmacion
	"""

	# Solicita nueva clave 	
	new_password = solicitar_clave()

	# Verifica lectura de archivo de sistema password
	try:
		with open("/etc/passwd", "r") as passwd_file:
			lines = passwd_file.readlines()
	except Exception as e:
		msg = f"Error al leer /etc/passwd: {e}"
		util.respuesta(msg, "error")
		logger.log(msg, "sistema")

	# Busca al usuario indica y escribe nueva clave encriptada
	try:
		with open("/etc/passwd", "w") as passwd_file:
			for line in lines:
				parts = line.strip().split(":")
				if parts[0] == username:
					parts[1] = new_password
				passwd_file.write(":".join(parts) + "\n")
	except Exception as e:
		msg = f"Error al escribir en /etc/passwd: {e}"
		util.respuesta(msg, "error")
		logger.log(msg, "sistema")

	msg = f"Se cambio password de usuario: {username}"
	util.respuesta(msg)
	logger.log(msg, "sistema")

def solicitar_clave(): 
	"""
		Retorna password encriptado
	"""
	while True:
		password = getpass.getpass(prompt="Ingrese password: ")
		confirmacion = getpass.getpass(prompt="Confirme password: ")

		if password != confirmacion:       
			util.respuesta("Clave y confirmacion no coinciden, intente nuevamente")
			continue 
		else:
			return crypt.crypt(password, "22")
