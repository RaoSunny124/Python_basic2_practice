# education = "inter"
# name = 'Hassan'
# age = 19
# city = "vehari"
# program = 'PIAIC'
# print(f'''My name is {name}.My age is {age}.
# I have completed my {education} from {city} college''')


# print(f"I am {name}.")

# print(f'I am a student of {program} in Batch 62')

#f_string is making easiest developer's life...






class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def calculate_average(self):
        return sum(self.scores) / len(self.scores)

    def is_passing(self, passing_score=40):
        return all(score >= passing_score for score in self.scores) 


class PerformanceTracker:
    def __init__(self):
        self.students = {}

    def add_student(self, name, scores):
        self.students[name] = Student(name, scores)

    def calculate_class_average(self):
        if not self.students:
            return 0
        total_average = sum(student.calculate_average() for student in self.students.values())
        return total_average / len(self.students)

    def display_student_performance(self):
        if not self.students:
            print("No student data available.")
            return

        for student in self.students.values():
            average = student.calculate_average()
            status = "Passing" if student.is_passing() else "Needs Improvement"
            print(f"Student: {student.name}, Average Score: {average:.2f}, Status: {status}")

        class_average = self.calculate_class_average()
        print(f"\nClass Average: {class_average:.2f}")


def main():
    tracker = PerformanceTracker()
    print("Welcome to the Student Performance Tracker!")

    while True:
        try:
            name = input("\nEnter student's name (or type 'done' to finish): ").strip()
            if name.lower() == "done":
                break

            scores = []
            for subject in ["Math", "Science", "English"]:
                while True:
                    try:
                        score = int(input(f"Enter score for {subject}: "))
                        if 0 <= score <= 100:
                            scores.append(score)
                            break
                        else:
                            print("Score must be between 0 and 100. Try again.")
                    except ValueError:
                        print("Invalid input. Please enter a valid integer.")

            tracker.add_student(name, scores)
            print(f"Added {name}'s scores: {scores}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    print("\nStudent Performance Report:")
    tracker.display_student_performance()


# if __name__ == "__main__":
#     main()
