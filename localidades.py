import re
import json

# Leer el contenido del archivo SQL
with open('ARGENTINA_PROVINCIAS_CIUDADES.sql', 'r', encoding='utf-8') as file:
    sql_content = file.read()

# Expresión regular para extraer las localidades de la tabla `localidades`
pattern = re.compile(r"INSERT INTO `localidades` \(`id`, `id_privincia`, `localidad`\) VALUES\n(.*?);", re.DOTALL)
matches = pattern.findall(sql_content)

# Filtrar las localidades de la provincia de Buenos Aires-GBA (id = 2)
localidades_buenos_aires_gba = []
for match in matches:
    rows = match.split('),\n(')
    for row in rows:
        columns = row.split(', ')
        if columns[1] == '2':
            localidad = columns[2].strip("'")
            localidades_buenos_aires_gba.append({"name": localidad, "provincia": {"id": 2}})

# Escribir el resultado en un archivo JSON
with open('localidades_buenos_aires_gba.json', 'w', encoding='utf-8') as json_file:
    json.dump(localidades_buenos_aires_gba, json_file, ensure_ascii=False, indent=4)