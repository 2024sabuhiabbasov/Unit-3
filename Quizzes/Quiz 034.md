# Quiz 034

![image](https://user-images.githubusercontent.com/111758436/212214697-cb31536a-9788-4135-85d4-db6f7360bf07.png)

## My code
```.py
# Program for Quiz 034

class quiz34:
    def __init__(self, num: int):
        self.num = num

    def solve(self) -> str:
        number = self.num
        if number > 100:
            raise ValueError("Input number must be less than or equal to 100")
        answer = ''
        num = [1, 4, 5, 9, 10, 40, 50, 90,
               100]
        rom = ["I", "IV", "V", "IX", "X", "XL",
               "L", "XC", "C"]
        cnt = 8

        while number:
            div = number // num[cnt]
            number %= num[cnt]

            while div:
                answer += rom[cnt]
                div -= 1
            cnt -= 1
        return answer


case1 = quiz34(num=59)
solution = case1.solve()
print(solution)
```
### Proof
![image](https://user-images.githubusercontent.com/111758436/214751104-65c8b514-eec4-4934-a7c5-be162b33ef79.png)
