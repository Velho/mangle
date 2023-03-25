
class Function:
    def __init__(self, ret_type, fun_name):
        self.ret = ret_type
        self.name = fun_name

    def __str__(self):
        return f"{self.ret} {self.name}"
