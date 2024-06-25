from core.common_utils import invoke_llm
from core.constants import GIT_TOKEN, REPO
from core.github_utils import check_pr_updates
from core.prompts import pr_review_agent_prompt, pr_action_agent_prompt


class Nodes:

    def __init__(self):
        pass

    def review_prs(self, state):
        # pr_state = state.get("pr_state", {})
        # pr_details = state.get("pr_details", [])
        pr_state, pr_details = check_pr_updates(GIT_TOKEN, REPO)
        llm_response = invoke_llm(pr_review_agent_prompt.format(pr_details))
        # TODO: We can iterate through every PR (pr_details) and pass it to llm for deciding the actions on every PR and store it in a list, then return the list to update state.

    def execute_action_on_prs(self, state):
        pass


# TODO:  Based on actions required - the specific tool/node will be called - for example we will have one tool (custom) for approving pr, one for commenting on pr, one for merging, etc.
