# class Book:
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages
        
#     def info(self):
#         print(  f'название: {self.title}\n'
#                 f'автор: {self.author}\n'
#                 f'количество страниц: {self.pages}')
        
        
#     def size(self):
#         if self.pages > 300:
#             print('книга большая')
#         else:
#             print('книга маленькая')
        
        
# book1 = Book('Преступление и наказание', 'Федор Достоевский', 350)

# book1.info()
# # book1.size()



# class Student:
    
#     def __init__(self, name):
#         self.name = name
#         self.grade = None
        
        
#     def set_grade(self, grade):
        
#         self.grade = grade
        
#     def get_grade(self):
#         if self.grade is None:
#             print('у студента не поставлена оценка')
#         else:
#             print(f'оценка студента: {self.grade}')
        
        
# student1 = Student('Iman')
# student1.get_grade()
# student1.set_grade(83)
# student1.get_grade()




# class Teacher:
#     def __init__(self, name, subject):
#         self.name = name
#         self.subject = subject
        
        
#     def info(self):
#         print(f'{self.name} предмет преподования {self.subject}')
        

# class TeacherMath(Teacher):
#     pass

# class TeacherLang(Teacher):
    
#     def info(self):
#         print('Я сперва унаследовал')
#         print(f'{self.name} предмет преподования {self.subject}')
        
        

# teacher_math = TeacherMath('Фибоначчи', 'Математика')
# teacher_lang = TeacherMath('Гвидо Ван Рассум', 'Python')

# teacher_math.info()
# teacher_lang.info()


class Venicle:
    def __init__(self, mark, model):
        self.mark = mark
        self.model = model
        
    
    def start_engine(self):
        print(f'{self.mark}-{self.model} заведен')
        
        
car1 = Venicle(mark='Toyota', model='Camry')
car1.start_engine()