from geopy.geocoders import Nominatim

# localizador = Nominatim(user_agent="myGeo")
loc = Nominatim(user_agent="myCode")
endereco = loc.geocode("120, Padre José Poliga, Curitiba, PR").point
print(f"Coordenadas do endereço: {endereco}")
print("#####----#####")
# obter endereço reverso
endereco1 = loc.reverse("25 28m 16.936s S, 49 11m 44.9243s W").address
print(endereco1)
