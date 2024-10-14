FROM python:3.12-slim

WORKDIR /bot

ENV PYTHONUNBUFFERED=1

COPY . .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt