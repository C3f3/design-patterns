"""
Clase singleton para crear una instancia de una clase
"""

class Singleton():
    _instance = None
    _value = 0

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instalce = cls()
        return cls._instalce
    
    def get_value(self):
        return self._value

    def set_value(self, v):
        self._value = v