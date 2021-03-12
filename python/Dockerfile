## Base image
FROM alpine:latest AS alpine-with-python
RUN apk add --no-cache libstdc++


## dependency package
FROM alpine-with-python AS installed-lib
RUN mkdir -p /app
WORKDIR /app

RUN apk --no-cache update && \
apk add --no-cache \
python3 \
py-pip


#RUN python3 -m pip install --target=/app awslambdaric

#FROM alpine-with-python
#COPY --from=installed-lib /app /app
#COPY . /app
#COPY entry.sh /
#ENTRYPOINT [ "/entry.sh" ]
#CMD ["time_now.handler"]
