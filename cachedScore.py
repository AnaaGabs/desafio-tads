class CachedScore:
    def __init__(self, score_service):
        self.score_service = score_service
        self.cache = {}

    def getScore(self, cpf):
        if cpf not in self.cache:
            self.cache[cpf] = self.score_service.getScore(cpf)
            print(self.score_service)
        return self.cache[cpf]

