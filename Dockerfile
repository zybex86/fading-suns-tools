FROM python:3.8-alpine
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -U pip
RUN pip install -r /requirements.txt

RUN mkdir /fst
WORKDIR /fst
COPY ./fst /fst

RUN adduser -D user
USER user
