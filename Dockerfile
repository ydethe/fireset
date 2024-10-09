# Docker file for Xandikos.
#
# Note that this dockerfile starts Xandikos without any authentication;
# for authenticated access we recommend you run it behind a reverse proxy.

FROM debian:sid-slim
LABEL maintainer="jelmer@jelmer.uk"

RUN apt-get update && \
    apt-get -y install --no-install-recommends python3-dev python3-venv python3-pip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/ && \
    groupadd -g 1000 xandikos && \
    useradd -d /code -c Xandikos -g xandikos -M -s /bin/bash -u 1000 xandikos

WORKDIR /code
COPY dist/*.whl /code
RUN python3 -m venv /code/venv && \
    /code/venv/bin/python -m pip install /code/*.whl
VOLUME /data
EXPOSE 8000
USER xandikos
ENTRYPOINT ["/code/venv/bin/python3", "-m", "xandikos", "--port=8000", "--metrics-port=8001", "--listen-address=0.0.0.0", "-d", "/data"]
CMD ["--defaults"]
