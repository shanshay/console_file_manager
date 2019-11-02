import os
import shutil
import platform


def create_dir():
    dir_name = input('Введите название папки, которую хотите создать: ')
    if os.path.exists(dir_name):
        print('Папка уже существует!')
    else:
        os.mkdir(dir_name)
        print('Создана папка: ', os.path.join(os.getcwd(), dir_name))


def del_dir():
    dir_name = input('Введите наименование папки, которую хотите удалить')
    if os.path.exists(dir_name):
        shutil.rmtree(dir_name)
        print('Папка удалена')
    else:
        print('Такой папки не существует')


def copy_tree():
    dir_name = input('Введите имя копируемой папки')
    if os.path.exists(dir_name):
        new_dir_name = input('Введите имя новой папки')
        shutil.copytree(dir_name, new_dir_name)
        print('Папка скопирована')
    else:
        print('Такой папки не существует')


def list_of_work_dir():
    print('Содержимое рабочей директории:')
    print(os.listdir(path='C:/Users/shans/PycharmProjects/console_file_manager/'))


def files_of_work_dir():
    print('Файлы рабочей директории: ')
    from os import listdir
    from os.path import isfile, join
    onlyfiles = [f for f in listdir('C:/Users/shans/PycharmProjects/console_file_manager/') if
                 isfile(join('C:/Users/shans/PycharmProjects/console_file_manager/', f))]
    print(onlyfiles)


def dirs_of_work_dir():
    print('Папки рабочей директории')
    from os import listdir
    from os.path import isfile, isdir, join
    onlydir = [f for f in listdir('C:/Users/shans/PycharmProjects/console_file_manager/') if
               isdir(join('C:/Users/shans/PycharmProjects/console_file_manager/', f))]
    print(onlydir)


def info_about_work_dir():
    print('Информация об операционной системе')
    print(platform.system(), ' ', platform.release())


def author():
    print('Создатель программы: Nadya Shanshay')


def change_directory():
    new_dir = input("Укажите новую рабочую директорию: ")
    while True:
        if not os.path.exists(new_dir):
            new_dir = input('Директория не обнаружена! Введите полный путь до нее или наберите "Отмена": ')
            if new_dir == 'Отмена':
                break
        else:
            os.chdir(new_dir)
            print('Рабочая директория изменена на: ', os.path.join(os.getcwd()))
            break