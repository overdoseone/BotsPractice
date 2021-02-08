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
users = ['nish_rdh', 'pradadagod', 'babyboyhaaaze']
session = InstaPy(username=un, password=pwd)
session.login()
session.like_by_tags(ht, amount=2, skip_top_posts=False)
# session.set_do_story(enabled = True, percentage = 70, simulate = False)
# session.story_by_users(users)
