import os
# import json
# import datetime
import boto3
# import PIL # for image resizing
# from PIL import Image
# from io import BytesIO

s3_client = boto3.client('s3')
DESTINATION_BUCKET = os.environ['DEST_BUCKET']


def resize(event,context):
    # get the bucket name and key from event

    # Get the image Object from S3

    # Resize the image
    # obj_body = obj.get()['Body'].read()
    # img = Image.open(BytesIO(obj_body))
    # img = img.resize((int(size_split[0]), int(size_split[1])), PIL.Image.ANTIALIAS)
    # buffer = BytesIO()
    # img.save(buffer, 'JPEG')
    # buffer.seek(0)


    # Upload the resized image to s3

    return
