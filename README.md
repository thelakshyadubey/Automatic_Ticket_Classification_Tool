# Automatic Ticket Classification Tool

**An AI-powered Streamlit app for automatic classification and management of support tickets using Pinecone vector database, GROQ's LLaMA-3 model, and SVM classification.**

---

## Table of Contents

- [Project Overview](#project-overview)  
- [Features](#features)  
- [Tech Stack](#tech-stack)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Folder Structure](#folder-structure)  
- [How It Works](#how-it-works)   
- [Author](#author)

---

## Project Overview

This project is a scalable and modular ticket classification system designed to automate support ticket routing across departments like HR, IT, and Transport. It leverages:

- Semantic similarity search using **Pinecone** vector database
- Contextual question answering powered by **GROQ's LLaMA-3**
- Text embedding via **SentenceTransformers**
- Classification using **Support Vector Machines (SVM)**
- A clean **Streamlit** UI with custom CSS styling for seamless user experience

The system enables:

- Upload and embedding of PDF documents into Pinecone for knowledge retrieval  
- Interactive user queries for relevant information and ticket creation  
- Department-wise ticket classification and management  
- Model training, evaluation, and saving for continuous improvement  

---

## Features

- **Document ingestion:** Extract text from PDFs, chunk it, and embed into Pinecone  
- **Semantic search:** Retrieve relevant docs using vector similarity  
- **LLM-powered QA:** Generate answers with LLaMA-3 model through GROQ API  
- **Ticket classification:** Classify user input into HR, IT, or Transport using SVM  
- **Custom UI:** Interactive Streamlit app with session management and CSS styling  
- **Model lifecycle:** Train, evaluate, save, and load classification models  
- **Departmental ticket views:** Separate tabs to view pending tickets per department  

---

## Tech Stack

- Python 3.10+  
- [Streamlit](https://streamlit.io/) — Frontend framework  
- [Pinecone](https://www.pinecone.io/) — Vector database for similarity search  
- [GROQ LLaMA-3](https://groq.com/) — Large language model API  
- [LangChain](https://langchain.com/) — Chain of LLM components  
- [SentenceTransformers](https://www.sbert.net/) — Embeddings generation  
- [Scikit-learn](https://scikit-learn.org/) — SVM classification and evaluation  
- [PyPDF](https://pypdf.readthedocs.io/en/latest/) — PDF text extraction  
- [Python-dotenv](https://pypi.org/project/python-dotenv/) — Environment variable management  

---

## Installation

1. Clone the repo:
```bash
git clone https://github.com/thelakshyadubey/Automatic_Ticket_Classification_Tool.git
cd yourrepo
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Setup environment variables in a .env file:
```bash
PINECONE_API_KEY=your_pinecone_api_key
GROQ_API_KEY=your_groq_api_key
```

## How It Works
- Data ingestion: PDFs are read and split into text chunks, which are embedded using SentenceTransformers and stored in Pinecone.
- User query: When a user submits a query, the app retrieves semantically similar documents from Pinecone.
- Answer generation: GROQ's LLaMA-3 model answers the query based on the retrieved documents.
- Ticket classification: User queries are embedded and classified via a trained SVM to determine the responsible department.
- Ticket management: Tickets are stored in Streamlit session state and displayed under respective department tabs.
- Model lifecycle: Admin interface allows loading CSV data, training the SVM model, evaluating accuracy, and saving/loading the model for future use.

## Author
Lakshya Dubey

## Preview
![image](https://github.com/user-attachments/assets/657f37ce-3692-49c7-a3ab-ac2c2a555f92)
![image](https://github.com/user-attachments/assets/7b453883-a0c9-4af9-8f5a-365b4d5b55b3)
![image](https://github.com/user-attachments/assets/f2aa4f2c-22d9-4b1e-bd84-f0253e73e918)
![image](https://github.com/user-attachments/assets/bd5a8706-15f9-46dc-a612-97974426291d)
