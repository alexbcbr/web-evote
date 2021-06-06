# Build container image locally

docker build -t local_votacao_flask:latest .
docker run -p 5000:5000 local_votacao_flask

curl http://0.0.0.0:5000/