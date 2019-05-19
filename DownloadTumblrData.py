import pytumblr
import datetime
import json
import os
from arguments import folder_name, tag
from secrets import c_key, c_s, o_token, o_s

# The file assumes, that the arguments are in arguments.py file
# This file is in the same folder, then from where the script is run
# In includes two pieces of info:
#     1. folder_name - where the posts are saved
#     2. tag - tag of post to search for
# The keys of Tumblir (which you can get from their site) are
# assumed to be saved in the secrets.py file

# Tumblr has an API limit of 1000 per hour and 5000 per day. So what I had was
# a cron job, which had run this script at 5 times per day

try:
    with open("timestamp.txt") as f:
        current_time_stamp = f.readlines()
        current_time_stamp = current_time_stamp[0].strip()
        current_time_stamp = int(current_time_stamp)
except FileNotFoundError or ValueError:
    current_time_stamp = int("{:%s}".format(datetime.datetime.now()))


client = pytumblr.TumblrRestClient(c_key, c_s, o_token, o_s)

time_data = True

for i in range(1000):
    if time_data:
        current_data = client.tagged(tag=tag, before=current_time_stamp)
        if not current_data:
            print(str(i) + " is empty dataset")
            break
        if isinstance(current_data, dict):
            print("Problem?")
            break
        for post in current_data:
            with open(os.path.join(folder_name, str(post["id"]) + ".json"), "w") as f:
                json.dump(post, f)
            current_time_stamp = post["timestamp"]
    else:
        break

try:
    new_timestamp = post["timestamp"]
    with open("timestamp.txt", "w") as f:
        f.write(str(new_timestamp))
except NameError:
    print("Done?")
