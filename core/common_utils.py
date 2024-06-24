from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0.5,
    max_tokens=None,
    timeout=None,
    max_retries=2)


def invoke_llm(system_prompt, user_prompt):
    messages = [("system", system_prompt,), ("human", user_prompt), ]
    ai_msg = llm.invoke(messages)
    return ai_msg.content
