from textblob import TextBlob
import facebook
import itertools
import json
import re
import requests

access_token = 'EAAYFLQ8JBEQBADZCW8N0CGnLJzqmnQ675amrL2Qd9KoBr4rzU1HZASdJ0wNLZBG3hzBp9jmP9BN5zeH0ZBdEOt730Blel5sOjVsVuxYYB5Lhy20dJKhJYskPwD8A0ItxwFZBov7V8YOR0DRYEBb8T0191lw6xfNkZD'

def getSentimentAnalysisScore(user, number_of_posts_limit=50, number_of_comments_limit=50):
    text = ""
    graph = facebook.GraphAPI(access_token=access_token, version='2.9')
    wall = graph.get_connections(id=user, connection_name="posts", limit = number_of_posts_limit)
    posts = wall['data']
    number_of_posts = len(posts)
    post_no = 0
    while post_no < number_of_posts:
        current_post = posts[post_no]
        current_id = current_post['id']
        commentdata = graph.get_connections(id=current_id, connection_name='comments', limit = number_of_comments_limit)
        comments = commentdata['data']
        comment_no = 0
        number_of_comments = len(comments)
        while comment_no < number_of_comments:
            current_comment = comments[comment_no]
            comment_content = current_comment['message']
            text = text + comment_content
            comment_no += 1
        post_no += 1
    blob = TextBlob(text)
    print(blob.polarity)

