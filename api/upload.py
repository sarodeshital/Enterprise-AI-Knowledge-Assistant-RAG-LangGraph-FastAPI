from fastapi import APIRouter, UploadFile
router=APIRouter()
@router.post("/upload")
async def upload(file:UploadFile):
    return {"filename":file.filename}
