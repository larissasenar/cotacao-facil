import requests
import pandas as pd

API_KEY = "SUA_CHAVE_AQUI"  # Substitua pela sua chave da Alpha Vantage

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

def buscar_historico(simbolo):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={simbolo}&apikey={API_KEY}&outputsize=compact"
    resposta = requests.get(url)
    dados = resposta.json()
    if "Time Series (Daily)" in dados:
        df = pd.DataFrame.from_dict(dados["Time Series (Daily)"], orient="index", dtype=float)
        df.index = pd.to_datetime(df.index)
        df = df.sort_index()
        return df.tail(30)
    return None
