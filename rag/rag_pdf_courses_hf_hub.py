from huggingface_hub import InferenceClient
from langchain_community.document_loaders import PyPDFLoader
from langchain_huggingface import HuggingFaceEndpointEmbeddings
from langchain_community.vectorstores import FAISS
import keys 

# 1. Load PDF document
loader = PyPDFLoader(
    r"courses_offered.pdf",
    mode="page")

docs = loader.load()
print('Loaded document count :', len(docs))

# 2. Initialize embeddings using Hugging Face Inference API
embedding_model = HuggingFaceEndpointEmbeddings(
    model="sentence-transformers/all-MiniLM-L6-v2",
    huggingfacehub_api_token= keys.HUGGINGFACEKEY
)

#  3. Create FAISS index from documents
db = FAISS.from_documents(docs, embedding_model)
 
print('Created FAISS index')

question = "Generative AI course fee"

# 4.  Get access to the LLM using Hugging Face Inference API
repo_id = "mistralai/Mistral-7B-Instruct-v0.3"
llm = InferenceClient(repo_id, provider="hf-inference", token=keys.HUGGINGFACEKEY, timeout=120)

# 5. Retrieve relevant documents based on the question
retriever = db.as_retriever()
results = retriever.invoke(question)

# 6. Create prompt with context and question
context = "\n".join([doc.page_content for doc in results])
prompt = f"""
Please answer the question using the context.

Context : {context}

Question: {question}
"""

# 7. Generate answer using the LLM and print the result
result =  llm.text_generation(prompt)
print(result)
