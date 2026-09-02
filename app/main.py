from dotenv import load_dotenv

from fastapi import FastAPI
from pydantic import BaseModel, Field

from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()


app = FastAPI()

# ---------- LLM ----------

llm = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-120b",
    provider="auto",
    max_new_tokens=200,
    temperature=0.3,
)

chat_model = ChatHuggingFace(llm=llm)

# ---------- Prompt ----------

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a helpful assistant that summarizes text. "
        "Provide a concise and clear summary."
    ),
    (
        "human",
        "Summarize the following text:\n\n{text}"
    ),
])

chain = prompt | chat_model

# ---------- Request model ----------
# defines what our API expects
class SummarizeRequest(BaseModel):
    text: str = Field(min_length=1) # empyty string is not allowed


# ---------- Routes ----------

@app.get("/")
def root():
    return {"message": "Hello from my Dockerized LLM app!"}


@app.post("/summarize")
def summarize(request: SummarizeRequest):
    response = chain.invoke({
        "text": request.text
    })

    return {
        "summary": response.content
    }


