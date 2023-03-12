import boto3

s3_client = boto3.client('s3')

def delete_file(event,context):
    # Deletes the source file from s3
    response = s3_client.delete_object(
        Bucket=event['s3']['bucket']['name'],
        Key=event['s3']['object']['key']
    )
    return