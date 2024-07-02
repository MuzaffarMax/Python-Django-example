from django.shortcuts import render




def home_page(request):
    return render(request, 'home.html')

def about_page(request):
    return render(request, 'about.html')

def python_file(request):

    import turtle
    import os

    wn = turtle.Screen()
    wn.title("Pong")
    wn.bgcolor("black")
    wn.setup(width=800, height=600)
    wn.tracer(0)


    score_a = 0
    score_b = 0

    # Wow you really reading my code? thanks ;)

    paddle_a = turtle.Turtle()
    paddle_a.speed(0.0)
    paddle_a.shape("square")
    paddle_a.color("white")
    paddle_a.shapesize(stretch_wid=5,stretch_len=1)
    paddle_a.penup()
    paddle_a.goto(-350, 0)


    paddle_b = turtle.Turtle()
    paddle_b.speed(0)
    paddle_b.shape("square")
    paddle_b.color("white")
    paddle_b.shapesize(stretch_wid=5,stretch_len=1)
    paddle_b.penup()
    paddle_b.goto(350, 0)


    ball = turtle.Turtle()
    ball.speed(0)
    ball.shape("square")
    ball.color("white")
    ball.penup()
    ball.goto(0, 0)
    ball.dx = 2
    ball.dy = 2


    pen = turtle.Turtle()
    pen.speed(0)
    pen.shape("square")
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)
    pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))


    def paddle_a_up():
        y = paddle_a.ycor()
        y += 20
        paddle_a.sety(y)

    def paddle_a_down():
        y = paddle_a.ycor()
        y -= 20
        paddle_a.sety(y)

    def paddle_b_up():
        y = paddle_b.ycor()
        y += 20
        paddle_b.sety(y)

    def paddle_b_down():
        y = paddle_b.ycor()
        y -= 20
        paddle_b.sety(y)


    wn.listen()
    wn.onkeypress(paddle_a_up, "w")
    wn.onkeypress(paddle_a_down, "s")
    wn.onkeypress(paddle_b_up, "Up")
    wn.onkeypress(paddle_b_down, "Down")


    while True:
        wn.update()
        
        
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)


        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1
            os.system("afplay bounce.wav&")
        
        elif ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1
            os.system("afplay bounce.wav&")


        if ball.xcor() > 350:
            score_a += 1
            pen.clear()
            pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
            ball.goto(0, 0)
            ball.dx *= -1

        elif ball.xcor() < -350:
            score_b += 1
            pen.clear()
            pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
            ball.goto(0, 0)
            ball.dx *= -1


        if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
            ball.dx *= -1 
            os.system("afplay bounce.wav&")
        
        elif ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
            ball.dx *= -1
            os.system("afplay bounce.wav&")

def python_file2 (request):
    

    while (True):

        print("What you are going to do with numbers?\n",
        "for multiplication enter '*'\n",
        "for division enter '/'\n",
        "for addition enter '+'\n",
        "for subtraction enter '-'\n")
        oper = input("Enter the operator: ")
        oper = str(oper)

        if oper == "+":
            try:
                x = float(input("Enter x: "))
                y = float(input("Enter y: "))
            except:
                print("\nPlease enter proper input!\n")
                continue


            print("The result of the addition is: "+str(x+y))

        elif oper == "-":
            try:
                x = float(input("Enter x: "))
                y = float(input("Enter y: "))
            except:
                print("\nPlease enter proper input!\n")
                continue


            print("The result of the subtraction is: "+str(x-y))

        elif oper == "*":
            try:
                x = float(input("Enter x: "))
                y = float(input("Enter y: "))
            except:
                print("\nPlease enter proper input!\n")
                continue

            print("The result of the multiplication is: "+str(x*y))

        elif oper == "/":
            try:
                x = float(input("Enter x: "))
                y = float(input("Enter y: "))
            except:
                print("\nPlease enter proper input!\n")
                continue

            print("The result of the division is: "+str(x/y))

        else:
            print("You are dolboeob")
        
        c = str(input("Continue?: (y/n)"))

        if c == "y":
            pass
        else:
            break 

def python_file3 (request):
    import random

    print("Welcome to the russian roulette \n",
        "Please choose any number to begin\n")

    bullet = random.randint(1,6)

    while (True) :

        click = int(input("Enter the digit\n"))

        if click > 6 or click < 1 :
            print ("You are moron\n")

        elif bullet == click :
            print ("You are dead\n")

        elif bullet != click :
            print ("you are alive\n")

        else :
            print("wtf are you doing?\n")


        answer = str(input("Wanna repeat? (y/n)"))

        if (answer == "y" or answer == "yeah" or 
            answer == "yep" or answer == "yes") :
            continue