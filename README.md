# Enterprise AI Knowledge Assistant — RAG + LangGraph + FastAPI

A Python-based GenAI application for asking questions about enterprise documents.

The project uses RAG to retrieve relevant information from documents before generating an answer. LangGraph is used to organize the workflow, while FastAPI provides the API layer.

I built this project to practice how a knowledge-assistant application can be structured using RAG, LLMs, agent workflows and a backend API.

## What the application does

A user sends a question to the application.

The application:

1. Receives the question through the FastAPI API.
2. Processes the request.
3. Retrieves relevant information from the available documents.
4. Passes the retrieved information to the LLM.
5. Generates an answer using the retrieved context.
6. Performs a validation step.
7. Returns the response along with source information where available.

The main idea is to give the LLM relevant document content instead of asking it to answer everything from its general knowledge.

## Example questions

An employee could ask:

- What is the company leave policy?
- How do I request system access?
- What is the incident escalation process?
- What are the vendor onboarding steps?
- Which document contains the access approval process?

The system searches the available knowledge and uses the retrieved information to generate the response.

## Architecture

```text
User
 |
 v
FastAPI
 |
 v
LangGraph Workflow
 |
 +----------------------+
 |                      |
 v                      v
Retrieval Agent       Validation
 |
 v
Embeddings
 |
 v
FAISS Vector Store
 |
 v
Relevant Documents
 |
 v
LLM
 |
 v
Grounded Response
```

## Technologies Used

- Python
- FastAPI
- LangChain
- LangGraph
- Azure OpenAI
- FAISS
- Pydantic
- Pytest
- Docker

FAISS is used as the local vector store for development.

For a larger deployment, the vector-search layer could be replaced with a managed service such as Azure AI Search.

## Why RAG?

Enterprise documents can change over time.

Instead of retraining the LLM whenever a document changes, RAG allows the application to retrieve the relevant document content at the time of the question.

The retrieved content is then provided to the LLM as context.

This also makes it possible to return the source information used for the answer.

## Why LangGraph?

I used LangGraph to organize the application into separate workflow steps.

A simplified version of the workflow is:

```text
Question
   |
   v
Retrieve
   |
   v
Generate
   |
   v
Validate
   |
   v
Response
```

Using a graph makes it easier to add conditions or additional steps later.

For example, a future version could route different types of questions to different retrieval or processing steps.

## Why FastAPI?

FastAPI provides the backend API for the application.

It allows the GenAI workflow to be accessed through an HTTP endpoint instead of keeping the application logic inside a user interface.

This also makes it easier to connect a frontend or another application to the backend later.

## Why Azure OpenAI?

Azure OpenAI can be used as the LLM provider for the application.

It is also possible to combine it with other Azure services for authentication, secrets, monitoring and deployment.

For local development, the project can also run in demo mode without Azure credentials.

## Project Structure

```text
Enterprise-AI-Knowledge-Assistant-RAG-LangGraph-FastAPI/
├── agents/
│   └── planner/
├── api/
│   └── chat/
├── backend/
│   └── main
├── docker/
├── docs/
│   └── architecture/
├── frontend/
│   └── streamlit_app/
├── rag/
│   └── embeddings/
├── tests/
│   └── test_api/
├── .env.example
├── docker-compose.yml
├── requirements.txt
└── README.md
```

## Run Locally

### 1. Create a virtual environment

```bash
python -m venv .venv
```

### 2. Activate the environment

**Windows PowerShell**

```powershell
.\.venv\Scripts\Activate.ps1
```

**Mac/Linux**

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Copy `.env.example` to `.env`.

Add the required configuration if you want to connect the application to Azure OpenAI or another configured LLM provider.

### 5. Start the application

```bash
uvicorn backend.main:app --reload
```

The API can then be accessed through:

```text
http://127.0.0.1:8000/docs
```

## Docker

The repository also contains a `docker-compose.yml` file for running the application using Docker.

```bash
docker compose up --build
```

## Local Demo

The project can be used in a local/demo setup without connecting to Azure credentials, depending on the configured application mode.

This makes it easier to test the API and RAG workflow locally.

## Testing

Tests are included for the API and application behavior.

Run:

```bash
pytest
```

## Possible Production Improvements

This is a portfolio project, so some components are kept simple for local development.

If I were extending the application for production, I would consider:

- Azure AI Search instead of local FAISS
- Microsoft Entra ID for authentication
- Azure Key Vault for secrets
- Azure Container Apps or AKS for deployment
- Application Insights or OpenTelemetry for monitoring
- Retry and timeout handling
- API rate limiting
- CI/CD
- RAG evaluation
- Response-quality monitoring
- Document ingestion and update pipelines

These are possible extensions and are not claims of an existing production deployment.

## Important Note

This repository is a portfolio project.

It is designed to demonstrate my understanding of RAG, LLM applications and agent workflows. It should not be interpreted as a production system with real enterprise users or production traffic.

The main areas demonstrated by the project are:

- RAG
- LLM integration
- LangGraph workflows
- Vector search
- FastAPI
- Agent-based application design
- API development
- Basic validation and guardrails
- Docker-based development

## Interview Explanation

### 30-second version

> "I built an enterprise knowledge assistant using Python, FastAPI, LangGraph and RAG. A user sends a question through the API, the application retrieves relevant information from the document knowledge base, and the LLM generates a response using that retrieved context. I also added a validation step so the workflow is more controlled than a simple LLM call. I used FAISS for local vector search and designed the project so the retrieval layer could later be moved to a managed service such as Azure AI Search."

## Key Technical Points I Can Explain

### RAG

How documents are processed, converted into embeddings and searched to retrieve relevant context.

### Embeddings

How text is converted into vectors so that semantically similar content can be retrieved.

### FAISS

How the local vector index is used for similarity search.

### LangGraph

How the application workflow is divided into multiple steps and how state can be passed between those steps.

### FastAPI

How the GenAI workflow is exposed through API endpoints.

### Azure OpenAI

How an Azure-hosted LLM can be connected to the application.

### Validation

How an additional validation step can be used to check the generated response before returning it.

### Production Evolution

How the local implementation could be extended with Azure AI Search, authentication, Key Vault, monitoring, CI/CD and evaluation.

## Limitations

The current project is primarily designed for learning and portfolio demonstration.

The local version uses sample documents and a local vector-search setup.

It is not presented as a production deployment.

Azure services mentioned in the production section are possible extensions unless they are explicitly configured and implemented in the current version.
