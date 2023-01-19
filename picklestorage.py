# -*- coding: utf-8 -*-

import pickle

class PickleStorage:
    def __init__(self, employee):
        self.employee = employee
    
    def store(self):
        pickle.dump((self.employee.maxID, self.employee.items), open("data.dat", "wb"))
        
    def load(self):
        (self.employee.maxID, self.employee.items) = pickle.load(open("data.dat", "rb"))
    