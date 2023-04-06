from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, data):
        self.__data = data
        self.__index = 0

    def __next__(self):
        try:
            current_product = self.__data[self.__index]
        except IndexError:
            raise StopIteration()
        else:
            self.__index += 1
        return current_product
