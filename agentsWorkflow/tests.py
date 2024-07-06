from django.test import TestCase

# Create your tests here.
import github


# TODO: Comments should contain mutiple objects
def submit_review(pr, request_type, request_body, file_path, line_number, comment_body):
    comment = pr.create_review(event=request_type, body=request_body,
                               comments=[{'path': file_path, 'position': line_number, 'body': comment_body}])
    return comment


def retrieve_review_comments(pr):
    all_comments = []
    comments = pr.get_review_comments()
    for comment in comments:
        all_comments.append({
            "type": "review_comment",
            "body": comment.body,
            "path": comment.path,
            "position": comment.position,
        })
    return comments


def retrieve_issue_comments(pr):
    comments = [comment.body for comment in pr.get_issue_comments()]
    return comments


def retrieve_review_header_comment(pr):
    comments = [comment.body for comment in pr.get_reviews()]
    return comments
