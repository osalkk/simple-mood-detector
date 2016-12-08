import boto3
import random

bucket='mood-detect'
key_name='mymood.png'
myrandom=str(random.random())

data='<html><body><img src="https://s3-eu-west-1.amazonaws.com/' + bucket + '/' + key_name + '?a=' + myrandom + '" /></body></html>'
client = boto3.client('ses')

def send_email():
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
                'Html': {
                    'Data': data
                }
            }
        }
    )

send_email()

