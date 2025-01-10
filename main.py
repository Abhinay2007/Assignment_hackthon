

import requests
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

BASE_API_URL = "https://api.langflow.astra.datastax.com"
LANGFLOW_ID = "cdd38aa6-347d-41ff-82e5-985c88941282"
FLOW_ID = "c5046f91-9426-4810-b286-e08a63e18177"
APPLICATION_TOKEN = os.environ.get("APP_TOKEN")
ENDPOINT = "User1" # The endpoint name of the flow



def run_flow(message: str) -> dict:
    
    api_url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/{ENDPOINT}"

    payload = {
        "input_value": message,
        "output_type": "chat",
        "input_type": "chat",
    }
    
    headers = {"Authorization": "Bearer " + APPLICATION_TOKEN, "Content-Type": "application/json"}
    response = requests.post(api_url, json=payload, headers=headers)
    return response.json()

def main():
    # st.title("Chat Interface")
    
    # message = st.text_area("message", placeholder="Ask something....")
    
    # if st.button("Run Flow"):
    #     if not message.strip():
    #         st.error("Please enter a message")
    #         return
        
    #     try:
    #         with st.spinner("Running Flow..."):
    #             response = run_flow(message)
    #             response_text = response["outputs"][0]["outputs"][0]["results"]["message"]["text"]
    #             st.markdown(response_text)
    #     except Exception as e:
    #         st.error(str(e))
    import streamlit as st
from PIL import Image

# Set the page configuration
st.set_page_config(
    page_title="Interactive Agent",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for styling
st.markdown(
    """
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        padding: 15px 32px;
        font-size: 16px;
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and subtitle
st.title("🤖 Interactive AI Agent")
st.subheader("Your personal AI assistant at your service")

# Add an image or logo
image = Image.open("abc.jpg")
st.image(image, width=200)  
# st.image(image, use_column_width=True)

# User input section
user_input = st.text_area("Enter your query:", height=100, placeholder="Type here...")

# Button to submit the query
if st.button("Submit"):
    response = f"Agent's response to: {user_input}"  
    
    try:
        with st.spinner("Running Flow..."):
            response = run_flow(user_input)
            st.write(response)

            response_text = response["outputs"][0]["outputs"][0]["results"]["message"]["text"]
            st.markdown(response_text)
    except Exception as e:
        st.error(str(e))

# Add a sidebar with additional options
st.sidebar.title("Settings")
st.sidebar.radio("Select Theme:", ["Light", "Dark"])
st.sidebar.slider("Adjust Font Size:", 10, 30, 16)

# Footer
st.markdown("---")
st.markdown("© 2025 My Agent, Inc. All rights reserved.")



if __name__ == "__main__":
    main()

