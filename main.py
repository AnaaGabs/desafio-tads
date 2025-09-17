from fastapi import FastAPI, HTTPException
import httpx
from typing import List

app = FastAPI()

# A URL base da API externa
BASE_URL = "https://score.hsborges.dev/api/score"

# Use uma lista se a ordem for importante. Se não, um set é ok, mas o acesso deve ser corrigido.
# Para manter a lógica original, vamos usar uma lista para o acesso por índice.
cpf_list = ['423.429.220-60', '320.532.470-61', '617.839.370-92']
requisicoes = []


# Função que faz a requisição à API externa
async def get_score_from_external_api(CLIENT_ID):
    global last_message
    headers = {
        "Client-ID": CLIENT_ID
    }
    
    async with httpx.AsyncClient() as client:
        try:
            # Pega o primeiro CPF da lista para a requisição
            cpf_request = cpf_list[0] 
            response = await client.get(
                BASE_URL + '?' + f'cpf={cpf_request}', 
                headers=headers
            )
            response.raise_for_status()
            score_data_from_api = response.json()
            
            last_message = score_data_from_api.get("message", "Mensagem não encontrada.")
            print(last_message)

            return score_data_from_api
        
        except httpx.HTTPStatusError as e:
            # Lança um erro HTTP se a requisição falhar com status 4xx/5xx
            raise HTTPException(status_code=e.response.status_code, detail=str(e))
        except httpx.RequestError as e:
            # Lança um erro interno se houver problemas na requisição
            raise HTTPException(status_code=500, detail=f"Erro na requisição: {str(e)}")

# Endpoint que chama o serviço externo
@app.get("/score")
async def get_score():
    for i in range(len(cpf_list)):
        CLIENT_ID = str(i+1) 
        score_data = await get_score_from_external_api(CLIENT_ID)
        requisicoes.append("Requisição do cliente {}: {}".format(i+1, last_message))
    return {"Requisicoes": requisicoes}