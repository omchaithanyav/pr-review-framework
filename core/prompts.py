pr_review_agent_prompt = """
You are provided with a json of Pull Request details and you need to review Pull Request and provide the following:
1. pr_number
2. List of actions that are required to be performed on the Pull Request.

Note: Pull Request actions can be any of the following: 
a. 
b.
c.
d.
e. 

Pull Request details: {{}}

Your output should be in json format and the json should contain only 'pr_number' and 'actions' which is a list of actions.
If no actions are required just give empty list for 'actions'
Dont include any extra information other than the json in your response.
"""

pr_action_agent_prompt = """
{} {}
"""
