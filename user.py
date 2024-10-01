class User:
    def __init__(self, user_name, password):
        self.__user_name = user_name
        self.__password = password

    def get_user_name(self):
        return self.__user_name

    def set_user_name(self, user_name):
        self.__user_name = user_name

    def display_user_info(self):
        print(f"Користувач: {self.__user_name}, пароль: {self.__password}")