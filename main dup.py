all_creators_data =[]
creators = 3
posts_per_creator = 4
for creator in range(creators):
    print("Analyzing creator",)
    creator_patterns = []
    for post in range(posts_per_creator):
        post_pattern = input("Enter pattern for this post: ")
        creator_patterns.append(post_pattern)
    all_creators_data.append(creator_patterns)
print("____ Creator analysis done____")
print("Full structured data:")
print(all_creators_data)
all_patterns = []
for mango in all_creators_data:
    for yoo in mango:
        all_patterns.append(yoo)
print("All extracted patterns:")
print(all_patterns)