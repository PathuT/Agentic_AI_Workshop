import streamlit as st
from agent.travel_agent import run_travel_agent

st.set_page_config(page_title="🌍 Travel Assistant AI", layout="centered")
st.title("🧳 Intelligent Travel Assistant")

st.markdown("Get the current **weather** and top **tourist attractions** for your destination!")

city = st.text_input("Enter a city", placeholder="e.g., Tokyo, Paris, New York")

if st.button("Plan My Trip"):
    if city.strip():
        with st.spinner("Planning your trip..."):
            prompt = f"I am planning a trip to {city}. What's the current weather and what should I visit?"
            try:
                response = run_travel_agent(prompt)
                st.success("Here’s what I found:")
                st.write(response)
            except Exception as e:
                st.error(f"Something went wrong: {str(e)}")
    else:
        st.warning("Please enter a city name.")
