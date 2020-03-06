FROM python:3-alpine

LABEL name=flask-app version=0.0.1 maintainer="Joshua Maier"

COPY flask-app /flask-app

WORKDIR /flask-app

RUN pip install -r requirements.txt

CMD ["python", "main.py"]
