FROM python:3.8-buster as builder

WORKDIR /opt/dev

COPY animal_ai/AnimalAI-Olympics/example/requirements.txt requirements.txt

RUN pip install -U pip \
    && pip install -r requirements.txt
