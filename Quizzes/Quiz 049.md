# Quiz 049

statement

## My codes
### Python
```.py
# Program for Quiz 049

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

total = 0

for row in result:
    (id, sender_id, receiver_id, amount, hash) = row
    string_hash = f"id {id},sender_id {sender_id},receiver_id {receiver_id},amount {amount}"
    checker = check_password(hashed_password=hash, user_password=string_hash)

    if checker:
        total += amount
    else:
        pass

print(total)
```
### Proof
![image](https://user-images.githubusercontent.com/111758436/221083415-a3bb6288-5411-4b45-8b1f-d692b451a12f.png)
