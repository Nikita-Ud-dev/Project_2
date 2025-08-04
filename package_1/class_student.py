from Project_2.package_1.class_human import Human

class Student(Human):
    number_student = 0

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name
        Student.number_student += 1
        self.number_student1 = Student.number_student

    def __eq__(self, other):
        # if not isinstance(other, Student): # Якщо об'єкт не являється екземпляром студента то Фолс
        #     return False
        return str(self) == str(other) # я зробив перевірку атребутів але цього не просить задача тому так # Порівнюються атребути щоб розуміти об'єкт дублікат студенту чи ні


        # elif self.first_name :
        #     return self.first_name == other.first_name
        # elif self.last_name == other.last_name:
        #     return self.last_name == other.last_name
        # elif self.age == other.age:
        #     return self.age == other.age
        # elif self.gender == other.gender:
        #     return self.gender == other.gender
        # elif self.record_book == other.record_book:
        #     return self.record_book == other.record_book
        # return None


    def __str__(self):
        return (f"Student {self.number_student1}\n"
                f"First_name: {self.first_name}\n"
                f"Last_name: {self.last_name}\n"
                f"Age: {self.age}\n"
                f"Gender: {self.gender}\n"
                f"Record_book: {self.record_book}\n")