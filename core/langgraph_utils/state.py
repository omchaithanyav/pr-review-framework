from typing import TypedDict


class GraphState(TypedDict):
    pr_state: dict
    pr_details: list[dict]
    action_required_prs: list[dict]  # [{pr_number: <pr_num>, actions_required: [actions]}