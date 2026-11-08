import os

# Каждая строка файла выглядит так: Content/Map.umap: filter: lfs
for line in open('.git/staged.txt', encoding='utf-8'):
    name, status = line.strip().split(': filter: ')

    # Проверка 1: служебные папки Unreal Engine
    folder = name.split('/')[0]
    if folder in ['Saved', 'Intermediate', 'Binaries', 'DerivedDataCache', '.vs']:
        print('ОШИБКА:', name, '- служебная папка Unreal, её нельзя коммитить')
        exit(1)

    # Проверка 2: файлы больше 50 МБ, которые не идут через LFS
    if os.path.isfile(name) and os.path.getsize(name) > 50 * 1024 * 1024 and status == 'unspecified':
        print('ОШИБКА:', name, 'больше 50 МБ и не идёт через LFS')
        exit(1)
