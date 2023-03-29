*GIT CONFIGURATION COMANDS*
git config: Used to set Git configuration variables.
 Para usar Git es necesario un nombre de usuario y un emial, para configurarlo utilizamos el siguiente comando:
  git config --global user.name "Nombre/Alias/Apellido"
  git config --global user.email "direccióndeemail@gmail.com"
 Tamibén podemos utilizar crear alias para agrupar una secuencia de comandos, por ejemplo:
  git config --global alias.<alias-name> "<git-command-sequence>" // git config --global alias.tree "git log --graph --decorate --all --oneline"

gitignore
 touch .gitignore (MAC/LINUX) y echo > .gitignore (WINDOWS). De esta forma se crea un fichero oculto (hacerlo en la raíz del proyecto) y todo lo que añadamos dentro no se tendrá en cuenta para git
 Add the files or directories you want to ignore in the .gitignore file using the format **/<file-name>

*COMANDOS DE ERRORES*
rm - f .git/index.lock (MAC/LINUX) // del .git\index.lock (WINDOWS)
 Removes Git lock files. Normalmente git los genera y los elimina, pero en caso de que produzca un error en el proceso el archivo puede quedarse sin desbloquear, esto impediría ejecutar comandos sobre él.

*COMNADOS BÁSICOS*
ls: Lists files and directories in the current repository
cd <directory-name>: Changes to the specified repository. We can concatenate <directory-name>/<directory-name>/<directory-name>
cd --: Returns to the previous repository
git init: Initializes a new Git repository
git add <file-name>: Adds a file or changes to the staging area
git add .: Adds all files in the current directory and its subdirectories to the staging area
git status: Shows the status of files and changes in the staging area
git commit -m "<commit-message>": Commits the changes with a commit message
git log: Shows the commit history
git tag <tag-name>: Creates a tag for a specific commit. Se pueden crear etquetas con anotaciones para ello usamos "git tag -a nombre_del_tag -m 'anotación que queremos dar'". También se pueden generar etiquetas en commits antiguos de la siguente manera "git tag nombre_del_tag hash_del_commit".
git checkout <branch-name/commit-hash>: Switches to a different branch or commit.  
 git checkout -b <new-branch-name>: To create a new branch a move there
 git checkout tags/<tag-name>: To move through tags
git diff: Shows the difference between the working directory and the last commit
git reset: Resets changes
 git reset --hard <commit-hash>: Resets the repository to a previous commit and discards local changes. Funciona tanto hacia detrás como hacia delante, por lo que si volver a un commit posterior solo hay que vovler a aplciar el commando con el hash del commit al que queremos volver
git reflog: Es útil para recuperar commits que han sido eliminados o perdidos. La diferencia con "git log" es que éste muestra el historial de commits del repositorio, mientras que "git reflog" muestra el historial de referencias y las acciones realizadas en ellas.
git branch <branch-name>: Creates a new branch. Lo que hace es una "copia" del último commit, dónde se inicia ese nuevo flujo.
 git branch -d <nombre_de_rama>: Para eliminar una rama que ya no se utiliza
git switch <branch-name>: Switches to a different branch
git merge <branch-name>: Merges changes from a branch to the current branch. Al hacerlo git crea un nuevo commit que registra la combinación de los cambios
git stash: Temporarily saves changes without committing them. 
 git stash list: lists all stashes
 git stash pop: retrieves the most recent stash
 git stash drop: discards the most recent stash.

#GITHUB
# git push
# git pull
# git clone
