import json
import os


BASE_DIR = "app/data/chats"


def get_history_path(chat_id):

    return os.path.join(
        BASE_DIR,
        chat_id,
        "history.json"
    )


def load_history(chat_id):

    path = get_history_path(chat_id)

    if not os.path.exists(path):

        return []

    with open(
        path,
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)


def save_message(
    chat_id,
    role,
    content
):

    history = load_history(chat_id)

    history.append({

        "role": role,

        "content": content

    })

    with open(
        get_history_path(chat_id),
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            history,
            f,
            indent=2
        )

def get_recent_history(
    chat_id,
    limit=6
):

    history = load_history(chat_id)

    recent = history[-limit:]

    text = ""

    for msg in recent:

        text += (

            f"{msg['role']}: "

            f"{msg['content']}\n\n"

        )

    return text