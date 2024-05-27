import math

class City:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def distance(city1, city2):
    dx = city1.x - city2.x
    dy = city1.y - city2.y
    return math.sqrt(dx * dx + dy * dy)

def total_distance(cities, path):
    total = 0.0
    for i in range(len(path) - 1):
        total += distance(cities[path[i]], cities[path[i + 1]])
    total += distance(cities[path[-1]], cities[path[0]])  # Return to starting point
    return total

def read_data_from_file(filename):
    cities = []
    with open(filename, 'r') as file:
        next(file)  # Skip the first line (header)
        for line in file:
            x, y = map(float, line.split())
            cities.append(City(x, y))
    return cities


def solve_tsp_nearest_neighbor(cities):
    n = len(cities)
    visited = [False] * n
    path = []

    # Başlangıç şehrini rastgele seçebilirsiniz, burada 0. şehri seçiyorum.
    current_city = 5
    visited[current_city] = True
    path.append(current_city)

    # Her adımda en yakın şehri ziyaret ederek yol oluştur.
    for i in range(n - 1):
        min_dist = float('inf')
        nearest_city = -1

        for j in range(n):
            if not visited[j] and j != current_city:
                dist = distance(cities[current_city], cities[j])
                if dist < min_dist:
                    min_dist = dist
                    nearest_city = j

        current_city = nearest_city
        visited[current_city] = True
        path.append(current_city)

    return path

if __name__ == "__main__":
    filename = "tsp_51_1"  # Verilerin olduğu dosya adı
    cities = read_data_from_file(filename)

    # Verileri başarılı bir şekilde okuduğumuzu kontrol etmek için ekrana yazdıralım
    # for city in cities:
    #     print("Şehir {}: ({}, {})".format(city.id, city.x, city.y))

    best_path = solve_tsp_nearest_neighbor(cities)

    print("Optimal maliyet degeri:", total_distance(cities, best_path))
    print("Optimal maliyeti sağlayan path:", best_path)
