import os

# Создаёт папку reports.
#
# Внутри неё создаёт файл log.txt и записывает туда строку "Hello, OS!".
#
# Проверяет, что файл действительно существует.
#
# Выводит полный путь к этому файлу.
#
# Удаляет файл и папку.

os.mkdir("reports")
os.chdir("reports")
with open("log.txt","w") as file:
    file.write("Hello, OS!")
print(os.path.exists("log.txt"))
print(os.path.abspath("log.txt"))
os.remove("log.txt")
os.chdir("..")
os.rmdir("reports")