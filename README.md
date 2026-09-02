# About  

I made this project to learn and understand basics of docker.  

## An image is a blueprint; a container is a running instance of that image.
docker ps  
docker images  
docker logs llm-summarizer-container  
docker exec -it llm-summarizer-container bash  

docker inspect --format="{{.State.Health.Status}}" llm-summarizer-container  


  
## With Docker:  
  
                         Your Computer  
                              │  
               ┌──────────────┴──────────────┐  
               │                             │  
               ▼                             ▼  
        localhost:8080                localhost:8000  
               │                             │  
               ▼                             ▼  
      ┌─────────────────┐          ┌─────────────────┐  
      │    Frontend     │          │     Backend     │  
      │    Container    │          │    Container    │  
      │                 │          │                 │  
      │     Nginx       │          │    FastAPI      │  
      │ HTML/CSS/JS     │          │       ↓         │  
      └─────────────────┘          │    LangChain    │  
                                   └────────┬────────┘  
                                            │  
                                            ▼  
                                      Hugging Face  
                                            │  
                                            ▼  
                                           LLM  


## Docker scheme:  

                 docker compose up  
                        │  
                        ▼  
                ┌───────────────┐  
                │      app      │  
                │   starting    │  
                └───────┬───────┘  
                        │  
                        ▼  
                 health check  
                        │  
                  ┌─────┴─────┐  
                  │           │  
               failure      success  
                  │           │  
                  │           ▼  
                  │      HEALTHY  
                  │           │  
                  │           ▼  
                  │     ┌──────────┐  
                  │     │ frontend │  
                  │     │  starts  │  
                  │     └──────────┘  
                  │  
                  └── retry  