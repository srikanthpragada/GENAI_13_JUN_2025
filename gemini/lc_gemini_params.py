import keys 

import os
os.environ["GOOGLE_API_KEY"] =  keys.GOOGLEKEY

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import HumanMessage

# Create a Gemini model instance (gemini-pro is the general-purpose model)
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", 
                             temperature=0.9, top_p = 0.9,
                             max_output_tokens=100,
                             model_kwargs= { "frequency_penalty": 1.5}
            )
                             

# Use invoke with a list of messages
response = llm.invoke([HumanMessage(content="write about sun. Keep it short")])
print(response.content)
 
