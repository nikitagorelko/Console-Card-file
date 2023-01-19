# -*- coding: utf-8 -*-

from company import Company

def main():
    company = Company()
    
    menu = [
        ["Добавить", company.add],
        ["Удалить", company.delete],
        ["Показать", company.write],
        ["Сохранить", company.store],
        ["Загрузить", company.load],
    ]

    while True:
        for i,menuItem in enumerate(menu, 1):
            print(f"{i}. {menuItem[0]}")
        m = int(input())
        menu[m-1][1]()
        
        
        
if __name__ == '__main__':
    main()
