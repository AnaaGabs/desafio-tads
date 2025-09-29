import time

class RateLimiter:
    def __init__(self, score_service):
        self.interval = 1  # janela fixa: 1 req/s
        self.timeToNext = time.time()
        self.score_service = score_service

    def wait(self):
        now = time.time()
        if now < self.timeToNext:
            sleep_time = self.timeToNext - now
            time.sleep(sleep_time)

    def updateWait(self):
        now = time.time()
        self.timeToNext = now + self.interval

    def getScore(self, cpf):
        self.wait()
        score = self.score_service.getScore(cpf)
        self.update_after_response()
        return score