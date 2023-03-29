print ("Archivo de pruebas")
print ("segunda_línea_de_prueba") 


### COMANDOS DE GIT ###

### COMANDOS DE CONFIGURACIÓN ###
# git config 
# git config --global alias.nombre_que_queramos "secuencia_de_comandos": podemos crear alias, asía grupamos una secuencia de comandos larga bajo un alias más cortito. EJEMPLO: git config --global alias.tree "git log --graph --decorate --all --oneline"

### COMANDOS DE ERRORES ###
# del .git\index.lock: eliminar archivos de bloqueo de git // rm - f .git/index.lock para version MAC


### COMNADOS BÁSICOS ###
# cd nombre_de_carpeta: para movernos por la carpeta en la que queremos estar
# cd --: volver a una carpeta anterior
# git init: iniciamos rama de git (Repositorio)
# git add nombre_de_archivo: añadimos un archvio o cambio al área de stage
# git add .: añadimso todos los archivos que se encuentren en la ruta en la que estamos
# git status: vemos el historial de archivos y cambios en stage
# git commit -m "comentario": sacamos la foto y le ponemos un comentario
# git log: vemos el historial de commits
# git checkout: No sirve para situarnos en un commit
# git reset: 
# git log --graph: pintamos una rama

### GIT IGNORE ###
# touch .gitignore: Para MAC y linux. De esta forma se crea un fichero oculto (hacerlo en la raíz del proyecto) y todo lo que añadamos dentro no se tendrá en cuenta para git
# echo > .gitignore: Lo mismo para Windows
# Dentro de este fchero creado tenemos que añadir con **/.Nombre_de_lo_que_queremos_ignorar


### BASICS ###
# "git checkout nombre_de_rama/hash_de_commit": Se utiliza para cambiar entre diferentes ramas de un repositorio o moverse hacia atrás y hacia adelante en una misma rama (entre los commits o tags que tengamos creados). Si queremos crear una nueva rama y movernos a ella usamos "git checkout -b nueva_rama". Para moverse entre tags usamos "git checkout tags/nombre_del_tag"
# "git diff": Nos muestra la diferencia de un archivo comparado con el último commit
# "git reset":
# "git reset --hard hash_de_commit": Deshace los cambios locales y restaura el estado del repositorio a un commit anterior de forma permanente. Funciona tanto hacia detrás como hacia delante, por lo que si volver a un commit posterior solo hay que vovler a aplciar el commando con el hash del commit al que queremos volver. 
# "git reflog": Permite ver un registro detallado de todos los cambios que se han realizado en el repositorio, incluyendo los cambios de ramas, los reseteos y los cambios de historial. Es útil para recuperar commits que han sido eliminados o perdidos. La diferencia con "git log" es que éste muestra el historial de commits del repositorio, mientras que "git reflog" muestra el historial de referencias y las acciones realizadas en ellas.
# "git tag nombre_del_tag": Sirve para etiquetar un punto específico en la historia del repositorio. Se pueden crear etquetas con anotaciones para ello usamos "git tag -a nombre_del_tag -m 'anotación que queremos dar'". También se pueden generar etiquetas en commits antiguos de la siguente manera "git tag nombre_del_tag hash_del_commit"
# "git branch nombre_nueva_rama": Permite crear nuevas ramas (al hacerlo el head sigue en el rama principal, para cambiar de rama usamos otro commando). Lo que hace es una "copia" del último commit, dónde se inicia ese nuevo flujo. Para eliminar una rama que ya no se usa utilizamos "git branch -d nombre_de_rama"
# "git switch nombre_rama_al_que_queremos_movernos": Permite movernos entre ramas (poner el head en esta rama)
# "git merge nombre_rama": Permite combinar cambios de diferentes ramas del repositorio (traer los cambios de una rama a otra). Al hacerlo git crea un nuevo commit que registra la combinación de los cambios

### OTHERS ###
# "git stash": Guardamos temporalmente solo en local, pero no hacemos commit. Con "git stash list" revisamos lo que tenemos en stash, y con "git stash pop" recuperamos lo que tenemos en stash. Y con "git stash drop" nos cargamos el stash

#GITHUB
# git push
# git pull
# git clone
