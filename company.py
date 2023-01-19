# -*- coding: utf-8 -*-

from employee import Employee
from manager import Manager
from director import Director
from picklestorage import PickleStorage


class Company:
    def __init__(self):
        self.items = dict()
        self.storage = PickleStorage(self)
        self.maxID = 0
    
    def add(self):
        self.maxID += 1
        post = [
            ["Сотрудник", 0],
            ["Менеджер", 1],  
            ["Директор", 2]     
        ]
        for i, Item in enumerate(post, 0):
            print(f"{i}.{Item[0]}")
        item = int(input('Введите должность: '))
        if item < 0 or item > len(post):
            print('Ошибка')
            return item
        elif item == 0:
            item = Employee(id=self.maxID)
        elif item == 1:
            item = Manager(id=self.maxID)
        elif item == 2:
            item = Director(id=self.maxID)
        item.read()
        self.items[item.id] = item
        
    def write(self):
        for id, item in self.items.items():
            item.write()
            
    def store(self):
        self.storage.store()

    def load(self):
        self.storage.load()

    def delete(self):
        id = int(input("id: "))
        del self.items[id]

