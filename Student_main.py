import sqlite3
import csv
conn=sqlite3.connect("student1.db")
query_create_table="""create table IF NOT EXISTS student1( id integer primary key, name text,age integer, grade text);"""
conn.execute(query_create_table)

# insert some values into database
insert_table="""insert or ignore into student1(id,name,age,grade)values('1','Asma','20','first');"""
conn.execute(insert_table)

insert_table="""insert or ignore into student1 values(?,?,?,?);"""
multiple_entries=[
('7','Shaik','30','distinction'),
('2','Manha','21','second'),
('3','Ayman','22','third'),
('4','Danish','23','first'),
('5','Zoya','24','second'),
('6','Jaffer','26','third')
]
conn.executemany(insert_table, multiple_entries)
conn.commit()


query_selectall="""select * from student1;"""
data=conn.execute(query_selectall)
data
for row in data:
    print(row)


#conn.executemany("INSERT OR IGNORE INTO student VALUES (?, ?, ?, ?);", multiple_entries) - we can use this to overcome integrity errors..

def stud_fun(query,data=None,db='student1.db'): #The SQL query to run,--data is type, list or single data,--db is our db
    conn=sqlite3.connect(db) #connects to the SQLite database file.
    cursor=conn.cursor() # Creates a cursor object to execute SQL commands.
    try:
        if data:
            cursor.executemany(query,data) if isinstance(data,list) else cursor.execute(query,data) # isinstance checks the type of data.if single row it runs execute or if data is many rows, it goes executemany()
        else:
            cursor.execute(query)
            
# Tries to run the SQL query passed into the function.
        if query.strip().lower().startswith("select"):
            result=cursor.fetchall() #This line fetches all result rows
            conn.close()
            return result #sends the list of rows back to the caller.
        else:
            conn.commit()#If it's not a SELECT (like INSERT, DELETE, UPDATE):Commits the changes to the DB (e.g., save new records).
            conn.close()
            return "query run successfully"
    except sqlite3.Error as e:
        conn.close()
        return f"An error occurred: {e}"

result = stud_fun("SELECT * FROM student1;")
for row in result:
    print(row)


with open('student_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['ID', 'Name', 'Age', 'Grade'])  # Column names
    writer.writerows(result)

print("Data exported to student_data.csv successfully ✅")