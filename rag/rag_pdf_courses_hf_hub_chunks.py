from huggingface_hub import InferenceClient
from langchain_community.document_loaders import PyPDFLoader
from langchain_huggingface import HuggingFaceEndpointEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
import keys 

loader = PyPDFLoader(
    r"courses_offered.pdf",
    mode="page")

docs = loader.load()
print('Loaded document count :', len(docs))

# Split docs into chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=400, 
    chunk_overlap=100)

chunks = splitter.split_documents(docs)
print("No. of chunks :", len(chunks))

embedding_model = HuggingFaceEndpointEmbeddings(
    model="sentence-transformers/all-MiniLM-L6-v2",
    huggingfacehub_api_token= keys.HUGGINGFACEKEY
)

# Facebook AI Similarity Search
db = FAISS.from_documents(chunks,embedding_model)   

print('Created FAISS index')

question = "What is the duration of Python course?"

repo_id = "mistralai/Mistral-7B-Instruct-v0.3"
llm = InferenceClient(repo_id, provider="hf-inference", token=keys.HUGGINGFACEKEY, timeout=120)


retriever = db.as_retriever(search_kwargs={"k": 2})
results = retriever.invoke(question)

context = "\n\n".join([doc.page_content for doc in results])

prompt = f"""
Please answer the question using the context.

Context : {context}

Question: {question}
Answer: 
"""


result =  llm.text_generation(prompt)
print(result)
