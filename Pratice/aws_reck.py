import boto3
from pprint import pprint
import image_helpers

client = boto3.client('rekognition')
imgurl = 'https://www.csun.edu/sites/default/files/AS-Earth_Month-Outdoor_Online.jpg'
imgbytes = image_helpers.get_image_from_url(imgurl)
rekresp = client.detect_labels(Image={'Bytes': imgbytes}, MinConfidence=1)
pprint(rekresp)
for label in rekresp['Labels']:
    print(label['Name'])
    