

class SymbolTable:
    def __init__(self):
        self.table = {}
    def create(self, var, var_type, value):
        if var in self.table:
            raise Exception("Variable already exists")
        else:
            self.table[var] = [var_type, value]

    def setter(self, var, var_type, value):
        if var in self.table:
            if self.table[var][0] == var_type:
                self.table[var][1] = value
            else:
                raise Exception(
                    f"Trying to associate a {var_type} to the variable '{var}' that declared as {self.table[var][0]}")
        else:
             Exception("Variable not found")

    def getter(self, var):
        if var in self.table:
            return self.table[var]
        else:
            raise Exception("Variable not found")