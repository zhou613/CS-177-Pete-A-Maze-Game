from graphics import *
from random import *

#
# project2.py
# Xiaoyu Zhou, 0028388913
# This program includes a game that allows the users to imput
#   their names and complete a maze game. The top four users with
#   lowest scores would be displayed.
#


# Game Panel
def first_stage():

    win = GraphWin('Game Panel', 300, 200)
    win.setBackground('grey')
    # Initialization
    # display the 'Pete-A-Maze' context on the top of the screen
    # this list contains the rectangle in need
    rec = []
    score_board = []
    
    r1 = Rectangle(Point(0,0), Point(300,40))
    r1.setFill("white")
    m1 = Text(Point(150,20), "Pete-A-Maze")
    m1.setSize(24)
    r1.draw(win)
    m1.draw(win)

    # New Player Panel
    r2 = Rectangle(Point(100,170), Point(200, 200))
    r2.setFill("Green")
    m2 = Text(Point(150,185), "NEW PLAYER")
    r2.draw(win)
    m2.draw(win)

    # Exit Panel
    r3 = Rectangle(Point(260,170), Point(300, 200))
    r3.setFill("Red")
    m3 = Text(Point(280,185), "EXIT")
    r3.draw(win)
    m3.draw(win)

    # Score Board
    r4 = Rectangle(Point(50,60), Point(250,150))
    r4.setFill("white")
    r4.draw(win)

    
    # display the Score Board
    title = Text(Point(150,70), "TOP SCORES")
    dividing_line = Text(Point(150,80), "============")
    lowest_four = scoresIn(win)

    t1 = Text(Point(150, 95), lowest_four[0])
    t2 = Text(Point(150, 110), lowest_four[1])
    t3 = Text(Point(150, 125), lowest_four[2])
    t4 = Text(Point(150, 140), lowest_four[3])
    title.draw(win)
    dividing_line.draw(win)
    t1.draw(win) , t2.draw(win), t3.draw(win), t4.draw(win)
    # store all the rectangle
    rec = [r2, r3, r4]
    score_board = [title, dividing_line, t1, t2, t3, t4]

    return win, rec, score_board


# This function display the input box after clicking start
def next_player(win):
    # if the player clicked New_Player box,
    # NEW PLAYER control label is changed to START!,
    # Player Name: Text label and Entry box

    # Start! Panel
    r1 = Rectangle(Point(100,170), Point(200, 200))
    r1.setFill("Green")
    m1 = Text(Point(150,185), "Start!")
    m2 = Text(Point(70,70), "Player Name: ")
    m2.setSize(18)

    # allow the user to input "Player Name"
    inputBox = Entry(Point(200,70), 20)
    inputBox.draw(win)
    
    r1.draw(win)
    m1.draw(win)
    m2.draw(win)
        
    return r1, m1, inputBox

        
# This function pops up the Field after "start!" is clicked
# Display the player's name and live score
def start(win, name):
    
    # create a Field screen
    Field = GraphWin("Field", 400, 400)
    Field.setBackground("white")

    # display the name
    # name = input
    m0 = Text(Point(180,70),"")
    m0.setText(name)
    m0.setSize(18)
    m0.draw(win)
    
    m1 = Text(Point(95, 110), "Score:")
    m1.setSize(18)
    m1.draw(win)
 
    # Reset Panel
    r1 = Rectangle(Point(0,170), Point(40, 200))
    r1.setFill("yellow")
    r1.draw(win)
    
    m3 = Text(Point(20,185), "RESET")
    m3.draw(win)

    # draw grid pattern on the Field
    for i in range(0,401,40):
        l1 = Line(Point(i, 0), Point(i,400))
        l2 = Line(Point(0,i), Point(400, i))
        l1.setOutline("light grey")
        l2.setOutline("light grey")
        l1.draw(Field)
        l2.draw(Field)

    # draw the start, end, and pete rectangle to the field
    r_start = Rectangle(Point(0,0), Point(40,40))
    r_start.setOutline("light grey")
    r_start.setFill("green")
    r_start.draw(Field)
    
    r_end = Rectangle(Point(360, 360), Point(400, 400))
    r_end.setOutline("light grey")
    r_end.setFill("red")
    r_end.draw(Field)

    pete = Rectangle(Point(2,2), Point(38,38))
    pete.setFill("gold")
    pete.draw(Field)

    return Field, pete, m1, r1, m0

# This function animate the pete 
def animate(Field, win, pete, sensor_loc):
    # initialize the score
    score = 0
    m1 = Text(Point(150,110), score)
    m1.setSize(18)
    m1.draw(win)
    
    while True:
        cp = Field.getMouse()

        pete_P1_x = pete.getP1().getX()
        pete_P1_y = pete.getP1().getY()
        pete_P2_x = pete.getP2().getX()
        pete_P2_y = pete.getP2().getY()
        old_pete_center_x = pete.getCenter().getX()
        old_pete_center_y = pete.getCenter().getY()
        # boolean token 
        add_3 = False
 
        # detect the position of pete
        # same row -> Y-axis is within range, move towards the click
        if(cp.getY() >= pete_P1_y and cp.getY() <= pete_P2_y):
            # if pete.X < click.X, then pete.X increase by 40
            # calculate the score, if cross the sensor: +3, if not:+1
            if(pete_P2_x < cp.getX()):
                pete.undraw()
                pete = Rectangle(Point(pete_P1_x+40, pete_P1_y), Point(pete_P2_x+40, pete_P2_y))
                pete.setFill("gold")
                pete.draw(Field)

                # get the new position of the pete
                new_pete_center_x = pete.getCenter().getX()
                new_pete_center_y = pete.getCenter().getY()

                # determine if pete cross the sensor, if True, add 3
                for x in sensor_loc:
                    if(x.getY() == new_pete_center_y and x.getX() <= new_pete_center_x and x.getX() >= old_pete_center_x):
                        score = score + 3
                        add_3 = True
                # if pete does not cross the sensor, add 1
                if(add_3 == False):
                    score = score + 1
                m1.setText(score)
                    
                        
            # vice versa
            if(pete_P1_x > cp.getX()):
                pete.undraw()
                pete = Rectangle(Point(pete_P1_x-40, pete_P1_y), Point(pete_P2_x-40, pete_P2_y))
                pete.setFill("gold")
                pete.draw(Field)

                # get the new position of the pete
                new_pete_center_x = pete.getCenter().getX()
                new_pete_center_y = pete.getCenter().getY()

                # determine if pete cross the sensor
                for x in sensor_loc:
                    if(x.getY() == new_pete_center_y and x.getX() >= new_pete_center_x and x.getX() <= old_pete_center_x):
                        score = score + 3
                        add_3 = True
                        
                if(add_3 == False):
                    score = score + 1
                m1.setText(score)

        # same column ->X-axis is within range, move towards the click 
        if(cp.getX() >= pete_P1_x and cp.getX() <= pete_P2_x):
            # if pete.Y < click.Y, then pete.X increase by 40
            if(pete_P2_y < cp.getY()):
                pete.undraw()
                pete = Rectangle(Point(pete_P1_x, pete_P1_y+40), Point(pete_P2_x, pete_P2_y+40))
                pete.setFill("gold")
                pete.draw(Field)

                # get the new position of the pete
                new_pete_center_x = pete.getCenter().getX()
                new_pete_center_y = pete.getCenter().getY()

                # determine if pete cross the sensor
                for x in sensor_loc:
                    if(x.getX() == new_pete_center_x and x.getY() <= new_pete_center_y and x.getY() >= old_pete_center_y):
                        score = score + 3
                        add_3 = True
                        
                if(add_3 == False):
                    score = score + 1
                m1.setText(score)

            # vice versa
            if(pete_P1_y > cp.getY()):
                pete.undraw()
                pete = Rectangle(Point(pete_P1_x, pete_P1_y-40), Point(pete_P2_x, pete_P2_y-40))
                pete.setFill("gold")
                pete.draw(Field)

                # get the new position of the pete
                new_pete_center_x = pete.getCenter().getX()
                new_pete_center_y = pete.getCenter().getY()

                # determine if pete cross the sensor
                for x in sensor_loc:
                    if(x.getX() == new_pete_center_x and x.getY() >= new_pete_center_y and x.getY() <= old_pete_center_y):
                        score = score + 3
                        add_3 = True
                if(add_3 == False):
                    score = score + 1
                m1.setText(score)
                    

        # get the current location of pete after moving               
        pete_center_x_cur = pete.getCenter().getX()
        pete_center_y_cur = pete.getCenter().getY()
        # if pete reaches the end， display "Finished! Click to Close"，
        # wait for click， and close Field
        if(pete_center_x_cur > 360 and pete_center_x_cur < 400 and pete_center_y_cur > 360 and pete_center_y_cur < 400):
            finish = Text(Point(200,200), "Finished! Click to Close")
            finish.draw(Field)
            click = Field.getMouse()
            break
    Field.close()
    return score, m1

def sensor(Field):
    # create 3 list which contains all the center location of the sensors
    l1 = []
    
    # loop through the column and generate the sensor by 40%
    for i in range(37, 364, 40):
        for j in range(2, 399,40):
            # if 40%, generate a sensor 36*5 rectangle
            if(random() == True):
                    rec1 = Rectangle(Point(i, j), Point(i+5, j+36))
                    rec1.setFill("orange")
                    rec1.draw(Field)
                    center1 = Point(rec1.getCenter().getX(), rec1.getCenter().getY())
                    l1.append(center1)
                    
    # loop through the row and generate the sensor by 40%
    for i in range(2, 399, 40):
        for j in range(37, 364,40):
            # if 40%, generate a sensor 5*36 rectangle
            if(random() == True):
                    rec2 = Rectangle(Point(i, j), Point(i+36, j+5))
                    rec2.setFill("orange")
                    rec2.draw(Field)
                    center2 = Point(rec2.getCenter().getX(), rec2.getCenter().getY())
                    l1.append(center2)

    return l1


def scoresOut(player_name, score):
    player = player_name + "," + str(score)

    file = open("top_scores.txt", "a")
    file.write(player)
    file.write("\n")

def scoresIn(win):
    file = open("top_scores.txt", "r")
    num = []
    res = []
    lowest_four = []
    for line in file:
        res.append(line.strip())
        num.append(line[-3:].strip())

    after_sort = selSort(num, res)

    return after_sort
        

def selSort(nums, player):
    # sort nums into ascending order
    n = len(nums)
    # For each position in the list (except the very last)

    for bottom in range(n-1):
        # find the smallest item in nums[bottom]..nums[n-1]

        mp = bottom                 # bottom is smallest initially
        for i in range(bottom+1, n):  # look at each position
            if nums[i] < nums[mp]:      # this one is smaller
                mp = i                  # remember its index

        nums[bottom], nums[mp] = nums[mp], nums[bottom]
        player[bottom], player[mp] = player[mp], player[bottom]        

    return player       

# This function generate random number from 1-10 and determine if the number is [1,4]
# return true if number is within [1,4], false otherwise
def random():
    random_num = randint(1, 10)
    if(random_num >= 1 and random_num <= 4):
        return True
    else: return False
         

# This function detects if the point clicked by the mouse is inside the rectangle
def click(r, point):
    # compare the coordinates of the points with the rectangle's
    if(point.getX() >= r.getP1().getX() and point.getX() <= r.getP2().getX()
       and point.getY() >= r.getP1().getY() and point.getY() <= r.getP2().getY()):
        return True
    return False

def main():
    loop = 1
    while loop == 1:
        # receive the "Screen", "Boxs", and "Score_Board" from gp()
        win, rec, score_board = first_stage()
        Field = None
        while loop == 1:
            cp = win.getMouse()

            # if "Exit" is clicked, end the program
            if(click(rec[1], cp) == True):
                loop = 0
                break

            
            # if "New Player" is clicked, then undraw all Score_Board and display then Entry
            if(click(rec[0], cp) == True):
                for i in range(0,6):
                    score_board[i].undraw()
                rec[2].undraw()
                # receive the "Player Name" and "Start!" box from start()
                start_box, message1, inputBox = next_player(win)
     

                # if name is not null and start is clicked,
                # load the game and display the name and score
                cp1 = win.getMouse()
                if(click(start_box, cp1) == True):
                    name = inputBox.getText()
                    inputBox.undraw()
                    message1.setText("NEW PLAYER")
                    Field, pete, score_box, reset_box, name_box = start(win, name)
                    sensor_loc = sensor(Field)
                    score, message2 = animate(Field, win, pete, sensor_loc)
                    scoresOut(name, score)
                    #click(rec[0], cp) = False

                    cp2 = win.getMouse()
                    # At the end of the game, reset the score
                    if(click(rec[0], cp2) == True):
                        message2.undraw()
                        score_box.undraw()
                        name_box.undraw()


                    # If reset box is clicked, then reset everything
                    if(click(reset_box, cp2) == True):
                        break

        win.close()
        if(Field is not None):
            Field.close()
main()
    
