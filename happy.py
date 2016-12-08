import boto3
import random

bucket='mood-detect'
key_name='mymood.png'
data='<html><body><h1>It is a great day</h1>https://www.youtube.com/watch?v=EAo4DXBZ81M</body></html>'
client = boto3.client('ses')

def lambda_handler(event, context):
    print event
    response = client.send_email(
        Source='from@gmail.com',
        Destination={
            'ToAddresses': [
                'to@gmail.com',
            ]
        },
        Message={
            'Subject': {
                'Data': 'Alert'
            },
            'Body': {
                'Html': {
                    'Data': data
                }
            }
        }
    )
