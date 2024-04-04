import requests

url = "https://jsonplaceholder.typicode.com/posts/10"

payload = {
  "userId": 1,
  "title": "titulo del ejemplo 2",
  "body": "esto es un ejemplo del body 2"
}

response = requests.post(url, json=payload)

if response.status_code == 200: #200 => created
  print("actualizacion exitosa")

  print(response.text)

else:
  print("error en la actualizacion de posts")