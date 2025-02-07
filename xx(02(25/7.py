# def add_phone_number():
#     phone_number = input("Напишите нового друга(номер телефона): ")
#     with open("phone_numbers.txt", "a") as file:
#         file.write(phone_number + "\n")
#
#
# def get_phone_numbers():
#     try:
#         with open("phone_numbers.txt", "r") as file:
#             numbers = file.readlines()
#             if numbers:
#                 print("все записаные номера:")
#                 for number in numbers:
#                     print(number.strip())
#             else:
#                 print("нет записаных номеров")
#     except FileNotFoundError:
#         print("Запись с номерами не наш/потерян")
#
#
# def main():
#     while True:
#         print("Меню:")
#         print("1. записать номер телефона")
#         print("2. получить все записи номеров")
#         print("3. закрыть блокнот")
#
#         choice = input("Выбрайте (1-3): ")
#
#         if choice == "1":
#             add_phone_number()
#         elif choice == "2":
#             get_phone_numbers()
#         elif choice == "3":
#             break
#         else:
#             print("ой неверно, выберите из меню.")
#
#
# if __name__ == "__main__":
#     main()
#
# def create_note():
#     note = input("запишите в блокнот: ")
#     with open("notes.txt", "a") as file:
#         file.write(note + "\n")
#
#
# def read_all_notes():
#     try:
#         with open("notes.txt", "r") as file:
#             notes = file.readlines()
#             if notes:
#                 print("все записи:")
#                 for index, note in enumerate(notes, start=1):
#                     print(f"{index}. {note.strip()}")
#             else:
#                 print("усп, у вас нет записей.")
#     except FileNotFoundError:
#         print("Записи были не ваши/потеряные.")
#
#
# def read_single_note():
#     note_number = int(input("номерация записи: "))
#     try:
#         with open("notes.txt", "r") as file:
#             notes = file.readlines()
#             if 0 < note_number <= len(notes):
#                 print(f"запись {note_number}: {notes[note_number - 1].strip()}")
#             else:
#                 print("упс, у вас нет такой записи")
#     except FileNotFoundError:
#         print("Файл з нотатками не знайдено.")
#
#
# def delete_note():
#     note_number = int(input("Введіть номер нотатки для видалення: "))
#     try:
#         with open("notes.txt", "r") as file:
#             notes = file.readlines()
#         if 0 < note_number <= len(notes):
#             del notes[note_number - 1]
#             with open("notes.txt", "w") as file:
#                 file.writelines(notes)
#             print("Вы удалили запись.")
#         else:
#             print("упс, у вас нет такой записи")
#     except FileNotFoundError:
#         print("Записи были не ваши/потеряные.")
#
#
# def main():
#     while True:
#         print("Меню:")
#         print("1. записать в блокнот")
#         print("2. посмотреть все записи")
#         print("3. посмотреть 1 запись")
#         print("4. удалить запись")
#         print("5. Вийти")
#
#         choice = input("Виберайте (1-5): ")
#
#         if choice == "1":
#             create_note()
#         elif choice == "2":
#             read_all_notes()
#         elif choice == "3":
#             read_single_note()
#         elif choice == "4":
#             delete_note()
#         elif choice == "5":
#             break
#         else:
#             print("ой неверно, выберите из меню.")
#
#
# if __name__ == "__main__":
#     main()
