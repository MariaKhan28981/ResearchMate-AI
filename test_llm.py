from src.llm.llm_client import get_llm


llm = get_llm()


from src.prompts.prompt_templates import research_prompt


chain = research_prompt | llm


response = chain.invoke(
    {
        "question": "Explain what a research paper is in simple words"
    }
)


print(response.content)