import streamlit as st
st.set_page_config(page_title="Automatic Ticket Classification", layout="wide")
from css_utils import inject_custom_css
import base64
from dotenv import load_dotenv
from user_utils import *
import os  # Needed for os.getenv

# Creating session variables
if 'HR_tickets' not in st.session_state:
    st.session_state['HR_tickets'] = []
if 'IT_tickets' not in st.session_state:
    st.session_state['IT_tickets'] = []
if 'Transport_tickets' not in st.session_state:
    st.session_state['Transport_tickets'] = []

def main():
    load_dotenv()
    inject_custom_css("background.png", "background.png", "sidebar.jpg", "style.css") # Use your paths

    st.header("🎫 Automatic Ticket Classification Tool")
    user_input = st.text_input("🔍 We are here to help you, please ask your question:")
    # st.write("You typed:", user_input)

    if user_input:
        embeddings = create_embeddings()
        index = pull_from_pinecone(os.getenv("PINECONE_API_KEY"), "us-east-1", "tickets", embeddings)
        relavant_docs = get_similar_docs(index, user_input)
        response = get_answer(relavant_docs, user_input)
        st.write(response)

        if st.button("Raise Ticket?"):
            query_result = embeddings.embed_query(user_input)
            department_value = predict(query_result)
            st.write("✅ Your ticket has been submitted to: **" + department_value + "**")

            if department_value == "HR":
                st.session_state['HR_tickets'].append(user_input)
            elif department_value == "IT":
                st.session_state['IT_tickets'].append(user_input)
            else:
                st.session_state['Transport_tickets'].append(user_input)

if __name__ == '__main__':
    main()
