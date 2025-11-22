from folium import Map, Marker
import os
import requests
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path)

token = os.getenv("SPTRANS_TOKEN")
print("Token:", token)

s = requests.Session()
res = s.post(
    f"http://api.olhovivo.sptrans.com.br/v2.1/Login/Autenticar?token={token.strip()}",
    verify=False  
)
print("Login:", res.text)

res = s.get(
    "http://api.olhovivo.sptrans.com.br/v2.1/Parada/BuscarParadasPorLinha?codigoLinha=2506",
    verify=False
)
paradas = res.json()
print(paradas[:3])

m = Map(location=[paradas[0]["py"], paradas[0]["px"]], zoom_start=14)
for i in paradas:
    Marker(location=[i["py"], i["px"]], popup=i["np"]).add_to(m)

m.save("mapa.html")
os.system("open mapa.html")
