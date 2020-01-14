# -*- coding: utf-8 -*-

#http://www.storybench.org/how-to-scrape-reddit-with-python/
#https://praw.readthedocs.io/en/latest/getting_started/quick_start.html
#https://github.com/reddit-archive/reddit/wiki/OAuth2-Quick-Start-Example#first-steps
#https://praw.readthedocs.io/en/latest/code_overview/models/subreddit.html
#https://www.reddit.com/dev/api/

#import pandas as pd
import praw
import os
import json

reddit = praw.Reddit(client_id='Os3d8lng12RvkQ', \
                     client_secret='lPkGWsG0iVWYY1TSigmV5NgpAcc', \
                     user_agent='re0123456', \
                     username='re0123456', \
                     password='Password@1')




#business is a subreddit
subreddit = reddit.subreddit('business')


#create dir
current_directory = os.path.join(os.getcwd(), r'business')
final_directory = os.path.join(current_directory, r'hot')
if not os.path.exists(final_directory):
    os.makedirs(final_directory)
comment_directory = os.path.join(final_directory, r'hotComment')
if not os.path.exists(comment_directory):
    os.makedirs(comment_directory)

	
#.hot, .new, .hot, .hot, .gilded, .search("SEARCH_KEYWORDS")
hot_subreddit = subreddit.hot(limit=None)# all, day, hour, month, week, year (default: all).
#subreddit.hot(limit=None)
#subreddit.new(limit=None)
#subreddit.gilded(limit=None)
#subreddit.hot('month')# all, day, hour, month, week, year (default: all).
#subreddit.search('lady')
#subreddit.search('female')


#create txt for log
logf = os.path.join(final_directory, 'hot.txt')
logf_c = os.path.join(comment_directory, 'hot_c.txt')
#generator
for submission in hot_subreddit:
    try:
        s = vars(submission)
        s1 = {k:(str(v) if len(str(type(v))) > 18 else v) for k,v in s.items()}
        #print(submission.title, submission.id)
        filename = os.path.join(final_directory, s1['id']+'.json')
        with open(filename, 'w') as outfile:
            json.dump(s1, outfile)
        with open(logf, 'a') as log:
            log.write(submission.id+', Success')
            log.write('\n')
        #comments
        for comment in submission.comments:
            try:
                c = vars(comment)
                c1 = {k:(str(v) if len(str(type(v))) > 18 else v) for k,v in c.items()}
                
                filename_c = os.path.join(comment_directory, c1['id']+'.json')
                with open(filename_c, 'w') as outfile:
                    json.dump(c1, outfile)
                with open(logf_c, 'a') as log:
                    log.write(comment.id + " Comment done" )
                    log.write('\n')
            except Exception as e:
                with open(logf_c, 'a') as log:
                    log.write("Failed to download {0}: {1}\n".format(submission.id, str(e)))
                continue
    except Exception as e:
        with open(logf, 'a') as log:
            log.write("Failed to download {0}: {1}\n".format("hot", str(e)))
        continue

