
students = ["Alice", "Bob", "Carol", "David", "Eve"]
scores = [85, 92, 78, 88, 95]
    
for idx, name in enumerate(students, start=1):
    print(f"{idx}. {name}")


for idx, name in enumerate(students):
    print(f"{name} - Score: {scores[idx]}")


high_scorers = [idx for idx, score in enumerate(scores) if score > 90]
print("Positions of high scorers:", high_scorers)


position_map = {idx: name for idx, name in enumerate(students)}
print(position_map)
