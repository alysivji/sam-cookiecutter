import os

ENVIRONMENT = os.getenv("ENVIRONMENT", None)

# local development configuration
LOCAL_DEV = ENVIRONMENT == "local"
LOCALSTACK_HOST = os.getenv("LOCALSTACK_HOST", "localstack")
LOCALSTACK_ENDPOINT = f"http://{LOCALSTACK_HOST}:4566"
