FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y python3 python3-pip git && \
    apt-get clean

WORKDIR /hbnb

COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 5000
