import datetime

class FileCreator:
    def __init__(self, path):
        self.path = path
        self.create_time = datetime.datetime.now()

    def __enter__(self):
        self.file = open(self.path)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        self.end_time = datetime.datetime.now()
        print(f'Время запуска кода: {self.create_time}\n')
        print(f'Время окончания работы кода: {self.end_time}\n')
        print(f'Времени потрачено на выполнение кода: {self.end_time - self.create_time}')


with FileCreator('datetime.txt') as file:
    a = int(input('Введите, сколько пингвинов хотите увидеть: '))
    print('   _~_    ' * a)
    print('  (o o)   ' * a)
    print(' /  V  \  ' * a)
    print('/(  _  )\ ' * a)
    print('  ^^ ^^   ' * a)
