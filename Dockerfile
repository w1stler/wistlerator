FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /wistlerator
WORKDIR /wistlerator
COPY requirements.txt /wistlerator/
RUN pip install -r requirements.txt
COPY . /wistlerator/