from pinecone import Pinecone as PineconeClient
from langchain_community.vectorstores import Pinecone
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain_groq import ChatGroq  # ✅ Replaced OpenAI
from langchain.chains.question_answering import load_qa_chain
from css_utils import inject_custom_css
import joblib
import os
# import os
# from langchain_community.llms import ChatGroq
from dotenv import load_dotenv
load_dotenv()
inject_custom_css("background.png", "background.png", "sidebar.jpg", "style.css")
#Function to pull index data from Pinecone...
def pull_from_pinecone(pinecone_apikey, pinecone_environment, pinecone_index_name, embeddings):
    PineconeClient(
        api_key=pinecone_apikey,
        environment=pinecone_environment
    )
    index_name = pinecone_index_name
    index = Pinecone.from_existing_index(index_name, embeddings)
    return index

def create_embeddings():
    embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    return embeddings

#This function will help us in fetching the top relevant documents from our vector store - Pinecone Index
def get_similar_docs(index, query, k=2):
    similar_docs = index.similarity_search(query, k=k)
    return similar_docs

#LLM QA function using GROQ's LLaMA model
def get_answer(docs, user_input):
    llm = ChatGroq(model="llama3-8b-8192", api_key=os.getenv("GROQ_API_KEY"))
    chain = load_qa_chain(llm, chain_type="stuff")
    response = chain.run(input_documents=docs, question=user_input)
    return response

def predict(query_result):
    Fitmodel = joblib.load('modelsvm.pk1')
    result = Fitmodel.predict([query_result])
    return result[0]
