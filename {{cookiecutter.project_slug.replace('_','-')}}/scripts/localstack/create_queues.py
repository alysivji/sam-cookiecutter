# Creating LocalStack resources for testing
import boto3

sqs = boto3.client("sqs", endpoint_url="http://0.0.0.0:4566")

queue_name = "{{ cookiecutter.sqs_name }}"
sqs.create_queue(QueueName=queue_name)
