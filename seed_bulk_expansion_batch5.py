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

def seed_bulk_batch_5():
    print("Seeding Batch 5 (Chemistry, ML, GATE, Grammar, Sports)...")
    
    # 21. Chemistry
    chem_quiz = get_quiz_for_category(get_category("Chemistry"))
    questions_chem = [
        ("What is the chemical symbol for Silver?", ["Ag", "Au", "Si", "Sl"], 0),
        ("What is the most abundant gas in the atmosphere of Mars?", ["Carbon Dioxide", "Nitrogen", "Oxygen", "Argon"], 0),
        ("Which element has the symbol 'Fe'?", ["Iron", "Fluorine", "Francium", "Fermium"], 0),
        ("What is the pH level of a neutral substance?", ["7", "0", "14", "1"], 0),
        ("Which gas is produced when an acid reacts with a metal?", ["Hydrogen", "Oxygen", "Carbon Dioxide", "Nitrogen"], 0),
        ("What is the chemical formula for water?", ["H2O", "HO2", "H2O2", "OH"], 0),
        ("Who discovered the electron?", ["J.J. Thomson", "Ernest Rutherford", "John Dalton", "James Chadwick"], 0),
        ("What is the atomic weight of Carbon approximately?", ["12", "1", "14", "16"], 0),
        ("Which noble gas is used in light bulbs to prevent the filament from burning?", ["Argon", "Helium", "Neon", "Xenon"], 0),
        ("What is the main acid in the human stomach?", ["Hydrochloric acid", "Sulfuric acid", "Nitric acid", "Acetic acid"], 0),
        ("Which element is the most electronegative?", ["Fluorine", "Oxygen", "Chlorine", "Nitrogen"], 0),
        ("What is the term for a reaction that releases heat?", ["Exothermic", "Endothermic", "Isothermic", "Adiabatic"], 0),
        ("What is the chemical formula for Ammonia?", ["NH3", "NO2", "CH4", "NaCl"], 0),
        ("What type of bond involves the transfer of electrons?", ["Ionic bond", "Covalent bond", "Metallic bond", "Hydrogen bond"], 0),
        ("Which metal is the best conductor of electricity?", ["Silver", "Copper", "Gold", "Aluminum"], 0),
        ("What is dry ice?", ["Solid Carbon Dioxide", "Solid Hydrogen", "Frozen Oxygen", "Nitrogen ice"], 0),
        ("What is the most abundant metal in the Earth's crust?", ["Aluminum", "Iron", "Gold", "Magnesium"], 0),
        ("What is the process of a liquid changing into a solid?", ["Freezing", "Melting", "Boiling", "Sublimation"], 0),
        ("What is the name of the vertical columns in the periodic table?", ["Groups", "Periods", "Blocks", "Families"], 0),
        ("Which element is known as the 'King of Chemicals'?", ["Sulfuric Acid", "Hydrochloric Acid", "Sodium Hydroxide", "Ammonia"], 0),
    ]
    for q_text, choices, idx in questions_chem:
        create_question(chem_quiz, q_text, choices, idx)

    # 22. Machine Learning
    ml_quiz = get_quiz_for_category(get_category("Machine Learning"))
    questions_ml = [
        ("What is the term for a single layer of neurons in a neural network?", ["Hidden Layer", "Input Node", "Neuron String", "Connection Layer"], 0),
        ("Which algorithm is an example of Unsupervised Learning?", ["K-Means Clustering", "Linear Regression", "Decision Tree", "Support Vector Machine"], 0),
        ("What is the purpose of a 'Training Set'?", ["To train the model to recognize patterns", "To evaluate final performance", "To clean the data", "To store results"], 0),
        ("What does 'SVM' stand for?", ["Support Vector Machine", "Super Vector Model", "Simple Variable Method", "None"], 0),
        ("In ML, what is 'Bias'?", ["The error from erroneous assumptions in the learning algorithm", "Personal opinion", "Data size", "Speed of training"], 0),
        ("Which activation function outputs a value between 0 and 1?", ["Sigmoid", "ReLU", "Tanh", "Leaky ReLU"], 0),
        ("What is 'Deep Learning'?", ["Machine learning based on artificial neural networks with multiple layers", "Learning from books", "Advanced SQL", "Robotics"], 0),
        ("What is the goal of 'Gradient Descent'?", ["To minimize the cost function", "To maximize accuracy", "To shuffle the data", "To increase learning rate"], 0),
        ("What is 'Feature Engineering'?", ["The process of selecting and transforming variables for a model", "Building hardware for AI", "Coding in Python", "Managing servers"], 0),
        ("Which of these is a popular library for data manipulation in Python?", ["Pandas", "Scikit-Learn", "TensorFlow", "Keras"], 0),
        ("What is 'Cross-Validation'?", ["A technique for assessing how the results of a statistical analysis will generalize", "Comparing two models", "Validating user input", "Checking for security bugs"], 0),
        ("What is the problem where the model is too simple to capture the underlying trend?", ["Underfitting", "Overfitting", "Bias", "Noise"], 0),
        ("Which type of ML is used in self-driving cars for decision making?", ["Reinforcement Learning", "Supervised Learning", "Unsupervised Learning", "Static Learning"], 0),
        ("What is the 'Softmax' function used for?", ["To turn a vector of numbers into a vector of probabilities", "To round numbers", "To delete data", "To increase speed"], 0),
        ("In a Decision Tree, what is an 'Entropy' a measure of?", ["Impurity or randomness", "The height of the tree", "The number of nodes", "The accuracy"], 0),
        ("What is 'Regularization' used for?", ["To prevent overfitting by adding a penalty to the loss function", "To format data", "To speed up training", "To increase memory use"], 0),
        ("Which neural network architecture is commonly used for sequential data like text?", ["RNN (Recurrent Neural Network)", "CNN", "MLP", "GCN"], 0),
        ("What is 'Data Augmentation'?", ["Technique to increase data diversity without collecting new data", "Buying more servers", "Using a bigger database", "Cleaning the data"], 0),
        ("Who is the lead developer of TensorFlow?", ["Google", "Facebook", "Microsoft", "OpenAI"], 0),
        ("What is a 'Perceptron'?", ["The simplest type of artificial neural network", "A type of database", "A hardware processor", "A data cleaning tool"], 0),
    ]
    for q_text, choices, idx in questions_ml:
        create_question(ml_quiz, q_text, choices, idx)

    # 23. GATE (Preparation)
    gate_quiz = get_quiz_for_category(get_category("GATE"))
    questions_gate = [
        ("What is the derivative of sin(x)?", ["cos(x)", "-cos(x)", "tan(x)", "sec^2(x)"], 0),
        ("If a matrix A is skew-symmetric, then A^T is equal to:", ["-A", "A", "I", "0"], 0),
        ("The probability of an impossible event is:", ["0", "1", "0.5", "Undefined"], 0),
        ("What is the value of log(1)?", ["0", "1", "e", "10"], 0),
        ("In Computer Science, what does 'HTTP' stand for?", ["Hypertext Transfer Protocol", "Hyperlink Text Tuning Process", "Home Tool Timing Protocol", "None"], 0),
        ("What is the integral of 1/x?", ["ln(x)", "x^2/2", "-1/x^2", "x"], 0),
        ("Which gate is known as the 'Universal Gate'?", ["NAND", "OR", "AND", "XOR"], 0),
        ("In Boolean Algebra, A + A' = ", ["1", "0", "A", "A'"], 0),
        ("What is the complexity of Bubble Sort in the worst case?", ["O(n^2)", "O(n)", "O(log n)", "O(n log n)"], 0),
        ("Which of these is a volatile memory?", ["RAM", "ROM", "Flash", "Disk"], 0),
        ("What is the base of the Hexadecimal number system?", ["16", "10", "8", "2"], 0),
        ("The binary equivalent of decimal 10 is:", ["1010", "1001", "1100", "0110"], 0),
        ("Which theorem is used to find the maximum possible power transfer to a load?", ["Maximum Power Transfer Theorem", "Thevenin's Theorem", "Norton's Theorem", "Superposition Theorem"], 0),
        ("What is the output of an AND gate if both inputs are 1?", ["1", "0", "A", "B"], 0),
        ("In C, which data type is used for storing characters?", ["char", "int", "float", "String"], 0),
        ("What is the sum of the first 10 natural numbers?", ["55", "50", "45", "10"], 0),
        ("Which of these is a valid IP address?", ["192.168.1.1", "256.0.0.1", "1.2.3", "192.168.1"], 0),
        ("What is the square root of 625?", ["25", "15", "35", "20"], 0),
        ("Which layer in the OSI model is responsible for routing?", ["Network Layer", "Data Link Layer", "Transport Layer", "Physical Layer"], 0),
        ("What is the value of pi (up to 2 decimal places)?", ["3.14", "3.12", "3.16", "3.18"], 0),
    ]
    for q_text, choices, idx in questions_gate:
        create_question(gate_quiz, q_text, choices, idx)

    # 24. Basic Grammar
    grammar_quiz = get_quiz_for_category(get_category("Basic Grammar"))
    questions_grammar = [
        ("Which of these is a verb?", ["Dance", "Table", "Quickly", "Yellow"], 0),
        ("Identify the conjunction: 'I like coffee and tea.'", ["and", "I", "like", "tea"], 0),
        ("Choose the correct word: 'The ___ is shining brightly.'", ["sun", "son", "soon", "sin"], 0),
        ("What is the opposite of 'Beautiful'?", ["Ugly", "Pretty", "Smart", "Tall"], 0),
        ("Which sentence is correct?", ["He does not like apples.", "He do not like apples.", "He not like apples.", "He doing not like apples."], 0),
        ("What is the past tense of 'Drink'?", ["Drank", "Drunk", "Drinks", "Drinking"], 0),
        ("Identify the adjective: 'The big dog barked.'", ["big", "dog", "barked", "the"], 0),
        ("Choose the plural for 'Fish':", ["Fish", "Fishes", "Fishs", "Fisher"], 0),
        ("Which is a synonym for 'Small'?", ["Little", "Large", "Long", "Fast"], 0),
        ("What is a 'Pronoun'?", ["A word that replaces a noun", "An action word", "A naming word", "A joining word"], 0),
        ("Identify the article: 'Could you pass me an apple?'", ["an", "me", "pass", "you"], 0),
        ("Choose the correct tense: 'They ___ playing football now.'", ["are", "is", "am", "was"], 0),
        ("Which of these is a proper noun?", ["London", "City", "Country", "Street"], 0),
        ("What is the comparative form of 'Good'?", ["Better", "Best", "Gooder", "More good"], 0),
        ("Choose the correct spelling:", ["Necessary", "Necesary", "Neccesary", "Necassary"], 0),
        ("Identify the subject: 'The teacher praised the students.'", ["The teacher", "Praised", "The students", "Teacher"], 0),
        ("What is the superlative form of 'Tall'?", ["Tallest", "Taller", "Tall", "Most tall"], 0),
        ("Which of these is an interjection?", ["Wow!", "The", "Quickly", "Run"], 0),
        ("Choose the correct preposition: 'She is interested ___ music.'", ["in", "on", "at", "with"], 0),
        ("What is the plural of 'Mouse'?", ["Mice", "Mouses", "Mices", "Mouse"], 0),
    ]
    for q_text, choices, idx in questions_grammar:
        create_question(grammar_quiz, q_text, choices, idx)

    # 25. Sports
    sports_quiz = get_quiz_for_category(get_category("Sports"))
    questions_sports = [
        ("Which country has won the most FIFA World Cups?", ["Brazil", "Germany", "Italy", "Argentina"], 0),
        ("How many players are on a basketball team on the court at one time?", ["5", "6", "11", "7"], 0),
        ("In which sport would you use a 'shuttlecock'?", ["Badminton", "Tennis", "Table Tennis", "Squash"], 0),
        ("Who is known as 'The Greatest' in boxing?", ["Muhammad Ali", "Mike Tyson", "Floyd Mayweather", "Joe Louis"], 0),
        ("How long is a marathon in kilometers?", ["42.195 km", "21 km", "10 km", "50 km"], 0),
        ("Which grand slam tournament is played on grass?", ["Wimbledon", "French Open", "US Open", "Australian Open"], 0),
        ("What is the highest possible score in a single frame of ten-pin bowling?", ["30", "10", "100", "50"], 0),
        ("Which city hosted the first modern Olympic Games in 1896?", ["Athens", "Paris", "London", "Rome"], 0),
        ("Who holds the world record for the 100m sprint?", ["Usain Bolt", "Tyson Gay", "Yohan Blake", "Carl Lewis"], 0),
        ("What is the national sport of Japan?", ["Sumo Wrestling", "Judo", "Baseball", "Karate"], 0),
        ("Which sport is played at 'The Masters' tournament?", ["Golf", "Tennis", "Cricket", "Polo"], 0),
        ("How many rings are on the Olympic flag?", ["5", "3", "6", "4"], 0),
        ("In which year did the FIFA World Cup start?", ["1930", "1950", "1900", "1945"], 0),
        ("Who has won the most Olympic gold medals ever?", ["Michael Phelps", "Usain Bolt", "Mark Spitz", "Carl Lewis"], 0),
        ("What is the nickname of the New Zealand national rugby team?", ["All Blacks", "Springboks", "Wallabies", "Pumas"], 0),
        ("Which sport features terms like 'Eagle', 'Birdie', and 'Bogey'?", ["Golf", "Cricket", "Tennis", "Hockey"], 0),
        ("What is the diameter of a standard basketball hoop in inches?", ["18 inches", "15 inches", "20 inches", "12 inches"], 0),
        ("How many players are on a cricket field (fielding side) at once?", ["11", "10", "12", "15"], 0),
        ("Which country won the first-ever Cricket World Cup in 1975?", ["West Indies", "Australia", "England", "India"], 0),
        ("Which sport uses the term 'Love' to mean a score of zero?", ["Tennis", "Badminton", "Volleyball", "Rugby"], 0),
    ]
    for q_text, choices, idx in questions_sports:
        create_question(sports_quiz, q_text, choices, idx)

    print("Batch 5(100 questions) seeded.")

if __name__ == "__main__":
    seed_bulk_batch_5()
