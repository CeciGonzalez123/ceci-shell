![](https://i.postimg.cc/HsYp7srS/ceci-logo.png)

### Requisitos
----
#### Instalar los siguientes módulos de python
- pip install colorama
- pip install emoji
- pip install psutil

#### Crear archivos para registro de logs
- touch /var/log/shell/accion.log
- touch /var/log/shell/sesion.log
- touch /var/log/shell/ftp.log
- touch /var/log/shell/sistema.log

##### Aplicar permisos
- chamox -R 775 /var/log/shell

### Instalación

#### Clonar repositorio
- git clone repor-ceci-shell

#### Preparar arranque automático

- touch /etc/profile
- vi /etc/profile
   #!/bin/bash <br>
   cd /sources/ceci-shell <br>
   python3 main.py <br>
   
- Asignar permisos de ejecucion
  - chmox +x /etc/profile
  - Ejecutar comando source o reiniciar sistema

----

## Table of Contents<br>
- [Despliegue de ayuda con comandos disponibles](#ayuda)<br>
- [Copiar archivo(s) y directorio(s)](#copiar)<br>
- [Mover archivo(s) y directorio(s)](#mover)<br>
- [Renombrar archivo o carpeta](#renombrar)<br>
- [Listar contenido de una ruta](#listar)<br>
- [Crear directorio(s)](#crear-directorio)<br>
- [Cambiar de directorio](#cambiar-a-directorio)<br>
- [Otorgar permiso a archivo o directorio](#permiso-de-archivos-o-carpetas)<br>
- [Cambiar propiedad de archivo o directorio](#propiedad-de-archivo-o-carpeta)<br>
- [Mostrar ruta actual](#mostrar-ruta-actual)<br>
- [Ver historial de comandos ejecutados](#historial)<br>
- [Buscar coincidencias de texto en archivo](#buscar)<br>
- [Ejecutar comandos no implementados](#ejecutar)<br>
- [Transferir archivo vía FTP](#transferir-archivo-vía-ftp)<br>
- [Matar procesos](#matar-procesos)<br>
- [Levantar procesos en segundo plano](#levantar-proceso-en-segundo-plano)<br>
- [Detener proceso en segundo plano](#detener-proceso-en-segundo-plano)<br>
- [Crear usuario](#crear-usuario)<br>
- [Cambiar contraseña de usuario](#cambiar-clave)<br>
- [Salir de la terminal](#salir-de-la-terminal)<br>


# Comandos de ceci-shell>

## Ayuda
- Escriba comando **ayuda** para obtener lista de los comandos disponibles

## Copiar
> Sintaxis:  copiar [origen_1] [origen_1] [origen_n] [destino]

- Ingrese comando **copiar** para copiar archivo(s) o carpetas(s)  a una ruta destino

## Mover
> Sintaxis:  mover [origen_1] [origen_1] [origen_n] [destino]

- Ingrese comando **mover** para mover archivo(s) o carpetas(s) a una ruta destino

## Renombrar
> Sintaxis:  renombrar [archivo] [nuevo_nombre]

- Ingrese comando **renombrar** para cambiar nombre de archivo o carpeta

## Listar
> Sintaxis:  listar [ruta] (opcionar)

- Ingrese comando **listar** para desplegar contenido de carpeta actual o directorio indicado como parametro

## Crear directorio
> Sintaxis:  creadir [dir_1] [dir_2] [dir_3]

- Ingrese comando **creadirar** para crear uno varios directorios

## Cambiar a directorio
> Sintaxis:  ir [directorio]

- Ingrese comando **ir** para cambirse a la ruta indicada

## Permiso de archivos o carpetas
> Sintaxis:  permiso [recurso] [numero_permiso]

- Ingrese comando **permiso** para asignar permiso a achivos o carpetas

## Propiedad de archivo o carpeta
> Sintaxis:  propiedad [archivo]

- Ingrese comando **propiedad** para cambiar el dueño del archivo o carpeta, sele pedira nombre de usuario y grupo

## Mostrar ruta actual
> Sintaxis:  ruta

- Ingrese comando **ruta** para desplegar ruta actual

## Historial
> Sintaxis:  historial

- Ingrese comando **historial** muestra el historial de comandos ejecutados

## Buscar
> Sintaxis:  buscar [archivo] [cadena]

- Ingrese comando **buscar** para realizar búsqueda de cadena de texto en el archivo indicado

## Ejecutar
> Sintaxis:  ejecutar [comando]

- Ingrese comando **ejecutar** para ejecutar comandos no implementados en la ceci-shell

## Transferir archivo vía FTP
> Sintaxis:  transferir [archivo]

- Ingrese comando **tansferir** para transferir el archivo indicado por vía FTP, se le solicitará nombre o ip del servidor FTP y las credenciales de usuario

## Matar procesos
> Sintaxis:  matar

- Ingrese comando **matar** para ver procesos activos y detenerlos indicando la PID del proceso, presione **enter** para salir

## Levantar proceso en segundo plano
> Sintaxis:  levantar

- Ingrese comando **levantar** para iniciar un proceso definido en segundo plano

## Detener proceso en segundo plano
> Sintaxis:  detener

- Ingrese comando **detener** para detener proceso en segundo plano

## Crear usuario
> Sintaxis:  crearusuario [nomber]

- Ingrese comando **propiedad** para crear nuevo usuario, se le solicitará indicar clave, nombre completo, hora de entrda y hora de salida "requiere privilegio root"

## Cambiar clave
> Sintaxis:  cambiarclave [usuaeio]

- Ingrese comando **cambiarclave** para cambiar la contraseña del usuario indicado "requiere privilegio root"

## Salir de la terminal
> Sintaxis:  salir

- Ingrese comando **salir** para salir de la ceci-shell
