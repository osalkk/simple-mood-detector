import boto3
import random

bucket='mood-detect'
key_name='mymood.png'
myrandom=str(random.random())

data='<html><body><img src="https://s3-eu-west-1.amazonaws.com/' + bucket + '/' + key_name + '?a=' + myrandom + '" /></body></html>'
data1='<a href="spotify:user:spotify:playlist:65V6djkcVRyOStLd8nza8E">Play now</a>'
client = boto3.client('ses')

def send_email():
    response = client.send_email(
        Source='salk.onur@gmail.com',
        Destination={
            'ToAddresses': [
                'salk.onur@gmail.com',
            ]
        },
        Message={
            'Subject': {
                'Data': 'Alert'
            },
            'Body': {
                'Text': {
                    'Data': "s3://' + bucket + '/' + key_name'"
                },
                'Html': {
                    'Data': data
                }
            }
        }
    )

send_email()

