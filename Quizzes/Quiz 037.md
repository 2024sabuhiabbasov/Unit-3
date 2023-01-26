# Quiz 037

![image](https://user-images.githubusercontent.com/111758436/214814374-5cce09d3-ecdf-4b47-b299-4636303ce521.png)

## My code
```.py
# Program for Quiz 037

class CompoundInterest:
    def __init__(self, principal, rate, no_of_years):
        self.principal = principal
        self.rate = rate
        self.no_of_years = no_of_years

    def calculate(self):
        return self.principal*(1+self.rate)**self.no_of_years

class AccountingProgram():

    def __init__(self):
        self.data = CompoundInterest(principal=0, rate=0, no_of_years=0)

    def set_principal(self, principal):
        self.data.principal = principal

    def set_rate(self, rate):
        self.data.rate = rate

    def set_years(self, years):
        self.data.years = years

    def calculate_interest(self):
        answer = self.data.calculate()
        return answer
```
### Proof
There is an error in test code.
