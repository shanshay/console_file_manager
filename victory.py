import random


def victory_game():
    gzl = []
    gzl01 = {'name': 'Джорд Вашингтон', 'date_of_birth': '22.02.1732', 'dob_long': 'Двадцать второе февраля 1732 года'}
    gzl02 = {'name': 'Джон Адамс', 'date_of_birth': '30.10.1735', 'dob_long': 'Тридцатое октября 1735 года'}
    gzl03 = {'name': 'Томас Джефферсон', 'date_of_birth': '13.04.1743', 'dob_long': 'Тринадцатое апреля 1743 года'}
    gzl04 = {'name': 'Джеймс Мэдисон', 'date_of_birth': '16.03.1751', 'dob_long': 'Шестнадцатое марта 1751 года'}
    gzl05 = {'name': 'Джеймс Монро', 'date_of_birth': '28.04.1758', 'dob_long': 'Двадцать восьмое апреля 1758 года'}
    gzl06 = {'name': 'Джон Куинси Адамс', 'date_of_birth': '11.07.1767', 'dob_long': 'Одиннадцатое июля 1767 года'}
    gzl07 = {'name': 'Эндрю Джексон', 'date_of_birth': '15.03.1767', 'dob_long': 'Пятнадцатое марта 1767 года'}
    gzl08 = {'name': 'Мартин Ваг Бюрен', 'date_of_birth': '05.12.1782', 'dob_long': 'Пятое декабря 1782 года'}
    gzl09 = {'name': 'Уильям Гаррисон', 'date_of_birth': '09.02.1773', 'dob_long': 'Девятое февраля 1773 года'}
    gzl10 = {'name': 'Джон Тайлер', 'date_of_birth': '29.03.1790', 'dob_long': 'Двадцать девятое марта 1790 года'}
    gzl.append(gzl01)
    gzl.append(gzl02)
    gzl.append(gzl03)
    gzl.append(gzl04)
    gzl.append(gzl05)
    gzl.append(gzl06)
    gzl.append(gzl07)
    gzl.append(gzl08)
    gzl.append(gzl09)
    gzl.append(gzl10)
    while True:
        print('Сыграем?')
        answer = input()
        if answer == 'да':
            result = random.sample(gzl, 5)
            i = 0
            count = 0;
            while i < 5:
                n = result[i]
                print('Дата рождения', n['name'])
                m = input()
                if m == n['date_of_birth']:
                    print('Ответ верный!!!')
                    count = count + 1
                else:
                    print('Неверно!!! Верная дата рождения', n['dob_long'])
                i = i + 1
            print('Вы набрали ', count, ' очков')
            if 0 <= count <= 2:
                print('You lose!! Loser hahaha')
            elif 2 < count < 5:
                print('You are norm, but you can be better :-)')
            else:
                print('You are the best!!!! Wow!!!')
        else:
            break