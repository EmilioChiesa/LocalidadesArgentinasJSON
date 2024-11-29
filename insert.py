import json
import psycopg2

# Cargar datos JSON
with open('localidades_cordoba.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Conectar a PostgreSQL
conexion = psycopg2.connect(
    dbname="clinicaVeterinaria",
    user="adminClinica",
    password="lindaCooper2021",
    host="localhost",
    port="5432"
)
cursor = conexion.cursor()

# Insertar datos en la tabla
for localidad in data:
    if all(key in localidad for key in ('name', 'provincia')):
        nombre = localidad["name"]
        provincia_id = localidad["provincia"]["id"]
        cursor.execute(
            '''
            INSERT INTO localidad (name, "provinciaId") 
            VALUES (%s, %s)
            ON CONFLICT (name) 
            DO UPDATE SET "provinciaId" = EXCLUDED."provinciaId"
            ''',
            (nombre, provincia_id)
        )
    else:
        print(f"Faltan claves en el elemento: {localidad}")

# Guardar cambios y cerrar conexión
conexion.commit()
cursor.close()
conexion.close()