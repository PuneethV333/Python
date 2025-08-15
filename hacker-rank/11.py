def second_lowest(students):
    # Extract all scores
    scores = sorted(set([score for _, score in students]))
    # Get the second lowest score
    second_lowest_score = scores[1]
    return second_lowest_score

# Read input
python_students = []
for _ in range(int(input())):
    name = input().strip()
    score = float(input())
    python_students.append([name, score])

# Find second lowest score
sec_score = second_lowest(python_students)

names = [name for name, score in python_students if score == sec_score]


for name in sorted(names):
    print(name)
