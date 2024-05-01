import praw
from src.config.config import *


def main():
    c = Config()

    client_id = c.get("REDDIT_CLIENT_ID")
    client_secret = c.get("REDDIT_CLIENT_SECRET")
    password = c.get("REDDIT_PASSWORD")
    user_agent = c.get("REDDIT_USERAGENT")
    username = c.get("REDDIT_USERNAME")

    subreddits = c.get("SUBREDDITS")

    reddit = praw.Reddit(
        client_id=client_id,
        client_secret=client_secret,
        password=password,
        user_agent=user_agent,
        username=username,
    )

    for subreddit in subreddits.split(','):
        subreddit = reddit.subreddit(subreddit)
        top_posts = subreddit.top('day')
        for post in top_posts:
            if post.score > 5:
                full_url = f"https://www.reddit.com{post.permalink}"
                print(f"r/{subreddit} -- [{post.score}] {post.title} ({full_url})")


if __name__ == '__main__':
    main()
