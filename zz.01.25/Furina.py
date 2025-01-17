import random
import pickle
import time
print("Здраствуйте,вы на Викторине по Геншине")
time.sleep(2)
print("c вами Фурина и мы начинаем")
time.sleep(2)
print("!Твой первый вопрос!")
time.sleep(2)
print("*вопросы повторяються, будте акуратные*")
time.sleep(2)


questions = [
     {"question": "кто такой Лини?", "options": ["Фокусник", "Косплеер", "Поет", "НПС"], "answer": "Фокусник"},
     {"question": "Райден изтрила(бг) в пепел?", "options": ["Синьору", "Арликину", "Дотторе", "Капитано"], "answer": "Синьору"},
     {"question": "Как мы можем назвать Паймон при встречи с Эмбер?", "options": ["Живая консерва", "Селестия под прикрытием", "Летающий покемон", "Лучший компаньон"],
     "answer": "Лучший компаньон"},
     {"question": "Самый живучий персонаж в игре?", "options": ["Паймон", "Синьора", "ГГ", "Ци Ци"], "answer": "ГГ"},
     {"question": "Невиллет, кто он?", "options": ["Гидро дед", "Гидро Архонт", "Гидро дракон", "Верховный судья"], "answer": "Гидро Архонт"},
     {"question": "Казнь Фокалорс помогло спасти?", "options": ["Фурину от смерти", "Фурину от смерти", "Людей от смерти", "Нёвиллету статть Архонтом"], "answer": "ЦЕЛЫЙ Фонтейн от пророчества"},
     {"question": "Питомец Венти это?", "options": ["Дракон Аджаха", "Дракон Двалин", "Кицуне Яе Мино", "Кит Бездны"], "answer": "Дракон Двалин"},
     {"question": "Кто человек из Адептов?", "options": ["Гань Юнь", "Сяо", "Шень Хень", "Сянь Юнь"], "answer": "Шень Хень"},
     {"question": "?", "options": ["", "", "", ""], "answer": ""},
     {"question": "?", "options": ["", "", "", ""], "answer": ""}
]

def get_random_question():
    return random.choice(questions)


def check_answer(question, user_answer):
    return question["answer"] == user_answer


def play_game():
    money = 0
    for i in range(10):
        question = get_random_question()
        print(question["question"])
        for idx, option in enumerate(question["options"]):
            print(f"{idx + 1}. {option}")

        while True:
            user_answer = input("Виберіть номер відповіді: ")
            if user_answer.isdigit():
                user_answer = int(user_answer)
                if 1 <= user_answer <= len(question["options"]):
                    break
                else:
                    print("Будь ласка, введіть номер в межах варіантів.")
            else:
                print("Будь ласка, введіть число.")

        if check_answer(question, question["options"][user_answer - 1]):
            money += 1000
            print("Правильно! Ви виграли 1000.")
        else:
            print("Неправильно. Гра закінчена.")
            break

    print(f"Ваш виграш: {money}")
if __name__ == "__main__":
    play_game()