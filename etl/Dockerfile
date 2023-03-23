FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./main.py .

RUN apt update -y  \
    && pip install --upgrade pip  \
    && pip install kafka-python