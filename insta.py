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
locations = {}
users = {}

user_user_mapping = {}
user_hashtag_mapping = {}
user_location_mapping = {}

for f in files:
    print(f)
    path = './insta_data/' + f
    with open(path, 'r') as f:
        data = json.load(f)
        user_id = data['owner']['id']
        user_ids.add(user_id)
        
        users[user_id] = {
            'username': data['owner']['username'],
            'full_name': data['owner']['full_name'],
            'is_verified': data['owner']['is_verified'],
            'is_private': data['owner']['is_private'],
        }
        for edge in data['edge_media_to_tagged_user']['edges']:
            tagged_users.add(edge['node']['user']['id'])
            user_user_mapping[user_id] = edge['node']['user']['id']
        for edge in data['edge_media_to_caption']['edges']:
            # find all hashtags
            for word in edge['node']['text'].split():
                if word[0] == '#':
                    hashtags.add(word)
                    user_hashtag_mapping[user_id] = word
        if data['location']:
            if data['location']['address_json'] == None:
                continue
            user_location_mapping[user_id] = data['location']['id']
            address_data = json.loads(data['location']['address_json'])
            locations[data['location']['id']] = {
                'city_name': address_data['city_name'],
                'country_code': address_data['country_code'],
                'zip_code': address_data['zip_code'],
            }

print(len(users))
print(len(user_ids))
print(len(tagged_users))
print(len(hashtags))
print(len(locations))

# # print the intersection
# for user_id in user_ids.intersection(tagged_users):
#     print(user_id)