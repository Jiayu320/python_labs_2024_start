import json

# 打开并读取 student.json 文件
with open('student.json', 'r') as file:
    data = json.load(file)

# 遍历并打印每个学生的信息
for student in data['students']:
    print(f"ID: {student['id']}, Name: {student['name']}, Age: {student['age']}, City: {student['city']}")

# print the second student's name
print(data['students'][1]['name'])
print(data['students'][1]['age'])