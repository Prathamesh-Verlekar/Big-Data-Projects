## Getting started with AWS + Lambda

## About

**This demonstrates the implementation of AWS CLI and other services like IAM, Amazon S3, comprehend and lambda.**


![Services](https://user-images.githubusercontent.com/59594174/109194273-405b6380-7767-11eb-9d3b-2205df0addf6.png)


## Requirements

1. Creating an AWS account

2. Configuring AWS CLI

3. Configuring AWS on your system

4. Getting started with IAM ( Identity Access Management )

5. Creating a virtual environment

6. Installing all the required packages in this virtual env - `first-lambda-function`

**Faker:**  Faker is a Python package that generates fake data for you. Whether you need to bootstrap your database, create good-looking XML documents, fill-in your persistence to stress test it, or anonymize data taken from a production service.

**Boto3:** Boto3 is the Amazon Web Services (AWS) Software Development Kit (SDK) for Python, which allows Python developers to write software that makes use of services like Amazon S3 and Amazon EC2.

```
- pip3 install Faker
- pip3 install boto3
```

## Test Results

#### Creating Amazon S3 Bucket

![S3](https://user-images.githubusercontent.com/59594174/109194316-494c3500-7767-11eb-81d0-f89879293d2b.png)


**Amazon S3** - a simple storage service is a scalable, high-speed, web-based cloud storage service. 


- Ensure below mentioned rules while creating any S3 bucket:
- Block all public access
- Disable bucket versioning
- Disable encryption


#### Contents

- `s3_upload.py` - Python script to generate some fake data using Faker and uploadthe same to your S3 Bucket 
- `s3_download.py` - Downloading the file from S3 to your local environemnt 
- `comprehend_function.py` - Using AWS Comprehend to implement sentiment analysis


## Lambda-serverless-py

**AWS Lambda** is a serverless compute service that lets you run code without provisioning or managing servers, creating workload-aware cluster scaling logic, maintaining event integrations, or managing runtimes. With Lambda, you can run code for virtually any type of application or backend service - all with zero administration. Just upload your code as a ZIP file or container image, and Lambda automatically and precisely allocates compute execution power and runs your code based on the incoming request or event, for any scale of traffic.


![lambda](https://user-images.githubusercontent.com/59594174/109194337-4fdaac80-7767-11eb-8598-060c8dd09af3.png)


1. Creating a basic `test-lambda` function

2. Creating an IAM role `lambda_basic_execution` with following privileges:

- Lambda basic execution
- Amazon S3 full access
- Amazon DynamoDB full access

3. Executing the ‘test-lambda function’

### Deploying Lambda function

1. Creating a virtual environment

2. Installing required packages

```
- pip3 install python-lambda
- pip3 install pandas

```

3. Initiating lambda deployment

`lambda.py init`

Three files will be generated viz. Config.yaml, events.json, service.py

The **service.py** is the file we will be using. We can edit service.py with our Python code.

4. **Deploying lambda function**

`lambda.py deploy`






