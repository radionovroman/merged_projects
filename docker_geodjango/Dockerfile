FROM python:3.10-slim-buster

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /djangorn

RUN apt-get update \
    && apt-get -y install netcat gcc postgresql \
    && apt-get clean

RUN apt-get update \
    && apt-get install -y binutils libproj-dev gdal-bin python-gdal python3-gdal

RUN pip install --upgrade pip

COPY ./requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .




