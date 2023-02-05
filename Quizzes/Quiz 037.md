# Quiz 037

![image](https://user-images.githubusercontent.com/111758436/214814374-5cce09d3-ecdf-4b47-b299-4636303ce521.png)

## My code
```.py
# Program for Quiz 037

class CompoundInterest:
    def __init__(self, principal: int, rate: float, year: int):
        self.principal = principal
        self.rate = rate
        self.year = year


class AccountingProgram:
    def __init__(self):
        self.compound = CompoundInterest(0, 0, 0)

    def set_principal(self, principal):
        if principal <= 0:
            raise ValueError("Principal should be greater than zero")
        self.compound.principal = principal
        return f"Principal set to {self.compound.principal}"

    def set_rate(self, rate):
        if rate <= 0:
            raise ValueError("Interest rate should be greater than zero")
        self.compound.rate = rate
        return f"Rate set to {self.compound.rate}"

    def set_years(self, year):
        if year <= 0:
            raise ValueError("Years should be greater than zero")
        self.compound.year = year
        return f"Year set to {self.compound.year}"

    def calculate_interest(self):
        temp = self.compound.principal * (1 + self.compound.rate) ** self.compound.year
        format_float = "{:.2f}".format(temp)
        return float(format_float)
```
### Proof
![image](https://user-images.githubusercontent.com/111758436/216808838-04dffd99-b470-4936-8d91-6c15ae2cb4a2.png)
