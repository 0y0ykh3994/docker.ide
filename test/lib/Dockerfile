FROM python:3.9-alpine3.12 AS builder
RUN apk add --no-cache build-base libtool autoconf automake libexecinfo-dev make cmake libcurl && \
    mkdir -p /app && \
    python3.9 -m pip install awslambdaric --target /app
COPY requirements.txt /app
RUN  pip install -r /app/requirements.txt --target /app

FROM amazonlinux
RUN yum update -y && yum install -y python3 pip3 libstdc++ && \
    mkdir -p /app && \
    cd /app && \
    yum clean all

COPY --from=builder /app /app
COPY app.py /app

