FROM python:2.7
MAINTAINER Ravi RT Merugu <rrmerugu@gmail.com>
ENV PYTHONUNBUFFERED 1

ARG build_env
ENV BUILD_ENV ${build_env}

# create webapp folder in the container
RUN [ -d /webapp ] || mkdir /webapp;
COPY ./webapp/ /webapp
COPY ./requirements/ /requirements
WORKDIR /webapp

RUN pip install -r /requirements/requirements.txt
RUN pip install uwsgi

RUN python manage.py collectstatic --noinput --verbosity=0
RUN python manage.py migrate

EXPOSE 8000

CMD uwsgi --http :8000 --wsgi-file coderplex_apis/wsgi.py --master
