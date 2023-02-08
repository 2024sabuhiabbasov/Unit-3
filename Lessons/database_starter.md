```.py
CREATE TABLE if not exists Driver(
    id INTEGER PRIMARY KEY,
    name text,
    email text,
    age int
);

INSERT INTO Driver (name, email, age) values ("bob", "bob@bob.com", 29);
INSERT INTO Driver (name, email, age) values ("bob", "bob@bob.com", 29);
INSERT INTO Driver (name, email, age) values ("bob", "bob@bob.com", 29);

SELECT name, id from Driver;
SELECT * from Driver;
SELECT count(*) from Driver;

DELETE from Driver where id = 5

UPDATE Driver SET name = "bob2" where id = 2;

select SUM(age) from Driver;
select avg(age) from Driver;
```
