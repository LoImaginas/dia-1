import requests

url = "https://jsonplaceholder.typicode.com/posts"

payload = {
  "userId": 1,
  "title": "titulo del ejemplo",
  "body": "esto es un ejemplo del body"
}

response = requests.post(url, json=payload)

if response.status_code == 201: #201 => created
  print("insercion exitosa")

  print(response.text)

else:
  print("error en la creacion de posts")