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

def seed_bulk_batch_2():
    print("Seeding Batch 2 (Literature, Movies, FLAT, CD, OS)...")
    
    # 6. Literature (Classic Literature)
    lit_quiz = get_quiz_for_category(get_category("Literature"))
    questions_lit = [
        ("Who wrote 'To Kill a Mockingbird'?", ["Harper Lee", "Mark Twain", "Ernest Hemingway", "F. Scott Fitzgerald"], 0),
        ("Which Shakespeare play features the characters Rosencrantz and Guildenstern?", ["Hamlet", "Macbeth", "Othello", "King Lear"], 0),
        ("What is the first name of Mr. Darcy in 'Pride and Prejudice'?", ["Fitzwilliam", "William", "Charles", "George"], 0),
        ("Who wrote the 'Iliad' and the 'Odyssey'?", ["Homer", "Virgil", "Sophocles", "Euripides"], 0),
        ("In 'Moby Dick', what is the name of the ship?", ["Pequod", "Beagle", "Discovery", "Endeavour"], 0),
        ("Who wrote 'Frankenstein'?", ["Mary Shelley", "Percy Shelley", "Lord Byron", "John Keats"], 0),
        ("What is the pen name of Samuel Clemens?", ["Mark Twain", "Lewis Carroll", "George Orwell", "Dr. Seuss"], 0),
        ("Which novel begins with the line 'It was the best of times, it was the worst of times'?", ["A Tale of Two Cities", "Great Expectations", "Oliver Twist", "David Copperfield"], 0),
        ("Who wrote 'The Odyssey'?", ["Homer", "Epicurus", "Plato", "Aristotle"], 0),
        ("Which Brontë sister wrote 'Wuthering Heights'?", ["Emily", "Charlotte", "Anne", "Maria"], 0),
        ("What is the name of the hobbit played by Elijah Wood in the movies?", ["Frodo Baggins", "Bilbo Baggins", "Samwise Gamgee", "Peregrin Took"], 0),
        ("Who wrote 'The Old Man and the Sea'?", ["Ernest Hemingway", "John Steinbeck", "William Faulkner", "Ray Bradbury"], 0),
        ("Which play by Samuel Beckett features two characters waiting for someone who never arrives?", ["Waiting for Godot", "Endgame", "Krapp's Last Tape", "Happy Days"], 0),
        ("Who wrote 'The Catcher in the Rye'?", ["J.D. Salinger", "Jack Kerouac", "Truman Capote", "Allen Ginsberg"], 0),
        ("In which century did Dante Alighieri write 'The Divine Comedy'?", ["14th Century", "12th Century", "16th Century", "10th Century"], 0),
        ("Who wrote 'Ulysses'?", ["James Joyce", "Virginia Woolf", "T.S. Eliot", "Franz Kafka"], 0),
        ("What is the real name of the author George Orwell?", ["Eric Arthur Blair", "Charles Lutwidge Dodgson", "Mary Ann Evans", "Hector Hugh Munro"], 0),
        ("Which Russian author wrote 'Crime and Punishment'?", ["Fyodor Dostoevsky", "Leo Tolstoy", "Anton Chekhov", "Vladimir Nabokov"], 0),
        ("Who wrote 'Les Misérables'?", ["Victor Hugo", "Alexandre Dumas", "Gustave Flaubert", "Honore de Balzac"], 0),
        ("What is the title of the first Harry Potter book?", ["Harry Potter and the Philosopher's Stone", "Harry Potter and the Chamber of Secrets", "Harry Potter and the Prisoner of Azkaban", "Harry Potter and the Goblet of Fire"], 0),
    ]
    for q_text, choices, idx in questions_lit:
        create_question(lit_quiz, q_text, choices, idx)

    # 7. Movies (Cinema History)
    movie_quiz = get_quiz_for_category(get_category("Movies"))
    questions_movies = [
        ("Who directed 'The Godfather'?", ["Francis Ford Coppola", "Martin Scorsese", "Steven Spielberg", "Alfred Hitchcock"], 0),
        ("Which movie won the Oscar for Best Picture in 1994?", ["Forrest Gump", "Pulp Fiction", "The Shawshank Redemption", "The Lion King"], 0),
        ("Who played the character of Neo in 'The Matrix'?", ["Keanu Reeves", "Laurence Fishburne", "Hugo Weaving", "Carrie-Anne Moss"], 0),
        ("Which director is known for the film 'Inception'?", ["Christopher Nolan", "Quentin Tarantino", "Wes Anderson", "David Fincher"], 0),
        ("Who played the lead role in 'Citizen Kane'?", ["Orson Welles", "Humphrey Bogart", "Cary Grant", "James Stewart"], 0),
        ("What was the first movie in the Marvel Cinematic Universe?", ["Iron Man", "The Incredible Hulk", "Thor", "Captain America: The First Avenger"], 0),
        ("Who directed 'Schindler's List'?", ["Steven Spielberg", "James Cameron", "Ridley Scott", "George Lucas"], 0),
        ("Which movie features the character Darth Vader?", ["Star Wars", "Star Trek", "Guardians of the Galaxy", "Blade Runner"], 0),
        ("Who played the Joker in 'The Dark Knight'?", ["Heath Ledger", "Jack Nicholson", "Joaquin Phoenix", "Mark Hamill"], 0),
        ("What is the name of the kingdom in 'The Lord of the Rings'?", ["Middle-earth", "Narnia", "Westeros", "Hogwarts"], 0),
        ("Who directed 'Psycho'?", ["Alfred Hitchcock", "Stanley Kubrick", "Orson Welles", "Roman Polanski"], 0),
        ("Which animation studio created 'Toy Story'?", ["Pixar", "DreamWorks", "Disney", "Studio Ghibli"], 0),
        ("Who played the character of Katniss Everdeen in 'The Hunger Games'?", ["Jennifer Lawrence", "Emma Watson", "Shailene Woodley", "Saoirse Ronan"], 0),
        ("Which movie features the line 'I'll be back'?", ["The Terminator", "Predator", "Total Recall", "Commando"], 0),
        ("Who directed 'Parasite' (2019)?", ["Bong Joon-ho", "Park Chan-wook", "Akira Kurosawa", "Hayao Miyazaki"], 0),
        ("What is the highest-grossing R-rated movie of all time?", ["Joker", "Deadpool", "Oppenheimer", "Logan"], 0),
        ("Who directed 'Avatar'?", ["James Cameron", "Steven Spielberg", "George Lucas", "Ridley Scott"], 0),
        ("Which movie features a character named 'Rose DeWitt Bukater'?", ["Titanic", "The Great Gatsby", "The Notebook", "Romeo + Juliet"], 0),
        ("Who played the lead in 'Pirates of the Caribbean'?", ["Johnny Depp", "Orlando Bloom", "Geoffrey Rush", "Keira Knightley"], 0),
        ("Which movie won the first-ever Academy Award for Best Animated Feature?", ["Shrek", "Monsters, Inc.", "Jimmy Neutron", "Spirit: Stallion of the Cimarron"], 0),
    ]
    for q_text, choices, idx in questions_movies:
        create_question(movie_quiz, q_text, choices, idx)

    # 8. FLAT (Formal Languages and Automata Theory)
    flat_quiz = get_quiz_for_category(get_category("FLAT"))
    questions_flat = [
        ("A language is regular if and only if it is accepted by a:", ["Finite Automaton", "Pushdown Automaton", "Turing Machine", "Linear Bounded Automaton"], 0),
        ("Which of the following is NOT a closed operation under regular languages?", ["Infinite Union", "Intersection", "Concatenation", "Kleene Star"], 0),
        ("The memory of a Pushdown Automaton is a:", ["Stack", "Queue", "Tape", "Register"], 0),
        ("Turing Machines are more powerful than PDAs because they have:", ["Infinite Tape memory", "Multiple stacks", "A scanner", "Faster processing"], 0),
        ("What is the Chomskey hierarchy level for Regular Languages?", ["Type 3", "Type 2", "Type 1", "Type 0"], 0),
        ("Which grammar generates Context-Free Languages?", ["Type 2", "Type 3", "Type 1", "Type 0"], 0),
        ("The pumping lemma for regular languages is used to prove a language is:", ["Not Regular", "Regular", "Finite", "Infinite"], 0),
        ("A DFA and an NFA are equivalent in power?", ["Yes", "No", "Only for small languages", "Depends on the alphabet"], 0),
        ("Which type of automaton is used for Context-Sensitive Languages?", ["Linear Bounded Automaton", "Finite Automaton", "PDA", "Turing Machine"], 0),
        ("The union of two Context-Free Languages is:", ["Context-Free", "Regular", "Context-Sensitive", "Recursive"], 0),
        ("What does 'NP' stand for in complexity theory?", ["Nondeterministic Polynomial time", "Non-Polynomial time", "Nearly Polynomial time", "Network Protocol"], 0),
        ("The Halting Problem is:", ["Undecidable", "Decidable", "NP-Complete", "Polynomial"], 0),
        ("Every Context-Free Grammar can be converted to:", ["Chomsky Normal Form", "Turing Machine", "Finite Automaton", "Regular Expression"], 0),
        ("Which machine is equivalent to a Type 0 grammar?", ["Turing Machine", "PDA", "Finite Automaton", "LBA"], 0),
        ("A language that can be decided by a Turing Machine is called:", ["Recursive", "Regular", "Context-Free", "Recursively Enumerable"], 0),
        ("The set of all strings over {a, b} containing an even number of a's is:", ["Regular", "Context-Free (but not regular)", "Context-Sensitive", "Non-Recursive"], 0),
        ("Which of the following problems is decidable?", ["Emptiness of a regular language", "Halting of a TM", "Equivalence of two CFGs", "Ambiguity of a CFG"], 0),
        ("A grammar is ambiguous if it has:", ["More than one left-most derivation", "No derivation", "Infinite strings", "Only one parse tree"], 0),
        ("Greibach Normal Form is a simplified version of:", ["Context-Free Grammar", "Regular Grammar", "Unrestricted Grammar", "Context-Sensitive Grammar"], 0),
        ("The power set construction is used to convert:", ["NFA to DFA", "PDA to TM", "DFA to NFA", "CFG to CNF"], 0),
    ]
    for q_text, choices, idx in questions_flat:
        create_question(flat_quiz, q_text, choices, idx)

    # 9. Compiler Design
    cd_quiz = get_quiz_for_category(get_category("Compiler Design"))
    questions_cd = [
        ("Which phase of the compiler is responsible for checking if a program follows the rules of the language grammar?", ["Syntax Analysis", "Lexical Analysis", "Semantic Analysis", "Code Generation"], 0),
        ("What is the output of the Syntax Analysis phase?", ["Parse Tree", "Tokens", "Assembly Code", "Object Code"], 0),
        ("Which tool is used for Lexical Analysis in Unix?", ["LEX", "YACC", "BISON", "GCC"], 0),
        ("A symbol table is a data structure used for:", ["Memory management and scope checking", "Error detection only", "Storing source code", "Formatting output"], 0),
        ("Left-recursion in a grammar can be problematic for which type of parser?", ["Top-down parser", "Bottom-up parser", "LR parser", "LALR parser"], 0),
        ("What is 'short-circuit evaluation' related to in compilation?", ["Logical operators", "Loops", "Function calls", "Variable declaration"], 0),
        ("Which phase of the compiler performs type checking?", ["Semantic Analysis", "Syntax Analysis", "Lexical Analysis", "Code Optimization"], 0),
        ("DAG (Directed Acyclic Graph) is often used in which phase?", ["Intermediate Code Generation", "Lexical Analysis", "Parsing", "Linking"], 0),
        ("What does LALR stand for?", ["Look-Ahead Left-to-right Right-most derivation", "Linear Algebraic Logical Representation", "Low Alt Level Recording", "None"], 0),
        ("Dead code elimination is a part of:", ["Code Optimization", "Intermediate Code Gen", "Semantic Analysis", "Loading"], 0),
        ("Which parser is also known as a Shift-Reduce parser?", ["Bottom-up parser", "Top-down parser", "Recursive Descent parser", "LL(1) parser"], 0),
        ("The process of replacing several instructions with a more efficient one is called:", ["Code Optimization", "Peep-hole Optimization", "Strength Reduction", "Constant Folding"], 0),
        ("What is an Abstract Syntax Tree (AST)?", ["A simplified Parse Tree", "A list of tokens", "A machine-code representation", "A symbol table entries"], 0),
        ("YACC is a tool used for generating:", ["Parsers", "Lexers", "Optimizers", "Linkers"], 0),
        ("Which phase produces the final executable program?", ["Linking", "Compilation", "Code Generation", "Assembly"], 0),
        ("Static checking is done during:", ["Compile-time", "Runtime", "Loading-time", "Execution-time"], 0),
        ("The input to the Code Generator is typically:", ["Intermediate Representation", "Source Code", "Tokens", "Parse Tree"], 0),
        ("Register allocation is a task of:", ["Code Generation", "Lexical Analysis", "Syntax Analysis", "Semantic Analysis"], 0),
        ("What is a three-address code?", ["An intermediate representation with at most three operands", "A machine code", "A high-level code", "A style of coding"], 0),
        ("The period during which an object is assigned memory is called its:", ["Lifetime", "Scope", "Extent", "Visibility"], 0),
    ]
    for q_text, choices, idx in questions_cd:
        create_question(cd_quiz, q_text, choices, idx)

    # 10. Operating Systems
    os_quiz = get_quiz_for_category(get_category("Operating Systems"))
    questions_os = [
        ("What is a process control block (PCB)?", ["A data structure for process information", "A part of the CPU", "A memory bank", "A user manual"], 0),
        ("Which scheduling algorithm gives each process a fixed time slice?", ["Round Robin", "FCFS", "SJF", "Priority"], 0),
        ("What is 'thrashing'?", ["High paging/swapping activity", "Deleting system files", "Fast CPU switching", "Hard drive failure"], 0),
        ("A critical section is a piece of code that:", ["Accesses shared resources", "Has many loops", "Is executed first", "Is very long"], 0),
        ("What is a 'deadlock'?", ["A state where two or more processes are waiting for each other", "A crashed program", "A slow computer", "A disconnected network"], 0),
        ("Virtual memory is typically implemented using:", ["Demand Paging", "RAM only", "Registers", "Cache"], 0),
        ("Which system call is used to wait for a child process to terminate?", ["wait()", "fork()", "exit()", "kill()"], 0),
        ("What is a semaphore used for?", ["Process synchronization", "Memory allocation", "File compression", "Network routing"], 0),
        ("The 'Kernel' is primarily responsible for:", ["Managing system resources", "Running user apps", "Designing UI", "Compiling code"], 0),
        ("What is 'context switching'?", ["Saving state of a process to switch to another", "Changing monitors", "Switching folders", "Replacing the OS"], 0)
    ]
    for q_text, choices, idx in questions_os:
        create_question(os_quiz, q_text, choices, idx)
    
    # 10. Operating Systems (Continued to 20)
    questions_os_2 = [
        ("What is the main advantage of a multi-threaded process?", ["Responsiveness and resource sharing", "Uses less memory", "No need for OS support", "Easier to debug"], 0),
        ("Which of these is a condition for deadlock?", ["Mutual Exclusion", "Process termination", "Low memory", "Fast I/O"], 0),
        ("What is a 'zombie' process?", ["A terminated process still in the process table", "A slow process", "A process that won't start", "A system process"], 0),
        ("Which architecture allows multiple CPUs to share the same memory?", ["Symmetric Multiprocessing (SMP)", "Client-Server", "Clustered", "Distributed"], 0),
        ("What is an 'interrupt'?", ["A signal indicating an event needing immediate attention", "A program error", "A user input", "A network disconnect"], 0),
        ("What is 'spooling'?", ["Managing I/O devices by storing data in a buffer", "Adding RAM", "Formatting a disk", "Installing software"], 0),
        ("Which memory management scheme avoids fragmentation?", ["Paging", "Segmentation", "Contiguous allocation", "Best-fit"], 0),
        ("What is a 'file descriptor'?", ["An integer used to identify an open file", "A file name", "A file size", "A folder icon"], 0),
        ("Which of these is a popular open-source operating system?", ["Linux", "Windows 11", "macOS", "iOS"], 0),
        ("What is the purpose of the 'Shell'?", ["An interface between user and kernel", "To protect the hardware", "To store data", "To manage power"], 0),
    ]
    for q_text, choices, idx in questions_os_2:
        create_question(os_quiz, q_text, choices, idx)

    print("Batch 2(100 questions) seeded.")

if __name__ == "__main__":
    seed_bulk_batch_2()
