import cv2
import boto3

file='/Users/onur/Downloads/mymood.png'
bucket='mood-detect'
key_name='mymood.png'



cap = cv2.VideoCapture(0)


cap.set(3,640);
cap.set(4,480);
def get_image():
	ret, img = cap.read()
	print "Say cheese!!!!!"
	return img
 
camera_capture = get_image()
file = "/Users/onur/Downloads/mymood.png"
cv2.imwrite(file, camera_capture)

client = boto3.client('s3')
s3 = boto3.resource('s3')
s3.meta.client.upload_file(file, bucket, key_name,{'ACL': 'public-read'})



