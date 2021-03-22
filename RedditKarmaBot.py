# import the modules
# pip install https://github.com/LilSpazJoekp/praw/archive/objectify_user_subreddit.zip
from os import environ
import praw

#Targets
target_points = int(environ["target_points"])


# Creds 
client_id = environ["client_id"]
client_secret = environ["client_secret"]
username = environ["username"]
password = environ["password"]
user_agent = "This is a reddit bot to update display name automatically based on current karma" 

# creating an authorized reddit instance 
reddit = praw.Reddit(client_id = client_id,  
                    client_secret = client_secret,  
                    username = username,  
                    password = password, 
                    user_agent = user_agent)  




#Get karma stats and calculate target

redditor1 = reddit.redditor(username)
link_points = redditor1.link_karma
comment_points = redditor1.comment_karma
awardee_points = redditor1.awardee_karma
awarder_points = redditor1.awarder_karma

total_points = link_points+comment_points+awardee_points+awarder_points
Points2Go = target_points - total_points

print("Your current karma is: " + str(total_points) + " & you need " + str(Points2Go) + " More Points")

Current_title = str(reddit.user.me(use_cache=False).subreddit.title)
newtitle = str(Points2Go) + " more more karma to go"

if newtitle != Current_title:
    #edit the display name
    reddit.user.me().subreddit.mod.update(title=newtitle)
    print("Name has been updated, New Title: " + reddit.user.me(use_cache=False).subreddit.title)
    exit()
else: 
    print("No change needed")
    exit()
