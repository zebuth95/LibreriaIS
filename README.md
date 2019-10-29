# LibreriaIS

1) crear entorno virtual

  python -m venv "nombre que gustes"
  
  cd/"nombre dado"    

 linux : source "nombre dado"/bin/activate , Windows: "nombre dado"\Scripts\activate 
  
2) Intallar Django
  
  python -m pip install --upgrade pip

  pip install -r requirements.txt
  
3) Clonamos

  git clone https://github.com/zebuth95/LibreriaIS.git
  
  cd/LibreriaIS

4) Correr poyecto

  python manage.py createsuperuser

  python manage.py makemigrations 

  python manage.py migrate --run-syncdb

  python manage.py runserver
