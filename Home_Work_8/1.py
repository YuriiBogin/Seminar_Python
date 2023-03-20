def show_data() -> str:
    '''Эта функциия показывает содержимое справочника'''
    with open('Home_Work_8/data.txt','r', encoding='utf-8') as file:
        book = file.read()
    return book


def new_data() -> None:
    '''Добавляет новую инфу в справочник'''
    with open('Home_Work_8/data.txt','a', encoding='utf-8') as file:
        a = input('Введите данные')    
        file.write(f'\n{a}')

def Find_Data():
    with open('Home_Work_8/data.txt','rt', encoding='utf-8') as file:
        temp = input()
        for index, line in enumerate(file):
            if temp in line:
                print (line)          
        
def delete_data():
    
    with open('Home_Work_8/data.txt','rt', encoding='utf-8') as file:
        
        temp = input()
        for index, line in enumerate(file):
            if temp in line:
                p = index
                           
        with open('Home_Work_8/data.txt','r', encoding='utf-8') as file:            
            book = file.readlines()     
            i = 0             
            with open('Home_Work_8/data.txt','w', encoding='utf-8') as file:
                for line in book:
                    if i != p:
                        file.write(line)
                    i+=1
               
                  
while True:
    mode = input('Выберите режим работы справочника(0-выход; 1-показать справочник; 2- добавить запись; 3 - найти запись; 4 - удалитть запись) ')
    if mode=='1':
        
        print(show_data())
        
    elif mode == '2':
        new_data()
        
    elif mode == '3':
        print('Введите данные для поиска')
        Find_Data()
        
    elif mode == '4':
        print('Введите данные для удаления')
        delete_data()

    elif mode == '0':
        break
    else:
        print('No mode')