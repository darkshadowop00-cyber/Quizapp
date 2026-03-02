import os
import django
import random

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quiz_project.settings')
django.setup()

from quiz.models import Category, Quiz, Question, Answer

def seed_requested_categories():
    data = {
        'History': {
            'description': 'Test your knowledge of past events and civilizations.',
            'questions': [
                ("Who was the first President of the United States?", ["George Washington", "Thomas Jefferson", "Abraham Lincoln", "John Adams"]),
                ("In which year did World War II end?", ["1945", "1939", "1918", "1963"]),
                ("Which ancient civilization built the pyramids of Giza?", ["Egyptians", "Mayans", "Romans", "Greeks"]),
                ("The Magna Carta was signed in which country?", ["England", "France", "Italy", "Germany"]),
                ("Who was known as the 'Maid of Orleans'?", ["Joan of Arc", "Marie Antoinette", "Queen Victoria", "Catherine the Great"]),
                ("Which empire was ruled by Julius Caesar?", ["Roman Empire", "Ottoman Empire", "British Empire", "Mongol Empire"]),
                ("The French Revolution began in which year?", ["1789", "1776", "1812", "1848"]),
                ("Who was the primary author of the Declaration of Independence?", ["Thomas Jefferson", "Benjamin Franklin", "James Madison", "Alexander Hamilton"]),
                ("Which famous explorer reached India by sea in 1498?", ["Vasco da Gama", "Christopher Columbus", "Ferdinand Magellan", "Marco Polo"]),
                ("The Berlin Wall fell in which year?", ["1989", "1991", "1985", "1980"]),
                ("Who was the first woman to win a Nobel Prize?", ["Marie Curie", "Mother Teresa", "Rosa Parks", "Eleanor Roosevelt"]),
                ("Which war was fought between the North and South regions of the US?", ["American Civil War", "War of 1812", "Revolutionary War", "Vietnam War"]),
                ("The Renaissance began in which European country?", ["Italy", "Spain", "Netherlands", "England"]),
                ("Who was the leader of the Soviet Union during World War II?", ["Joseph Stalin", "Vladimir Lenin", "Nikita Khrushchev", "Mikhail Gorbachev"]),
                ("Which document starts with 'We the People'?", ["US Constitution", "Bill of Rights", "Common Sense", "Magna Carta"]),
                ("The Titanic sank in which ocean?", ["Atlantic Ocean", "Pacific Ocean", "Indian Ocean", "Arctic Ocean"]),
                ("Who was the first human to travel into space?", ["Yuri Gagarin", "Neil Armstrong", "Buzz Aldrin", "John Glenn"]),
                ("Which city was the capital of the Byzantine Empire?", ["Constantinople", "Rome", "Athens", "Alexandria"]),
                ("The Battle of Waterloo was the final defeat for which leader?", ["Napoleon Bonaparte", "King Louis XVI", "Duke of Wellington", "Admiral Nelson"]),
                ("Which ancient Greek city-state was known for its military culture?", ["Sparta", "Athens", "Corinth", "Thebes"])
            ]
        },
        'Geography': {
            'description': 'Explore the world\'s physical features and political boundaries.',
            'questions': [
                ("Which is the largest continent by area?", ["Asia", "Africa", "North America", "Europe"]),
                ("Which river is the longest in the world?", ["Nile", "Amazon", "Yangtze", "Mississippi"]),
                ("What is the capital city of Australia?", ["Canberra", "Sydney", "Melbourne", "Perth"]),
                ("Mount Everest is located in which mountain range?", ["Himalayas", "Andes", "Rockies", "Alps"]),
                ("Which country has the largest population in the world?", ["India", "China", "USA", "Indonesia"]),
                ("The Great Barrier Reef is off the coast of which country?", ["Australia", "Brazil", "Mexico", "Thailand"]),
                ("Which desert is the largest hot desert in the world?", ["Sahara", "Gobi", "Kalahari", "Arabian"]),
                ("What is the smallest country in the world by land area?", ["Vatican City", "Monaco", "Nauru", "San Marino"]),
                ("Which ocean is the largest on Earth?", ["Pacific Ocean", "Atlantic Ocean", "Indian Ocean", "Southern Ocean"]),
                ("What is the capital of Japan?", ["Tokyo", "Kyoto", "Osaka", "Nagoya"]),
                ("Which country is known as the Land of the Rising Sun?", ["Japan", "South Korea", "China", "Thailand"]),
                ("Which line divides the Earth into Northern and Southern Hemispheres?", ["Equator", "Prime Meridian", "Tropic of Cancer", "International Date Line"]),
                ("What is the capital of Canada?", ["Ottawa", "Toronto", "Vancouver", "Montreal"]),
                ("Which European city is built on over 100 small islands?", ["Venice", "Amsterdam", "Stockholm", "Copenhagen"]),
                ("The Amazon Rainforest is primarily located in which country?", ["Brazil", "Peru", "Colombia", "Venezuela"]),
                ("Which African country was formerly known as Abyssinia?", ["Ethiopia", "Egypt", "South Africa", "Nigeria"]),
                ("What is the capital of France?", ["Paris", "Lyon", "Marseille", "Bordeaux"]),
                ("Which sea is bordered by Europe, Africa, and Asia?", ["Mediterranean Sea", "Red Sea", "Caribbean Sea", "Black Sea"]),
                ("Which country is both a continent and a country?", ["Australia", "Greenland", "Antarctica", "Madagascar"]),
                ("What is the capital city of Russia?", ["Moscow", "Saint Petersburg", "Novosibirsk", "Yekaterinburg"])
            ]
        },
        'Political Science': {
            'description': 'Learn about government systems, political theories, and international relations.',
            'questions': [
                ("What is the primary function of the legislative branch of government?", ["Making laws", "Enforcing laws", "Interpreting laws", "Declaring war"]),
                ("Which political ideology advocates for common ownership of the means of production?", ["Communism", "Capitalism", "Liberalism", "Conservatism"]),
                ("Who wrote 'The Republic'?", ["Plato", "Aristotle", "Socrates", "Machiavelli"]),
                ("What is a 'democracy'?", ["Rule by the people", "Rule by a king", "Rule by the wealthy", "Rule by the military"]),
                ("Which international organization was founded in 1945 to maintain world peace?", ["United Nations", "NATO", "European Union", "WHO"]),
                ("What is the highest court in the United States?", ["Supreme Court", "District Court", "Appeals Court", "Tax Court"]),
                ("The term 'Third World' originally referred to countries aligned with which group during the Cold War?", ["Neither NATO nor Warsaw Pact", "NATO", "Warsaw Pact", "United Nations"]),
                ("Which system of government features a single person with absolute power?", ["Autocracy", "Oligarchy", "Democracy", "Republic"]),
                ("Who is credited with the 'Separation of Powers' theory?", ["Baron de Montesquieu", "John Locke", "Thomas Hobbes", "Jean-Jacques Rousseau"]),
                ("What is the voting age in the United States?", ["18", "16", "21", "25"]),
                ("Which branch of government is headed by the President?", ["Executive", "Legislative", "Judicial", "Administrative"]),
                ("What is a 'Constitution'?", ["A set of fundamental principles for a state", "A list of laws", "A peace treaty", "A declaration of war"]),
                ("Which political movement fought for women's right to vote?", ["Suffragette movement", "Civil Rights movement", "Labor movement", "Environmental movement"]),
                ("What does 'Universal Suffrage' mean?", ["The right of all adult citizens to vote", "Taxation for all", "Freedom of speech", "Global peace"]),
                ("Who wrote 'The Communist Manifesto' with Friedrich Engels?", ["Karl Marx", "Vladimir Lenin", "Leon Trotsky", "Joseph Stalin"]),
                ("The 'Social Contract' theory is most associated with which philosopher?", ["Jean-Jacques Rousseau", "John Stuart Mill", "Immanuel Kant", "Friedrich Nietzsche"]),
                ("What is 'Diplomacy'?", ["The profession of managing international relations", "Starting a war", "Collecting taxes", "Building infrastructure"]),
                ("Which type of election is used to choose a party's candidate for a general election?", ["Primary election", "General election", "Recall election", "Referendum"]),
                ("What is the lower house of the United Kingdom parliament called?", ["House of Commons", "House of Lords", "Senate", "National Assembly"]),
                ("The concept of 'checks and balances' is designed to prevent what?", ["Any one branch from becoming too powerful", "Corruption", "Economic recession", "Foreign invasion"])
            ]
        },
        'Reasoning': {
            'description': 'Challenge your logical thinking and problem-solving skills.',
            'questions': [
                ("If All A are B, and All B are C, then:", ["All A are C", "Some A are not C", "No A are C", "All C are A"]),
                ("Find the next number in the series: 2, 4, 8, 16, ...", ["32", "24", "20", "64"]),
                ("Which word does not belong with the others? (Apple, Banana, Carrot, Grape)", ["Carrot", "Apple", "Banana", "Grape"]),
                ("If 'BLUE' is coded as 'CMVF', how is 'RED' coded?", ["SFE", "QDC", "TFG", "RDS"]),
                ("A man is 30 years older than his son. In 5 years, he will be 4 times as old as his son. How old is the son now?", ["5", "10", "15", "20"]),
                ("Which number comes next in the sequence: 1, 1, 2, 3, 5, 8, ...", ["13", "10", "11", "15"]),
                ("Light is to Window as Air is to:", ["Vent", "Door", "Wall", "Floor"]),
                ("If you rearrange the letters 'BARI', you get the name of a:", ["Bird", "City", "Animal", "Country"]),
                ("What is the missing number? 10, 13, 17, 22, ?", ["28", "26", "27", "30"]),
                ("Pointing to a photograph, a man says, 'I have no brother or sister, but that man's father is my father's son.' Whose photograph is it?", ["His son's", "His father's", "His own", "His nephew's"]),
                ("If North-East becomes North, North becomes North-West and so on, what will West become?", ["South-West", "North-West", "South", "East"]),
                ("A clock shows 4:30. If the minute hand points East, in what direction will the hour hand point?", ["South-East", "North-East", "North", "South"]),
                ("In a certain code, 'WORK' is written as '4-12-9-11'. How is 'DONE' written?", ["23-12-13-22", "4-15-14-5", "5-14-15-4", "22-13-12-23"]),
                ("Which of the following is the odd one out? (Kilometer, Meter, Liter, Mile)", ["Liter", "Kilometer", "Meter", "Mile"]),
                ("If Friday is the 4th of the month, what day will be the 20th?", ["Sunday", "Monday", "Tuesday", "Saturday"]),
                ("How many 9s are there in the sequence 8909219394 which are immediately preceded by an even number?", ["2", "1", "3", "0"]),
                ("If '+' means 'x', '-' means '+', 'x' means '/' and '/' means '-', what is the value of 6 + 4 - 8 x 2 / 2?", ["26", "24", "28", "30"]),
                ("A is the brother of B. B is the daughter of C. D is the father of C. How is A related to D?", ["Grandson", "Grandfather", "Son", "Brother"]),
                ("Book is to Author as Statue is to:", ["Sculptor", "Painter", "Musician", "Architect"]),
                ("If 'MIGHTY' is written as 'BHRFLS', how is 'BUILD' written?", ["CHVKC", "ATKCE", "CVKDE", "BTIKC"])
            ]
        }
    }

    for category_name, content in data.items():
        category, created = Category.objects.get_or_create(name=category_name)
        
        quiz, created = Quiz.objects.get_or_create(
            category=category,
            title=f"{category_name} Quiz",
            defaults={'slug': f"{category_name.lower().replace(' ', '-')}-quiz"}
        )
        
        print(f"Adding questions to {category_name}...")
        for q_text, answers in content['questions']:
            # Create question
            question, created = Question.objects.get_or_create(
                quiz=quiz,
                text=q_text
            )
            
            if created:
                # Add answers
                for i, a_text in enumerate(answers):
                    Answer.objects.create(
                        question=question,
                        text=a_text,
                        is_correct=(i == 0) # First answer is correct
                    )

    print("Seeding complete!")

if __name__ == "__main__":
    seed_requested_categories()
