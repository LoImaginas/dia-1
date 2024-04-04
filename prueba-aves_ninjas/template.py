from string import Template

html_template = Template
('''<!DOCTYPE html>
<html>
<head>
<title>Aves de Chile</title>
</head>
<body>

<h1>Aves de Chile</h1>

$body

</body>
</html>
''')

pajaritos_template = Template("""
            <img src="$url_img_full"
            <h1 $titulo_esp</h1>
            <h2 $titulo_en</h2>
               
""")