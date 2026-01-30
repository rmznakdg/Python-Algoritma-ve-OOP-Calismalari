class Student:
    def __init__(self, name: str, grades: list[int]):
        self.name = name
        self.grades = grades

    def add_grade(self, added_grades: list[int]):
        for g in added_grades:
            if not isinstance(g, int):
                raise ValueError("Grades must be integers")
            if g < 0 or g > 100:
                raise ValueError("Grades must be between 0 and 100")

        self.grades.extend(added_grades)

        for i, grade in enumerate(self.grades, start=1):
            print(f"{i}. grade: {grade}")

    def average(self) -> float:
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    def is_passing(self, threshold: float = 50.0) -> bool:
        return self.average() >= threshold


if __name__ == "__main__":
    student1 = Student("Muallim", [45, 86, 74])

    menu = """
Information:
1 --> Add grades
2 --> See average
3 --> Compare the average with input value
q --> Quit
"""
    print(menu)

    while True:
        option = input("Enter your option: ").strip()

        if option == "q":
            print("Program ending.")
            break

        elif option == "1":
            try:
                grades_input = input("Enter the grades you want to add separated by ',': ")
                grades_list = [int(g.strip()) for g in grades_input.split(",")]
                student1.add_grade(grades_list)
                print("Grades added successfully.")
            except ValueError as e:
                print("Invalid input:", e)

        elif option == "2":
            avg = student1.average()
            print(f"The average is: {avg:.2f}")

        elif option == "3":
            try:
                threshold = float(input("Enter the grade threshold: "))
                result = student1.is_passing(threshold)
                print(f"Passing (>= {threshold}): {result}")
            except ValueError:
                print("Please enter a valid value for threshold.")

        else:
            print("Unknown option.")
