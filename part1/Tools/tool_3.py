import requests

def get_random_quote():
    try:
        res = requests.get("https://zenquotes.io/api/random")
        data = res.json()[0]
        return f'"{data["q"]}" - {data["a"]}'
    except:
        return "Couldn't fetch a quote."
