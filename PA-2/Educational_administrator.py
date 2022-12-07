import control_system
class Educational_administrator(control_system.System):
    def __init__(self,Username,Password):
        self.Username=Username
        self.psw=Password