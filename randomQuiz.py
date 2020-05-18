'''
Project: Generating Random Quiz Files

You're a teacher and you want to randomize the order of the questions on your test 

What the program does;
- Creates 35 different quizzes
- Creates 50 mutliple choics questions for each quiz in random order 
- provide the correct answer and three random wrong answers for each question 
- writes the quizzes to 35 text files 
- writes the answer to the 35 text files
    
    This means the code will need to do the following 
- store the states and their capitals in a dictonary 
- Call open(), write(), and close() for the quiz answer and text files
- Use random.shuffle to randimize order of the question 

'''

# STEP 1: STORE THE QUIZ DATA IN A DICTIONARY
import random

# The quiz data. Keys are states and vales and thier capitals
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
            'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
            'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
            'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
            'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
            'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
            'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
            'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
            'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
            'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
            'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
            'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
            'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
            'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
            'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
            'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West'
            'Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}


# Generate 35 quiz files

# STEP 2: Create the Quiz File and Shuffle the Question Order
for quizNum in range(35):
    # Create the quiz answer key files
    # This creates the text document of the quiz files numbered 1 to 35
    quizFile = open('capitalsquiz%s.txt' % (quizNum + 1), 'w')
    # This creates the text document of the quiz answer files umbered 1 to 35
    answerKeyFile = open('capitalsquiz_answers%s.txt' % (quizNum + 1), 'w')

    # Write out the header for the quiz
    # This gives the students space to write out all the required info(name, date,..etc) on a new line
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    # This indents the cursor and places the title of the test and version number of the test
    quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' %
                   (quizNum + 1))
    # This creates a couple newlines after the title of the test
    quizFile.write('\n\n')

    # shuffle the order of the states
    # We create a variable to hold the dictonary capital's keys - so we dont change the original
    states = list(capitals.keys())
    random.shuffle(states)

    # STEP 3: Create the Answer Option
    for questionNum in range(50):
        # Here we index the capitals by the question number this refers to some key in states which we pass to capitals to find the value
        correctAnswer = capitals[states[questionNum]]
        # Here we store all the values in capital in a list called wrongAnswers
        wrongAnswers = list(capitals.values())
        # Here we find the index of the answers we got correct and del them from the list wrongAnswers
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        # Here we return a list of length 3 from wrongAnswers and store is in wrongAnswers
        wrongAnswers = random.sample(wrongAnswers, 3)
        # Here create the answer options (multiple choice) with 3 wrong answers and and on correct answer ans store it
        answerOptions = wrongAnswers + [correctAnswer]
        # finally we shuffle the answer options - that way the correct answer isn't always d
        random.shuffle(answerOptions)

        # STEP 4: Write content to the quiz and Answer Key Files

        # Now we write all the questions and answer options for the quiz file
        # Now we write to the current quizfile the following question
        quizFile.write('%s. what is the capital of %s?\n' %
                       (questionNum + 1, states[questionNum]))
        # We have a loop iterate from 0 - 3
        for i in range(4):
            # To the quiz file we place in our multiple choice the answerOptions we made earlier letter A-D
            quizFile.write('   %s. %s\n' % ('ABCD'[i], answerOptions[i]))
            # Then we create a new line
        quizFile.write('\n')

        # Write the answer key to the answerKeyFile
        answerKeyFile.write('%s.%s\n' % (
            questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))

quizFile.close()
answerKeyFile.close()
