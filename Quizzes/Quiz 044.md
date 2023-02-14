# Quiz 044

![image](https://user-images.githubusercontent.com/111758436/218715325-0034e7a9-18fb-4d05-8b16-796b38de3a27.png)

## My codes

### Console
```
-- Question 1:
select count(name) from sqlite_master;
-- Question 2:
select count(personid) from INHABITANT where gender='Male' and state='Friendly';
-- Question 3:
select villageid, avg(gold) from INHABITANT group by villageid;
-- Question 4:
select count(item) from ITEM where item LIKE 'A%';
-- Question 5:
select count(DISTINCT job) from INHABITANT;
-- Question 6:
select * from INHABITANT where job='Herbalist';
select * from ITEM where owner=4 or owner=18

```
### Proof
![image](https://user-images.githubusercontent.com/111758436/218716056-b303fee3-a8fe-497b-8d06-13a8c200f9d0.png)
<p align='center'>
<i>Question 1 and 2</i>
</p>

![image](https://user-images.githubusercontent.com/111758436/218716633-0fe87ea0-2c13-414d-9036-991b6607a4f8.png)
<p align='center'>
<i>Question 3 and 4</i>
</p>

![image](https://user-images.githubusercontent.com/111758436/218718894-e1ebc8df-2755-4445-9440-ff3a3b124775.png)
<p align='center'>
<i>Question 5 and 6</i>
</p>
