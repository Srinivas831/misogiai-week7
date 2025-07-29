
facebook_friends  = {"alice", "bob", "charlie", "diana", "eve", "frank"}
instagram_friends = {"bob", "charlie", "grace", "henry", "alice", "ivan"}
twitter_friends   = {"alice", "diana", "grace", "jack", "bob", "karen"}
linkedin_friends  = {"charlie", "diana", "frank", "grace", "luke", "mary"}

def analyze_friendships():
    all_platforms = facebook_friends & instagram_friends & twitter_friends & linkedin_friends
    print("all platforms", all_platforms)
    
# analyze_friendships()

def only_fb():
    print(facebook_friends - (instagram_friends | twitter_friends | linkedin_friends))
    
# only_fb()

instagram_xor_twitter = instagram_friends ^ twitter_friends
# print("instagram XOR twitter:", instagram_xor_twitter)


# total_unique = len(facebook_friends | instagram_friends | twitter_friends | linkedin_friends)  



platforms = [facebook_friends, instagram_friends, linkedin_friends, twitter_friends]

from collections import defaultdict
# print(dict())
# print(defaultdict)
friend_count = defaultdict(int)
print(friend_count)

for plat in platforms:
    for i in plat:
        friend_count[i]+=1
        
print(friend_count)

exactly_two_platforms = { friend for friend, count in friend_count.items() if count==2}
print(exactly_two_platforms)


for key in friend_count:
    if friend_count[key]==2:
        print(key)
        