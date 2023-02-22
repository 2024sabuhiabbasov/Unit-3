# Quiz 046

![image](https://user-images.githubusercontent.com/111758436/220594562-fcf0bbd6-d4a1-4db0-a424-7bedb7390818.png)

## My codes

### Python
```.py
# Program for Quiz 046

import sqlite3

haiku = """Code flows like a stream
Algorithms guide its way
In silence, it solves
"""

#Create Database with table Words

class database_handler():
    def __init__(self, namedb: str):
        self.connection = sqlite3.connect(namedb)
        self.cursor = self.connection.cursor()

    def create_table(self):
        query = f"""CREATE TABLE if not exists WORDS(
            id INTEGER PRIMARY KEY not NULL,
            word text not NULL,
            length int not NULL
            )"""
        self.run_query(query)

    def run_query(self, query: str):
        self.cursor.execute(query)
        self.connection.commit()

    def close(self):
        self.connection.close()

    def insert(self, word, length):
        #id_number = random.choice(rand_list)
        #rand_list.remove(id_number)
        query = f"INSERT into WORDS VALUES (null, '{word}', '{length}')"
        self.run_query(query)

db = database_handler(namedb="Quiz_046_database.db")
db.create_table()

for word in haiku.split():
    db.insert(word, len(word))

query = f"SELECT AVG(length) from WORDS"
db.run_query(query)
print(db.cursor.fetchone())

db.close()
```
### Proof
![image](https://user-images.githubusercontent.com/111758436/220628802-b00cc2e4-30ec-4763-a1a7-78ce1bc0b37d.png)
