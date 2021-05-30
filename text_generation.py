import requests

url = "https://api.imgflip.com/caption_image"



querystring = {"template_id":"112126428","username":"","password":"","text0":"Testing","text1":"Testes"}



response = requests.post(url,data=querystring )

url_i=response.json()['data']['url']

response = requests.get(url_i)

file = open("sample_image.png", "wb")
file.write(response.content)
file.close()