# Creating LocalStack resources for testing
import boto3

dynamodb = boto3.resource("dynamodb", endpoint_url="http://0.0.0.0:4566")
table = dynamodb.create_table(
    TableName="{{ cookiecutter.dynamodb_name }}",
    KeySchema=[
        {"AttributeName": "organization_id", "KeyType": "HASH"},
        {"AttributeName": "key", "KeyType": "RANGE"},
    ],
    AttributeDefinitions=[
        {"AttributeName": "organization_id", "AttributeType": "S"},
        {"AttributeName": "key", "AttributeType": "S"},
    ],
    ProvisionedThroughput={"ReadCapacityUnits": 5, "WriteCapacityUnits": 5},
)
