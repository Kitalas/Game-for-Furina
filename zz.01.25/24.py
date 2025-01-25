# class Animals:
#     def __init__(self, name:str, color:str):
#         self.name = name
#         self.color = color
#     def move(self):
#         print(f"{self.name}")
#     def eat(self):
#         print(f"{self.name}")
# class Bird(Animals):
#     #can add properties
#     #can nodify nethods
#     def move(self):
#         super().move()
#         print("i can fly")
#
#     #can rewrite nethods
#     def eat(self):
#         print(f"{self.name}")
#     #can rewrite properties
#     def eat(self):
#         print("")
#     #can rewrite properties
#     #can create own nethods
#     def pack(self):
#         print(f"{self.name}")
# class Fish:
#     def move(self):
#         super().move()
#         print("")
#
# bird1 = Bird("bird", "blue")
# bird1.move()
# bird1.eat()
# -----------------------------------------
class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def write_to_chat(self):
        return f"{self.email} може писати в чат."

class BlockedUser(User):
    def __init__(self, email, password, unblock_time):
        super().__init__(email, password)
        self.unblock_time = unblock_time

    def write_to_chat(self):
        return f"{self.email} НЕ МОЖЕ писати в чат."

    def when_can_write(self):
        return f"{self.email} зможе писати в чат з {self.unblock_time}."

user = User("kit_ti_mamu_mav@gmail.com", "For_Natlan")
blocked_user = BlockedUser("kit_ti_tata_mav@gmail.com", "For_Sumeru", "24/01/2025")

print(user.write_to_chat())
print(blocked_user.write_to_chat())
print(blocked_user.when_can_write())
# -----------------------------------------
