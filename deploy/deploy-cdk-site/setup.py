import setuptools

with open("README.md") as fp:
    long_description = fp.read()


setuptools.setup(
    name="deploy_cdk_site",
    version="0.0.1",

    description="A sample CDK Python app",
    long_description=long_description,
    long_description_content_type="text/markdown",

    author="author",

    package_dir={"": "deploy_cdk_site"},
    packages=setuptools.find_packages(where="deploy_cdk_site"),

    install_requires=[
        "aws-cdk.core==1.105.0",
        "aws-cdk.aws_iam==1.105.0",
        "aws-cdk.aws_sqs==1.105.0",
        "aws-cdk.aws_sns==1.105.0",
        "aws-cdk.aws_sns_subscriptions==1.105.0",
        "aws-cdk.aws_s3==1.105.0",
        "aws-cdk.aws_elasticloadbalancing=1.105.0"
    ],

    python_requires=">=3.6",

    classifiers=[
        "Development Status :: 4 - Beta",

        "Intended Audience :: Developers",

        "License :: OSI Approved :: Apache Software License",

        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",

        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",

        "Typing :: Typed",
    ],
)
