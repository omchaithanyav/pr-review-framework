from typing import TypedDict


class GraphState(TypedDict):
    pr_state: dict
    pr_details: list[dict]
    action_required_prs: dict  # {pr_number: <pr_num>, action_required: action, approved: boolean}
