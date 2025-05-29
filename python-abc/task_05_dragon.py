#!/usr/bin/env python3
"""
This module demonstrates mixins in Python by
creating SwimMixin, FlyMixin, and a Dragon class
that inherits from both.
"""


class SwimMixin:
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    def roar(self):
        print("The dragon roars!")
