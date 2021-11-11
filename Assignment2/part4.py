P = 800000
R = 6
L = 103
tentativeM = 10000
remainder = 0

for x in range(L):
    P = P * R / 100 / 12 - tentativeM

if P > 0:
    remainder = P

totalPayment = (L - 1) * tentativeM + remainder

M = totalPayment / L

print('%1.0f' % M)  # or can use int(M)
