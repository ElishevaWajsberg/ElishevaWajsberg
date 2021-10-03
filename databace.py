class Database:
    __instance = None
    _data_base = {}

    def __new__(cls, *args):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def insert(self, key, value):
        if key in Database._data_base.keys():
            Database._data_base[key].append(value)
        else:
            Database._data_base[key] = [value]

    def get(self, key):
        return Database._data_base[key]


    def __str__(self):
        return f"{Database._data_base}"