import sqlite3, json

connection = sqlite3.connect("./04-Databases/demo.db")

# Using primary memory
# connection = sqlite3.connect(":memory:")

cursor = connection.cursor()

command = "SELECT count(*) FROM sqlite_master WHERE type = 'table' AND name = 'Students'"
cursor.execute(command)
num_tables = cursor.fetchone()[0]
print(f"Number of tables of Students: {num_tables}")

if num_tables == 0:
    command = "CREATE TABLE Students (StudentID, Name, Surname, Course, Score)"
    cursor.execute(command)

command = "SELECT * FROM Students"
cursor.execute(command)

row = cursor.fetchone()
while row:
    print(row)
    row = cursor.fetchone()

command = "INSERT INTO Students (StudentID, Name) VALUES ('000', 'Borja')"
cursor.execute(command)
connection.commit()

command = "INSERT INTO Students VALUES ('001', 'Julián', 'Sánchez', '2A', Null)"
cursor.execute(command)
connection.commit()

command = "SELECT * FROM Students"
cursor.execute(command)
for row in cursor.fetchall():
    print(row)

# It went crazy for no reason when printing Students table with a while loop before
# I forgot to commit on database, however, the error was quite strange
students = [
    ('002', 'Ana', 'Trujillo', '2C', None),
    ('003', 'Adrian', 'Sánz', '2A', json.dumps([7.5, 6, 9, 5, 6.9])),
    ('004', 'María', 'Sánchez', '2B', None)
]

command = "INSERT INTO Students VALUES (?, ?, ?, ?, ?)"
cursor.executemany(command, students)
connection.commit()
print(f"Number of inserted registries: {cursor.rowcount}")

command = "SELECT * FROM Students"
cursor.execute(command)
for row in cursor.fetchall():
    print(row)

command = "UPDATE Students SET Name = 'Adrián' WHERE StudentID = '003'"
cursor.execute(command)
connection.commit()
print(f"Number of updated registries: {cursor.rowcount}")

command = "SELECT * FROM Students"
cursor.execute(command)
for row in cursor.fetchall():
    print(row)

command = "DELETE FROM Students WHERE StudentID = '004'"
cursor.execute(command)
connection.commit()
print(f"Number of deleted registries: {cursor.rowcount}")

command = "SELECT * FROM Students"
cursor.execute(command)
for row in cursor.fetchall():
    print(row)

connection.close()
