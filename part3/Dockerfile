FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

# Install Python, pip, and venv
RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-venv git && \
    apt-get clean

WORKDIR /hbnb

COPY requirements.txt .

RUN python3 -m venv venv && \
    ./venv/bin/pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["./venv/bin/python3", "app.py"]