# Quiz 033

![image](https://user-images.githubusercontent.com/111758436/216805695-5d2ea056-46a8-44ed-ab7f-3ef02d1c0a24.png)

## My solutions
### Code for program
```.py
# Program for quiz 033

def mystery(list1, list2:list):
    output = []
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                output.append(list1[i])
    return output
```
**Testing the code**

**Test**

![image](https://user-images.githubusercontent.com/111758436/216805889-def1d6eb-a931-47da-9cbd-2e7f3860ae95.png)
