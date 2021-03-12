#!/bin/sh
if [ -z "${AWS_LAMBDA_RUNTIME_API}" ]; then
    exec /bin/aws-lambda-rie /bin/python -m awslambdaric
else
    exec /bin/python -m awslambdaric
fi
