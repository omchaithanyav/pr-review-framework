from core.common_utils import invoke_llm
from core.constants import *
from core.github_utils import check_pr_updates
from core.prompts import initial_node_system_prompt, initial_node_user_prompt


class Nodes:

    def __init__(self):
        pass

    def determine_pr_action(self, state):
        # pr_state = state.get("pr_state", {})
        # pr_details = state.get("pr_details", [])
        pr_state, pr_details = check_pr_updates(GIT_TOKEN, REPO, AGENT_GIT_USERNAME)
        action_required_prs = []
        for pr in pr_details:
            response = invoke_llm(system_prompt=initial_node_system_prompt,
                                  user_prompt=initial_node_user_prompt.format(pr))
            # ToDo From response we need to extract pr_number and action_required

        return {
            **state,
            "pr_state": pr_state,
            "pr_details": pr_details,
            # "action_required_prs": action_required_prs, # [{pr_number: <pr_num>, action_required: action, approved: boolean}]
        }
        # pr_state: dict
        # pr_details: list[dict]
        # action_required_prs: dict  # {pr_number: <pr_num>, action_required: action, approved: boolean}

