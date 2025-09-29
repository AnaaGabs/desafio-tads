from fastapi import FastAPI
from score import Score 
from cachedScore import CachedScore
from ratelimitt import RateLimiter

app = FastAPI()
score = Score()
rateLimitedScore = RateLimiter(score)
cachedScore = CachedScore(rateLimitedScore)

# Função que faz a requisição à API externa
@app.get("/consulta/")
def getScore(cpf: str):
    return cachedScore.getScore(cpf)