{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"provenance":[{"file_id":"1W8lBvE01Q5I2oLj601viHOYUbE9dMYA3","timestamp":1710098499498}],"authorship_tag":"ABX9TyNbQos671aKIqEOKz7R9HM0"},"kernelspec":{"name":"python3","display_name":"Python 3"},"language_info":{"name":"python"}},"cells":[{"cell_type":"markdown","source":["Personal Library Management System\n","Double-click (or enter) to edit\n","\n","Project Title: Personal Library Management System\n","\n","Project Description: For this project, you will be building a Personal Library Management System using the Python programming concepts you've learned so far. This system will allow users to manage their personal book collection, add new books, remove books, search for books, and store information about each book.\n","\n","Project Requirements:\n","\n","Class Definitions:\n","\n","Create a class named Book to represent a book with attributes like title, author, genre, and publication year.\n","Create a class named Library to represent the personal library. This class should have methods to add a book, remove a book, search for a book by title or author, and display the entire library.\n","Data Structure:\n","\n","Use appropriate data structures like lists, dictionaries, or sets to store and manage the collection of books in the library.\n","File Handling:\n","\n","Implement methods in the Library class to save and load the library data to/from a text or CSV file. This will ensure that the library data is persistent across different program executions.\n","Exception Handling:\n","\n","Implement exception handling to handle potential errors gracefully. For instance, handle cases where a book is not found, a file is not found, or input validation errors occur.\n","User Interaction:\n","\n","Create a user-friendly command-line interface that allows users to interact with the library. Provide options to add a book, remove a book, search for a book, and display the entire library.\n","Project Steps:\n","\n","Class Definitions:\n","\n","Define the Book class with appropriate attributes and a constructor.\n","Define the Library class with methods for adding, removing, searching, and displaying books.\n","Data Structure:\n","\n","Initialize an empty data structure (list or dictionary) in the Library class to store the book objects.\n","File Handling:\n","\n","Implement methods in the Library class to save the library data to a file (e.g., \"library.txt\" or \"library.csv\").\n","Implement methods to load the library data from the file during program startup.\n","Exception Handling:\n","\n","Implement try-except blocks to handle errors related to user input, file operations, and book search.\n","User Interaction:\n","\n","Create a user-friendly menu that presents options to the user (e.g., \"Add a book,\" \"Search for a book,\" etc.).\n","Based on the user's choice, call the appropriate methods in the Library class.\n","Project Extensions: If you'd like to take this project further, consider adding the following features:\n","\n","Implement a graphical user interface (GUI) using a library like Tkinter or PyQt.\n","Allow users to rate and review books.\n","Sort and display books by different criteria (e.g., title, author, genre).\n","Provide recommendations based on the user's reading history.\n","Integrate an online book API to fetch book details automatically.\n"],"metadata":{"id":"xDR0dFBZxtp8"}},{"cell_type":"code","execution_count":null,"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"_s4MxUwExaWm","executionInfo":{"status":"ok","timestamp":1710098097263,"user_tz":-120,"elapsed":275047,"user":{"displayName":"Sara Metawea","userId":"16002586230669284741"}},"outputId":"39f4fa80-eaef-427d-a894-43fc7d441e3d"},"outputs":[{"name":"stdout","output_type":"stream","text":["Library file not found. Starting with an empty library.\n","\n","Menu:\n","1. Add a book\n","2. Remove a book\n","3. Search for a book by title\n","4. Search for a book by author\n","5. Display entire library\n","6. Save library to file\n","7. Exit\n","Enter your choice: 7\n"]}],"source":["import csv\n","\n","class Book:\n","    def __init__(self, title, author, genre, publication_year):\n","        self.title = title\n","        self.author = author\n","        self.genre = genre\n","        self.publication_year = publication_year\n","\n","    def __str__(self):\n","        return f\"{self.title} by {self.author} ({self.publication_year}) - {self.genre}\"\n","\n","class Library:\n","    def __init__(self):\n","        self.books = []\n","\n","    def add_book(self, book):\n","        self.books.append(book)\n","\n","    def remove_book(self, title):\n","        for book in self.books:\n","            if book.title == title:\n","                self.books.remove(book)\n","                print(f\"Book '{title}' removed successfully.\")\n","                return\n","        print(f\"Book '{title}' not found.\")\n","\n","    def search_by_title(self, title):\n","        found_books = []\n","        for book in self.books:\n","            if title.lower() in book.title.lower():\n","                found_books.append(book)\n","        return found_books\n","\n","    def search_by_author(self, author):\n","        found_books = []\n","        for book in self.books:\n","            if author.lower() in book.author.lower():\n","                found_books.append(book)\n","        return found_books\n","\n","    def display_library(self):\n","        if not self.books:\n","            print(\"The library is empty.\")\n","        else:\n","            print(\"Library contents:\")\n","            for book in self.books:\n","                print(book)\n","\n","    def save_library_to_csv(self, filename):\n","        with open(filename, 'w', newline='') as file:\n","            writer = csv.writer(file)\n","            for book in self.books:\n","                writer.writerow([book.title, book.author, book.genre, book.publication_year])\n","\n","    def load_library_from_csv(self, filename):\n","        try:\n","            with open(filename, 'r') as file:\n","                reader = csv.reader(file)\n","                for row in reader:\n","                    title, author, genre, publication_year = row\n","                    self.add_book(Book(title, author, genre, publication_year))\n","            print(\"Library loaded successfully from file.\")\n","        except FileNotFoundError:\n","            print(\"Library file not found. Starting with an empty library.\")\n","\n","if __name__ == \"__main__\":\n","    my_library = Library()\n","\n","    # Load library data from a CSV file\n","    my_library.load_library_from_csv(\"library.csv\")\n","\n","    # User interaction loop\n","    while True:\n","        print(\"\\nMenu:\")\n","        print(\"1. Add a book\")\n","        print(\"2. Remove a book\")\n","        print(\"3. Search for a book by title\")\n","        print(\"4. Search for a book by author\")\n","        print(\"5. Display entire library\")\n","        print(\"6. Save library to file\")\n","        print(\"7. Exit\")\n","\n","        choice = input(\"Enter your choice: \")\n","\n","        if choice == \"1\":\n","            title = input(\"Enter title: \")\n","            author = input(\"Enter author: \")\n","            genre = input(\"Enter genre: \")\n","            publication_year = input(\"Enter publication year: \")\n","            my_library.add_book(Book(title, author, genre, publication_year))\n","        elif choice == \"2\":\n","            title = input(\"Enter title of the book to remove: \")\n","            my_library.remove_book(title)\n","        elif choice == \"3\":\n","            title = input(\"Enter title to search: \")\n","            found_books = my_library.search_by_title(title)\n","            if found_books:\n","                print(\"Matching books:\")\n","                for book in found_books:\n","                    print(book)\n","            else:\n","                print(\"No matching books found.\")\n","        elif choice == \"4\":\n","            author = input(\"Enter author to search: \")\n","            found_books = my_library.search_by_author(author)\n","            if found_books:\n","                print(\"Matching books:\")\n","                for book in found_books:\n","                    print(book)\n","            else:\n","                print(\"No matching books found.\")\n","        elif choice == \"5\":\n","            my_library.display_library()\n","        elif choice == \"6\":\n","            my_library.save_library_to_csv(\"library.csv\")\n","            print(\"Library saved to file.\")\n","        elif choice == \"7\":\n","            break\n","        else:\n","            print(\"Invalid choice. Please try again.\")\n"]},{"cell_type":"markdown","source":["Student Grade Tracker\n","Project Title: Student Grade Tracker\n","Project Description: In this project, you will build a Student Grade Tracker program that allows users to enter and manage student grades for different subjects. You'll utilize Python's basic data structures, file handling, exception handling, and object-oriented programming concepts to implement this project.\n","\n","Project Requirements:\n","\n","Class Definitions:\n","\n","Create a class named Student to represent a student with attributes like name and a dictionary to store subject grades.\n","Create a class named Subject to represent a subject with attributes like name and grades.\n","Data Structure:\n","\n","Use dictionaries and lists to organize student and subject information.\n","File Handling:\n","\n","Implement methods to save and load student data to/from a text file.\n","Store each student's name, subjects, and respective grades.\n","Exception Handling:\n","\n","Implement exception handling to handle input errors, file errors, and grade validation (ensure grades are within a valid range).\n","User Interaction:\n","\n","Create a user-friendly command-line interface that allows users to add students, add subjects and grades, view student grades, and save/load data.\n","Project Steps:\n","\n","Class Definitions:\n","\n","Define the Student class with attributes for the student's name and a dictionary to store subjects and grades.\n","Define the Subject class with attributes for the subject's name and a list to store grades.\n","Data Structure:\n","\n","Create a dictionary to store student objects, where keys are student names and values are corresponding Student objects.\n","File Handling:\n","\n","Implement methods to save student data to a text file and load data from the file.\n","Use a format that allows you to save and load student names, subjects, and grades.\n","Exception Handling:\n","\n","Use try-except blocks to handle errors such as invalid inputs and file-related issues.\n","User Interaction:\n","\n","Create a loop that presents a menu of options to the user (e.g., \"Add Student,\" \"Add Subject and Grade,\" \"View Student Grades,\" \"Save and Exit\").\n","Based on the user's choice, call the appropriate methods in your classes to perform the desired actions.\n","Project Extensions: To extend the project's functionality, consider adding the following features:\n","\n","Calculate and display each student's average grade.\n","Allow users to update or delete students, subjects, and grades.\n","Implement a basic graphical user interface using the tkinter library.\n","Allow users to export student grade reports to a text or CSV file.\n","[ ]\n"],"metadata":{"id":"USgo_Pwpx7y3"}},{"cell_type":"code","source":["import os\n","\n","class Subject:\n","    def __init__(self, name):\n","        self.name = name\n","        self.grades = []\n","\n","    def add_grade(self, grade):\n","        self.grades.append(grade)\n","\n","    def average_grade(self):\n","        if not self.grades:\n","            return 0\n","        return sum(self.grades) / len(self.grades)\n","\n","class Student:\n","    def __init__(self, name):\n","        self.name = name\n","        self.subjects = {}\n","\n","    def add_subject(self, subject_name):\n","        self.subjects[subject_name] = Subject(subject_name)\n","\n","    def add_grade(self, subject_name, grade):\n","        if subject_name in self.subjects:\n","            self.subjects[subject_name].add_grade(grade)\n","        else:\n","            print(f\"Subject '{subject_name}' not found for student {self.name}.\")\n","\n","    def average_grade(self):\n","        total_average = 0\n","        for subject in self.subjects.values():\n","            total_average += subject.average_grade()\n","        return total_average / len(self.subjects)\n","\n","class GradeTracker:\n","    def __init__(self):\n","        self.students = {}\n","\n","    def add_student(self, student_name):\n","        self.students[student_name] = Student(student_name)\n","\n","    def add_subject_to_student(self, student_name, subject_name):\n","        if student_name in self.students:\n","            self.students[student_name].add_subject(subject_name)\n","        else:\n","            print(f\"Student '{student_name}' not found.\")\n","\n","    def add_grade_to_student(self, student_name, subject_name, grade):\n","        if student_name in self.students:\n","            self.students[student_name].add_grade(subject_name, grade)\n","        else:\n","            print(f\"Student '{student_name}' not found.\")\n","\n","    def save_data(self, filename):\n","        with open(filename, 'w') as file:\n","            for student_name, student in self.students.items():\n","                file.write(f\"{student_name},\")\n","                for subject_name, subject in student.subjects.items():\n","                    file.write(f\"{subject_name}:\")\n","                    for grade in subject.grades:\n","                        file.write(f\"{grade},\")\n","                    file.write(\"|\")\n","                file.write(\"\\n\")\n","\n","    def load_data(self, filename):\n","        if os.path.exists(filename):\n","            with open(filename, 'r') as file:\n","                for line in file:\n","                    data = line.strip().split(',')\n","                    student_name = data[0]\n","                    self.add_student(student_name)\n","                    subjects_data = data[1:]\n","                    for subject_data in subjects_data:\n","                        if subject_data:\n","                            subject_name, grades_data = subject_data.split(':')\n","                            self.add_subject_to_student(student_name, subject_name)\n","                            grades = [float(grade) for grade in grades_data.split(',') if grade]\n","                            for grade in grades:\n","                                self.add_grade_to_student(student_name, subject_name, grade)\n","            print(\"Data loaded successfully.\")\n","        else:\n","            print(\"Data file not found.\")\n","\n","    def display_student_grades(self, student_name):\n","        if student_name in self.students:\n","            student = self.students[student_name]\n","            print(f\"Grades for student '{student_name}':\")\n","            for subject_name, subject in student.subjects.items():\n","                print(f\"{subject_name}: {subject.grades}\")\n","        else:\n","            print(f\"Student '{student_name}' not found.\")\n","\n","if __name__ == \"__main__\":\n","    grade_tracker = GradeTracker()\n","\n","    # Load data from file (if exists)\n","    grade_tracker.load_data(\"student_grades.txt\")\n","\n","    while True:\n","        print(\"\\nMenu:\")\n","        print(\"1. Add Student\")\n","        print(\"2. Add Subject to Student\")\n","        print(\"3. Add Grade to Student\")\n","        print(\"4. Display Student Grades\")\n","        print(\"5. Save and Exit\")\n","\n","        choice = input(\"Enter your choice: \")\n","\n","        if choice == \"1\":\n","            student_name = input(\"Enter student name: \")\n","            grade_tracker.add_student(student_name)\n","        elif choice == \"2\":\n","            student_name = input(\"Enter student name: \")\n","            subject_name = input(\"Enter subject name: \")\n","            grade_tracker.add_subject_to_student(student_name, subject_name)\n","        elif choice == \"3\":\n","            student_name = input(\"Enter student name: \")\n","            subject_name = input(\"Enter subject name: \")\n","            grade = float(input(\"Enter grade: \"))\n","            grade_tracker.add_grade_to_student(student_name, subject_name, grade)\n","        elif choice == \"4\":\n","            student_name = input(\"Enter student name: \")\n","            grade_tracker.display_student_grades(student_name)\n","        elif choice == \"5\":\n","            grade_tracker.save_data(\"student_grades.txt\")\n","            print(\"Data saved successfully.\")\n","            break\n","        else:\n","            print(\"Invalid choice. Please try again.\")\n"],"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"M7qSRW5KyVYl","outputId":"cdf32df2-b032-47d6-ecf1-b567b2132c3f"},"execution_count":null,"outputs":[{"output_type":"stream","name":"stdout","text":["Data file not found.\n","\n","Menu:\n","1. Add Student\n","2. Add Subject to Student\n","3. Add Grade to Student\n","4. Display Student Grades\n","5. Save and Exit\n"]}]},{"cell_type":"markdown","source":["Library Management System - Coding Exercise\n","Your task is to create a simple Library Management System using Object-Oriented Programming (OOP) principles in Python. The system should have the following classes:\n","class book\n","attributes:\n","title: Title of the book\n","author: Author of the book\n","isbn: ISBN of the book\n","checked_out: Boolean indicating whether the book is checked out\n","Methods\n","init(self, title, author, isbn): Constructor to initialize the attributes\n","str(self): Returns a string representation of the book in the format \"Title by Author\"\n","class Patron\n","attributes:\n","name: Name of the patron\n","patron_id: Patron ID\n","checked_out_books: List of checked out books (initially empty)\n","Methods\n","init(self, name, patron_id): Constructor to initialize the attributes\n","str_(self): Returns the name of the patron\n","class Library\n","attributes:\n","books: List to store Book instances\n","atrons: List to store Patron instances\n","Methods\n","init(self): Constructor to initialize the lists\n","dd_book(self, book): Adds a Book instance to the list of books\n","dd_patron(self, patron): Adds a Patron instance to the list of patrons\n","heck_out(self, patron, book): Checks out a book for a patron if available\n","heck_in(self, patron, book): Checks in a book returned by a patron\n","ist_checked_out_books(self, patron): Returns a list of strings representing checked out books by a patron\n","\n"],"metadata":{"id":"_2z9NPS8ytmF"}},{"cell_type":"code","source":["class Book:\n","    def __init__(self, title, author, isbn):\n","        self.title = title\n","        self.author = author\n","        self.isbn = isbn\n","        self.checked_out = False\n","\n","    def __str__(self):\n","        return f\"{self.title} by {self.author}\"\n","\n","class Patron:\n","    def __init__(self, name, patron_id):\n","        self.name = name\n","        self.patron_id = patron_id\n","        self.checked_out_books = []\n","\n","    def __str__(self):\n","        return self.name\n","\n","class Library:\n","    def __init__(self):\n","        self.books = []\n","        self.patrons = []\n","\n","    def add_book(self, book):\n","        self.books.append(book)\n","\n","    def add_patron(self, patron):\n","        self.patrons.append(patron)\n","\n","    def check_out(self, patron, book):\n","        if book.checked_out:\n","            print(\"Book is already checked out.\")\n","        else:\n","            book.checked_out = True\n","            patron.checked_out_books.append(book)\n","\n","    def check_in(self, patron, book):\n","        if book in patron.checked_out_books:\n","            book.checked_out = False\n","            patron.checked_out_books.remove(book)\n","        else:\n","            print(\"Book is not checked out by this patron.\")\n","\n","    def list_checked_out_books(self, patron):\n","        checked_out_books = []\n","        for book in patron.checked_out_books:\n","            checked_out_books.append(str(book))\n","        return checked_out_books\n","\n","# Example usage:\n","if __name__ == \"__main__\":\n","    book1 = Book(\"Harry Potter\", \"J.K. Rowling\", \"123456789\")\n","    book2 = Book(\"The Great Gatsby\", \"F. Scott Fitzgerald\", \"987654321\")\n","\n","    patron1 = Patron(\"John\", 1)\n","    patron2 = Patron(\"Alice\", 2)\n","\n","    library = Library()\n","    library.add_book(book1)\n","    library.add_book(book2)\n","    library.add_patron(patron1)\n","    library.add_patron(patron2)\n","\n","    library.check_out(patron1, book1)\n","    library.check_out(patron2, book2)\n","\n","    print(\"Books checked out by John:\", library.list_checked_out_books(patron1))\n","    print(\"Books checked out by Alice:\", library.list_checked_out_books(patron2))\n","\n","    library.check_in(patron1, book1)\n","    print(\"Books checked out by John after returning:\", library.list_checked_out_books(patron1))\n"],"metadata":{"id":"bKv4kvYuy_WP","executionInfo":{"status":"ok","timestamp":1710098549374,"user_tz":-120,"elapsed":8,"user":{"displayName":"Sara Metawea","userId":"16002586230669284741"}},"outputId":"49cbac27-1396-4c25-e3a1-990e2f34c85e","colab":{"base_uri":"https://localhost:8080/"}},"execution_count":1,"outputs":[{"output_type":"stream","name":"stdout","text":["Books checked out by John: ['Harry Potter by J.K. Rowling']\n","Books checked out by Alice: ['The Great Gatsby by F. Scott Fitzgerald']\n","Books checked out by John after returning: []\n"]}]}]}