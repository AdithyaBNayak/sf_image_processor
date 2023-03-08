import os
import boto3
import time 

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['DBNAME'])


def put_item(event, context):
    # Adds the meta data of images into DB
    table.put_item(
        Item={
                'original': 'originalTest',
                'thumbnail': 'thumbnailTest',
                'timestamp' : str(time.time())
            }
        )
    return
