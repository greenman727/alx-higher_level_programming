#!/python/usr/bin/python3
"""Defines a class that inherits from list"""


class MyList(list):
    """Defines sorted printing"""

    def print_sorted(self):
        """prints the list sorted inascending order"""
        print(sorted(self))
