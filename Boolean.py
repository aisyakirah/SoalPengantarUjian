# Definisikan variabel p, q, dan r
p = 11
q = 5
r = 4

# a. ((p - r) == (r + q))
hasil_a = ((p - r) == (r + q))
print("a. ((p - r) == (r + q))", hasil_a)

# b. (((p%3)+q)!=(r%2))
hasil_b = (((p % 3) + q) != (r % 2))
print("b. (((p%3)+q)!=(r%2)) =", hasil_b)

# c. ((q-3)==(p%2+q))
hasil_c = ((q - 3) == (p % 2 + q))
print("c. ((q-3)==(p%2+q)) =", hasil_c)

# d. ((r+q)!=((p*2)%2))
hasil_d = ((r + q) != ((p * 2) % 2))
print("d. ((r+q)!=((p*2)%2)) =", hasil_d)

# e. ((((q%3)+p)>(r%2)))
hasil_e = (((q % 3) + p) > (r % 2))
print("e. ((((q%3)+p)>(r%2))) =", hasil_e)

# f. (((r+p))<=(q*5))
hasil_f = ((r + p) <= (q * 5))
print("f. (((r+p))<=(q*5)) =", hasil_f)