# -*- coding: utf-8 -*-

from dataclasses import dataclass
from employee import Employee

@dataclass
class Manager(Employee):
    current_project: str = ""
    department: str = ""
    def read(self):
        Employee.read(self)
        self.current_project = self.io.input('current project')
        self.department = self.io.input('department')
    def write(self):
        Employee.write(self)
        self.io.output('current project', self.current_project)
        self.io.output('department', self.department)