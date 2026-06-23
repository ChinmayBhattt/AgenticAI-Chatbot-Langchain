import streamlit as st

st.set_page_config(page_title="Langgraph Agent UI", layout="centered")
st.title("AI Chatbot Agent")
st.write("Create and Interact With the AI Agent")

system_prompt=st.text_area("Define Your AI Agent: ", height=70, placeholder="Type your system prompt here...")

MODEL_NAMES_GROQ=["LLama3-70b-8192", "mixtral-8x7b-32768", "LLama-3.3-70b-versatile"]
MODEL_NAMES_GEMINI=["gemini-2.5-flash"]

provider=st.radio("Select Model: ", ("Groq", "Gemini"))

if provider == "Groq":
    selected_model = st.selectbox("Select Groq Model: ", MODEL_NAMES_GROQ)
elif provider == "Gemini":
    selected_model = st.selectbox("Select Gemini Model: ", MODEL_NAMES_GEMINI)

allow_web_search=st.checkbox("Allow Web Search")

user_query=st.text_area("Enter Your Query: ", height=150, placeholder="Ask Anything!")

API_URL="http://10.94.144.69:8503/chat"

if st.button("Ask Agent"):
    if user_query.strip():
        import requests

        payload={
            "model_name": selected_model,
            "model_provider": provider,
            "system_prompt": system_prompt,
            "messages": [user_query],
            "allow_search": bool
        }

        response=requests.post(API_URL, json=payload)
        if response.status_code == 200:
            response_data = response.json()
            if "error" in response_data:
                st.error(response_data["error"])
            else: 
                st.subheader("Agent Response")
                st.markdown(f"**Final Response:** {response}")