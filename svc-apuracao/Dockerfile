FROM python:3.8
RUN pip install flask
COPY app/ /app
WORKDIR /app
EXPOSE 80
CMD python -m flask run --host=0.0.0.0 --port=80