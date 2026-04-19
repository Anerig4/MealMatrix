const express = require('express');
const cors = require('cors');
const axios = require('axios');

const app = express();
app.use(cors());
app.use(express.json());

app.get('/', (req, res) => {
  res.send("MealMatrix API running 🚀");
});

app.post('/recommend', async (req, res) => {
  try {
    const response = await axios.post('http://127.0.0.1:8000/recommend', req.body);
    res.json(response.data);
  } catch {
    res.status(500).json({ error: "AI error" });
  }
});

app.listen(3000, () => console.log("Server running on 3000"));
