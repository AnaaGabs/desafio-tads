const express = require('express');
const axios = require('axios');
const app = express();
const PORT = 3000;

// URL da API externa
const API_URL = 'https://score.hsborges.dev/api/score/';

// Função para fazer a requisição à API externa
const getScoreFromExternalAPI = async () => {
  try {
    const response = await axios.get(API_URL);
    return response.data; // Retorna os dados recebidos da API externa
  } catch (error) {
    throw new Error(`Erro ao fazer requisição: ${error.message}`);
  }
};

// Rota para expor o endpoint
app.get('/get_score', async (req, res) => {
  try {
    const scoreData = await getScoreFromExternalAPI();
    res.json({ score_data: scoreData });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

// Inicia o servidor na porta 3000
app.listen(PORT, () => {
  console.log(`Servidor rodando em http://localhost:${PORT}`);
});
