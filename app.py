import os
import streamlit as st
from dotenv import load_dotenv
from openai import AzureOpenAI

# Load environment variables
load_dotenv()

# Get configuration settings
open_ai_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
open_ai_key = os.getenv("AZURE_OPENAI_API_KEY")
chat_model = os.getenv("CHAT_MODEL")
embedding_model = os.getenv("EMBEDDING_MODEL")
search_url = os.getenv("SEARCH_ENDPOINT")
search_key = os.getenv("SEARCH_KEY")
product_index = os.getenv("product_index")
manual_index = os.getenv("maunal_index")

# Initialize Azure OpenAI client
chat_client = AzureOpenAI(
    api_version="2024-12-01-preview",
    azure_endpoint=open_ai_endpoint,
    api_key=open_ai_key
)

# Page configuration
st.set_page_config(page_title="Contoso Assistant", page_icon="🤖", layout="wide")

# Welcome message
st.markdown("""
<div style='background-color: #f0f8ff; padding: 15px; border-radius: 10px; margin-bottom: 20px;'>
    <h4>👋 Welcome to the Contoso RAG Assistant Demo</h4>
    <p style='margin-bottom: 0;'>
        This application was created by <strong>Aparna Rajawat</strong> to showcase the powerful capabilities 
        of <strong>Retrieval-Augmented Generation (RAG)</strong> using Azure OpenAI and Azure AI Search.
    </p>
    <p style='margin-bottom: 0;'>
        Feel free to use this in your sessions to demonstrate how RAG can effectively combine the power of 
        large language models with enterprise data to provide accurate, grounded, and contextual responses.
    </p>
</div>
""", unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Select a page:", ["Product Assistant", "Manual Assistant"])

# Initialize session state for chat history
if "product_messages" not in st.session_state:
    st.session_state.product_messages = []
if "manual_messages" not in st.session_state:
    st.session_state.manual_messages = []

def get_rag_response(user_input, index_name, system_message):
    """Get response using RAG pattern with Azure Search"""
    messages = [{"role": "system", "content": system_message}]
    
    # Add chat history
    if page == "Product Assistant":
        messages.extend(st.session_state.product_messages)
    else:
        messages.extend(st.session_state.manual_messages)
    
    # Add current user input
    messages.append({"role": "user", "content": user_input})
    
    # RAG parameters
    rag_params = {
        "data_sources": [
            {
                "type": "azure_search",
                "parameters": {
                    "endpoint": search_url,
                    "index_name": index_name,
                    "authentication": {
                        "type": "api_key",
                        "key": search_key,
                    },
                    "query_type": "vector",
                    "embedding_dependency": {
                        "type": "deployment_name",
                        "deployment_name": embedding_model,
                    },
                }
            }
        ],
    }
    
    # Get response from Azure OpenAI
    response = chat_client.chat.completions.create(
        model=chat_model,
        messages=messages,
        extra_body=rag_params
    )
    
    return response.choices[0].message.content

# Product Assistant Page
if page == "Product Assistant":
    st.title("🛍️ Product Assistant")
    st.markdown("Ask questions about our products and get instant answers!")
    
    # Display chat history
    for message in st.session_state.product_messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Chat input
    if prompt := st.chat_input("Ask about products..."):
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Add user message to history
        st.session_state.product_messages.append({"role": "user", "content": prompt})
        
        # Get assistant response
        with st.chat_message("assistant"):
            with st.spinner("Searching product information..."):
                try:
                    response = get_rag_response(
                        prompt, 
                        product_index, 
                        "You are a helpful product assistant for Contoso. Provide accurate information about products based on the available data."
                    )
                    st.markdown(response)
                    
                    # Add assistant response to history
                    st.session_state.product_messages.append({"role": "assistant", "content": response})
                except Exception as e:
                    st.error(f"Error: {str(e)}")
    
    # Clear chat button
    if st.sidebar.button("Clear Product Chat"):
        st.session_state.product_messages = []
        st.rerun()

# Manual Assistant Page
elif page == "Manual Assistant":
    st.title("📚 Manual Assistant")
    st.markdown("Get help with product manuals and documentation!")
    
    # Display chat history
    for message in st.session_state.manual_messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Chat input
    if prompt := st.chat_input("Ask about manuals and documentation..."):
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Add user message to history
        st.session_state.manual_messages.append({"role": "user", "content": prompt})
        
        # Get assistant response
        with st.chat_message("assistant"):
            with st.spinner("Searching manual information..."):
                try:
                    response = get_rag_response(
                        prompt, 
                        manual_index, 
                        "You are a helpful manual assistant for Contoso. Provide accurate information from product manuals and documentation."
                    )
                    st.markdown(response)
                    
                    # Add assistant response to history
                    st.session_state.manual_messages.append({"role": "assistant", "content": response})
                except Exception as e:
                    st.error(f"Error: {str(e)}")
    
    # Clear chat button
    if st.sidebar.button("Clear Manual Chat"):
        st.session_state.manual_messages = []
        st.rerun()

# Sidebar info
st.sidebar.markdown("---")
st.sidebar.markdown("### About")
st.sidebar.info("This assistant uses AI to help you find information about products and manuals.")
st.sidebar.markdown("---")
st.sidebar.markdown("**Created by:** Aparna Rajawat")
