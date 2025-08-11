from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama
import scripts.config as config

query_refinement_template_str = """
You are an expert at converting user questions into a set of relevant keywords suitable for retrieving information from a knowledge base. Don't generate any keyword if the User's question is not relarted to any memory or doesn't need memories to answer.
Your last response: {ai_response}
User question: {user_question}
Generate up to 10 distinct (less is better), concise keywords that capture the main concepts. Remove articles and unnecessary words. Separate the keywords with commas.
Keywords:
"""
query_refinement_prompt_template_obj = ChatPromptTemplate.from_template(query_refinement_template_str)

def get_query_refinement_chain():
    query_ref_llm = ChatOllama(
        model=config.OLLAMA_MODEL_NAME_SMALL, base_url=config.OLLAMA_ENDPOINT_SMALL,
        num_ctx=config.OLLAMA_NUM_CTX_SMALL, temperature=0
    )
    return query_refinement_prompt_template_obj | query_ref_llm
