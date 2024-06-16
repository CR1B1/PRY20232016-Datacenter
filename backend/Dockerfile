FROM python:3.8

ARG  DJANGO_SUPERUSER_PASSWORD=admin
ARG  DJANGO_SUPERUSER_EMAIL=admin@admin.com
ARG  DJANGO_SUPERUSER_USERNAME=admin

# install python dependencies

RUN python3 -m venv /venv
RUN . /venv/bin/activate

RUN pip install --upgrade pip
COPY requirements.txt /tmp/requirements.txt
RUN python3 -m pip install --no-cache-dir -r /tmp/requirements.txt
RUN python3 -m pip install --no-cache-dir tensorflow

EXPOSE 8000

COPY . .


RUN python manage.py collectstatic --noinput
# running migrations
RUN python manage.py makemigrations
RUN python manage.py makemigrations authentication
RUN python manage.py makemigrations public
RUN python manage.py migrate

# create superuser

RUN python manage.py createsuperuser --noinput --email $DJANGO_SUPERUSER_EMAIL; exit 0
RUN nohup jupyter lab --port=6000 --no-browser --allow-root &
RUN pwd

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
