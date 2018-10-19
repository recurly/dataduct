### Development Image ###
FROM ubuntu:latest as build
LABEL app=pipelines type=runtime env=development
ARG ENVIRONMENT=qa4

WORKDIR build
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update
RUN apt-get install -y python-pip python-dev build-essential make vim git awscli
RUN apt-get install -y mysql-client mysql-common libmysqlclient-dev

COPY pipelines/requirements.txt requirements.txt
COPY pipelines/dataduct-${ENVIRONMENT}.cfg /etc/dataduct.cfg
RUN pip install --upgrade pip 
RUN pip install --upgrade virtualenv 
RUN pip install -r requirements.txt
RUN pip install mysql-python requests psycopg2

COPY dataduct /dataduct
RUN ls -l /dataduct 
RUN cd /dataduct && python setup.py install
ENV PYTHON_PATH /dataduct;/build/dataduct_custom_steps

COPY aws_config /root/.aws/config
RUN chmod 600 /root/.aws/config

CMD /bin/bash
