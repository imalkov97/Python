#If you leave the money in the bank
S=int(10000)
ib=int(2)
tb=int(5)

valb=S*(1+(ib/100))**tb
print("If you leave your £10,000 in the bank, you will earn:",valb)

#If you invest in Product A
iA1=int(1)
tA1=int(3)
iA2=int(5)
tA2=int(2)

valA=(S*(1+(iA1/100))**tA1)+(S*(1+(iA2/100))**tA2)
print("If you invest your £10,000 into Product A, you will earn:",valA)

#If you invest in Product B
iB1=int(1)
tB1=int(4)
iB2=int(10)
tB2=int(1)

valB=(S*(1+(iB1/100))**tB1)+(S*(1+(iB2/100))**tB2)
print("If you invest your £10,000 into Product B, you will earn:",valB)
print()
print("Product B would be the wise choice here...")

