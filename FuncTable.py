class FuncTable:
    table = {}
    @staticmethod
    def create(func, ref):
        if func in FuncTable.table:
            raise Exception("Func already exists")
        else:
            FuncTable.table[func] = ref

    @staticmethod
    def getter(func):
        if func in FuncTable.table:
            return FuncTable.table[func]
        else:
            raise Exception("Func not found")