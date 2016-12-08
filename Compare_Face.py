import boto3

def lambda_handler(event, context):

    bucket='mood-detect'
    key_name='mymood.png'
    target_key_name='onur.jpg'
    
    client = boto3.client('rekognition')
    
    response = client.compare_faces(
        SourceImage={
            'S3Object': {
                'Bucket': bucket,
                'Name': key_name
            }
        },
        TargetImage={
            'S3Object': {
                'Bucket': bucket,
                'Name': target_key_name
            }
        },
        SimilarityThreshold=70
    )
    if len(response['FaceMatches'])==0:
        print "not matched"
        person="NotOnur"
    else:
        print response['FaceMatches'][0]['Similarity']
        person="Onur"
    
    return {"type": person}
