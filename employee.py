# -*- coding: utf-8 -*-

from dataclasses import dataclass
from consoleIO import ConsoleIO

@dataclass
class Employee:
    id: int = 0
    name: str = ""
    surname: str = ""
    age: int = 0

    def __post_init__(self):
        self.io = ConsoleIO()
    
    def read(self):
        self.name = self.io.input('name')
        self.surname = self.io.input('surname')
        self.age = self.io.input('age')
        
    def write(self):
        self.io.output('ID', self.id)
        self.io.output('name', self.name)
        self.io.output('surname', self.surname)
        self.io.output('age', self.age)
    
