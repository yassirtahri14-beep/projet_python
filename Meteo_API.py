import requests

# Étape 1 : détecter la position via l'IP
position = requests.get("http://ip-api.com/json/")
donnees_position = position.json()
latitude = donnees_position["lat"]
longitude = donnees_position["lon"]
ville = donnees_position["city"]

# Étape 2 : météo avec ces coordonnées
meteo = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true")
donnees_meteo = meteo.json()
temperature = donnees_meteo["current_weather"]["temperature"]

print(f"La température actuelle à {ville} est de {temperature}°C")


