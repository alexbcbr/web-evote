# Build container image locally

docker build -t flask_json:latest .
docker run -p 5000:5000 flask_json

curl http://0.0.0.0:5000/