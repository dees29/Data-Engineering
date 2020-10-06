import boto3
from pprint import pprint
import image_helpers


client = boto3.client('rekognition')

#grab the image from online
#imgurl = 'https://www.csun.edu/sites/default/files/AS-Earth_Month-Outdoor_Online.jpg'
imgurl = 'http://media.comicbook.com/uploads1/2015/07/fox-comic-con-panel-144933.jpg'
#imgurl = 'https://blog.njsnet.co/content/images/2017/02/trumprecognition.png'

imgbytes = image_helpers.get_image_from_url(imgurl)

rekresp = client.recognize_celebrities(Image={'Bytes': imgbytes})
# pprint(rekresp['CelebrityFaces'])
for face in rekresp['CelebrityFaces']:
    print(face['Name'], 'confidence:', face['MatchConfidence'], 'url:', face['Urls'])

