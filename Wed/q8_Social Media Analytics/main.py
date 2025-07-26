posts = [
    {"id": 1, "user": "alice", "content": "Love Python programming!", "likes": 15, "tags": ["python", "coding"]},
    {"id": 2, "user": "bob", "content": "Great weather today", "likes": 8, "tags": ["weather", "life"]},
    {"id": 3, "user": "alice", "content": "Data structures are fun", "likes": 22, "tags": ["python", "learning"]}
]

users = {
    "alice": {"followers": 150, "following": 75},
    "bob": {"followers": 89, "following": 120}
}


# all_tags=list()

# for post in posts:
#     all_tags.extend(post["tags"])

# # print(all_tags)

# from collections import Counter

# tag_counter = Counter(all_tags)
# print(tag_counter)

# for tag, count in tag_counter.most_common():
#     print(count)


from collections import defaultdict
# Step 1: Create defaultdict to store total likes per user
user_likes = defaultdict(int)

for post in posts:
    user = post["user"]
    likes = post["likes"]
    user_likes[user] += likes

print(user_likes)


for user, total in user_likes.items():
    print(f"{user}: {total}")



    # Sort posts by likes in descending order
sorted_posts = sorted(posts, key=lambda post: post["likes"], reverse=True)

# Print sorted posts
print("Posts sorted by likes (high to low):")
for post in sorted_posts:
    print(f"ID: {post['id']}, User: {post['user']}, Likes: {post['likes']}")
