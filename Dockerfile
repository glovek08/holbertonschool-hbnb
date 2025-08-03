FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1
ENV FLASK_APP=app.py
ENV FLASK_ENV=development

#Sys dep
RUN apt-get update && \
    apt-get install -y \
        python3 \
        python3-pip \
        python3-venv \
        python3-dev \
        default-libmysqlclient-dev \
        build-essential \
        pkg-config \
        git \
        curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /hbnb

RUN python3 -m venv venv

COPY requirements.txt .

RUN ./venv/bin/pip install --upgrade pip && \
    ./venv/bin/pip install --no-cache-dir -r requirements.txt

COPY app/ ./app/
COPY static/ ./static/
COPY templates/ ./templates/
COPY swaggerui/ ./swaggerui/
COPY app.py .
COPY config.py .

RUN mkdir -p instance

# Create non-root user for security
RUN useradd --create-home --shell /bin/bash hbnb && \
    chown -R hbnb:hbnb /hbnb

USER hbnb


EXPOSE 5000


HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:5000/api/v1/ || exit 1

CMD ["./venv/bin/python3", "app.py"]
