import os 

from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate


load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-120b",
    provider="auto",
    max_new_tokens=100,
    temperature=0.7,
    
)

chat_model = ChatHuggingFace(llm=llm)

prompt = ChatPromptTemplate.from_messages([
  SystemMessagePromptTemplate.from_template("You're a helpful assistant."),
  HumanMessagePromptTemplate.from_template("{user_question}"),
])

chain = prompt | chat_model

response = chain.invoke({"user_question": "Explain Docker in one sentence."})

print(response.content)