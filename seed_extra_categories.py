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

def get_category(name, slug_str=None):
    if not slug_str:
        slug_str = slugify(name)
    category, _ = Category.objects.update_or_create(
        name=name,
        defaults={'slug': slug_str}
    )
    return category

def get_quiz(title, description, category, slug_str=None):
    if not slug_str:
        slug_str = slugify(title)
    quiz, _ = Quiz.objects.update_or_create(
        title=title,
        category=category,
        defaults={'description': description, 'slug': slug_str}
    )
    return quiz

def seed_extra_data():
    print("Seeding extra categories and questions...")
    
    # --- Categories ---
    physics_cat = get_category("Physics")
    chemistry_cat = get_category("Chemistry")
    ml_cat = get_category("Machine Learning")
    gate_cat = get_category("GATE")
    grammar_cat = get_category("Basic Grammar")

    # --- Physics Quiz ---
    physics_quiz = get_quiz("Physics Fundamentals", "Test your knowledge of classical and modern physics.", physics_cat)
    create_question(physics_quiz, "What is the unit of force in the SI system?", ["Newton", "Joule", "Watt", "Pascal"], 0)
    create_question(physics_quiz, "What is the speed of light in a vacuum?", ["299,792,458 m/s", "150,000,000 m/s", "3,000,000 m/s", "343 m/s"], 0)
    create_question(physics_quiz, "Who developed the theory of General Relativity?", ["Albert Einstein", "Isaac Newton", "Niels Bohr", "Stephen Hawking"], 0)
    create_question(physics_quiz, "What is the first law of thermodynamics?", ["Conservation of energy", "Entropy increases", "Absolute zero", "Action-reaction"], 0)
    create_question(physics_quiz, "Which particle has a negative electric charge?", ["Electron", "Proton", "Neutron", "Photon"], 0)
    create_question(physics_quiz, "What is the acceleration due to gravity on Earth (approximately)?", ["9.8 m/s²", "5.5 m/s²", "12.0 m/s²", "1.6 m/s²"], 0)
    create_question(physics_quiz, "What is the primary source of energy for the Earth?", ["The Sun", "Wind", "Nuclear Fission", "The Moon"], 0)
    create_question(physics_quiz, "Which law states that for every action there is an equal and opposite reaction?", ["Newton's Third Law", "Newton's First Law", "Ohm's Law", "Kepler's Law"], 0)
    create_question(physics_quiz, "What is the process of a solid turning directly into a gas?", ["Sublimation", "Evaporation", "Condensation", "Melting"], 0)
    create_question(physics_quiz, "Who is known for the uncertainty principle?", ["Werner Heisenberg", "Max Planck", "Marie Curie", "Richard Feynman"], 0)
    create_question(physics_quiz, "What does an ammeter measure?", ["Electric current", "Voltage", "Resistance", "Power"], 0)
    create_question(physics_quiz, "What is the study of sound called?", ["Acoustics", "Optics", "Thermodynamics", "Kinematics"], 0)
    create_question(physics_quiz, "Which color of light has the longest wavelength?", ["Red", "Violet", "Blue", "Green"], 0)
    create_question(physics_quiz, "What is the most abundant element in the universe?", ["Hydrogen", "Helium", "Oxygen", "Carbon"], 0)
    create_question(physics_quiz, "What instrument is used to measure atmospheric pressure?", ["Barometer", "Thermometer", "Hygrometer", "Anemometer"], 0)

    # --- Chemistry Quiz ---
    chem_quiz = get_quiz("Chemistry Basics", "Explore elements, reactions, and the periodic table.", chemistry_cat)
    create_question(chem_quiz, "What is the chemical symbol for gold?", ["Au", "Ag", "Fe", "Pb"], 0)
    create_question(chem_quiz, "What is the atomic number of Hydrogen?", ["1", "2", "6", "8"], 0)
    create_question(chem_quiz, "Which gas is most abundant in the Earth's atmosphere?", ["Nitrogen", "Oxygen", "Carbon Dioxide", "Argon"], 0)
    create_question(chem_quiz, "What is the pH of pure water?", ["7", "0", "14", "5"], 0)
    create_question(chem_quiz, "Who is considered the father of modern chemistry?", ["Antoine Lavoisier", "Dmitri Mendeleev", "John Dalton", "Robert Boyle"], 0)
    create_question(chem_quiz, "What is the chemical formula for common table salt?", ["NaCl", "KCl", "MgCl2", "CaCl2"], 0)
    create_question(chem_quiz, "Which element is found in all organic compounds?", ["Carbon", "Oxygen", "Nitrogen", "Sulfur"], 0)
    create_question(chem_quiz, "What type of bond involves the sharing of electron pairs?", ["Covalent bond", "Ionic bond", "Hydrogen bond", "Metallic bond"], 0)
    create_question(chem_quiz, "What is the lightest element in the periodic table?", ["Hydrogen", "Helium", "Lithium", "Oxygen"], 0)
    create_question(chem_quiz, "Which substance is known as the 'universal solvent'?", ["Water", "Alcohol", "Acetone", "Benzene"], 0)
    create_question(chem_quiz, "What is the chemical formula for methane?", ["CH4", "C2H6", "NH3", "CO2"], 0)
    create_question(chem_quiz, "Which transition metal is liquid at room temperature?", ["Mercury", "Gallium", "Cesium", "Bromine"], 0)
    create_question(chem_quiz, "What process involves a gas turning into a liquid?", ["Condensation", "Evaporation", "Freezing", "Boiling"], 0)
    create_question(chem_quiz, "What is the main component of natural gas?", ["Methane", "Propane", "Butane", "Ethane"], 0)
    create_question(chem_quiz, "Which acid is found in lemons?", ["Citric acid", "Acetic acid", "Hydrochloric acid", "Sulfuric acid"], 0)

    # --- Machine Learning Quiz ---
    ml_quiz = get_quiz("Machine Learning & AI", "Test your knowledge of ML algorithms and concepts.", ml_cat)
    create_question(ml_quiz, "What type of learning involves training on labeled data?", ["Supervised Learning", "Unsupervised Learning", "Reinforcement Learning", "Deep Learning"], 0)
    create_question(ml_quiz, "Which algorithm is commonly used for classification tasks?", ["Random Forest", "Linear Regression", "K-Means", "PCA"], 0)
    create_question(ml_quiz, "What does 'ReLU' stand for in neural networks?", ["Rectified Linear Unit", "Relative Linear Unit", "Rectified Logistic Unit", "Recursive Linear Unit"], 0)
    create_question(ml_quiz, "What is the problem where a model performs well on training data but poorly on test data?", ["Overfitting", "Underfitting", "Bias", "Variance"], 0)
    create_question(ml_quiz, "In K-Means clustering, what does 'K' represent?", ["Number of clusters", "Number of iterations", "Number of features", "Constant factor"], 0)
    create_question(ml_quiz, "Which technique is used to reduce the dimensionality of data?", ["PCA", "CNN", "RNN", "Gradient Descent"], 0)
    create_question(ml_quiz, "What is the most common loss function for binary classification?", ["Cross-Entropy", "Mean Squared Error", "Absolute Error", "Hinge Loss"], 0)
    create_question(ml_quiz, "Which type of neural network is best suited for image processing?", ["CNN", "RNN", "MLP", "Transformer"], 0)
    create_question(ml_quiz, "What is the term for the process of tuning hyperparameters?", ["Hyperparameter Optimization", "Normalization", "Regularization", "Feature Engineering"], 0)
    create_question(ml_quiz, "Who is often called the 'Father of Artificial Intelligence'?", ["John McCarthy", "Alan Turing", "Geoffrey Hinton", "Andrew Ng"], 0)
    create_question(ml_quiz, "What does 'NLP' stand for?", ["Natural Language Processing", "Neural Logic Programming", "New Layer Pattern", "Non-Linear Programming"], 0)
    create_question(ml_quiz, "Which library is most popular for Deep Learning in Python?", ["PyTorch", "Pandas", "Matplotlib", "BeautifulSoup"], 0)
    create_question(ml_quiz, "What is the 'Bias-Variance' tradeoff?", ["Balanced model complexity", "Training vs Testing error", "Speed vs Accuracy", "Data size vs Memory"], 0)
    create_question(ml_quiz, "Which algorithm uses 'Backpropagation'?", ["Neural Networks", "Decision Trees", "SVM", "K-Nearest Neighbors"], 0)
    create_question(ml_quiz, "What is an ensemble method?", ["Combining multiple models", "Using a single large model", "Data cleaning technique", "Feature scaling"], 0)

    # --- GATE Quiz ---
    gate_quiz = get_quiz("GATE Preperation", "General Aptitude and Engineering basics for GATE.", gate_cat)
    create_question(gate_quiz, "If the sum of two numbers is 20 and their difference is 4, what is the larger number?", ["12", "10", "14", "16"], 0)
    create_question(gate_quiz, "What is the probability of getting a sum of 7 when two fair dice are rolled?", ["1/6", "1/12", "1/4", "5/36"], 0)
    create_question(gate_quiz, "Which of the following is equivalent to (A and B)' in Boolean algebra?", ["A' or B'", "A' and B'", "A or B", "A xor B"], 0)
    create_question(gate_quiz, "What is the eigenvalue of an identity matrix?", ["1", "0", "-1", "Depends on size"], 0)
    create_question(gate_quiz, "What is the derivative of e^x?", ["e^x", "x*e^(x-1)", "ln(x)", "1/x"], 0)
    create_question(gate_quiz, "In a graph, a circuit that visits every vertex exactly once is called:", ["Hamiltonian circuit", "Eulerian circuit", "Spanning tree", "Bipartite graph"], 0)
    create_question(gate_quiz, "What is the rank of a 3x3 matrix whose determinant is non-zero?", ["3", "2", "1", "0"], 0)
    create_question(gate_quiz, "What is the Laplace transform of a unit step function u(t)?", ["1/s", "1/s^2", "s", "1"], 0)
    create_question(gate_quiz, "Which data structure uses the LIFO principle?", ["Stack", "Queue", "Linked List", "Tree"], 0)
    create_question(gate_quiz, "What is the time complexity of binary search?", ["O(log n)", "O(n)", "O(n log n)", "O(1)"], 0)
    create_question(gate_quiz, "What is the value of i^2 in complex numbers?", ["-1", "1", "0", "i"], 0)
    create_question(gate_quiz, "How many edges does a complete graph with 5 vertices have?", ["10", "5", "15", "20"], 0)
    create_question(gate_quiz, "A square matrix A is orthogonal if:", ["A * A^T = I", "A = A^T", "det(A) = 0", "A = I"], 0)
    create_question(gate_quiz, "What is the limit of (sin x)/x as x approaches 0?", ["1", "0", "Infinity", "Undefined"], 0)
    create_question(gate_quiz, "Which of these is a prime number?", ["17", "15", "21", "27"], 0)

    # --- Basic Grammar Quiz ---
    grammar_quiz = get_quiz("English Grammar", "Check your basic English grammar skills.", grammar_cat)
    create_question(grammar_quiz, "Which of these is a noun?", ["Apple", "Run", "Beautifully", "Under"], 0)
    create_question(grammar_quiz, "Choose the correct verb form: 'She ___ to the store yesterday.'", ["went", "go", "goes", "gone"], 0)
    create_question(grammar_quiz, "What is the plural of 'child'?", ["children", "childs", "childes", "childrens"], 0)
    create_question(grammar_quiz, "Which word is an adjective?", ["Blue", "Quickly", "Jump", "They"], 0)
    create_question(grammar_quiz, "Identify the preposition: 'The cat is on the table.'", ["on", "cat", "is", "the"], 0)
    create_question(grammar_quiz, "Which is a synonym for 'happy'?", ["Joyful", "Sad", "Angry", "Tired"], 0)
    create_question(grammar_quiz, "Choose the correct article: 'I saw ___ elephant at the zoo.'", ["an", "a", "the", "No article"], 0)
    create_question(grammar_quiz, "What is the past participle of 'eat'?", ["eaten", "ate", "eating", "eats"], 0)
    create_question(grammar_quiz, "Which of these is a pronoun?", ["He", "Man", "Big", "Talk"], 0)
    create_question(grammar_quiz, "Identify the adverb: 'He ran quickly.'", ["quickly", "ran", "he", "None"], 0)
    create_question(grammar_quiz, "Which sentence is in the present continuous tense?", ["I am reading.", "I read.", "I will read.", "I have read."], 0)
    create_question(grammar_quiz, "What is the antonym of 'difficult'?", ["Easy", "Hard", "Simple", "Tough"], 2)
    create_question(grammar_quiz, "Which of these is a conjunction?", ["And", "Wait", "Fast", "Me"], 0)
    create_question(grammar_quiz, "Choose the correct possessive: 'That is ___ book.' (belonging to John)", ["John's", "Johns'", "Johns", "John be"], 0)
    create_question(grammar_quiz, "What is a 'subject' in a sentence?", ["The person/thing doing the action", "The action itself", "The object being acted upon", "The ending"], 0)

    print("Extra seeding complete!")

if __name__ == "__main__":
    seed_extra_data()
