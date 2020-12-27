pushd ../web-auth
aws s3 sync . s3://w2.abcgov.com.br --region us-east-1 --acl public-read
