FROM python:3.9-alpine3.12 AS build

RUN apk add --no-cache libstdc++ build-base libtool autoconf automake libexecinfo-dev make cmake libcurl && \
    mkdir -p /app
COPY . /app
RUN python3.9 -m pip install -r /app/requirements.txt --target /app
RUN python3.9 -m pip install awslambdaric --target /app

FROM python:3.9-alpine3.12

RUN apk add --no-cache libstdc++
WORKDIR /app
COPY --from=build /app /app
CMD [ "app.handler" ]
