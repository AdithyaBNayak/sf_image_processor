import os
import boto3
from aws_lambda_powertools import Logger

logger = Logger()

s3_client = boto3.client('s3')
DESTINATION_BUCKET = os.environ['DEST_BUCKET']
REGION = os.environ['REGION']

def copy_file(event,context):
    key = event['s3']['object']['key']
    source = event['s3']['bucket']['name']
    logger.info(key)
    logger.info(source)

    response = s3_client.copy_object(
        Bucket= DESTINATION_BUCKET,
        CopySource={'Bucket': source, 'Key': key},
        Key=key
    )

    return {
        'region': REGION,
        'bucket': DESTINATION_BUCKET,
        'key': key
    }
