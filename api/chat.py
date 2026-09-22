from fastapi import APIRouter
router=APIRouter()
@router.post("/chat")
def chat(body:dict):
    return {"answer":"Sample response. Connect Azure OpenAI here."}
