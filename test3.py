arrays = input("กรอกข้อมูลArray รูปแบบ aaa bbb ccc:  ")#เว้นวรรคเพื่อขึ้นคำใหม่
new_arrays = arrays.split(' ')

x = input('กรอกตัวที่ต้องการค้นหา : ')
found = False

for index,words in enumerate(new_arrays): 
    found_index = None
    for num,word in enumerate(words): 
        if word.lower() == x.lower():
             if found_index is None: 
                found_index = num
                found = True
                print(words,'index ที่ ',found_index)
    if not found:
        print("No results found")
        break
        