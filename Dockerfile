FROM gliderlabs/alpine:3.1

RUN apk add --update \
    python \
    python-dev \
    py-pip

RUN pip install elasticsearch-curator==3.0.0

COPY curator_wrapper.py /

ENTRYPOINT ["python", "/curator_wrapper.py"]
