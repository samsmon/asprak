# B4. Jenis Segitiga
a = int(input())
b = int(input())
c = int(input())
if a <= 0 or b <= 0 or c <= 0:
    print("Sisi harus positif")
elif a + b <= c or a + c <= b or b + c <= a:
    print("Bukan segitiga")
elif a == b and b == c:
    print("Segitiga sama sisi")
elif a == b or b == c or a == c:
    print("Segitiga sama kaki")
else:
    print("Segitiga sembarang")
