# Add necessary imports and global variables
import os
import hashlib

# Define User class
class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = hashlib.sha256(password.encode()).hexdigest()
        self.role = role

# Define Authentication class
class Authentication:
    def __init__(self):
        self.users = []

    def register(self, username, password, role):
        self.users.append(User(username, password, role))

    def login(self, username, password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        for user in self.users:
            if user.username == username and user.password == hashed_password:
                return user
        return None

# Define Course and VirtualClassroom classes
class Course:
    def __init__(self, name):
        self.name = name
        self.students = []

    def join_course(self, student):
        self.students.append(student)

class VirtualClassroom:
    def __init__(self):
        self.courses = []

    def join_course(self, course, student):
        course.join_course(student)

# Define Resource and ResourceDatabase classes
class Resource:
    def __init__(self, name, link):
        self.name = name
        self.link = link

class ResourceDatabase:
    def __init__(self):
        self.resources = []

    def add_resource(self, name, link):
        self.resources.append(Resource(name, link))

# Define Message and MessagingSystem classes
class Message:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content

class MessagingSystem:
    def __init__(self):
        self.messages = []

    def send_message(self, sender, receiver, content):
        self.messages.append(Message(sender, receiver, content))

# Define StudentPanel and StaffPanel classes
class StudentPanel:
    def __init__(self):
        pass

    def show_welcome_message(self):
        print("Welcome to the Student Panel!")

    def remote_learning(self):
        print("Remote Learning is in progress...")

    def access_resources(self, resource_db):
        print("Accessing Resources:")
        for resource in resource_db.resources:
            print(f"Resource: {resource.name}, Link: {resource.link}")

    def view_attendance(self):
        print("Viewing Attendance...")

    def view_calendar(self):
        print("Viewing Calendar...")

class StaffPanel:
    def __init__(self):
        pass

    def show_welcome_message(self):
        print("Welcome to the Staff Panel!")

    def mark_attendance(self):
        print("Marking Attendance...")

    def view_holidays(self):
        print("Viewing Holidays...")

    def manage_subjects(self):
        print("Managing Subjects...")

    def manage_classes(self):
        print("Managing Classes...")

    def apply_leave(self):
        print("Applying for Leave...")

    def view_assigned_classes(self):
        print("Viewing Assigned Classes...")

# Define UserDatabase class
class UserDatabase:
    def __init__(self):
        self.auth = Authentication()

    def register_user(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        role = input("Enter role (staff/student): ")
        self.auth.register(username, password, role)

    def login_user(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        return self.auth.login(username, password)

# Modify main function to integrate new features
def main():
    user_db = UserDatabase()
    student_panel = StudentPanel()
    staff_panel = StaffPanel()
    resource_db = ResourceDatabase()

    while True:
        os.system("clear")
        print("\t\t-----------------------------------------------")
        print("\t\t     Educational Management System")
        print("\t\t----------------------------------------------")
        print("\n\t\t\tEnter <1> to Register")
        print("\t\t\tEnter <2> to Login")
        print("\t\t\tEnter <0> to Exit\n")
        choice = input("\nEnter Your Choice: ")
        if choice == '1':
            user_db.register_user()
        elif choice == '2':
            user = user_db.login_user()
            if user:
                if user.role == 'student':
                    student_panel.show_welcome_message()
                    student_panel.remote_learning()
                    student_panel.access_resources(resource_db)
                    student_panel.view_attendance()
                    student_panel.view_calendar()
                    input("Press Enter to continue...")
                elif user.role == 'staff':
                    staff_panel.show_welcome_message()
                    staff_panel.mark_attendance()
                    staff_panel.view_holidays()
                    staff_panel.manage_subjects()
                    staff_panel.manage_classes()
                    staff_panel.apply_leave()
                    staff_panel.view_assigned_classes()
                    input("Press Enter to continue...")
                else:
                    print("Invalid user role.")
            else:
                print("Login failed. Invalid username or password.")
        elif choice == '0':
            break
        else:
            print("\nWRONG CHOICE!!!\nTRY AGAIN")

if __name__ == "__main__":
    main()
