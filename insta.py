import os
import json

files = os.listdir('./insta_data')

'''
data[owner] -> user info like username, id, full_name, etc.
data[id] -> post id
data[edge_media_preview_like] -> number of likes
data[edge_media_to_tagged_user] -> tagged users
data[location] -> location
data[edge_media_to_parent_comment] -> comment metadata
data[taken_at_timestamp] -> timestamp
data[edge_media_to_caption] -> caption
data[is_ad] -> is ad
data[edge_media_to_sponsor_user] -> sponsor user
'''

user_ids = set()
tagged_users = set()
hashtags = set()

for f in files:
    print(f)
    path = './insta_data/' + f
    with open(path, 'r') as f:
        data = json.load(f)
        print(data.keys())
        break
        user_id = data['owner']['id']
        user_ids.add(user_id)
        for edge in data['edge_media_to_tagged_user']['edges']:
            tagged_users.add(edge['node']['user']['id'])
        for edge in data['edge_media_to_caption']['edges']:
            # find all hashtags
            for word in edge['node']['text'].split():
                if word[0] == '#':
                    hashtags.add(word)
        if data['location']:
            print(data['location'])

print(len(user_ids))
print(len(tagged_users))
print(len(hashtags))

# check intersection
print(len(user_ids.intersection(tagged_users)))

for i, hashtag in enumerate(hashtags):
    print(hashtag)
    if i > 4:
        break

# # print the intersection
# for user_id in user_ids.intersection(tagged_users):
#     print(user_id)