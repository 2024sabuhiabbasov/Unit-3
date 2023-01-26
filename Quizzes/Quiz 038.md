# Quiz 038

![image](https://user-images.githubusercontent.com/111758436/214815990-5509d6a2-4cf5-49c2-9244-b945f85698b1.png)

## My code
```.py
# Program for Quiz 038

import random
import matplotlib.pyplot as plt

class coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"[coordinate]x={self.x} y={self.y}"


class city:
    def __init__(self, name: str, location: coordinate):
        self.name = name
        self.location = location

    def get_name(self):
        return self.name

    def __repr__(self) -> str:
        return f"[City class] {self.name} located at {self.location}"

    def distance(self, cityB):
        xa, ya = self.location.x, self.location.y
        xb, yb = cityB.location.x, cityB.location.y
        d = ((xa - xb) ** 2 + (ya - yb) ** 2) ** (1 / 2)
        return round(d, 2)


class country:
    def __init__(self, name: str):
        self.cities = []
        self.name = name

    def add_city(self, new_city: city):
        if isinstance(new_city, city):
            self.cities.append(new_city)
        else:
            raise ValueError("City must be a city object")


Azerbaijan = country("Azerbaijan")

cities = ["Baku", "Ganja", "Nakhchivan", "Kalbajar", "Guba", "Gusar", "Gabala", "Shaki", "Shusha", "Aghdam"]

for ct in cities:
    coord = coordinate(random.randint(1, 100), random.randint(1, 100))
    cityy = city(name=ct, location=coord)
    Azerbaijan.add_city(cityy)

x = []
y = []

for i in range(0, 10):
    x.append(Azerbaijan.cities[i].location.x)
    y.append(Azerbaijan.cities[i].location.y)
    print(Azerbaijan.cities[i].name)

ax = plt.axes()
ax.set_facecolor("lightsteelblue") # Choosing the background color
plt.grid(True, color='dimgray')
plt.scatter(x, y, color='lightblue')
for i in range(0, 10):
    plt.text(x[i], y[i], Azerbaijan.cities[i].name, color='blue')
plt.xlabel("x-coordinate")
plt.ylabel("y-coordinate")
total_distance = 0
for i in range(0, len(Azerbaijan.cities)-1):
    start_city = Azerbaijan.cities[i]
    end_city = Azerbaijan.cities[i+1]
    X = [start_city.location.x, end_city.location.x]
    Y = [start_city.location.y, end_city.location.y]
    plt.plot(x, y, color='green')
    total_distance += start_city.distance(end_city)
    print(f"Connecting city {start_city.name} to {end_city.name} {start_city.distance(end_city)} km")

print(f"Total distance for this problem is {round(total_distance, 2)} km")
plt.show()
```
### Proof
![image](https://user-images.githubusercontent.com/111758436/214816190-b088b185-303b-4e94-aa9a-ea87677fa0eb.png)
