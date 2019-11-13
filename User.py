class User:
    
    num_user = 0

    def __init__(self, id, pw, token=None):
        self.id = id
        self.password = pw
        self.token = token