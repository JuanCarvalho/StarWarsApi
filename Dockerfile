FROM python:3.10

WORKDIR /app

COPY ./app /app
COPY ./entrypoint.sh /app/entrypoint.sh

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt


ENTRYPOINT ["/app/entrypoint.sh"]
