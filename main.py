import FastAPI, HTTPException

app = FastAPI()

# A URL base da API externa
BASE_URL = "https://score.hsborges.dev/api/score/"

# Função que faz a requisição à API externa
async def get_score_from_external_api():
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(BASE_URL)
            response.raise_for_status()  # Vai gerar um erro se a resposta for 4xx ou 5xx
            return response.json()
        except httpx.HTTPStatusError as e:
            raise HTTPException(status_code=e.response.status_code, detail=str(e))
        except httpx.RequestError as e:
            raise HTTPException(status_code=500, detail=f"Erro na requisição: {str(e)}")

# Endpoint que chama o serviço externo
@app.get("/get_score/")
async def get_score():
    score_data = await get_score_from_external_api()
    return {"score_data": score_data}