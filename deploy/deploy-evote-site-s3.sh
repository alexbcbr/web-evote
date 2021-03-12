pushd ../web
npm run build
cd dist
aws s3 cp . s3://eleicoes.abcgov.com.br --region sa-east-1 --recursive --acl public-read

#curl http://eleicoes.abcgov.com.br