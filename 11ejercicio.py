pro = 1
N = int(input("valor de N :"))

for f in range(1, N+1):
    print(f)
    pro += pro * f
print()
print("PRODUCTO DE", N, "ES:", pro)
