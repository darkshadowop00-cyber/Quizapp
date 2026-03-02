import os
import django
from django.utils.text import slugify

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quiz_project.settings')
django.setup()

from quiz.models import Category, Quiz, Question, Answer

def create_question(quiz, text, choices, correct_index):
    question, created = Question.objects.get_or_create(quiz=quiz, text=text)
    if created:
        for i, choice_text in enumerate(choices):
            Answer.objects.create(
                question=question,
                text=choice_text,
                is_correct=(i == correct_index)
            )

def get_category(name):
    return Category.objects.get(name=name)

def get_quiz_for_category(category):
    return category.quizzes.first()

def seed_bulk_batch_3():
    print("Seeding Batch 3 (DBMS, C, C++, Java, HTML)...")
    
    # 11. DBMS (Database Management)
    dbms_quiz = get_quiz_for_category(get_category("DBMS"))
    questions_dbms = [
        ("What is the primary key in a database table?", ["A unique identifier for each record", "A reference to another table", "A list of all records", "A temporary table"], 0),
        ("Which SQL command is used to retrieve data from a table?", ["SELECT", "INSERT", "UPDATE", "DELETE"], 0),
        ("What does normalization in a database accomplish?", ["Reduces data redundancy", "Increases data size", "Adds duplicate records", "Encrypts data"], 0),
        ("Which of the following is NOT an ACID property?", ["Durability", "Atomicity", "Consistency", "Integrity"], 3),
        ("What is a foreign key?", ["A column that creates a link between two tables", "A secret key", "A global variable", "A primary key in the same table"], 0),
        ("Which SQL clause is used to filter records?", ["WHERE", "GROUP BY", "ORDER BY", "HAVING"], 0),
        ("What is the difference between DELETE and TRUNCATE?", ["TRUNCATE is faster and doesn't log individual row deletions", "DELETE is faster", "They are identical", "DELETE removes the table"], 0),
        ("Which normal form handles partial dependencies?", ["2NF", "1NF", "3NF", "BCNF"], 0),
        ("What is a 'join' in SQL?", ["Combining rows from two or more tables", "Deleting two tables", "Merging two databases", "Creating a link to a file"], 0),
        ("Which SQL operator is used to search for a specified pattern in a column?", ["LIKE", "IN", "BETWEEN", "EXISTS"], 0),
        ("What is a 'view' in a database?", ["A virtual table based on a result-set", "A physical copy of a table", "A screenshot of data", "A type of index"], 0),
        ("Which statement is used to remove a table from the database?", ["DROP TABLE", "DELETE TABLE", "REMOVE TABLE", "CLEAR TABLE"], 0),
        ("What is the purpose of the 'GROUP BY' statement?", ["To arrange identical data into groups", "To sort data", "To delete duplicates", "To count records"], 0),
        ("A database 'index' is primarily used to:", ["Speed up data retrieval", "Protect data", "Resize the database", "Format data"], 0),
        ("Which integrity constraint prevents null values in a column?", ["NOT NULL", "UNIQUE", "PRIMARY KEY", "CHECK"], 0),
        ("What is the default port for PostgreSQL?", ["5432", "3306", "1521", "27017"], 0),
        ("In NoSQL, what does 'schema-less' mean?", ["Data can be stored without a fixed structure", "No data is stored", "The database is empty", "Only numbers can be stored"], 0),
        ("Which command is used to modify existing records in a table?", ["UPDATE", "MODIFY", "CHANGE", "ALTER"], 0),
        ("What is a 'Stored Procedure'?", ["A prepared SQL code that you can save and reuse", "A type of backup", "A data entry tool", "A database user"], 0),
        ("Which SQL clause is used with aggregate functions?", ["HAVING", "WHERE", "ORDER BY", "LIMIT"], 0),
    ]
    for q_text, choices, idx in questions_dbms:
        create_question(dbms_quiz, q_text, choices, idx)

    # 12. C Programming
    c_quiz = get_quiz_for_category(get_category("C Programming"))
    questions_c = [
        ("What is the entry point of every C program?", ["main()", "start()", "init()", "printf()"], 0),
        ("Which operator is used to get the address of a variable?", ["&", "*", "@", "#"], 0),
        ("How do you declare a pointer in C?", ["int *ptr;", "int &ptr;", "ptr int;", "pointer ptr;"], 0),
        ("What is the result of sizeof(int) on most modern systems?", ["4", "1", "2", "8"], 0),
        ("Which function is used to output to the console in C?", ["printf()", "cout", "print()", "write()"], 0),
        ("Which keyword is used to define a custom data type in C?", ["typedef", "struct", "class", "union"], 0),
        ("What is the purpose of '#include <stdio.h>'?", ["Includes standard I/O library", "Starts the program", "Defines integers", "Allocates memory"], 0),
        ("Which loop is guaranteed to execute at least once?", ["do-while", "for", "while", "None"], 0),
        ("What does 'malloc' return on failure?", ["NULL", "0", "A random pointer", "-1"], 0),
        ("How do you end a string in C?", ["\\0 (null terminator)", ";", ".", "\\n"], 0),
        ("What is a 'segmentation fault'?", ["Accessing a restricted memory area", "A mathematical error", "A missing semicolon", "A slow loop"], 0),
        ("Which operator is used to access members of a structure using a pointer?", ["->", ".", ":", "::"], 0),
        ("What is the keyword 'static' used for in a function?", ["To persist variable value across calls", "To make it faster", "To allow global access", "To prevent recursion"], 0),
        ("What is a 'union' in C?", ["Memory shared by multiple members of different types", "A group of countries", "A type of loop", "A function library"], 0),
        ("Which function is used to free dynamically allocated memory?", ["free()", "delete()", "clear()", "remove()"], 0),
        ("How do you define a macro in C?", ["#define", "macro", "const", "final"], 0),
        ("What is the result of 10 / 3 in integer division in C?", ["3", "3.33", "4", "0"], 0),
        ("Which data type is used to store high precision floating point numbers?", ["double", "float", "int", "char"], 0),
        ("What char code corresponds to 'A' in ASCII?", ["65", "97", "48", "100"], 0),
        ("Which operator is used for the logical AND operation in C?", ["&&", "||", "!", "&"], 0),
    ]
    for q_text, choices, idx in questions_c:
        create_question(c_quiz, q_text, choices, idx)

    # 13. C++ Programming
    cpp_quiz = get_quiz_for_category(get_category("C++ Programming"))
    questions_cpp = [
        ("Which of the following is NOT an OOP concept in C++?", ["Pointers", "Encapsulation", "Polymorphism", "Inheritance"], 0),
        ("What keyword is used to create a class in C++?", ["class", "struct", "object", "type"], 0),
        ("Which operator is used for input in C++?", [">>", "<<", ">", "<"], 0),
        ("What is a 'constructor'?", ["A special member function called on object creation", "A tool to compile code", "A memory manager", "A style guide"], 0),
        ("Which keyword is used for runtime polymorphism?", ["virtual", "static", "friend", "this"], 0),
        ("What is the difference between a class and a struct in C++?", ["Default visibility is private in class, public in struct", "Classes are faster", "Structs cannot have methods", "They are identical"], 0),
        ("Which keyword is used to handle exceptions in C++?", ["try/catch", "throw/catch", "error/handle", "if/else"], 0),
        ("What is 'encapsulation'?", ["Grouping data and methods together and hiding details", "Storing data on disk", "Using multiple CPUs", "Inheriting from a parent"], 0),
        ("Which operator is used as the scope resolution operator?", ["::", ".", "->", ":"], 0),
        ("What does 'STL' stand for in C++?", ["Standard Template Library", "Static Type Logic", "Simple Tool Library", "Structured Theory List"], 0),
        ("What is a 'destructor'?", ["A function called when an object is destroyed", "A virus", "A tool to delete files", "A type of loop"], 0),
        ("Which keyword allows a non-member function access to private members?", ["friend", "public", "protected", "private"], 0),
        ("How do you declare inheritance in C++?", [":", "extends", "implements", "from"], 0),
        ("What is the purpose of the 'this' pointer?", ["Points to the current object", "Points to the parent class", "Points to the main function", "Points to NULL"], 0)
    ]
    for q_text, choices, idx in questions_cpp:
        create_question(cpp_quiz, q_text, choices, idx)
    
    # 13. C++ Continued
    questions_cpp_2 = [
        ("What is a 'template' in C++?", ["A blueprint for creating generic classes/functions", "A UI theme", "A code comment", "A database schema"], 0),
        ("Which of these is used to dynamically allocate memory in C++?", ["new", "malloc", "alloc", "create"], 0),
        ("What is 'multiple inheritance'?", ["A class inheriting from more than one parent", "Two classes having the same name", "Multiple objects of one class", "A class with many methods"], 0),
        ("Which header is required for using string objects in C++?", ["<string>", "<iostream>", "<stdio.h>", "<math.h>"], 0),
        ("What is a 'pure virtual function'?", ["A function with =0 that makes a class abstract", "A function that is very fast", "A function with no code", "A function in the main file"], 0),
        ("The 'endl' manipulator is used to:", ["Insert a newline and flush the stream", "End the program", "Clear the screen", "Format numbers"], 0),
    ]
    for q_text, choices, idx in questions_cpp_2:
        create_question(cpp_quiz, q_text, choices, idx)

    # 14. Java Programming
    java_quiz = get_quiz_for_category(get_category("Java Programming"))
    questions_java = [
        ("Is Java platform-independent?", ["Yes, via bytecode and JVM", "No, it only runs on Windows", "Only for web applications", "Only on Linux"], 0),
        ("Which keyword is used to inherit a class in Java?", ["extends", "implements", "inherits", "import"], 0),
        ("What is the purpose of the 'final' keyword for a variable?", ["Makes it a constant", "Makes it static", "Allows multiple values", "Prevents deletion"], 0),
        ("Which component is responsible for automated memory management in Java?", ["Garbage Collector", "JVM", "JRE", "Compiler"], 0),
        ("Which of these is NOT a primitive data type in Java?", ["String", "int", "boolean", "char"], 0),
        ("What is the default value of an uninitialized boolean variable?", ["false", "true", "null", "0"], 0),
        ("Which keyword is used to refer to the current object?", ["this", "super", "self", "me"], 0),
        ("How many public classes can a single Java file have?", ["One", "Unlimited", "Zero", "Must match file name"], 0),
        ("Which package contains the Scanner class for user input?", ["java.util", "java.lang", "java.io", "java.net"], 0),
        ("What is an 'Interface' in Java?", ["A collection of abstract methods", "A GUI window", "A type of variable", "A database link"], 0),
        ("Which keyword is used to refer to a parent class?", ["super", "this", "parent", "base"], 0),
        ("Can a constructor be overloaded in Java?", ["Yes", "No", "Only if it is public", "Only in interfaces"], 0),
        ("What is the purpose of 'static' in a method declaration?", ["It belongs to the class rather than an instance", "It makes the method faster", "It prevents overriding", "It allows private access"], 0),
        ("What is a 'thread' in Java?", ["A lightweight unit of execution", "A string of characters", "A memory block", "A network connection"], 0),
        ("Which keyword is used to catch an exception?", ["catch", "try", "throw", "handle"], 0),
        ("What is the root class of all Java classes?", ["Object", "Class", "System", "Root"], 0),
        ("Which method is used to get the length of a String in Java?", ["length()", "size()", "count()", "len()"], 0),
        ("What does JVM stand for?", ["Java Virtual Machine", "Java Variable Manager", "Joined Visual Method", "None"], 0),
        ("Which access modifier makes a member accessible only within its own class?", ["private", "public", "protected", "default"], 0),
        ("What is an 'ArrayList' in Java?", ["A resizable array implementation", "A fixed-size list", "A type of database", "A mathematical function"], 0),
    ]
    for q_text, choices, idx in questions_java:
        create_question(java_quiz, q_text, choices, idx)

    # 15. HTML
    html_quiz = get_quiz_for_category(get_category("HTML"))
    questions_html = [
        ("What does HTML stand for?", ["HyperText Markup Language", "Hyperlink Text Mark Language", "Home Tool Markup Language", "Hyper Transfer Main Language"], 0),
        ("Which tag is used for the smallest heading?", ["<h6>", "<h1>", "<h7>", "<small>"], 0),
        ("Which attribute is used to define an image's source?", ["src", "href", "link", "url"], 0),
        ("What is the correct tag for a line break?", ["<br>", "<lb>", "<break>", "<hr>"], 0),
        ("How do you create a hyperlink in HTML?", ["<a href='url'>Link</a>", "<a>url</a>", "<link src='url'>", "<url='url'>"], 0),
        ("Which tag is used to create an ordered list?", ["<ol>", "<ul>", "<li>", "<dl>"], 0),
        ("Which HTML element is used for the page's main content?", ["<main>", "<body>", "<content>", "<div>"], 0),
        ("How do you add a comment in HTML?", ["<!-- comment -->", "// comment", "/* comment */", "# comment"], 0),
        ("Which tag defines a table row?", ["<tr>", "<td>", "<th>", "<row>"], 0),
        ("What is the correct tag for the title of the document?", ["<title>", "<head>", "<header>", "<meta>"], 0),
        ("Which HTML5 element is used to play audio files?", ["<audio>", "<sound>", "<play>", "<music>"], 0),
        ("What is the purpose of the 'alt' attribute in an <img> tag?", ["Provides alternative text if the image fails to load", "Sets the alignment", "Sets the transparency", "Adds a border"], 0),
        ("Which tag is used for a dropdown list?", ["<select>", "<list>", "<dropdown>", "<input>"], 0),
        ("How do you define important text in HTML?", ["<strong>", "<b>", "<important>", "<i>"], 0),
        ("What is the default value of the target attribute in an <a> tag?", ["_self", "_blank", "_parent", "_top"], 0),
        ("Which element is used to group related elements in a form?", ["<fieldset>", "<group>", "<section>", "<div class='form'>"], 0),
        ("What is the purpose of the <!DOCTYPE html> declaration?", ["Tells the browser to use HTML5", "Starts the head section", "Defines the language", "Adds a style script"], 0),
        ("Which tag is used to embed an external webpage?", ["<iframe>", "<frame>", "<window>", "<embed>"], 0),
        ("Which element is used to display a scalar measurement within a known range?", ["<meter>", "<progress>", "<gauge>", "<range>"], 0),
        ("What is the correct tag for a footer?", ["<footer>", "<bottom>", "<end>", "<section id='footer'>"], 0),
    ]
    for q_text, choices, idx in questions_html:
        create_question(html_quiz, q_text, choices, idx)

    print("Batch 3(100 questions) seeded.")

if __name__ == "__main__":
    seed_bulk_batch_3()
