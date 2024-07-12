FROM python:3
LABEL authors="kostik80_80@gmail.ru"
WORKDIR /network
COPY ./requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir
COPY . .