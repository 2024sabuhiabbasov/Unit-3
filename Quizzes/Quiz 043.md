# Quiz 043

image

## My codes

### Console
```
CREATE TABLE if not exists Movies(
    id INTEGER PRIMARY KEY,
    name text,
    producer text,
    director text,
    category text,
    budget int,
    year int
);

INSERT into Movies (id, name, producer, director, category, budget, year) values (1, 'Call Me by Your Name', 'Peter Spears', 'Luca Guadagnino', 'coming-of-age romantic drama', 3500000, 2017);
INSERT into Movies (id, name, producer, director, category, year) values (2, 'Single All The Way', 'Joel S. Rice', 'Michael Mayer', 'romantic comedy', 2021);

select name, category, year from Movies
```
### Proof
![image](https://user-images.githubusercontent.com/111758436/217418654-f9a30800-e9a9-41da-b7bb-5fda50d3497a.png)
