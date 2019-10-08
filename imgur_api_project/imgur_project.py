import base64
import sys
import requests
import json
import webbrowser




#this is reading the image from console
#eg. in consol I would type in:  python3 imgur_project.py shaq.jpg
#this program and the image needs to be in the same place for this to work. else, you put the directory where
#it is located
img = sys.argv[1]

print('Selected image is: ' + img)
print(type(img))


#this is taking the image and encoding it in base64. This is what the imgur api takes as an image
with open(img, 'rb') as image_file:
	encode_string = base64.b64encode(image_file.read())


#print(encode_string)

clientID = 'YOUR_CLIENT_ID' #you would use your clien_id here

clientID_Authorization = 'Client-ID %s'%clientID

url = 'https://api.imgur.com/3/image'

image_body_request = {'image': encode_string}


headers = {'Authorization' :  clientID_Authorization}


#this is what is sent to the imgur api as the request
response = requests.request('POST', url, headers = headers, data = image_body_request)

#this is converting the json string response into a python dictionary
json_resonse = json.loads(response.text)
print(type(json_resonse))

#this gets the link from the dictionary
link = json_resonse['data']['link']
print(link)

#this opens the link in your browser
webbrowser.open(link)

