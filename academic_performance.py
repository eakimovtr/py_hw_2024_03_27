class Student:
    def __init__(self):
        self.marks: list[int] = []
        self.set_marks(Student.input_marks())
        self.scholarship: bool = self.is_eligible_scholarship()
        
    def set_marks(self, marks_list: list[int]) -> None:
        self.marks = marks_list
            
    def get_marks(self) -> list[int]:
        return self.marks
    
    def is_eligible_scholarship(self) -> bool:
        return sum(self.marks) / len(self.marks) >= 10.7
    
    # Check that mark value is in the correct range
    @staticmethod
    def check_mark_value(mark: int) -> bool:
        return 1 <= mark <= 12
    
    def retry(self, key: int, value: int) -> None:
        if not 0 <= key < len(self.marks):
            raise IndexError("Marks index out of range")
        if not Student.check_mark_value(value):
            raise ValueError("Invalid value for mark")
        self.marks[key] = value
     
    @staticmethod
    def input_marks() -> list[int]:
        print("Enter marks separated by comma (,)")
        usr_input: list = input().strip().split(",")
        if len(usr_input) != 10:
            raise ValueError("Number of marks must be 10")
        res: list[int] = []
        for str_mark in usr_input:
            try:
                mark = int(str_mark)
            except ValueError as e:
                mark = round(mark)
            if not Student.check_mark_value(mark):
                raise ValueError("Invalid value for mark")
            res.append(mark)
        return res
    
    def sort_display(self, desc=False) -> None:
        print(sorted(self.marks, reverse=desc))
    
    
student1 = Student()
print(student1.get_marks())
print(student1.is_eligible_scholarship())
student1.sort_display(desc=True)