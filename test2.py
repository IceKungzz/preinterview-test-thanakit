
n = int(input('กรอก n : '))
i = int(input('กรอก i : '))
j = int(input('กรอก j : '))


for a in range (1,n+1):
    if a % i == 0 and a % j != 0:
        print(a,' ping')
    elif a % i != 0 and a % j == 0:
        print(a,' pong')
    elif a % i ==0 and a % j == 0:
        print(a, 'ping pong')