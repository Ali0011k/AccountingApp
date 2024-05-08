python manage.py makemigrations --no-input
python manage.py migrate --no-input
python manage.py createsuperuser --username $USERNAME --email $EMAIL --no-input
python manage.py runserver 0.0.0.0:8000
