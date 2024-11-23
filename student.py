'''Звонков А.А. гр.3587 ИДЗ№5'''
class Student:
    last_name_len = 0
    first_name_len = 0
    second_name_len = 0

    def __init__(self, last_name: str, first_name: str, second_name: str = ''):
        self.last_name = last_name
        self.first_name = first_name
        self.second_name = second_name
        
        # Обновляем максимальные длины полей
        Student.last_name_len = max(Student.last_name_len, len(self.last_name))
        Student.first_name_len = max(Student.first_name_len, len(self.first_name))
        Student.second_name_len = max(Student.second_name_len, len(self.second_name))

    @staticmethod
    def line():
        print('-' * (Student.last_name_len + Student.first_name_len + Student.second_name_len + 10))

    def __str__(self) -> str:
        return f'| {self.last_name:<{Student.last_name_len}} ' \
               f'| {self.first_name:<{Student.first_name_len}} ' \
               f'| {self.second_name:<{Student.second_name_len}} |'
