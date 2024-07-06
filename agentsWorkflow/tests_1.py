from core.constants import *
from core.github_utils import check_pr_updates
from core.common_utils import invoke_llm
from core.prompts import initial_node_user_prompt, initial_node_system_prompt

token = GIT_TOKEN
repo_url = REPO

pr_state, updates = check_pr_updates(token, REPO, AGENT_GIT_USERNAME)
print(updates)
print("==================================================================")
# print(updates[0]['changes'])


response = invoke_llm(system_prompt=initial_node_system_prompt, user_prompt=initial_node_user_prompt.format(updates))
print(response)

# ToDO - Create an github account for the model and add it as a reviewer in the PR. Use it's username for login in functions, Also use it's github token.
