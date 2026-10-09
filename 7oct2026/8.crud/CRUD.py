import sqlite3

conn = sqlite3.connect('students.db')
cursor = conn.cursor()

#Table Creation

cursor.execute('''CREATE TABLE IF NOT EXISTS students(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER,
                grade TEXT
                )'''
               )
conn.commit()
print("Table Created")

def add_std(name,age,grade):
    cursor.execute(
        '''INSERT INTO students (name,age,grade)
            VALUES(?,?,?)''',(name,age,grade))
conn.commit()
print("added succesfully")
add_std('mohit',20,'A')
add_std('mohit',20,'A')


def update_std(student_id,new_name,new_age,new_grade):
    cursor.execute(
        '''UPDATE students
        SET name=? , age =?,grade=?
        WHERE id =?''',(new_name,new_age,new_grade,student_id)
    )

update_std(1,'Mohit singh',21,'B+')



def fetch_std():
    cursor.execute('SELECT * FROM students ')
    rows =cursor.fetchall()
    for row in rows:
        print(row)
fetch_std()



def delete_std(student_id):
    cursor.execute('DELETE FROM students WHERE id =?',(student_id,)
    )
    conn.commit()
    print(f"student with ID {student_id} deleted succefully")
delete_std(2)

def fetch_std():
    cursor.execute('SELECT * FROM students ')
    rows =cursor.fetchall()
    for row in rows:
        print(row)
fetch_std()
