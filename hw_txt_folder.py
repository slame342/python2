import os


with open("folder/file.txt") as file:
    text = file.readlines()
    # print(text)

    new_file = []
    for line in text:
        if len(line) > 1:
            new_file.append(line)
try:
    os.mkdir("folder/Folder")
except:
    print("Attention!!!such a folder has already been created!")
    for word in range(0, len(new_file)):
        file_name = f'folder/Folder/file{word}.txt'
        with open(file_name, 'w') as file1:
            file1.write(new_file[word])

    try:
        os.remove('folder/file.txt')  # удаление файла
    except Exception as error:
        print(error)
    finally:
        print('файл успешно удален')

