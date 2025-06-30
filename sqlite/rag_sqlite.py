import sqlite3
from langchain.prompts import PromptTemplate
from huggingface_hub import InferenceClient
 
import keys 

db_path = r"courses.db"

def get_courses():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM courses")
    courses = cursor.fetchall()
    conn.close()
    return courses

def concate_course(course):
    course_id, title, description, duration, fee, prerequisite = course
    return f"Title: {title}\nDescription: {description}\nFee: {fee}\nDuration: {duration}\nPrerequisite: {prerequisite}"

# Load courses data
courses = get_courses()

context = ""
for course in courses:
    context += concate_course(course) + "\n\n"

#print(context)

prompt_template = """
Answer the question based on the given context. 
Context : {context}
Question: {question}
"""

prompt = PromptTemplate.from_template(prompt_template)
prompt_value = prompt.format(context=context, 
                question="What is the fee for Generative AI course?")

repo_id = "mistralai/Mistral-7B-Instruct-v0.3"
llm = InferenceClient(repo_id, provider="hf-inference", token=keys.HUGGINGFACEKEY, timeout=120)

response = llm.text_generation( prompt_value)
print(response)












 