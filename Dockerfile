# Docker file for Xandikos.
#
# Note that this dockerfile starts Xandikos without any authentication;
# for authenticated access we recommend you run it behind a reverse proxy.

FROM debian:sid-slim
LABEL maintainer="jelmer@jelmer.uk"

ARG FIRESET_USER
ENV FIRESET_USER=$FIRESET_USER

ARG FIRESET_PASSWORD
ENV FIRESET_PASSWORD=$FIRESET_PASSWORD

ARG DATABASE_URI
ENV DATABASE_URI=$DATABASE_URI

ARG PHANTOMBUSTER_KEY
ENV PHANTOMBUSTER_KEY=$PHANTOMBUSTER_KEY

ARG PHANTOMBUSTER_LISTID
ENV PHANTOMBUSTER_LISTID=$PHANTOMBUSTER_LISTID

ARG LOGFIRE_TOKEN
ENV LOGFIRE_TOKEN=$LOGFIRE_TOKEN

ARG LOGLEVEL
ENV LOGLEVEL=$LOGLEVEL

RUN apt-get update && \
    apt-get -y install --no-install-recommends libpq-dev gcc python3-dev python3-venv python3-pip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists

WORKDIR /code
COPY dist/*.whl /code
RUN python3 -m venv /code/venv && \
    /code/venv/bin/python -m pip install /code/*.whl
VOLUME /code/data
EXPOSE 3665
ENTRYPOINT ["/code/venv/bin/python", "-m", "fireset"]
