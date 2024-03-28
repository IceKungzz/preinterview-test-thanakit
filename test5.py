history = []
numhistory = -1

def prev(numhistory):
    if numhistory <= 0:
        print('No website to previous') 
        numhistory = -1
        return numhistory
    else:
        print('Now you on ',history[numhistory-1])
        numhistory = numhistory-1 
        return numhistory
    


def next(numhistory):
    if numhistory < len(history) - 1:
        numhistory += 1
        print('Now you on ',history[numhistory])
    else:
        print('No website to go')

    return numhistory


while True:
    words = input('commnad: ')
    command = words.split(' ')


    if command[0] == 'input':
        history.append(command[1])
        numhistory = numhistory + 1
    elif command[0] == 'current':
        print('Now you on ',history[numhistory])
    elif command[0] == 'all':
        print(history)
    elif command[0] == 'prev':  
        numhistory = prev(numhistory)
    elif command[0] == 'next':
        numhistory = next(numhistory)
    elif command[0] == 'exit':
        break
    else:
        print('ป้อนคำสั่ง ให้ถูกต้อง ถ้าต้องการออกป้อน exit ')