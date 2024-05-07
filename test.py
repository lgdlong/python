import math



def length_between_points(x1, y1, x2, y2):
  result = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
  return result

print("Toa do cua A(x1, y1)")
x1 = int(input("Nhap x1: "))
y1 = int(input("Nhap y1: "))

print("Toa do cua B(x2, y2)")
x2 = int(input("Nhap x2: "))
y2 = int(input("Nhap y2: "))

print("Toa do cua C(x3, y3)")
x3 = int(input("Nhap x3: "))
y3 = int(input("Nhap y3: "))

print("Toa do cua D(x4, y4)")
x4 = int(input("Nhap x4: "))
y4 = int(input("Nhap y4: "))


# Do dai cac canh
length_of_AB = length_between_points(x1, y1, x2, y2)
length_of_BC = length_between_points(x3, y3, x2, y2)
length_of_CD = length_between_points(x4, y4, x3, y3)
length_of_AD = length_between_points(x4, y4, x1, y1)