m_course = [{
    "name": "Patricia",
    "id": "001",
    "score": 8.1
},
    {
        "name": "Nicole",
        "id": "002",
        "score": 6.6
    },
    {
        "name": "Javier",
        "id": "003",
        "score": 10
    },
    {
        "name": "Verónica",
        "id": "004",
        "score": 8.6
    },
    {
        "name": "Guillermo",
        "id": "005",
        "score": 4
    },
    {
        "name": "Pablo",
        "id": "006",
        "score": 9
    },
    {
        "name": "Patricia",
        "id": "007",
        "score": 2.3
    }
]

a_course = [
    {
        "name": "Germán",
        "id": "001",
        "score": 6.8
    },
    {
        "name": "Sara",
        "id": "002",
        "score": 8.8
    },
    {
        "name": "Jorge",
        "id": "003",
        "score": 3.3
    },
    {
        "name": "María",
        "id": "004",
        "score": 9.8
    },
    {
        "name": "Alicia",
        "id": "005",
        "score": 5.6
    },
    {
        "name": "Hernesto",
        "id": "006",
        "score": 6.8
    }]

all_courses = [*a_course, *m_course]

# Practice No. 1
for students in a_course:
    if students["name"] == "Hernesto":
        print(students["score"])

# Practice No. 2
p_sum = 0
for students in all_courses:
    if students["name"].startswith("P"):
        p_sum += 1

print(f'The number of student with the name start with "P" is: {p_sum}')

# Practice No. 3
student = None
max_score = []
for students in all_courses:
    max_score.append((students["score"]))
    if students["score"] == max(max_score):
        student = students["name"]

print(f'The Student {student} as the High Score: {max(max_score)}')

# Practice No. 4
student = None
min_score = []
for students in all_courses:
    min_score.append((students["score"]))
    if students["score"] == min(min_score):
        student = students["name"]

print(f'The Student {student} as the Lower Score: {min(max_score)}')

# Practice No. 5
new_score = None
for students in all_courses:
    if students["name"] == "Alicia":
        new_score = students["score"] = 6.7

print(f'The New Score of Alicia is: {new_score}')

# Practice No. 6
for students in m_course:
    students["id"] = f'M{students["id"]}'

print(m_course)
# Practice No. 7
for students in a_course:
    students["id"] = f'A{students["id"]}'

print(a_course)

# Practice No. 8
approved = []
failed = []

for students in all_courses:
    if students["score"] < 5.0:
        failed.append(students)
    else:
        approved.append(students)

print(f'The list of Approved Student is: {approved}')
print(f'The list of Failed Student is: {failed}')
