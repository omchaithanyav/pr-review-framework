from github import Github
from typing import List, Dict, Any, TypedDict, Optional

# ToDo - use django models instead of global dictionary to store details of PRs.
pr_state = {}


def git_authenticate(token):
    return Github(token)


def git_get_repo(github, repo_url):
    return github.get_repo(repo_url)


def git_get_pull_requests(repo):
    return repo.get_pulls(state='open', sort='created', direction='desc')


def git_fetch_pr_details(pr):
    details = {
        'number': pr.id,
        'title': pr.title,
        'body': pr.body,
        'user': pr.user.login,
        'created_at': pr.created_at,
        'updated_at': pr.updated_at,
        'comments': [comment.body for comment in pr.get_issue_comments()],
        'files': [{
            'filename': file.filename,
            'patch': file.patch,
            'blob_url': file.blob_url
        } for file in pr.get_files()],
        'changes': [file.patch for file in pr.get_files() if file.patch],
        'reviewers': [reviewer.login for reviewer in pr.get_review_requests()[0]],
        'latest_commit': pr.get_commits().reversed[0].sha,
        'mergeable': pr.mergeable,
        'mergeable_state': pr.mergeable_state,
        'merged': pr.merged,
        'state': pr.state
    }
    return details


def git_add_comment(pr, comment):
    pr.create_issue_comment(comment)


def git_request_re_review(pr):
    reviewers = [reviewer.login for reviewer in pr.get_review_requests()[0]]
    if reviewers:
        pr.create_review_request(reviewers)


def git_approve_pr(pr):
    pr.create_review(body="Approved", event="APPROVE")


def git_check_new_commits(pr, last_commit_sha):
    latest_commit_sha = pr.get_commits().reversed[0].sha
    return latest_commit_sha != last_commit_sha


def git_get_org_repos(org_name):
    github = git_authenticate()
    org = github.get_organization(org_name)
    repos = org.get_repos()
    repo_list = [{"name": repo.name, "url": repo.html_url} for repo in repos]
    return repo_list


def git_get_user_repos(github, username):
    user = github.get_user(username)
    repos = user.get_repos()
    repo_list = [{"name": repo.name, "url": repo.html_url, "private": repo.private} for repo in repos]
    return repo_list


def git_merge_pr(pr):
    if pr.mergeable and pr.mergeable_state == 'clean':
        pr.merge()
        return f"PR #{pr.number} has been successfully merged."
    else:
        return f"PR #{pr.number} cannot be merged due to conflicts or other issues."


def check_pr_updates(token: str, repo_url: str) -> List[Dict[str, Any]]:
    global pr_state

    github = git_authenticate(token)
    repo = git_get_repo(github, repo_url)
    pull_requests = git_get_pull_requests(repo)

    updates = []
    for pr in pull_requests:
        pr_details = git_fetch_pr_details(pr)
        if pr_details['state'] == "open":
            pr_number = pr_details['number']

            prev_state = pr_state.get(str(pr_number), {})
            prev_commit_sha = prev_state.get('latest_commit', None)
            prev_comments_count = prev_state.get('comments_count', 0)

            new_commit = git_check_new_commits(pr, prev_commit_sha)

            comments_list = list(pr.get_issue_comments())
            new_comments = comments_list[prev_comments_count:]
            new_comments_text = [comment.body for comment in new_comments]

            update_info = {
                'pr_number': pr_number,
                'new_commit': new_commit,
                'new_comments': new_comments_text,
                'mergeable': pr_details['mergeable'],
                'mergeable_state': pr_details['mergeable_state'],
                'merged': pr_details['merged'],
                'state': pr_details['state']
            }

            if new_commit:
                update_info['changes'] = pr_details['changes']
                update_info['files'] = []
                for file in pr.get_files():
                    file_content = repo.get_contents(file.filename, ref=pr.head.sha)
                    update_info['files'].append({
                        'filename': file.filename,
                        'content': file_content.decoded_content.decode('utf-8')
                    })

            updates.append(update_info)

            pr_state[str(pr_number)] = {
                'latest_commit': pr_details['latest_commit'],
                'comments_count': len(comments_list)
            }

    return pr_state, updates
