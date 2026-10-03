# Enterprise GenAI Knowledge & Agent Platform

A Python-based GenAI application that lets users ask questions about enterprise documents and get answers using RAG and an agent workflow.

The project is mainly built to understand and demonstrate how an enterprise-style GenAI application can be structured using FastAPI, LangGraph, vector search and Azure OpenAI.

## What this project does

A user sends a question to the application.

The application then:

1. Receives the question through a FastAPI API.
2. Determines what type of request it is.
3. Searches the available documents for relevant information.
4. Passes the retrieved information to the LLM.
5. Generates an answer based on the retrieved content.
6. Runs a validation step before returning the response.
7. Returns the answer along with the available source information.

The main goal is to keep the generated answer connected to the retrieved documents instead of asking the LLM to answer everything from its own knowledge.

## Example Use Case

An employee could ask questions such as:

- What is the company leave policy?
- What is the process for requesting access?
- What are the steps for an incident escalation?
- Which documents describe the vendor onboarding process?

The system retrieves relevant document content and uses that information to generate the response.

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
  +-------------------+
  |                   |
  v                   v
Retrieval Agent    Validation
  |
  v
Vector Search
  |
  v
FAISS
  |
  v
Relevant Documents
  |
  v
Azure OpenAI / LLM
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

FAISS is used as the local vector store for this project. For a larger deployment, it could be replaced with a managed search service such as Azure AI Search.

## Why RAG?

Enterprise documents can change regularly. Retraining an LLM every time a document changes would not be practical.

With RAG, the application can retrieve the relevant information at query time and provide that information to the LLM as context.

This also makes it easier to show where the answer came from.

## Why LangGraph?

I used LangGraph to keep the workflow organized into separate steps.

For example:

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

This makes it easier to add conditional steps later instead of putting the entire workflow into one large prompt or function.

## Why Azure OpenAI?

Azure OpenAI can be used when the application needs an Azure-based LLM deployment.

It also fits well with other Azure services that could be added later for authentication, secrets, monitoring and deployment.

For local development, the project can run in demo mode without Azure credentials.

## Project Structure

```text
enterprise-genai-rag-agent-platform/
├── app/
│   ├── main.py
│   ├── config.py
│   ├── schemas.py
│   ├── graph.py
│   ├── agents/
│   │   └── retrieval_agent.py
│   └── services/
│       ├── embeddings.py
│       ├── llm.py
│       └── vector_store.py
├── data/
│   └── sample_documents/
├── tests/
├── .env.example
├── .gitignore
├── Dockerfile
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

### 3. Install the dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Copy:

```text
.env.example
```

to:

```text
.env
```

Add the required configuration if you want to use the Azure OpenAI integration.

### 5. Start the API

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000/docs
```

## Local Demo

The project includes a demo mode so the basic application can be tested without connecting to Azure.

This is useful for testing the API and project workflow locally before configuring an LLM provider.

## Testing

Tests are included for the application logic and API behavior.

Run:

```bash
pytest
```

## Possible Production Changes

This repository is a portfolio project, so some components are kept simple for local development.

If I were extending it for a production environment, I would consider:

- Azure AI Search instead of local FAISS
- Microsoft Entra ID for authentication
- Azure Key Vault for secrets
- Azure Container Apps or AKS for deployment
- Application Insights/OpenTelemetry for monitoring
- Retry and timeout handling
- Rate limiting
- CI/CD pipeline
- RAG evaluation and response-quality monitoring

These are possible production improvements and are not being claimed as implemented in this repository.

## Important Note

This is a portfolio/reference implementation.

I have not represented it as a production system with real enterprise users or production traffic.

The purpose of the project is to demonstrate my understanding of:

- RAG
- LLM integration
- LangGraph workflows
- Vector search
- FastAPI
- Agent-based application design
- Basic validation and guardrails

## Interview Explanation

### 30-second explanation

> "I built an enterprise-style knowledge assistant using Python, FastAPI, LangGraph and RAG. The user sends a question through the API, the application retrieves relevant information from a vector store, and the LLM generates an answer using that retrieved context. I also added a validation step so the workflow is not just a single LLM call. I used FAISS for local development and designed the project so it could later be extended with Azure AI Search and other Azure services."

### Key points I can explain

- How document retrieval works
- Why embeddings are required
- How FAISS performs similarity search
- How RAG reduces unsupported answers
- Why LangGraph is useful for multi-step workflows
- How FastAPI exposes the GenAI application
- How Azure OpenAI can be integrated
- How the project could be moved from local development to Azure
- How validation/guardrails can be added around an LLM

## Limitations

This project currently uses a local FAISS vector store and sample documents.

It is not presented as a production deployment.

The Azure components mentioned in the production section are possible extensions rather than claims of an existing production implementation.
