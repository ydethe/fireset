FROM python:3.10-alpine

ARG SERVER_URL
ENV SERVER_URL=$SERVER_URL

ARG LOGFIRE_TOKEN
ENV LOGFIRE_TOKEN=$LOGFIRE_TOKEN

ARG DATABASE_URI
ENV DATABASE_URI=$DATABASE_URI

ARG PORT
ENV PORT=$PORT

RUN apk add --no-cache gcc musl-dev linux-headers py3-psycopg2

WORKDIR /code
COPY dist/*.whl /code
RUN pip install /code/*.whl
EXPOSE $PORT
CMD ["sh", "-c", "uvicorn fireset.server:app --host 0.0.0.0 --port ${PORT}"]
