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
RUN python manage.py migrate

