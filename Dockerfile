FROM python:latest

WORKDIR /app/

COPY ./server.py /app/
COPY ./requirements.txt /app/

RUN pip install -r requirements.txt

CMD uvicorn --host=0.0.0.0 --port 8000 server:app