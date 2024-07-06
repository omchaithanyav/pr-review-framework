from langchain_openai import ChatOpenAI
import os
from core.constants import *

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

llm = ChatOpenAI(
    model=MODEL_IN_USE,
    temperature=0.5,
    max_tokens=None,
    timeout=None,
    max_retries=2)


def invoke_llm(system_prompt="You are a helpful assistant.", user_prompt=None):

    messages = [("system", system_prompt,), ("human", user_prompt), ]
    llm_response = llm.invoke(messages)
    return llm_response.content
