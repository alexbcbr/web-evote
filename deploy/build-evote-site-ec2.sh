pushd ../web
npm run build
cd dist
zip -r evote-web.zip ./
#aws s3 cp evote-web.zip s3://alexbc.demoapp --region us-east-1 --acl public-read
aws s3 cp evote-web.zip s3://alexbc.demoapp --region us-east-1
rm evote-web.zip
