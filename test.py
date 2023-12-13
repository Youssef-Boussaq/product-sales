from classes import Produit, Commandes

p = Produit("f/764563", "AUDI RS7", 200000, 250000)
p1 = Produit("f/54894534", "AUDI RS6", 1500000, 200000)

print(p)
print(p1)

print(p == p1)

c = Commandes("2023/12/13", 1, p)
c1 = Commandes("2023/12/13", 1, p1)

print(c)
print(c1)
