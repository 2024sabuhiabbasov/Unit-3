# Quiz 048

Statement

## My codes
### Python
```.py
# Program for Quiz 048

from secure_password import check_password
import sqlite3

end_code = "\033[00m"
red = "\33[0;31m"
green = "\33[0;32m"

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
        print(f"{green}Tx(id={id}) Signature matches{end_code}")
    else:
        print(f"{red}Tx(id={id}) Error signature{end_code}")
```
### Proof
![image](https://user-images.githubusercontent.com/111758436/220821637-2d681f6f-b681-43f9-b352-c576b07b2903.png)
