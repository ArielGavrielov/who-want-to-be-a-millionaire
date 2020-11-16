import os;
import random;
from time import sleep;

q = 0;
floor = 0;
questionPrefix = 'What will be the output of the code below?';
Prizes = [100,200,300,500,1000,2000,5000,10000,250000,1000000];
passTimer = 5; # time to show the Pass Questions;
isAudio = True;

########## Game questions and rules ##########
rules = [
    'Do not make any mistake!',
    'You need to choose the correct answer out of four with numbers 1-4.',
    'You can call one time to anyone you think that can help you.',
    '50:50, which cuts two wrong answers.',
    'Every question you can press `q` to quit'
];

data = [
    {
        'question': "print('Ariel','and','Mor')",
        'answers': ["ArielandMor", "Ariel and Mor", "'Ariel','and','Mor'", "'Ariel' 'and' 'Mor'"],
        'indexRight': 1
    },
    {
        'question': "print(1 + 2)",
        'answers': ["3", "12", "1 2", "2"],
        'indexRight': 0
    },
    {
        'question': "x=5\ny=7\nprint(x+y)",
        'answers': ["35", "57", "12", "7"],
        'indexRight': 2
    },
    {
        'question': "list = ['a', 'b', 'c', 'd', 'e']\nprint(list[10:])",
        'answers': ["['a', 'b', 'c', 'd', 'e']", "['d', 'e']", "['a', 'b']", "IndexError"],
        'indexRight': 3
    },
    {
        'question': "list = [1,2,3,4,5]\nlist.append(6)\nprint(list)",
        'answers': ["[1,2,3,4,5]", "[6,1,2,3,4,5]", "[1,2,3,4,5,6]", "6"],
        'indexRight': 2
    },
    {
        'question': "list = ['Ariel','Mor','Lea']\nprint(list[0], 'and', list[1], 'learn with', list[2])",
        'answers': ["IndexError", "Ariel and Mor learn with Lea", "ArielandMorlearn withLea", "Lea and Mor learn with Ariel"],
        'indexRight': 1
    },
    {
        'question': "list = [1,2,3,4,5]\nlist.insert(1,3)\nprint(list)",
        'answers': ["[1,2,1,4,5]", "[3,2,3,4,5]", "[1,3,2,3,4,5]", "[1,2,3,1,4,5]"],
        'indexRight': 2
    },
    {
        'question': "def func(x):\n     return x*x\nfunc(5)",
        'answers': ["10", "25", "5", "Nothing."],
        'indexRight': 3
    },
    {
        'question': "def func(x):\n     return x*x\nprint(func(5))",
        'answers': ["10", "25", "5", "Nothing."],
        'indexRight': 1,
    },
    {
        'question': "def AAA(x):\n     if x < 10:\n          return x\n     return x%10 + AAA(x//10)\nprint(AAA(123))",
        'answers': ["321", "123", "6", "3"],
        'indexRight': 2
    }
]
########## Aid functions ##########
def Clear():
    os.system('clear' if os.name == 'posix' else 'cls')
    print();

def playSound(file):
    if isAudio:
        os.system('killall afplay 2>/dev/null')
        os.system('afplay ' + file if os.name == 'posix' else 'start ' + file)

def randomInd():
    global randomIndex
    randomIndex = int(random.randint(0,3))
    if randomIndex == data[indList[q]].get('indexRight'):
        return randomInd()
    return randomIndex

def printAnswers(*ind):
    for i in range(4) if not(ind) else sorted(ind):
        print((i+1),end='. ');
        print(data[indList[q]].get('answers')[i]);

def inputAnswer(Message = '', helps = True, playAgain = False, Start = False, Rules = False, Fifty = False):
    global inAnswer;
    global randomIndex;
    global isAudio;

    inAnswer = input(Message + '\n');

    if inAnswer.lower() == 't':
        isAudio = not(isAudio);
        print('You turn ' + ('on' if isAudio else 'off') + ' the audio.\n');
        return inputAnswer(Message, helps, playAgain, Start, Rules, Fifty);

    if inAnswer.lower() == 'q' and not(playAgain): # if choosen Quit the game;
        finishScreen(selfQuit = True);

    if playAgain: # Play again input;
        if inAnswer != '1' and inAnswer != '2':
            return inputAnswer("Enter your answer 1/2:", playAgain = True)
        if inAnswer == '1':
            return True;
        else:
            return False;

    elif Fifty:
        if ((ord(inAnswer)-ord('0') != randomIndex+1) and (ord(inAnswer)-ord('0') != data[indList[q]].get('indexRight')+1)) or ord(inAnswer) < 48:
            return inputAnswer('Wrong input. Choose only ' + str(randomIndex+1) + '/' + str(data[indList[q]].get('indexRight')+1) + " or `Q` to quit:" if randomIndex < data[indList[q]].get('indexRight') else 'Wrong input. Choose only ' + str(data[indList[q]].get('indexRight')+1) + '/' + str(randomIndex+1) + " or `Q` to quit:", Fifty = True)

    elif Start: # Start game input;
        if inAnswer.lower() != 'r' and inAnswer.lower() != 's':
            return inputAnswer("The input should to be only 'S', 'R', 'T' or 'Q'",Start = True)
        return inAnswer;
    elif Rules:
        if inAnswer != 's' and inAnswer != 'S':
            return inputAnswer("The input should to be only 'S', 'T' or 'Q'",Rules = True)
        return inAnswer;

    elif helps:
        if callHelp and fiftyHelp:
            if inAnswer < '1' or inAnswer > '6':
                return inputAnswer("Please choose 1-6, 'T' or 'Q' to quit:\n")

        elif callHelp or fiftyHelp:
            if inAnswer < '1' or inAnswer > '5':
                return inputAnswer("Please choose 1-5, 'T' or 'Q' to quit:\n")

        else:
            if inAnswer < '1' or inAnswer > '4':
                return inputAnswer("Please choose 1-4, 'T' or 'Q' to quit:\n")

    else:
        if inAnswer < '1' or inAnswer > '4':
            return inputAnswer("Please choose 1-4, 'T' or 'Q' to quit:\n", helps = False)
    inAnswer = ord(inAnswer)-ord('0');

def passQuestion():
    global floor;
    global wallet;
    global q;

    if q == 9:
        q += 1;
        return finishScreen()

    wallet = Prizes[q];
    Clear();
    playSound('welldone.wav &')
    for i in range(passTimer):
        print('Well done! you won', str(Prizes[q]),end='$.\n');
        print('More',(len(data)-(q+1)),'questions to the million!\n')
        for j in range(len(Prizes)-1,-1,-1):
            if j == 4 or j == 6 or j == 8:
                print('-'*3*j);
            print(' '*j,end='')
            print(Prizes[j], '(PASS)' if j <= q else '(NEXT QUESTION)' if j == q+1 else '')
        print('\nNext question more', str(passTimer-i), 'seconds.');
        sleep(1);
        Clear();
    q += 1;
    if q > 4:
        if q == 5:
            floor = 1000;
        elif q == 7:
            floor = 5000;
        elif q == 9:
            floor = 250000;
    playScreen()

########## SCREENS ##########
def welcomeScreen():
    Clear()
    print("Who want's to be a millionaire?\n")
    print("Copyright for Ariel Gavrielov & Mor Ben Shushan\n")
    start = inputAnswer("What you want to do?\nR. Rules.\nS. Start the game."  + '\nT. Toggle audio.' + "\nQ. Quit the game.", Start = True)

    # Rules;
    Clear()
    if start == 'r':
        print('The rules:')
        for i in range(len(rules)):
            print((i+1), end='. ')
            print(rules[i])
        start = inputAnswer("\nWhat you want to do?\nS. Start the game.\nQ. Quit the game.\n", Rules = True)

    startScreen()

def startScreen():
    # Get/Set global varibles;
    global callHelp
    global fiftyHelp
    global indList
    global wallet
    global q
    global floor

    callHelp = True
    fiftyHelp = True
    indList = random.sample(range(10),10) # Random questions list;
    wallet = 0
    q = 0;
    floor = 0

    # Start game;
    playSound('start.wav &')
    for i in range(passTimer):
        Clear()
        print("The game will start on",(passTimer-i),"seconds.\nGood luck!")
        sleep(1)
    playScreen()

def playScreen():
    showQuestionScreen()

    inputAnswer('Choose your answer:');

    if inAnswer == 5  or inAnswer == 6:
        if ((inAnswer == 5 and not(callHelp)) or inAnswer == 6) and fiftyHelp:
            showQuestionScreen(fifty = True)
        elif callHelp:
            showQuestionScreen(call = True)

    if (inAnswer-1) != data[indList[q]].get('indexRight'):
        return finishScreen();

    passQuestion();

def showQuestionScreen(helps = True, fifty = False, call = False):
    global callHelp
    global fiftyHelp

    Clear()

    print('Your wallet is', str(wallet),end='$.\n\n')

    print('Question number',str(q+1),'for', str(Prizes[q]),end='$:\n\n')

    print(questionPrefix + '\n' + ('-'*len(questionPrefix)))
    print(data[indList[q]].get('question'))
    print('-'*len(questionPrefix),end='\n\n')

    # 50/50 HELP
    if fifty:
        playSound('fifty.wav')
        randomIndex = randomInd()
        printAnswers(randomIndex,data[indList[q]].get('indexRight'))
        print('\nT. Toggle audio.' + '\nQ. Quit the game.')
        fiftyHelp = False
        return inputAnswer('\nNow choose your answer: ',Fifty = True)
######## FIFTY/FIFTY HELP END ##########
    printAnswers()

    if helps and not(fifty) and not(call):
        print("\n5. Call Help.\n6. 50/50 Help.\n" if callHelp and fiftyHelp else "\n5. Call help.\n" if callHelp else "\n5. 50/50 Help.\n" if fiftyHelp else '',end='')

    print('\nT. Toggle audio.' + '\nQ. Quit the game.')
    # CALL HELP
    if call:
        callHelp = False
        print('\nRinging...')
        for i in range(random.randint(2,3)):
            playSound('bip.wav')
            sleep(1);

        print('\nYour call help said the right answer is:\n');
        randomIndex = int(random.randint(0,3));
        printAnswers(randomIndex);
        inputAnswer('\nChoose your answer:', helps = False);
    else:
        playSound('million.wav &' if q == 9 else 'floor.wav &' if q == 4 or q == 6 or q == 8 else 'eq.wav &')
def finishScreen(selfQuit = False):
    Clear();
    if floor == 0:
        print('GAME OVER!!!\nYoure leaving with empty hands.');
        playSound('gameover.wav &')
    elif q == 10:
        print('WOW, i can`t believe!!\nYou`re a MILLIONAIRE!!!!')
        playSound('winner.wav &')
    else:
        print('GAME OVER!!!')
        print('You won',str(floor),end='$\n')
        playSound('gameover.wav &')

    if not(selfQuit):
        if inputAnswer('\nDo you want play again?\n1. Yes. I LOVE IT!\n2. No thanks.\n\nEnter your answer:',playAgain = True):
            startScreen()
        else:
            print('\nGood bye!')
    exit()

welcomeScreen()
