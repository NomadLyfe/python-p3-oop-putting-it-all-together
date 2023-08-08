#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self._size = size
    def get_size(self):
        return self._size
    def set_size(self, size):
        if size in (int, float):
            self._size = size
        else:
            print("size must be an integer")
    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = 'New'
    size = property(get_size, set_size)