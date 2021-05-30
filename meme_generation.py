import requests

url = "https://api.imgflip.com/caption_image"
i=598
lc=0
text0 =""
text1=""
with open("kc.txt", "r") as a_file:
  for line in a_file:
      text0 = line.strip()
      querystring = {"template_id":"1202623","username":"","password":"","text0":text0,"text1":""}
      response = requests.post(url,data=querystring )
      url_i=response.json()['data']['url']
      response = requests.get(url_i)
      file = open(str(i)+".png", "wb")
      file.write(response.content)
      file.close()
      i=i+1
      lc=0
