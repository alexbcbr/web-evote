compile and generate jar
upload to S3
compile code with java amazon correto

sudo aws s3 cp s3://alexbc.demoapp/ThreadLeak.jar .

java -classpath ThreadLeak.jar com.chaosengineering.thread.ThreadLeakDemo