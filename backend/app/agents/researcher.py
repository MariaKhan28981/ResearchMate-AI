from app.core.vectorstore import get_vectorstore


def classify_intent(question: str):

    q = question.lower()

    if any(word in q for word in [
        "title",
        "author",
        "authors",
        "affiliation",
        "journal",
        "conference",
        "published",
        "doi"
    ]):
        return "metadata"

    elif any(word in q for word in [
        "summary",
        "summarize",
        "overview",
        "abstract"
    ]):
        return "summary"

    elif any(word in q for word in [
        "method",
        "methodology",
        "approach",
        "framework",
        "architecture",
        "algorithm",
        "model"
    ]):
        return "methodology"

    elif any(word in q for word in [
        "dataset",
        "data",
        "samples",
        "training data"
    ]):
        return "dataset"

    elif any(word in q for word in [
        "result",
        "accuracy",
        "performance",
        "experiment",
        "evaluation",
        "metric"
    ]):
        return "results"

    elif any(word in q for word in [
        "conclusion",
        "conclude",
        "final findings"
    ]):
        return "conclusion"

    elif any(word in q for word in [
        "future work",
        "future scope",
        "future direction"
    ]):
        return "future_work"

    elif any(word in q for word in [
        "limitation",
        "limitations",
        "drawback",
        "weakness"
    ]):
        return "limitations"

    return "general"


def retrieve_docs(vectorstore, intent, question):

    if intent == "metadata":

        query = """
        title authors affiliations journal conference publication
        """

        return vectorstore.similarity_search(
            query,
            k=15
        )

    elif intent == "summary":

        query = """
        abstract introduction contribution overview paper summary
        """

        return vectorstore.similarity_search(
            query,
            k=15
        )

    elif intent == "methodology":

        query = """
        methodology proposed method framework architecture algorithm
        """

        return vectorstore.similarity_search(
            query,
            k=15
        )

    elif intent == "dataset":

        query = """
        dataset data collection preprocessing samples
        """

        return vectorstore.similarity_search(
            query,
            k=15
        )

    elif intent == "results":

        query = """
        results experiments evaluation performance accuracy recall precision
        """

        return vectorstore.similarity_search(
            query,
            k=15
        )

    elif intent == "conclusion":

        query = """
        conclusion concluding remarks findings summary of results
        """

        return vectorstore.similarity_search(
            query,
            k=20
        )

    elif intent == "future_work":

        query = """
        future work future scope future directions
        """

        return vectorstore.similarity_search(
            query,
            k=20
        )

    elif intent == "limitations":

        query = """
        limitations drawbacks challenges weaknesses
        """

        return vectorstore.similarity_search(
            query,
            k=20
        )

    return vectorstore.similarity_search(
        question,
        k=15
    )


def research_agent(state):

    print("🔍 Research Agent Running...")

    chat_id = state["chat_id"]
    question = state["question"]

    vectorstore = get_vectorstore(chat_id)

    intent = classify_intent(question)

    print(f"Detected intent: {intent}")

    docs = retrieve_docs(
        vectorstore,
        intent,
        question
    )

    context = ""

    for doc in docs:

        source = doc.metadata.get(
            "source",
            "Unknown"
        )

        page = doc.metadata.get(
            "page",
            "Unknown"
        )

        context += f"""

SOURCE FILE: {source}
PAGE: {page}

{doc.page_content}

=================================================

"""

    return {

        "context": context

    }