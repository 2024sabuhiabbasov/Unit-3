# Quiz 048

Statement

## My codes
### Python
```.py
# Program for Quiz 048

from secure_password import check_password
import sqlite3

class database_worker:
    def __init__(self, name):
        self.connection = sqlite3.connect(name)
        self.cursor = self.connection.cursor()

    def search(self, query):
        result = self.cursor.execute(query).fetchall()
        return result

    def run_save(self, query):
        self.cursor.execute(query)
        self.connection.commit()

    def close(self):
        self.connection.close()

db = database_worker("bitcoin_exchange.db")
query = "SELECT * from ledger"
result = db.search(query)
db.close()

for row in result:
    (id, sender_id, receiver_id, amount, hash) = row
    string_hash = f"id {id},sender_id {sender_id},receiver_id {receiver_id},amount {amount}"
    checker = check_password(hashed_password=hash, user_password=string_hash)

    if checker:
        print(f"ID = {sender_id}: Signature matches")
    else:
        print(f"ID = {sender_id}: Signature doesn't match")
```
### Proof
![image](https://user-images.githubusercontent.com/111758436/220819114-40139950-bb7e-4e09-bab5-546b37e631c7.png)
