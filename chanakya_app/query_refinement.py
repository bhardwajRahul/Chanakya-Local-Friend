from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI
import scripts.config as config
from .app_setup import app

query_refinement_template_str = """
You are an expert at converting user questions into a set of relevant keywords suitable for retrieving information from a knowledge base. Don't generate any keyword if the User's question is not relarted to any memory or doesn't need memories to answer.
Your last response: {ai_response}
User question: {user_question}
Generate up to 10 distinct (less is better), concise keywords that capture the main concepts. Remove articles and unnecessary words. Separate the keywords with commas.
Keywords:
"""
query_refinement_prompt_template_obj = ChatPromptTemplate.from_template(query_refinement_template_str)

def get_query_refinement_chain():
    provider = config.LLM_PROVIDER.lower()
    app.logger.info(f"Configuring Query Refinement LLM with provider: {provider}")

    if not config.LLM_MODEL_NAME_SMALL or not config.LLM_ENDPOINT_SMALL:
        app.logger.warning("Small LLM not configured, query refinement will be disabled.")
        return None

    if provider == 'ollama':
        query_ref_llm = ChatOllama(
            model=config.LLM_MODEL_NAME_SMALL,
            base_url=config.LLM_ENDPOINT_SMALL,
            num_ctx=config.LLM_NUM_CTX_SMALL,
            temperature=0
        )
    elif provider == 'openai' or provider == 'lmstudio':
        query_ref_llm = ChatOpenAI(
            model=config.LLM_MODEL_NAME_SMALL,
            base_url=config.LLM_ENDPOINT_SMALL,
            api_key=config.LLM_API_KEY or "NA",
            temperature=0,
            max_tokens=50 # Keywords should be short
        )
    else:
        raise ValueError(f"Unsupported LLM_PROVIDER for query refinement: {config.LLM_PROVIDER}")

    return query_refinement_prompt_template_obj | query_ref_llm
