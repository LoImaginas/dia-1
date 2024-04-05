import template as t
from get import request_get

def pagina_html(url):
    response = request_get(url)
    texto = ''
    for aninja in response:
        titulo_esp = aninja['name']['spanish']
        titulo_en = aninja['name']['english']
        url = aninja['images']['main']
        texto += t.pajaritos_template.substitute(titulo_esp=titulo_esp,
                                                 titulo_en=titulo_en,
                                                 url=url)
    return texto

if __name__ == '__main__':
    url = "https://aves.ninjas.cl/api/birds"
    
    html = pagina_html(url)
    with open('prueba-aves_ninjas/index.html', 'w', encoding='utf-8') as f:
        f.write(html)
        print("")
        print("Sitio web generado correctamente")
       