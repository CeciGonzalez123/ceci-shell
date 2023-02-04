# LFS DOCUMENTACIÓN
## ETAPA 1: 

**Resumen breve de los comandos ejecutados, sin entrar en detalle de los parámetros.**
- Solo lectura, no hay comandos.

**Problemas encontrados y las soluciones implementadas**
- No hubo problemas.

**Consideraciones a tener en cuenta:**
- Ninguna.

## ETAPA 2:
**Resumen breve de los comandos ejecutados, sin entrar en detalle de los parámetros.**
- cat
- cfdisk
- fdisk
- mkfs
- mkswap
- cd
- export
- mkdir
- mount
- chmod
- wget
- chown
- groupadd
- useradd
- passwd
- exit
- su 
- ls
- source

**Problemas encontrados y las soluciones implementadas**

- Al comienzo cree un disco que no tenía suficiente espacio, luego instale un disco de 1TB en mi computadora porque más adelante tuve problemas en el capítulo 8 con las capturas y cree una partición de 35 GB  para el LFS por recomendación y para el host del Ubuntu server utilice 10GB.

**Consideraciones a tener en cuenta:**

- Ingresar como usuario root, tomar capturas si es posible de cada sección de los capítulos.

## ETAPA 3

**Resumen breve de los comandos ejecutados, sin entrar en detalle de los parámetros.**

- echo
- cd
- mkdir
- make
- make install
- configure
- tar 
- mv 
- rm
- cat
- find
- pushd
- popd
- ln
- ls
- sed
- chown
- mount
- chroot
- install
- chgrp
- exec
- cp
- mountpoint
- umount
- exit

**Problemas encontrados y las soluciones implementadas**

- Tuve problemas en el capitulo 7 con en usuario chroot ya dejo de ingresar cada vez que probaba en la maquina por lo que volvi a hacer el capitulo 7 y ya pudo ingresar de vuelta.

**Consideraciones a tener en cuenta:**

- Ingresar como usuario root, tomar capturas si es posible de cada sección de los capítulos, hacer el capitulo 7 sin parar.

## ETAPA 4

**Resumen breve de los comandos ejecutados, sin entrar en detalle de los parámetros.**

- echo
- grep
- patch
- cd
- mkdir
- make
- make test
- make install
- make check
- makeinfo
- configure
- tar
- rm
- cat
- find
- ls
- ln
- sed
- chmod
- mount
- chroot
- install
- wget
- umount
- exit
- logout
-  cat
-  unmount
-  ip addr
-  vi
-  history

**Problemas encontrados y las soluciones implementadas**

- En el capitulo 8 tuve problemas al hacer make test con librerías de shadow y gettext por lo que volvi a hacer desde las capturas anteriores a estos capítulos, y seguía con el error decidí continuar por recomendación y no hubo problemas.

**Consideraciones a tener en cuenta**

- Siempre controlar que la variable $LFS= /mnt/lfs, estar dentro de la carpeta mnt/lfs/sources y que los paquetes se descarguen ahí, entrar como usuario chroot siempre

**Para el capitulo 9 tener en cuenta lo siguiente:**

    - Hacer ip address para averiguar tu mcadress
    - <network-device-name>: Hacer el comando sudo lshw -class network -short, y poner lo que sale en la columna device
    - <Your Domain Name>: localhost
    - <IP address of your primary nameserver>: 8.8.8.8 2001:4860:4860::8888
    - <IP address of your secondary nameserver>: 8.8.4.4 2001:4860:4860::8844
    - <FQDN>: <tu-nombre>.localsite
    - <HOSTNAME>: El resultado de hacer el comando hostname en el Ubuntu.
    - Capitulo 9.3 no es necesario hacer
    - Capitulo 9.4 no es necesario hacer
    - En el capitulo 9.6 cambiar la variable de keymap y colocar “us”
    - En el capitulo 9.7 buscar la iso de Paraguay al ejecutar locale-a y colocar en <locale-name>

**Para el capitulo 10 tener en cuenta lo siguiente:**

- Usar el /etc/fstab para determinar dónde se montarán los sistemas de archivos de forma predeterminada, en qué orden y cuáles se deben comprobar.
- En el 10.3. Linux-6.1.9 al aparecer el menú azul, controlar con la nota que marcar y que no.
- En el 10.4.2 tener en cuenta que el libro dice que GRUB utiliza su propia estructura de nombres para unidades y particiones en forma de (hdn,m), donde n es el número de disco duro y m es el número de partición. Los números de disco duro comienzan desde cero, pero los números de partición comienzan desde uno para particiones normales, esto hay que considerar en el 10.4.4
- Para el dual boot use el archivo del 10.4.4
