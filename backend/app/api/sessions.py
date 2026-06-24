from fastapi import APIRouter
import uuid
import os
import json

router = APIRouter()

BASE_DIR = "app/data/chats"


@router.post("/new-chat")
def create_chat():

    chat_id = str(uuid.uuid4())

    chat_path = os.path.join(
        BASE_DIR,
        chat_id
    )

    os.makedirs(
        os.path.join(chat_path, "papers"),
        exist_ok=True
    )

    os.makedirs(
        os.path.join(chat_path, "chroma"),
        exist_ok=True
    )

    history_path = os.path.join(
        chat_path,
        "history.json"
    )

    with open(
        history_path,
        "w"
    ) as f:

        json.dump([], f)

    return {
        "chat_id": chat_id
    }