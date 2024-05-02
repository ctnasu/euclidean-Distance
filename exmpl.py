import math

# Noktalar
points = [(1, 2), (3, 5), (6, 1), (7, 7), (2, 9)]

# Öklid Mesafesi
def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance

# Mesafelerin hesaplanması
distances = []
n = len(points)
for i in range(n):
    for j in range(i + 1, n):
        dist = euclideanDistance(points[i], points[j])
        distances.append(dist)

# Minimum mesafenin bulunması
min_distance = min(distances) if distances else None

# Sonuçların yazdırılması
print("Hesaplanan mesafeler:")
print(distances)
print("Minimum mesafe:")
print(min_distance)
