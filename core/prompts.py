"""
This file contains all the user and system prompts.
"""


initial_node_system_prompt = "You should understand the given PR details and decide the action to be performed on the PR."

initial_node_user_prompt = f"""
You are provided with a JSON containing Pull Request details. Properly review the PR details and provide the following:
1. pr_number
2. action: Next Action required to be performed on the PR.
3. reason: Provide the reason for action decided.

Possible Actions are:
a. review_pr: Add review comments on PR and request for changes.
b. approve_pr: Approve the PR.
c. merge_pr: Merge the PR.
d. none: No action required.

Criteria to Decide Action:
- review_pr: Select this action if there are issues that need to be addressed or if the PR needs additional examination before a final decision can be made.
- approve_pr: Select this action if all criteria are met, and the PR is ready for merging.
- merge_pr: Select this action if the PR is approved and no other changes are required on the PR.
- none: Select this action if PR details is empty.

PR details: {{}}

Important: Do not include any extra information other than the JSON in your response.

Instructions: 
1. Your output should be in JSON format and the JSON should contain only 'pr_number', 'action', and 'reason'.
2. You should refer to the title, description, and previous comments of the PR, and check the file changes. If any aspect is not satisfied, or if any code files do not adhere to coding standards and best practices, your action should be review_pr. If everything is satisfied, your action should be approve_pr.
3. When the `mergeable` flag is true and the `merged` flag is false, do not approve the PR directly. Instead, review the PR details thoroughly and ensure it meets all criteria before deciding on the appropriate action.
"""
# a. add_review_comments: Provide detailed review comments.
# b. request_changes: Request specific changes.
# c. re_request_reviews: Re-request reviews from reviewers.
# d. approve_pr: Approve the PR.
# e. merge_pr: Merge the PR.
# f. close_pr: Close the PR.

pr_action_agent_prompt = """
{} {}
"""
