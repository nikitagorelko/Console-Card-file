# -*- coding: utf-8 -*-

from dataclasses import dataclass
from employee import Employee

@dataclass
class Director(Employee):
    number_of_subordinates: str = ""
    
    def read(self):
        Employee.read(self)
        self.number_of_subordinates = self.io.input('number of subordinates')
        
    def write(self):
        Employee.write(self)
        self.io.output('number of subordinates', self.number_of_subordinates)