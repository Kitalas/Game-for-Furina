# class User:
#     def __init__(self, email, password, age):
#         self.__email = email
#         self.__password = password
#         self.__age = age
#
#     def get_email(self):
#         return self.__email.split('@')[0]
#     def set_email(self, new_email):
#         if new_email.endswith('@gmail.com'):
#             self.__email = new_email
#     def sent_email_message(self, message_text:str):
#         self.__smpt_connect("idbsugsdol", "ftyftys")
#         nsg = self.__create_message_structure(message_text, "tropp[os]")
#     def __smpt_connect(self, login, password):
#         pass
#     def __create_message_structure(self, text, topic):
#         return None
#
# user1 = User("rnb@gmail.com", "mem_bsd_i_evangeliuma")
# user1.set_email('arlecino@gmail.com')
# email_of_user = user1.set_email()
# print(email_of_user)
#
# user1.__password = "rsnkugob1983"
# print(user1.__password)

# ///////////////////////////////////
import  turtle
class Shape:
    def __init__(self, size:int, color:str, pen_width:int, speed:int, x:int, y:int):
        self.__size = size
        self.__color = color
        self.__pen_width = pen_width
        self.__speed = speed
        self.__x = x
        self.__y = y
