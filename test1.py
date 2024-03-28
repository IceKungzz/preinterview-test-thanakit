
n = int(input('กรอก: '))


for i in range (1,n+1):
    if i % 3 == 0 and i % 5 != 0:
        print(i,' ping')
    elif i % 3 != 0 and i % 5 == 0:
        print(i,' pong')
    elif i % 3 ==0 and i % 5 == 0:
        print(i, 'ping pong')