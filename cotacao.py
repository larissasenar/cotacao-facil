import requests

API_KEY = "6JPCXIJ7G3QU388I"

def buscar_cotacao(simbolo):
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={simbolo}&apikey={API_KEY}"
    resposta = requests.get(url)
    dados = resposta.json()
    if "Global Quote" in dados:
        info = dados["Global Quote"]
        return {
            "Símbolo": info["01. symbol"],
            "Preço Atual": info["05. price"],
            "Variação": info["10. change percent"]
        }
    return None
