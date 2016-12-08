import boto3

def lambda_handler(event, context):

    client = boto3.client('stepfunctions')
    response = client.start_execution(
    stateMachineArn='arn:aws:states:eu-west-1:111122223333:stateMachine:MoodDetector'
)    



