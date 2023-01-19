# Quiz 035

![image](https://user-images.githubusercontent.com/111758436/213423635-c40e0187-f185-4e60-a4fe-039fcb38f27f.png)

## My code
```.py
# Program for Quiz 035

import random
import pytest

class Account:
    def __init__(self):
        self.balance = 0
        self.holder_name = ""
        self.holder_email = ""
        a = random.randint(100, 1000)
        b = random.randint(10000, 100000)
        c = random.randint(0, 10)
        self.number = [a, b, c]

    def set_holder_name(self, name: str) -> str:
        if not isinstance(name, str):
            raise ValueError("The name must be a string")
        self.holder_name = name
        return f"Holder's name set to {self.holder_name.title()}"

    def get_balance(self)->int:
        return self.balance

    def deposit(self, amount: int)->str:
        self.balance += amount
        return f"New balance: {self.balance} USD"

    def get_account_no(self):
        n, m, p = self.number
        return f"{n}-{m}-{p}"

    def set_holder_email(self, email: str) -> str:
        self.holder_email = email

        return f"Holder's email set to {self.holder_email}"
```
### Proof
![image](https://user-images.githubusercontent.com/111758436/213424478-a062e679-5171-4262-9744-17936cc92139.png)
