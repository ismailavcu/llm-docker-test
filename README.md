## An image is a blueprint; a container is a running instance of that image.
docker ps  
docker images  
docker logs llm-summarizer-container  
docker exec -it llm-summarizer-container bash  


## Before Docker:

Windows
  ↓
Python .venv
  ↓
FastAPI
  ↓
LangChain
  ↓
Hugging Face


## With Docker:

Windows
  ↓
Docker
  ↓
Container
  ↓
Python
  ↓
FastAPI
  ↓
LangChain
  ↓
Hugging Face


