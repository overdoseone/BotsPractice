# import schedule
from instapy import InstaPy
import dotenv
import os

# load credentials
dotenv.load_dotenv('.env')

# grab credentials for us
un = os.environ.get('IG_USERNAME')
pwd = os.environ.get('IG_PWD')


ht = ['aquariusnewmoon']
users = ['nish_rdh', 'pradadagod', 'babyboyhaaaze', '2beesinthetrap']  #followers
comments = []

# session login
session = InstaPy(username=un, password=pwd)
session.login()

# liked by tags
# session.like_by_tags(ht, amount=2, skip_top_posts=False)


# watch users story
session.set_do_story(enabled = True, percentage = 70, simulate = False)
session.story_by_users(users)

# Interact with specific users
# set_do_like, set_do_comment, set_do_follow are applicable

# session.set_do_follow(enabled=False, percentage=50)
# session.set_comments(comments)
# session.set_do_comment(enabled=True, percentage=80)
# session.set_do_like(True, percentage=70)
# session.interact_by_users(users, amount=5, randomize=True, media='Photo')


# session logout
session.end()
