import json
import os


SUMMARY_FILE="paper_summary.json"



def save_summary(summary):

    with open(
        SUMMARY_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            {
                "summary":summary
            },
            f
        )



def load_summary():

    if not os.path.exists(SUMMARY_FILE):
        return None


    with open(
        SUMMARY_FILE,
        encoding="utf-8"
    ) as f:

        data=json.load(f)

    return data["summary"]