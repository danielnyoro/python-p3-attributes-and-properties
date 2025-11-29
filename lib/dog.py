#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    approved_breeds = ["Mastiff", "Chihuahua", "Corgi", "Shar Pei", "Beagle", "French Bulldog", "Pug", "Pointer"]
    
    def __init__(self, name=None, breed=None):
        self.name = name
        self.breed = breed

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value is None:
            self._name = ""
        elif isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value
        else:
            print("Name must be string between 1 and 25 characters.")
            self._name = ""

    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, value):
        if value is None:
            self._breed = "Mutt"
        elif value in Dog.approved_breeds:
            self._breed = value
        else:
            print("Breed must be in list of approved breeds.")
            self._breed = "Mutt"