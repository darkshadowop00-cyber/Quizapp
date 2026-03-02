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

def seed_bulk_batch_4():
    print("Seeding Batch 4 (CSS, JS, Software Design, Cloud, Physics)...")
    
    # 16. CSS
    css_quiz = get_quiz_for_category(get_category("CSS"))
    questions_css = [
        ("What does CSS stand for?", ["Cascading Style Sheets", "Creative Style Sheets", "Computer Style Sheets", "Colorful Style Sheets"], 0),
        ("Where in an HTML document is the correct place to refer to an external style sheet?", ["In the <head> section", "In the <body> section", "At the end of the document", "Inside the <html> tag"], 0),
        ("Which HTML tag is used to define an internal style sheet?", ["<style>", "<script>", "<css>", "<design>"], 0),
        ("Which HTML attribute is used to define inline styles?", ["style", "class", "id", "font"], 0),
        ("Which CSS property is used to change the background color?", ["background-color", "color", "bgcolor", "fill"], 0),
        ("How do you add a background color for all <h1> elements?", ["h1 {background-color: #FFFFFF;}", "all.h1 {background-color: #FFFFFF;}", "h1.all {background-color: #FFFFFF;}", "h1:bg {background-color: #FFFFFF;}"], 0),
        ("Which CSS property is used to change the text color of an element?", ["color", "text-color", "fgcolor", "font-color"], 0),
        ("Which CSS property controls the text size?", ["font-size", "text-size", "size", "font-weight"], 0),
        ("What is the correct CSS syntax for making all the <p> elements bold?", ["p {font-weight: bold;}", "p {text-size: bold;}", "p {font: bold;}", "p {weight: bold;}"], 0),
        ("How do you display hyperlinks without an underline?", ["a {text-decoration: none;}", "a {text-decoration: no-underline;}", "a {underline: none;}", "a {decoration: no-underline;}"], 0),
        ("Which property is used to change the font of an element?", ["font-family", "font-style", "font-weight", "font-type"], 0),
        ("How do you make the text bold?", ["font-weight: bold;", "font: bold;", "font-style: bold;", "text-weight: bold;"], 0),
        ("How do you display a border like this: The top border = 10px, bottom border = 5px, left border = 20px, right border = 1px?", ["border-width: 10px 1px 5px 20px;", "border-width: 10px 5px 20px 1px;", "border-width: 10px 20px 5px 1px;", "border-width: 10px 5px 1px 20px;"], 0),
        ("Which property is used to change the left margin of an element?", ["margin-left", "padding-left", "indent", "margin-left-edge"], 0),
        ("When using the padding property; are you allowed to use negative values?", ["No", "Yes", "Only if it is zero", "Only in Firefox"], 0),
        ("How do you select an element with id 'demo'?", ["#demo", ".demo", "demo", "*demo"], 0),
        ("How do you select elements with class name 'test'?", [".test", "#test", "test", "*test"], 0),
        ("How do you select all p elements inside a div element?", ["div p", "div.p", "div + p", "div > p"], 0),
        ("What is the default value of the position property?", ["static", "relative", "fixed", "absolute"], 0),
        ("How do you make a list that lists its items with squares?", ["list-style-type: square;", "list-type: square;", "type: square;", "square: true;"], 0),
    ]
    for q_text, choices, idx in questions_css:
        create_question(css_quiz, q_text, choices, idx)

    # 17. JavaScript
    js_quiz = get_quiz_for_category(get_category("JavaScript"))
    questions_js = [
        ("Inside which HTML element do we put the JavaScript?", ["<script>", "<js>", "<javascript>", "<scripting>"], 0),
        ("How do you write 'Hello World' in an alert box?", ["alert('Hello World');", "msg('Hello World');", "msgBox('Hello World');", "console.log('Hello World');"], 0),
        ("How do you create a function in JavaScript?", ["function myFunction()", "function:myFunction()", "function = myFunction()", "sub myFunction()"], 0),
        ("How do you call a function named 'myFunction'?", ["myFunction()", "call myFunction()", "call function myFunction()", "invoke myFunction()"], 0),
        ("How to write an IF statement in JavaScript?", ["if (i == 5)", "if i = 5 then", "if i == 5 then", "if i = 5"], 0),
        ("How to write an IF statement for executing some code if 'i' is NOT equal to 5?", ["if (i != 5)", "if (i <> 5)", "if i <> 5", "if i != 5 then"], 0),
        ("How does a WHILE loop start?", ["while (i <= 10)", "while i <= 10", "while (i <= 10; i++)", "while i = 1 to 10"], 0),
        ("How does a FOR loop start?", ["for (i = 0; i <= 5; i++)", "for (i <= 5; i++)", "for i = 1 to 5", "for (i = 0; i <= 5)"], 0),
        ("How can you add a comment in a JavaScript?", ["//This is a comment", "<!--This is a comment-->", "'This is a comment", "/*This is a comment*/"], 0),
        ("How do you round the number 7.25, to the nearest integer?", ["Math.round(7.25)", "rnd(7.25)", "Math.rnd(7.25)", "round(7.25)"], 0),
        ("How do you find the number with the highest value of x and y?", ["Math.max(x, y)", "Math.ceil(x, y)", "ceil(x, y)", "top(x, y)"], 0),
        ("Which event occurs when the user clicks on an HTML element?", ["onclick", "onmouseclick", "onchange", "onmouseover"], 0),
        ("How do you declare a JavaScript variable?", ["var carName;", "variable carName;", "v carName;", "dim carName;"], 0),
        ("Which operator is used to assign a value to a variable?", ["=", "*", "-", "x"], 0),
        ("What will the following code return: Boolean(10 > 9)?", ["true", "false", "NaN", "Error"], 0),
        ("Is JavaScript case-sensitive?", ["Yes", "No", "Only for variables", "Only for function names"], 0),
        ("Which keyword is used to declare a block-scope variable?", ["let", "var", "global", "dim"], 0),
        ("What is the result of '2' + 2?", ["'22'", "4", "Error", "NaN"], 0),
        ("Which method is used to remove the last element of an array?", ["pop()", "push()", "shift()", "splice()"], 0),
        ("How do you find the length of a string in JavaScript?", ["str.length", "str.size", "len(str)", "str.count"], 0),
    ]
    for q_text, choices, idx in questions_js:
        create_question(js_quiz, q_text, choices, idx)

    # 18. Software Design
    design_quiz = get_quiz_for_category(get_category("Software Design"))
    questions_design = [
        ("What does the 'L' in SOLID stand for?", ["Liskov Substitution Principle", "Layered Architecture", "Loose Coupling", "Link Principle"], 0),
        ("Which design pattern is used to notify multiple objects about state changes?", ["Observer", "Singleton", "Factory", "Decorator"], 0),
        ("What is the primary goal of 'Unit Testing'?", ["To test individual components in isolation", "To test the entire system", "To test database performance", "To test user behavior"], 0),
        ("In the MVC pattern, what does 'C' stand for?", ["Controller", "Center", "Component", "Core"], 0),
        ("What is 'refactoring'?", ["Restructuring code without changing its external behavior", "Adding new features", "Fixing bugs", "Rewriting from scratch"], 0),
        ("Which principle states that a class should have only one reason to change?", ["Single Responsibility Principle", "Open-Closed Principle", "Interface Segregation", "Dependency Inversion"], 0),
        ("What is 'dependency injection'?", ["A technique where an object receives its dependencies from outside", "Injecting data into a database", "A type of virus", "Calling a function from another file"], 0),
        ("Which design pattern provides an interface for creating objects in a superclass but allows subclasses to alter the type?", ["Factory Method", "Builder", "Abstract Factory", "Prototype"], 0),
        ("What is the 'DRY' principle?", ["Don't Repeat Yourself", "Do Repeat Yourself", "Data Retrieval Yield", "Direct Run Yearly"], 0),
        ("What is the 'KISS' principle?", ["Keep It Simple, Stupid", "Knowledge Is Super Smart", "Key Interface Simple System", "None"], 0),
        ("What is 'Technical Debt'?", ["The implied cost of future rework caused by choosing an easy solution now", "Money owed to a server provider", "Salaries for developers", "Cost of a database license"], 0),
        ("Which diagram is most commonly used to show the relationship between classes in UML?", ["Class Diagram", "Sequence Diagram", "Use Case Diagram", "State Diagram"], 0),
        ("In 'Agile' development, what is a 'Sprint'?", ["A set period of time during which specific work has to be completed", "A running race for developers", "A fast computer", "A type of bug"], 0),
        ("What is 'Coupling' in software design?", ["The degree of interdependence between software modules", "The speed of execution", "Combining two files", "Matching colors in UI"], 0),
        ("What is 'Cohesion'?", ["The degree to which the elements inside a module belong together", "The speed of the network", "Connecting to a database", "Naming variables correctly"], 0),
        ("Which pattern allows you to attach new behaviors to objects by placing these objects inside special wrapper objects?", ["Decorator", "Adapter", "Bridge", "Proxy"], 0),
        ("What is the 'Open-Closed Principle'?", ["Software entities should be open for extension but closed for modification", "Software should be open source", "Folders should be open", "Apps should be closed after use"], 0),
        ("What is a 'User Story'?", ["An informal, natural language description of features of a software system", "A full manual", "A biography of a developer", "A bug report"], 0),
        ("Which pattern ensures that a class has only one instance and provides a global point of access to it?", ["Singleton", "Prototype", "Flyweight", "Facade"], 0),
        ("What is the primary benefit of 'Microservices' architecture?", ["Scalability and independent deployment", "Easier debugging", "Uses less memory", "Runs faster"], 0),
    ]
    for q_text, choices, idx in questions_design:
        create_question(design_quiz, q_text, choices, idx)

    # 19. Cloud Computing
    cloud_quiz = get_quiz_for_category(get_category("Cloud Computing"))
    questions_cloud = [
        ("What is 'IaaS'?", ["Infrastructure as a Service", "Internet as a Service", "Instruction as a Service", "Investment as a Service"], 0),
        ("Which of the following is a key characteristic of Cloud Computing?", ["On-demand self-service", "Manual provisioning", "Fixed capacity", "Single-tenant only"], 0),
        ("What is 'PaaS'?", ["Platform as a Service", "Product as a Service", "Performance as a Service", "Program as a Service"], 0),
        ("Which cloud model is a combination of public and private clouds?", ["Hybrid Cloud", "Community Cloud", "Personal Cloud", "Multi-Cloud"], 0),
        ("What is 'SaaS'?", ["Software as a Service", "Storage as a Service", "System as a Service", "Security as a Service"], 0),
        ("Which AWS service is used for scalable object storage?", ["S3", "EC2", "RDS", "Lambda"], 0),
        ("What is 'Serverless Computing'?", ["Cloud provider manages the server infrastructure entirely", "No servers are used at all", "Servers are in space", "User must buy physical servers"], 0),
        ("Which company provides 'AWS'?", ["Amazon", "Google", "Microsoft", "Oracle"], 0),
        ("What is the primary benefit of 'Auto-scaling'?", ["To adjust resources automatically based on demand", "To make code faster", "To reduce security risks", "To backup data"], 0),
        ("In Cloud Computing, what does 'Elasticity' mean?", ["The ability to grow or shrink resources dynamically", "The speed of the network", "The cost of the service", "The number of users"], 0),
        ("Which service from Microsoft is a cloud platform?", ["Azure", "AWS", "GCP", "Salesforce"], 0),
        ("What is a 'Region' in cloud computing?", ["A physical location where data centers are grouped", "A country", "A specific server rack", "A type of database"], 0),
        ("What is an 'Availability Zone' (AZ)?", ["Isolated locations within a region to ensure high availability", "A time zone", "A public Wi-Fi area", "A backup drive"], 0),
        ("Which tool is used for containerization in cloud computing?", ["Docker", "Jenkins", "Ansible", "Terraform"], 0),
        ("What is 'Kubernetes' primarily used for?", ["Container orchestration", "Word processing", "Image editing", "Sending emails"], 0),
        ("What is 'Latency' in the context of cloud services?", ["The time delay in data transfer", "The price per month", "The size of a virtual machine", "The number of files stored"], 0),
        ("What is 'Multi-tenancy'?", ["A single instance of software runs on a server and serves multiple customers", "Many people in one house", "Using many servers for one user", "A type of billing"], 0),
        ("Which service is used for 'Content Delivery Network' (CDN) in AWS?", ["CloudFront", "Route 53", "Direct Connect", "VPC"], 0),
        ("What is the main benefit of 'Pay-as-you-go' pricing?", ["Cost efficiency and no upfront investment", "Fixed monthly costs", "Unlimited resources", "Free service forever"], 0),
        ("What is 'VPC' stand for?", ["Virtual Private Cloud", "Variable Power Control", "Visual Programming Center", "None"], 0),
    ]
    for q_text, choices, idx in questions_cloud:
        create_question(cloud_quiz, q_text, choices, idx)

    # 20. Physics
    physics_quiz = get_quiz_for_category(get_category("Physics"))
    questions_physics = [
        ("What is the unit of electric current?", ["Ampere", "Volt", "Ohm", "Watt"], 0),
        ("What is the formula for Force?", ["F = m * a", "F = m / a", "F = v * t", "F = m * g"], 0),
        ("Who is the father of observational astronomy?", ["Galileo Galilei", "Isaac Newton", "Johannes Kepler", "Edwin Hubble"], 0),
        ("What is the property of an object to resist changes in its state of motion?", ["Inertia", "Velocity", "Gravity", "Momentum"], 0),
        ("What is the SI unit of work?", ["Joule", "Watt", "Newton", "Pascal"], 0),
        ("Which lens is used to correct myopia (near-sightedness)?", ["Concave lens", "Convex lens", "Bifocal lens", "Cylindrical lens"], 0),
        ("What is the speed of sound in air (approximately)?", ["343 m/s", "300,000 km/s", "100 m/s", "1,200 m/s"], 0),
        ("What is the primary color of light that isn't red or green?", ["Blue", "Yellow", "Cyan", "Magenta"], 0),
        ("What is the acceleration due to gravity on the Moon?", ["1.62 m/s²", "9.8 m/s²", "3.7 m/s²", "0 m/s²"], 0),
        ("What is the term for the maximum displacement of a wave from its rest position?", ["Amplitude", "Wavelength", "Frequency", "Period"], 0),
        ("Which particle carries a positive charge?", ["Proton", "Electron", "Neutron", "Positron"], 0),
        ("What instrument is used to measure electric voltage?", ["Voltmeter", "Ammeter", "Ohmmeter", "Galvanometer"], 0),
        ("What is the law that states energy cannot be created or destroyed?", ["Law of Conservation of Energy", "Newton's First Law", "Law of Entropy", "Ohm's Law"], 0),
        ("What is the boing point of water in Fahrenheit?", ["212°F", "100°F", "32°F", "180°F"], 0),
        ("What type of energy is stored in a compressed spring?", ["Potential Energy", "Kinetic Energy", "Thermal Energy", "Chemical Energy"], 0),
        ("Which branch of physics deals with the behavior of light?", ["Optics", "Mechanics", "Thermodynamics", "Electromagnetism"], 0),
        ("What is the unit of frequency?", ["Hertz", "Baud", "Decibel", "Pascal"], 0),
        ("Who proposed that light is made of 'quanta' or photons?", ["Albert Einstein", "Max Planck", "Niels Bohr", "Louis de Broglie"], 0),
        ("What is the term for a material that allows electricity to flow easily through it?", ["Conductor", "Insulator", "Semiconductor", "Resistor"], 0),
        ("What is the most abundant direct evidence for the Big Bang theory?", ["Cosmic Microwave Background Radiation", "Black Holes", "Asteroids", "Sunspots"], 0),
    ]
    for q_text, choices, idx in questions_physics:
        create_question(physics_quiz, q_text, choices, idx)

    print("Batch 4(100 questions) seeded.")

if __name__ == "__main__":
    seed_bulk_batch_4()
