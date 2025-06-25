import os
from dotenv import load_dotenv
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from tools.weather_tool import get_weather_tool
from tools.attraction_tool import get_top_attractions

load_dotenv()

# Set up Gemini Flash LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

# Tools
tools = [get_weather_tool, get_top_attractions]

# ✅ REQUIRED prompt format (input + scratchpad)
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful travel assistant. Answer questions using tools when necessary."),
    ("human", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad")
])

# Agent setup
agent = create_tool_calling_agent(llm=llm, tools=tools, prompt=prompt)

# Executor setup
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# Callable function
def run_travel_agent(prompt: str) -> str:
    return agent_executor.invoke({"input": prompt})["output"]
