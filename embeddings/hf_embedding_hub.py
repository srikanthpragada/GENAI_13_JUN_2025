from langchain_huggingface import HuggingFaceEndpointEmbeddings
import keys 
 
embeddings_model = HuggingFaceEndpointEmbeddings(
    model="sentence-transformers/all-MiniLM-L6-v2",
    huggingfacehub_api_token= keys.HUGGINGFACEKEY
)

embeddings = embeddings_model.embed_documents(
    [
        "This is beautiful",
        "That soup was awful",
        "Your hair looks great",
        "I work for 9 to 10 hours a day",
        "I love football and swimming"
    ]
)

print(len(embeddings), len(embeddings[0]))
print(embeddings[0][:10])  

