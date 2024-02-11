FROM python:alpine3.19
WORKDIR /app
ADD . .
RUN pip install requirements.txt
CMD pytest -k ""