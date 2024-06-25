from langchain_openai import ChatOpenAI
import os
from core.constants import OPENAI_API_KEY

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0.5,
    max_tokens=None,
    timeout=None,
    max_retries=2)


def invoke_llm(system_prompt="You are a helpful assistant.", user_prompt=None):

    messages = [("system", system_prompt,), ("human", user_prompt), ]
    ai_msg = llm.invoke(messages)
    return ai_msg.content
