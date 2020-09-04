class User:
    """
    Class that generates new instances of users
    """
    user_list = []

    def _init_(self,user_name,pasword):
        self.user_name = user_name
        self.pasword = pasword

    def save_user(self):
        """
        save_user method saves the new users object
        """
        User.user_list.append(self)