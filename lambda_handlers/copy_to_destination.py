import os
import boto3

s3_client = boto3.client('s3')
DESTINATION_BUCKET = os.environ['DEST_BUCKET']

def copy_file(event,context):
    key = event['s3']['object']['key']
    
    response = s3_client.copy_object(
        Bucket= DESTINATION_BUCKET,
        CopySource={
            'Bucket': event['s3']['bucket']['name'], 
            'Key': event['s3']['object']['key']
            },
        Key=event['s3']['object']['key'] 
    )

    return {
        'region': '',
        'bucket': DESTINATION_BUCKET,
        'key': key
    }
