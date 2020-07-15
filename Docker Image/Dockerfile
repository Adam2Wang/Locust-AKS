FROM python:3.7-alpine3.10

COPY docker-entrypoint.sh /

RUN    apk --no-cache add --virtual=.build-dep build-base git \
    && apk --no-cache add zeromq-dev libffi-dev \
    && python3 -m pip install --no-cache-dir git+https://github.com/locustio/locust.git@1.0.3#egg=locustio  \
    && apk del .build-dep \
    && chmod +x /docker-entrypoint.sh \
    && mkdir /locust
WORKDIR /locust
EXPOSE 8089 5557 5558

ENTRYPOINT ["/docker-entrypoint.sh"]