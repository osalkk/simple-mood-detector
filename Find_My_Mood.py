import boto3

def lambda_handler(event, context):

    bucket='mood-detect'
    key_name='mymood.png'

    client = boto3.client('rekognition')
    response = client.detect_faces(
    Image={
            'S3Object': {
                'Bucket': bucket,
                'Name': key_name
            }
        },
        Attributes=[
            'ALL',
        ]
    )
    moods=response['FaceDetails'][0]['Emotions']
    moods_temp_array={}
    for emotion in moods:
        moods_temp_array[emotion['Type']]=emotion['Confidence']
    mymood=max(moods_temp_array.iterkeys(), key=(lambda key: moods_temp_array[key]))

    return {"type": mymood}



