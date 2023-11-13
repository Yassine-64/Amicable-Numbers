
M = int(input("Enter the first number: "))
N = int(input("Enter the second number: "))

s_div_M = 0
for i in range(2, M):
    if M % i == 0:
        s_div_M += i

s_div_N = 0
for i in range(2, N):
    if N % i == 0:
        s_div_N += i

if s_div_M == N and s_div_N == M:
    print(M, "and", N, "are amicable numbers.")
else:
    print(M, "and", N, "are not amicable numbers.")
