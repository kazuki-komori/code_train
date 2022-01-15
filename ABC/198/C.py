import math
from decimal import Decimal

R, X, Y = map(int, input().split())
euc = Decimal(str(X**2 + Y**2))**Decimal('0.5')

if R > euc:
    print(2)
else:
    print(math.ceil(euc/R))
