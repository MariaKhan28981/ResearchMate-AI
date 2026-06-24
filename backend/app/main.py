from fastapi import FastAPI

from app.api.sessions import router as session_router
from app.api.upload import router as upload_router
from app.api.chat import router as chat_router
app = FastAPI(
    title="ResearchHelp API"
)

app.include_router(session_router)
app.include_router(upload_router)
app.include_router(chat_router)