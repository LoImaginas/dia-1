import template as t
from get import request_get

url=('https://aves.ninjas.cl/api/birds')
response = request_get(url)

texto = ''
for aninja in response:

       texto += t.pajaritos_template.substitute(h1=aninja["name"]["spanish"],
                                                h2=aninja["name"]["english"],
                                                url=aninja["images"]["main"])
       
       