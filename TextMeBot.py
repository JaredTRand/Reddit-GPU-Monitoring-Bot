import praw
import prawcore
import pdb
import re
import os
import SMS
import time


reddit = praw.Reddit('bot1')
sub = "buildapcsales"
subreddit = reddit.subreddit(sub)
start_time = time.time()
count = 0



if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []
else:
    with open("posts_replied_to.txt", "r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = list(filter(None, posts_replied_to))

for submission in subreddit.stream.submissions():
        if submission.id not in posts_replied_to:
            if re.search("gpu", submission.title, re.IGNORECASE):
                count += 1
                print("Found GPU\n Sending...")
                message = ("\n{0} \n\n\n {1}".format(submission.title, submission.url))
                SMS.send4(message)
                print("\n ::Sent:: \n GPUs Sent: {0}\n\n".format(str(count)))

                with open("posts_replied_to.txt", "w") as f:
                    for post_id in posts_replied_to:
                        f.write(post_id + "\n")
