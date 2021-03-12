ARG FUNCTION_DIR="/home/app"

FROM amazonlinux:2 AS builder
ARG FUNCTION_DIR
WORKDIR ${FUNCTION_DIR}
COPY . ${FUNCTION_DIR}
RUN yum install -y python3.7 python3-devel.x86_64 gcc* gzip make autoconf automake libtool
RUN python3.7 -m pip install cmake && \
    python3.7 -m pip install awslambdaric --target ${FUNCTION_DIR} && \
    python3.7 -m pip install -r requirements.txt --target ${FUNCTION_DIR}

FROM amazonlinux:2
ARG FUNCTION_DIR
WORKDIR ${FUNCTION_DIR}
RUN yum install -y python3.7 python3-devel.x86_64
COPY --from=Builder ${FUNCTION_DIR} ${FUNCTION_DIR}

ENTRYPOINT [ "/bin/python3.7", "-m", "awslambdaric" ]
CMD [ "app.handler" ]
