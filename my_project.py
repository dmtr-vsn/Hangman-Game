import csv
import random
import tkinter as tk
import turtle
import string

wrong_answers_counter = 0

def click_button(button, letter):
    global puzzle_word, puzzle_word_buttons, wrong_answers_counter

    # if clicked buttons letter in puzzle word, we check and open all letters of puzzle word. Then disable used button.
    if letter in puzzle_word:
        for i in range(len(puzzle_word_buttons)):
            if puzzle_word[i] == button['text']:
                puzzle_word_buttons[i]['text'] = puzzle_word[i]
                button.configure(state=tk.DISABLED)

    # if no such letter, wrong answer increases by 1.
    # as we have only 8 tries, we check them every time. If wrong answers equals 8 the game is over.
    # otherwise we execute one action
    else:
        wrong_answers_counter += 1
        if wrong_answers_counter == 8:
            print('You are DEAD!')
            loose()
            for button in alphabet_buttons:
                button.configure(state=tk.DISABLED)


        else:
            button.configure(state=tk.DISABLED)
            code = 'wrong_' + str(wrong_answers_counter) + '()'
            exec(code)

    # after every move we check if the puzzle word is guessed.
    if check_success():
        win()
        print('You have just saved you ass!')
    # TODO: check if i need this block here or move it to check success

def check_success():
    global puzzle_word
    guessed_letters = 0

    # with cycle 'for' we check already guessed letters
    for button in puzzle_word_buttons:
        if button['text'] != '':
            guessed_letters += 1

    # if guessed letters quantity is the same length as puzzle word, the word is guessed
    if guessed_letters == len(puzzle_word):
        print('WIN')
        return True

def activate_hint():
    # This function opens unguessed letters

    # Here we are looking for possitions of unguessed letters
    # by searching through puzzle word buttons.
    # On output we have got list of numbers.
    unguessed_letters_possition = []
    for i in range(len(puzzle_word_buttons)):
        if puzzle_word_buttons[i]['text'] == '':
            unguessed_letters_possition.append(i)

    random.shuffle(unguessed_letters_possition)

    # Lets open half of unguessed letters.
    # If there are, for example, 5 unguessed letter then 3 will be opened
    hint_size = int(len(unguessed_letters_possition)/2 + 0.5)

    # Iterate through puzzle word buttons giving them corresponding letter from puzzle word
    for i in range(hint_size):
        letter = unguessed_letters_possition[i]
        puzzle_word_buttons[letter]['text'] = puzzle_word[letter]

    hint_button.configure(state=tk.DISABLED)


root = tk.Tk()
root.configure(background='gray70')
root.title('Hangout')
root.geometry("+200+150")


alphabet = string.ascii_uppercase

top_box = tk.Label(root, text='top box', background='gray70', width=50, height=5)
canvas = tk.Canvas(root, height=500)
middle_box = tk.Label(root, background='gray70', width=50, height=20)
lower_box = tk.Label(root, background='gray70', width=50, height=5)

top_box.pack()
canvas.pack()
middle_box.pack()
lower_box.pack()


alphabet_buttons = []
for i in range(len(alphabet)):
    alphabet_buttons.append(tk.Button(lower_box, width=4, height=2, text=alphabet[i], command=lambda i=i: click_button(alphabet_buttons[i], alphabet[i])))

for i in range(len(alphabet)):
    if i < 9:
        alphabet_buttons[i].grid(row=1, column=i, padx=1)
    if 8 < i < 18:
        alphabet_buttons[i].grid(row=2, column=i-9, padx=1, pady=1)
    if i > 17:
        alphabet_buttons[i].grid(row=3, column=i-18, padx=1)


words = []
with open('words.csv') as f:
    csv_reader = csv.reader(f)

    for row in csv_reader:
        for word in row:
            words.append(word.upper())

puzzle_word = words[random.randint(0, len(words)-1)]
print(puzzle_word)
puzzle_word_buttons = []           # buttons for puzzle word
for i in range(len(puzzle_word)):
    puzzle_word_buttons.append(tk.Button(middle_box, width=4, height=2, font=('', '12', 'bold'), text='', relief='groove', state=tk.DISABLED))

for i in range(len(puzzle_word_buttons)):
    puzzle_word_buttons[i].grid(row=0, column=i, padx=1, pady=10)




hint_button = tk.Button(top_box, text = '50/50', width=10, height=2, command= lambda: activate_hint())
hint_button.grid(row=0, column=0)



#=================== turtle =====================

#screen = turtle.TurtleScreen(canvas)

turtle_shape_image = "pencil.gif"

frame = turtle.RawTurtle(canvas)
human = turtle.RawTurtle(canvas)

human.hideturtle()
frame.hideturtle()

screen = frame.getscreen()

screen.register_shape("pencil.gif")

frame.shape(turtle_shape_image)
human.shape(turtle_shape_image)

# define zero coordinate to move turtle easily
x_coord = 20
y_coord = 0

frame.pensize(7)
frame.penup()
frame.goto(x_coord-120, y_coord-150)
frame.pendown()
frame.showturtle()
frame.goto(x_coord-120, y_coord+150)
frame.goto(x_coord+60, y_coord+150)
frame.penup()
frame.goto(x_coord-80, y_coord+150)
frame.pendown()
frame.goto(x_coord-120, y_coord+110)

frame.penup()
frame.goto(x_coord-120, y_coord-100)
frame.pendown()
frame.goto(x_coord-160, y_coord-150)

frame.penup()
frame.goto(x_coord-120, y_coord-100)
frame.pendown()
frame.goto(x_coord-80, y_coord-150)
frame.hideturtle()

x_coord_human = 40
y_coord_human = 50

def wrong_1():
    # drawing head
    human.penup()
    human.pensize(5)
    human.goto(x_coord_human, y_coord_human)
    human.pendown()
    human.showturtle()
    human.circle(20)
    human.hideturtle()

def wrong_2():
    # drawing eyes and mouth
    human.penup()
    human.goto(x_coord_human-8, y_coord_human+25)
    human.pensize(3)
    human.pendown()
    human.showturtle()
    human.dot()
    human.penup()
    human.goto(x_coord_human+8, y_coord_human+25)
    human.pendown()
    human.dot()
    human.penup()
    x = x_coord_human - 8
    y = y_coord_human + 15
    human.goto(x, y)
    human.pendown()
    ys = [y-3, y-3.5, y-4.5, y-5, y-4.5, y-3.5, y-3, y]

    for i in range(8):
        if i < 4:
            x += 2
            y = ys[i]
            print(x, y)
            human.goto(x, y)

        else:
            x += 2
            y = ys[i]
            human.goto(x, y)

    human.hideturtle()


def wrong_3():

    # drawing body
    human.penup()
    human.goto(x_coord_human, y_coord_human - 5)
    human.pensize(5)
    human.pendown()
    human.showturtle()
    human.goto(x_coord_human, y_coord_human - 65)
    human.hideturtle()

def wrong_4():
    # drawing right hand
    human.penup()
    human.goto(x_coord_human, y_coord_human - 10)
    human.pendown()
    human.showturtle()
    human.goto(x_coord_human - 30, y_coord_human - 45)
    human.hideturtle()

def wrong_5():
    # drawing left hand
    human.penup()
    human.goto(x_coord_human, y_coord_human-10)
    human.pendown()
    human.showturtle()
    human.goto(x_coord_human + 30, y_coord_human - 45)
    human.hideturtle()

def wrong_6():
    # drawing right leg
    human.penup()
    human.goto(x_coord_human, y_coord_human - 65)
    human.pendown()
    human.showturtle()
    human.goto(x_coord_human - 30, y_coord_human-110)
    human.hideturtle()

def wrong_7():
    # drawing left leg
    human.penup()
    human.goto(x_coord_human, y_coord_human-65)
    human.pendown()
    human.showturtle()
    human.goto(x_coord_human + 30, y_coord_human-110)
    human.hideturtle()

def win():
    # clean previous
    human.clear()

    x_coord_human = 40
    y_coord_human = -40

    # drawing head
    human.hideturtle()
    human.pensize(5)
    human.penup()
    human.goto(x_coord_human, y_coord_human)
    human.pendown()
    human.circle(20)

    # drawing eyes and mouth
    human.penup()
    human.goto(x_coord_human - 8, y_coord_human + 25)
    human.pensize(3)
    human.pendown()
    human.dot()
    human.penup()
    human.goto(x_coord_human + 8, y_coord_human + 25)
    human.pendown()
    human.dot()
    human.penup()
    x = x_coord_human - 8
    y = y_coord_human + 15
    human.goto(x, y)
    human.pendown()
    ys = [y - 3, y - 3.5, y - 4.5, y - 5, y - 4.5, y - 3.5, y - 3, y]
    for i in range(8):
        if i < 4:
            x += 2
            y = ys[i]
            print(x, y)
            human.goto(x, y)
        else:
            x += 2
            y = ys[i]
            human.goto(x, y)

    # drawing right hand
    human.penup()
    human.goto(x_coord_human, y_coord_human - 10)
    human.pensize(5)
    human.pendown()
    human.goto(x_coord_human - 20, y_coord_human - 5)
    human.goto(x_coord_human - 40, y_coord_human + 20)

    # drawing left hand
    human.penup()
    human.goto(x_coord_human, y_coord_human - 10)
    human.pendown()
    human.goto(x_coord_human + 20, y_coord_human - 5)
    human.goto(x_coord_human + 40, y_coord_human + 20)

    # drawing body
    human.penup()
    human.goto(x_coord_human, y_coord_human - 5)
    human.pendown()
    human.goto(x_coord_human, y_coord_human - 65)

    # drawing right leg
    human.goto(x_coord_human - 30, y_coord_human - 110)

    # drawing left leg
    human.penup()
    human.goto(x_coord_human, y_coord_human - 65)
    human.pendown()
    human.goto(x_coord_human + 30, y_coord_human - 110)

def loose():
    human.clear()

    x_coord_human = 40
    y_coord_human = 20

    # drawing rope
    human.penup()
    human.goto(x_coord_human-20, y_coord_human+130)
    human.pensize(2)
    human.pendown()
    human.goto(x_coord_human - 5, y_coord_human - 8)
    human.pensize(5)
    human.goto(x_coord_human + 8, y_coord_human - 15)


    # drawing head
    human.hideturtle()
    human.penup()
    human.pensize(5)
    human.goto(x_coord_human+10, y_coord_human-8)
    human.pendown()
    human.circle(20)

    # drawing eyes and mouth
    human.penup()
    human.pensize(2)

    human.goto(x_coord_human + 5, y_coord_human + 15)
    human.pendown()
    human.goto(x_coord_human + 10, y_coord_human + 10)
    human.penup()
    human.goto(x_coord_human + 5, y_coord_human + 10)
    human.pendown()
    human.goto(x_coord_human + 10, y_coord_human + 15)
    human.penup()

    human.goto(x_coord_human + 15, y_coord_human + 15)
    human.pendown()
    human.goto(x_coord_human + 20, y_coord_human + 10)
    human.penup()
    human.goto(x_coord_human + 15, y_coord_human + 10)
    human.pendown()
    human.goto(x_coord_human + 20, y_coord_human + 15)
    human.penup()

    x = x_coord_human + 7
    y = y_coord_human - 1
    human.goto(x, y)
    human.pendown()
    ys = [y + 3.5, y + 4.5, y + 4.5, y + 3.5, y]
    for i in range(5):
       if i < 4:
           x += 2
           y = ys[i]
           print(x, y)
           human.goto(x, y)
       else:
           x += 2
           y = ys[i]
           human.goto(x, y)

    # drawing right hand
    human.penup()
    human.goto(x_coord_human, y_coord_human - 10)
    human.pensize(5)
    human.pendown()
    human.goto(x_coord_human, y_coord_human - 5)
    human.goto(x_coord_human - 5, y_coord_human - 50)

    # drawing left hand
    human.penup()
    human.goto(x_coord_human, y_coord_human - 10)
    human.pendown()
    human.goto(x_coord_human, y_coord_human - 5)
    human.goto(x_coord_human + 5, y_coord_human - 50)

    # drawing body
    human.penup()
    human.goto(x_coord_human, y_coord_human - 5)
    human.pendown()
    human.goto(x_coord_human, y_coord_human - 65)

    # drawing right leg
    human.goto(x_coord_human - 5, y_coord_human - 110)

    # drawing left leg
    human.penup()
    human.goto(x_coord_human, y_coord_human - 65)
    human.pendown()
    human.goto(x_coord_human + 5, y_coord_human - 110)



root.mainloop()




