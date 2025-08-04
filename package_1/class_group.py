class Group:

    def __init__(self, number):
        self.number = number
        self.group = [] # Замінив сет на лист щоб зберегти порядок, і використовуючи тип данних слист я рузумію що метод hash мені не потрібен


    def add_student(self, student):
        if student not in self.group:
            self.group.append(student)
        else:
            print("Виявлено дублікат студенту\n")

    def delete_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return self.group.remove(student)
        return None

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = "\n"
        for student in self.group:
            all_students = all_students + str(student)
            all_students = all_students + "\n"
        return f'Number:{self.number}\n{all_students}'