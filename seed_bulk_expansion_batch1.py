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
    category = Category.objects.get(name=name)
    return category

def get_quiz_for_category(category):
    # Find the quiz for this category. Most categories have one main quiz.
    quiz = category.quizzes.first()
    return quiz

def seed_bulk_batch_1():
    print("Seeding Batch 1 (Tech, Science, GK, History, Geography)...")
    
    # 1. Technology (Python Basics)
    tech_quiz = get_quiz_for_category(get_category("Technology"))
    questions_tech = [
        ("What is the correct way to open a file in Python for reading?", ["open('file.txt', 'r')", "open('file.txt', 'w')", "read('file.txt')", "file.open('r')"], 0),
        ("Which of these is a valid variable name in Python?", ["my_var", "2myvar", "my-var", "my var"], 0),
        ("What does the 'self' keyword represent in a Python class?", ["The instance of the class", "The class itself", "The parent class", "A global variable"], 0),
        ("Which module is used for regular expressions in Python?", ["re", "regex", "math", "random"], 0),
        ("What is the purpose of the 'finally' block in exception handling?", ["To execute code regardless of whether an exception occurred", "To catch specific errors", "To retry the block", "To exit the program"], 0),
        ("Which function is used to convert a string to an integer?", ["int()", "str()", "float()", "convert()"], 0),
        ("What is a lambda function in Python?", ["An anonymous one-line function", "A high-level class", "A recursion technique", "A built-in module"], 0),
        ("How do you add an element to a set?", ["add()", "append()", "plus()", "insert()"], 0),
        ("What is the result of 2 ** 3?", ["8", "6", "9", "5"], 0),
        ("Which method removes the last element from a list?", ["pop()", "remove()", "delete()", "clear()"], 0),
        ("What does the 'break' statement do in a loop?", ["Exits the loop entirely", "Skips the current iteration", "Pauses the loop", "Starts the loop from the beginning"], 0),
        ("Which of these is not a Python data type?", ["Array", "List", "Dictionary", "Tuple"], 0),
        ("How do you check if a key exists in a dictionary?", ["'key' in dict", "dict.has('key')", "dict.exists('key')", "dict.contains('key')"], 0),
        ("What is the correct extension for a Python file?", [".py", ".pyt", ".python", ".pyc"], 0),
        ("Which function returns the number of items in an object?", ["len()", "size()", "count()", "length()"], 0),
        ("What is the purpose of the 'pass' statement?", ["A null operation to serve as a placeholder", "To skip an error", "To end a loop", "To return a value"], 0),
        ("Which keyword is used to import specific names from a module?", ["from", "import", "using", "include"], 0),
        ("What is a decorator in Python?", ["A function that modifies the behavior of another function", "A UI component", "A style guide", "A type of class"], 0),
        ("How do you define a block of code in Python?", ["Indentation", "Curly braces", "Parentheses", "Keywords like 'begin' and 'end'"], 0),
        ("What is the result of 'bool(0)'?", ["False", "True", "Error", "None"], 0),
    ]
    for q_text, choices, idx in questions_tech:
        create_question(tech_quiz, q_text, choices, idx)

    # 2. Science (Biology Basics)
    science_quiz = get_quiz_for_category(get_category("Science"))
    questions_science = [
        ("What is the process by which plants make their own food?", ["Photosynthesis", "Respiration", "Transpiration", "Fermentation"], 0),
        ("Which part of the cell contains the genetic material?", ["Nucleus", "Cytoplasm", "Cell wall", "Mitochondria"], 0),
        ("What gas is released as a byproduct of photosynthesis?", ["Oxygen", "Carbon Dioxide", "Nitrogen", "Methane"], 0),
        ("Which system in the human body is responsible for hormones?", ["Endocrine system", "Nervous system", "Circulatory system", "Digestive system"], 0),
        ("What is the smallest unit of life?", ["Cell", "Atom", "Molecule", "Tissue"], 0),
        ("How many chambers are there in the human heart?", ["4", "2", "3", "1"], 0),
        ("What is the main function of the large intestine?", ["Absorbing water", "Protein digestion", "Pumping blood", "Thinking"], 0),
        ("Which blood type is known as the universal donor?", ["O negative", "AB positive", "A positive", "B negative"], 0),
        ("What is the common name for the patella?", ["Kneecap", "Shin bone", "Funny bone", "Wrist"], 0),
        ("Which vitamin is essential for blood clotting?", ["Vitamin K", "Vitamin A", "Vitamin C", "Vitamin D"], 0),
        ("What is the study of fossils called?", ["Paleontology", "Archeology", "Geology", "Biology"], 0),
        ("Where is the smallest bone in the human body located?", ["Ear", "Hand", "Foot", "Nose"], 0),
        ("What organ filters blood and produces urine?", ["Kidney", "Liver", "Spleen", "Bladder"], 0),
        ("Which compound is known as 'laughing gas'?", ["Nitrous oxide", "Carbon monoxide", "Methane", "Ammonia"], 0),
        ("What is the hardest substance in the human body?", ["Tooth enamel", "Femur", "Skull", "Nail"], 0),
        ("Which protein carries oxygen in the blood?", ["Hemoglobin", "Insulin", "Keratin", "Collagen"], 0),
        ("What is the medical term for the windpipe?", ["Trachea", "Larynx", "Esophagus", "Bronchus"], 0),
        ("How many chromosomes are in a normal human cell?", ["46", "23", "48", "32"], 0),
        ("What type of blood vessel carries blood away from the heart?", ["Artery", "Vein", "Capillary", "Valve"], 0),
        ("What is the most common element in the human body by mass?", ["Oxygen", "Carbon", "Hydrogen", "Nitrogen"], 0),
    ]
    for q_text, choices, idx in questions_science:
        create_question(science_quiz, q_text, choices, idx)

    # 3. General Knowledge (Space Exploration)
    gk_quiz = get_quiz_for_category(get_category("General Knowledge"))
    questions_gk = [
        ("Which planet is known for its Great Red Spot?", ["Jupiter", "Mars", "Saturn", "Neptune"], 0),
        ("What is the name of the first woman to fly in space?", ["Valentina Tereshkova", "Sally Ride", "Mae Jemison", "Peggy Whitson"], 0),
        ("Which telescope was launched in 1990 to provide detailed images of space?", ["Hubble Space Telescope", "James Webb Space Telescope", "Kepler Space Telescope", "Spitzer Space Telescope"], 0),
        ("What is the temperature of the Sun's core approximately?", ["15 million degrees Celsius", "1 million degrees Celsius", "5,500 degrees Celsius", "100 million degrees Celsius"], 0),
        ("Which space agency launched the Mangalyaan mission to Mars?", ["ISRO", "NASA", "ESA", "Roscosmos"], 0),
        ("What is a light-year a measure of?", ["Distance", "Time", "Speed", "Intensity"], 0),
        ("Which planet rotates on its side?", ["Uranus", "Neptune", "Venus", "Saturn"], 0),
        ("What is the name of the boundary around a black hole from which nothing can escape?", ["Event Horizon", "Singularity", "Escape Velocity", "Schwarzschild Radius"], 0),
        ("Who formulated the laws of planetary motion?", ["Johannes Kepler", "Isaac Newton", "Galileo Galilei", "Nicolaus Copernicus"], 0),
        ("What is the largest volcano in the solar system, located on Mars?", ["Olympus Mons", "Mauna Kea", "Mount Etna", "Vesuvius"], 0),
        ("Which moon of Jupiter is thought to have a subsurface ocean of water?", ["Europa", "Ganymede", "Callisto", "Io"], 0),
        ("What does NASA stand for?", ["National Aeronautics and Space Administration", "North American Space Agency", "National Aerospace and Science Association", "New Age Space Alliance"], 0),
        ("Which constellation is known as the 'Hunter'?", ["Orion", "Ursa Major", "Cassiopeia", "Leo"], 0),
        ("What is the most common type of star in the Milky Way?", ["Red Dwarf", "Blue Giant", "White Dwarf", "Yellow Dwarf"], 0),
        ("In which year did the Apollo 11 mission land on the Moon?", ["1969", "1961", "1972", "1965"], 0),
        ("What is the term for a star that has collapsed under its own gravity to a very high density?", ["Neutron Star", "White Dwarf", "Supernova", "Protostar"], 0),
        ("Which planet has the shortest day in our solar system?", ["Jupiter", "Earth", "Mars", "Saturn"], 0),
        ("What is the name of the first human-made object to enter interstellar space?", ["Voyager 1", "Voyager 2", "Pioneer 10", "New Horizons"], 0),
        ("What gas makes up most of the atmosphere of Venus?", ["Carbon Dioxide", "Nitrogen", "Oxygen", "Sulfur Dioxide"], 0),
        ("What is the name of the galaxy we live in?", ["Milky Way", "Andromeda", "Sombrero", "Triangulum"], 0),
    ]
    for q_text, choices, idx in questions_gk:
        create_question(gk_quiz, q_text, choices, idx)

    # 4. History (World War II)
    hist_quiz = get_quiz_for_category(get_category("History"))
    questions_hist = [
        ("Which battle is considered the turning point of the war in the Pacific?", ["Battle of Midway", "Battle of Guadalcanal", "Battle of Iwo Jima", "Battle of Okinawa"], 0),
        ("Who was the leader of Fascist Italy during WWII?", ["Benito Mussolini", "Adolf Hitler", "Francisco Franco", "Victor Emmanuel III"], 0),
        ("In which month and year did Germany surrender?", ["May 1945", "June 1944", "August 1945", "April 1945"], 0),
        ("What was the name of the genocide committed by the Nazi regime?", ["The Holocaust", "The Blitz", "The Purge", "The Great Terror"], 0),
        ("Which city was the site of the longest siege in WWII?", ["Leningrad", "Stalingrad", "Moscow", "Berlin"], 0),
        ("What was the name of the Allied strategy in the Pacific?", ["Island Hopping", "Blitzkrieg", "Total War", "Containment"], 0),
        ("Who was the supreme commander of the Allied forces in Europe?", ["Dwight D. Eisenhower", "Douglas MacArthur", "George Patton", "Bernard Montgomery"], 0),
        ("Which tiny island was the site of a famous flag-raising by US Marines?", ["Iwo Jima", "Guam", "Midway", "Saipan"], 0),
        ("What was the name of the secret German encryption machine?", ["Enigma", "Lorenz", "Purple", "Sigaba"], 0),
        ("In which country was the Auschwitz concentration camp located?", ["Poland", "Germany", "Austria", "Czechoslovakia"], 0),
        ("What event brought the United States into WWII?", ["Attack on Pearl Harbor", "Invasion of Poland", "Fall of France", "Sinking of the Lusitania"], 0),
        ("Which conference saw the Big Three plan the post-war world?", ["Yalta Conference", "Potsdam Conference", "Tehran Conference", "Casablanca Conference"], 0),
        ("What was the code name for the evacuation of Allied soldiers from Dunkirk?", ["Operation Dynamo", "Operation Sea Lion", "Operation Torch", "Operation Overlord"], 0),
        ("Who was the famous German general known as the 'Desert Fox'?", ["Erwin Rommel", "Heinz Guderian", "Hermann Göring", "Karl Dönitz"], 0),
        ("Which was the last major German offensive on the Western Front?", ["Battle of the Bulge", "Battle of the Somme", "Battle of Verdun", "Battle of Arnhem"], 0),
        ("What was the name of the B-29 bomber that dropped the first atomic bomb?", ["Enola Gay", "Bockscar", "Spirit of St. Louis", "Memphis Belle"], 0),
        ("Which country was the first to reach Berlin in 1945?", ["Soviet Union", "USA", "UK", "France"], 0),
        ("What was the 'Blitz'?", ["Heavy bombing of British cities by Germany", "German rapid tank invasion", "Allied naval blockade", "Japanese suicide attacks"], 0),
        ("Who was the Japanese Emperor during WWII?", ["Hirohito", "Akihito", "Mutsuhito", "Yoshihito"], 0),
        ("What was the name of the collaborationist government in France during WWII?", ["Vichy France", "Free France", "The Resistance", "The Fourth Republic"], 0),
    ]
    for q_text, choices, idx in questions_hist:
        create_question(hist_quiz, q_text, choices, idx)

    # 5. Geography (World Capitals)
    geo_quiz = get_quiz_for_category(get_category("Geography"))
    questions_geo = [
        ("What is the capital of China?", ["Beijing", "Shanghai", "Guangzhou", "Shenzhen"], 0),
        ("What is the capital of Russia?", ["Moscow", "Saint Petersburg", "Novosibirsk", "Yekaterinburg"], 0),
        ("What is the capital of India?", ["New Delhi", "Mumbai", "Bangalore", "Kolkata"], 0),
        ("What is the capital of Germany?", ["Berlin", "Munich", "Frankfurt", "Hamburg"], 0),
        ("What is the capital of the United Kingdom?", ["London", "Edinburgh", "Manchester", "Birmingham"], 0),
        ("What is the capital of France?", ["Paris", "Lyon", "Marseille", "Nice"], 0),
        ("What is the capital of Japan?", ["Tokyo", "Osaka", "Kyoto", "Nagoya"], 0),
        ("What is the capital of Australia?", ["Canberra", "Sydney", "Melbourne", "Perth"], 0),
        ("What is the capital of Canada?", ["Ottawa", "Toronto", "Vancouver", "Montreal"], 0),
        ("What is the capital of Brazil?", ["Brasília", "Rio de Janeiro", "São Paulo", "Salvador"], 0),
        ("What is the capital of Italy?", ["Rome", "Milan", "Naples", "Florence"], 0),
        ("What is the capital of South Africa?", ["Pretoria", "Cape Town", "Bloemfontein", "Johannesburg"], 0),
        ("What is the capital of Mexico?", ["Mexico City", "Cancun", "Guadalajara", "Monterrey"], 0),
        ("What is the capital of Spain?", ["Madrid", "Barcelona", "Valencia", "Seville"], 0),
        ("What is the capital of South Korea?", ["Seoul", "Busan", "Incheon", "Daegu"], 0),
        ("What is the capital of Egypt?", ["Cairo", "Alexandria", "Giza", "Luxor"], 0),
        ("What is the capital of Argentina?", ["Buenos Aires", "Córdoba", "Rosario", "Mendoza"], 0),
        ("What is the capital of Thailand?", ["Bangkok", "Phuket", "Chiang Mai", "Pattaya"], 0),
        ("What is the capital of Turkey?", ["Ankara", "Istanbul", "Izmir", "Bursa"], 0),
        ("What is the capital of Switzerland?", ["Bern", "Zurich", "Geneva", "Basel"], 0),
    ]
    for q_text, choices, idx in questions_geo:
        create_question(geo_quiz, q_text, choices, idx)

    print("Batch 1 (100 questions) seeded.")

if __name__ == "__main__":
    seed_bulk_batch_1()
