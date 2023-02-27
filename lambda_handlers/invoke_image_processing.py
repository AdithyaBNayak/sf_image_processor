import json
import boto3
import os 

sf_client = boto3.client('stepfunctions')
sf_arn = os.environ['SF']

def invokeImageProcessing(event, context):
    print(event)
    records = event['Records'][0]
    response = sf_client.start_execution(
        stateMachineArn=sf_arn,
        input=json.dumps(records),
    )

    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
