# Quiz 034

![image](https://user-images.githubusercontent.com/111758436/212214697-cb31536a-9788-4135-85d4-db6f7360bf07.png)

## My code
```.py
# Program for Quiz 034

def to_roman(num: int) -> str:
    answer = ''
    while num - 100 >= 0:
        answer += 'C'
        num -= 100
    if num > 100:
        raise ValueError("Input number must be less than or equal to 100")
    while num - 50 >= 0:
        answer += 'L'
        num -= 50
    while num - 10 >= 0:
        answer += 'X'
        num -= 10
    while num - 5 >= 0:
        answer += 'V'
        num -= 5
    while num - 1 >= 0:
        answer += 'I'
        num -= 1
    if "IIII" in answer:
         answer = answer.replace("IIII", "IV")
    if "VIV" in answer:
        answer = answer.replace("VIV", "IX")
    if "XXXX" in answer:
        answer = answer.replace("XXXX", "XL")
    if "LXL" in answer:
        answer = answer.replace("LXL", "XC")
    return answer
print(to_roman(100))
```
### Proof
![image](https://user-images.githubusercontent.com/111758436/212216787-d43bad09-1f59-4987-97a8-016ef66295cb.png)
