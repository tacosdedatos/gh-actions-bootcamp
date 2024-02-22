import requests

# URL de la API
api_url = "https://my.api.mockaroo.com/cf_usuarios"
headers = {"x-api-key": "03ee11f0"}

# Hacer la petición a la API
response = requests.get(api_url, headers=headers)

# Verificar que la petición fue exitosa
if response.status_code == 200:    
    # Guardar los datos en un archivo CSV
    with open('users_data.csv', 'w') as file:
        file.write(response.text)
    
    print("Datos extraídos y guardados en 'users_data.csv'.")
else:
    print("Error al hacer la petición a la API:", response.status_code)
