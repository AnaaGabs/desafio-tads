import requests

class Score:

    def getScore(self, cpf: str):
        url = "https://score.hsborges.dev/api/score"

        headers = {
            "accept": "application/json",
            "client-id": "fiani"
        }

        response = requests.get(f"{url}/?cpf={cpf}", headers=headers)
        return response.json()