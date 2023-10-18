
M = int(input("Entrez le premier nombre : "))
N = int(input("Entrez le deuxième nombre : "))

s_div_M = 0
for i in range(2, M):
    if M % i == 0:
        s_div_M += i

s_div_N = 0
for i in range(2, N):
    if N % i == 0:
        s_div_N += i

if s_div_M == N and s_div_N == M:
    print(M, "et",N,"sont des nombres amis")
else:
    print(M, "et",N,"ne sontpas  des nombres amis  ")