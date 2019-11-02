import os
import shutil
import victory
import platform
import personal_count
import work_functions


while True:
    print('1. Создать папку')
    print('2. Удалить файл/папку')
    print('3. Копировать файл/папку')
    print('4. Просмотр содержимого рабочей директории')
    print('5. Посмотреть только файлы')
    print('6. Посмотреть только папки')
    print('7. Просмотр информации об операционной системе')
    print('8. Создатель программы')
    print('9. Играть в викторину')
    print('10. Мой банковский счет')
    print('11.Сменить рабочую директорию')
    print('12. Выход')
    choice = input('Выберите пункт меню')
    if choice == '1':
        work_functions.create_dir()
    elif choice == '2':
        work_functions.del_dir()
    elif choice == '3':
        work_functions.copy_tree()
    elif choice == '4':
        work_functions.list_of_work_dir()
    elif choice == '5':
        work_functions.files_of_work_dir()
    elif choice == '6':
        work_functions.dirs_of_work_dir()
    elif choice == '7':
        work_functions.info_about_work_dir()
    elif choice == '8':
        work_functions.author()
    elif choice == '9':
        victory.victory_game()
    elif choice == '10':
        personal_count.call_personal_count()
    elif choice == '11':
        work_functions.change_directory()
    elif choice == '12':
        break
    else:
        print('Неверный пункт меню')