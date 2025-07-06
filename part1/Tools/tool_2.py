import requests

def get_random_joke():
    try:
        res = requests.get("https://icanhazdadjoke.com/", headers={"Accept": "application/json"})
        data = res.json()
        return data.get("joke", "No joke found!")
    except:
        return "Couldn't fetch a joke."
