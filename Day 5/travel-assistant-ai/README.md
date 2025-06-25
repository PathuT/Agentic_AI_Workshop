# Intelligent Travel Assistant AI

An AI-powered travel assistant that helps you:

- Get the **current weather** of your destination (via WeatherAPI)
- Find **top tourist attractions** (via DuckDuckGo Search)
- Powered by **LangChain agents**, **Gemini 2.0 Flash**, and a **Streamlit UI**

---

## Features

- Real-time weather using WeatherAPI.com
- Live attraction search using DuckDuckGo
- LangChain `create_tool_calling_agent` with Gemini LLM
- Simple and clean Streamlit frontend

---

## Tech Stack

- [LangChain](https://python.langchain.com)
- [Gemini 2.0 Flash](https://makersuite.google.com/app)
- [WeatherAPI.com](https://www.weatherapi.com/)
- [DuckDuckGo Search](https://pypi.org/project/duckduckgo-search/)
- Streamlit

---

## Project Structure

```
travel-assistant-ai/
│
├── app.py # Streamlit frontend
├── agent/
│ └── travel_agent.py # LangChain + Gemini agent
├── tools/
│ ├── weather_tool.py # Custom tool for weather
│ └── attraction_tool.py # Custom tool for attractions
├── utils/
│ └── weather_api.py # WeatherAPI fetch helper
├── .env # Stores API keys
├── requirements.txt # All dependencies
└── README.md # This file

```


---

## Environment Variables

Create a `.env` file in the root directory:

```
env
GOOGLE_API_KEY=your_gemini_api_key_here
WEATHER_API_KEY=your_weatherapi_key_here

```
pip install -r requirements.txt

```

```run
streamlit run app.py
```
