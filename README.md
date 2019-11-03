# LibreriaIS

## Instrucciones para correr el proyecto

1.**crear entorno virtual**

    > python -m venv <NOMBRE_DEL_ENTORNO>
    // ejemplo: python -m venv biblioteca
    
    > cd/<NOMBRE_DEL_ENTORNO>

En Linux:  

    > source <NOMBRE_DEL_ENTONRNO>/bin/activate

En Windows:  

    > source <NOMBRE_DEL_ENTONRNO>/Scripts/activate

2.**Clonar el repositorio**

    > git clone https://github.com/zebuth95/LibreriaIS.git
  
    > cd/LibreriaIS

3.**Installar Django**

    > python -m pip install --upgrade pip

    > pip install -r requirements.txt
  

4.**Correr poyecto**

    > python manage.py createsuperuser

    > python manage.py makemigrations 

    > python manage.py migrate --run-syncdb

    > python manage.py runserver
