##################################################
#	Submitted by : Rahul Sinha
#	User name    : rahsinha
##################################################

from random import randint
##################################################
#	method : move_gen()
#       returns: position in the range 1-9
#	move generator for AI
##################################################
def move_gen():
##################################################
#try winning horizontally or vertically: mark if 3 in a row are possible
#in a row or a column
##################################################
    for i in range(0,3):   
	if (map[i][0] == map[i][1] == computer) and (map[i][2] == " ") :
	    return 3+(i*3)  
	elif (map[i][2] == map[i][0] == computer) and (map[i][1] == " ") :
	    return 2+(i*3)   
	elif (map[i][1] == map[i][2] == computer) and (map[i][0] == " ") :
	    return 1+(i*3)   
	elif (map[0][i] == map[1][i] == computer) and (map[2][i] == " ") :
	    return 7+i 
	elif (map[2][i] == map[0][i] == computer) and (map[1][i] == " ") :
	    return 4+i
	elif (map[1][i] == map[2][i] == computer) and (map[0][i] == " ") :
	    return 1+i 
######################################################################
#try winning diagonally: mark if 3 in a row are possible in a diagonal
######################################################################
    if (map[0][0] == map[1][1] == computer) and (map[2][2] == " ") :
	return 9
    elif (map[1][1] == map[2][2] == computer) and (map[0][0] == " ") :
	return 1
    elif (map[2][2] == map[0][0] == computer) and (map[1][1] == " ") :
	return 5
    elif (map[0][2] == map[1][1] == computer) and (map[2][0] == " ") :
	return 7
    elif (map[1][1] == map[2][0] == computer) and (map[0][2] == " ") :
	return 3
    elif (map[2][0] == map[0][2] == computer) and (map[1][1] == " ") :
	return 5

######################################################################################
#try blocking opponent: block human if there are 2 in a row horizontally or vertically
######################################################################################

    for i in range(0,3):
	if (map[i][0] == map[i][1] == human) and (map[i][2] == " ") :
	    return 3+(i*3)  
	elif (map[i][2] == map[i][0] == human) and (map[i][1] == " ") :
	    return 2+(i*3)   
	elif (map[i][1] == map[i][2] == human) and (map[i][0] == " ") :
	    return 1+(i*3)   
	elif (map[0][i] == map[1][i] == human) and (map[2][i] == " ") :
	    return 7+i 
	elif (map[2][i] == map[0][i] == human) and (map[1][i] == " ") :
	    return 4+i
	elif (map[1][i] == map[2][i] == human) and (map[0][i] == " ") :
	    return 1+i
#########################################################################
#try blocking opponent: block human if there are 2 in a row on a diagonal
#########################################################################
    
    if (map[0][0] == map[1][1] == human) and (map[2][2] == " ") :
	return 9
    elif (map[1][1] == map[2][2] == human) and (map[0][0] == " ") :
	return 1
    elif (map[2][2] == map[0][0] == human) and (map[1][1] == " ") :
	return 5
    elif (map[0][2] == map[1][1] == human) and (map[2][0] == " ") :
	return 7
    elif (map[1][1] == map[2][0] == human) and (map[0][2] == " ") :
	return 3
    elif (map[2][0] == map[0][2] == human) and (map[1][1] == " ") :
	return 5
##########################################################################
#Make meaningful moves: 
#			|   |		1st move : AI -> O at 2
#			|   | 		2nd move : human -> X at 1
#		      X	| O |		3rd move : AI -> avoid putting O 
#						   at 3 as it is pointless
#                                                  at this point of time
#
#	exception :  ie. if it the last possible empty space.
##########################################################################
    poz = randint(1,9)
    for i in range(0,3):
	if (map[i][0] == human) and (map[i][1] == computer) and (map[i][2] == " ") and (count<7):
	    while (poz == (3+(i*3))):
    		poz = randint(1,9)
	    return poz
	elif (map[i][0] == computer) and (map[i][1] == human) and (map[i][2] == " ") and (count<7):
	    while (poz == (3+(i*3))):
    		poz = randint(1,9)
	    return poz
	elif (map[i][0] == human) and (map[i][2] == computer) and (map[i][1] == " ") and (count<7):
	    while (poz == (2+(i*3))):
    		poz = randint(1,9)
	    return poz
	elif (map[i][0] == computer) and (map[i][2] == human) and (map[i][1] == " ") and (count<7):
	    while (poz == (2+(i*3))):
    		poz = randint(1,9)
	    return poz
	elif (map[i][1] == human) and (map[i][2] == computer) and (map[i][0] == " ") and (count<7):
	    while (poz == (1+(i*3))):
    		poz = randint(1,9)
	    return poz
	elif (map[i][1] == computer) and (map[i][2] == human) and (map[i][0] == " ") and (count<7):
	    while (poz == (1+(i*3))):
    		poz = randint(1,9)
	    return poz
##########################################################################
#Make meaningful moves: 
#			|   |		1st move : AI -> O at 4
#		      O	|   | 		2nd move : human -> X at 1
#		      X	|   |		3rd move : AI -> avoid putting O 
#						   at 7 as it is pointless
#                                                  at this point of time
#
#	exception :  ie. if it the last possible empty space.
##########################################################################
	elif (map[0][i] == human) and (map[1][i] == computer) and (map[2][i] == " ") and (count<7):
	    while (poz == 7+i):
    		poz = randint(1,9)
	    return poz
	elif (map[0][i] == computer) and (map[1][i] == human) and (map[2][i] == " ") and (count<7):
	    while (poz == 7+i):
    		poz = randint(1,9)
	    return poz
	elif (map[2][i] == human) and (map[0][i] == computer) and (map[1][i] == " ") and (count<7):
	    while (poz == 4+i):
    		poz = randint(1,9)
	    return poz
	elif (map[2][i] == computer) and (map[0][i] == human) and (map[1][i] == " ") and (count<7):
	    while (poz == 4+i):
    		poz = randint(1,9)
	    return poz
	elif (map[1][i] == human) and (map[2][i] == computer) and (map[0][i] == " ") and (count<7):
	    while (poz == 1+i):
    		poz = randint(1,9)
	    return poz
	elif (map[1][i] == computer) and (map[2][i] == human) and (map[0][i] == " ") and (count<7):
	    while (poz == 1+i):
    		poz = randint(1,9)
	    return poz
##########################################################################
#Make meaningful moves: 
#			|   |		1st move : AI -> O at 5
#		      	| O | 		2nd move : human -> X at 1
#		      X	|   |		3rd move : AI should avoid putting O 
#						   at 9 as it is pointless
#                                                  at this point of time
#
#	exception :  ie. if it the last possible empty space.
##########################################################################
    	elif (map[0][0] == human) and (map[1][1] == computer) and (map[2][2] == " ") and (count<7):
	    while (poz == 9):
    		poz = randint(1,9)
	    return poz
    	elif (map[0][0] == computer) and (map[1][1] == human) and (map[2][2] == " ") and (count<7) and (count !=2):
	    while (poz == 9):
    		poz = randint(1,9)
	    return poz
    	elif (map[1][1] == human) and (map[2][2] == computer) and (map[0][0] == " ") and (count<7) and (count !=2):
	    while (poz == 1):
    		poz = randint(1,9)
	    return poz
    	elif (map[1][1] == computer) and (map[2][2] == human) and (map[0][0] == " ") and (count<7):
	    while (poz == 1):
    		poz = randint(1,9)
	    return poz
	elif (map[2][2] == human) and (map[0][0] == computer) and (map[1][1] == " ") and (count<7):
	    while (poz == 5):
    		poz = randint(1,9)
	    return poz
	elif (map[2][2] == computer) and (map[0][0] == human) and (map[1][1] == " ") and (count<7):
	    while (poz == 5):
    		poz = randint(1,9)
	    return poz
   	elif (map[0][2] == human) and (map[1][1] == computer) and (map[2][0] == " ") and (count<7):
	    while (poz == 7):
    		poz = randint(1,9)
	    return poz
   	elif (map[0][2] == computer) and (map[1][1] == human) and (map[2][0] == " ") and (count<7) and (count != 2):
	    while (poz == 7):
    		poz = randint(1,9)
	    return poz
        elif (map[1][1] == human) and (map[2][0] == computer) and (map[0][2] == " ") and (count<7) and (count !=2):
	    while (poz == 3):
    		poz = randint(1,9)
	    return poz
        elif (map[1][1] == computer) and (map[2][0] == human) and (map[0][2] == " ") and (count<7):
	    while (poz == 3):
    		poz = randint(1,9)
	    return poz
        elif (map[2][0] == human) and (map[0][2] == computer) and (map[1][1] == " ") and (count<7):
	    while (poz == 5):
    		poz = randint(1,9)
	    return poz
        elif (map[2][0] == computer) and (map[0][2] == human) and (map[1][1] == " ") and (count<7):
	    while (poz == 5):
    		poz = randint(1,9)
	    return poz
###################################################################################
#Make meaningful moves: 
#			|   |		1st move : human -> X at 5
#		      	| X | 		2nd move : AI -> O should try to select
#		      O	|   |			   randomly from positions 1,3,7,9
#						   as that maximizes the chances 
#						   for the AI to win
#
####################################################################################
        if (map[1][1] == human != " ") and (count == 1):
	    while (poz == 2 or poz == 4 or poz == 6 or poz == 8):
	        poz = randint(1,9)
	    return poz
###################################################################################
#Make meaningful moves: 
#		      	|   | X		1st move : AI -> X at 1
#			| O |		2nd move : hunman -> O at 5
#		      X	|   |		3rd move : AI should try putting X at 9
#						   as it opens up more chances for
#						   the AI to win.
#                                                  
#
###################################################################################
        elif (map[1][1] == human != " ") and (map[0][0] == computer != " ") and (map[2][2] == " ") and (count == 2):
	    return 9
        elif (map[1][1] == human != " ") and (map[2][0] == computer != " ") and (map[0][2] == " ") and (count == 2):
	    return 3
        elif (map[1][1] == human != " ") and (map[2][2] == computer != " ") and (map[0][0] == " ") and (count == 2):
	    return 1
        elif (map[1][1] == human != " ") and (map[0][2] == computer != " ") and (map[2][0] == " ") and (count == 2):
	    return 7
	
    return (randint(1,9))
######################
#
#print board function
#
######################
def print_board():
    for i in range(0,3):
        for j in range(0,3):
            print map[2-i][j],
            if j != 2:
                print "|",
        print ""
##########################
#
#check for end conditions
#
##########################

def check_done():
    for i in range(0,3):
        if map[i][0] == map[i][1] == map[i][2] != " " \
        or map[0][i] == map[1][i] == map[2][i] != " ":
            if turn == human:
	        print  "You won with ",turn
                return True
            else:
	        print  "Computer won with ",turn
                return True

        
    if map[0][0] == map[1][1] == map[2][2] != " " \
    or map[0][2] == map[1][1] == map[2][0] != " ":
        if turn == human:
	    print  "You won with ",turn
            return True
        else:
	    print  "Computer won with ",turn
            return True

    if " " not in map[0] and " " not in map[1] and " " not in map[2]:
        print "Draw"
        return True
        

    return False


count = 0
map = [[" "," "," "],
       [" "," "," "],
       [" "," "," "]]
done = False
selection = False
while selection != True:	# till human chooses X or O (proper input validation)
    turn = raw_input("Select X or O: ")
    try:
        if turn == "x" or turn == "X":
            turn = "X"
	    selection = True
        elif turn == "o" or turn == "O":
            turn = "O"
	    selection = True
    except: 
        print "Enter valid choice"

computer = "X"
human = "O"
player = True
##############################
#Making sure the first move is
#of X.
#
##############################
if turn == "O" :
    player = False

if player == False:
    turn = "X"
    computer = "X"
    human = "O"
else :
    computer = "O"
    human = "X"
     

while done != True:
    print_board()
    
    print turn, "'s turn"
    print
    
    moved = False
    while moved != True:
        if player == True:
            print "Please select position by typing in a number between 1 and 9, see below for which number that is which position..."
            print "7|8|9"
            print "4|5|6"
            print "1|2|3"
            print
	else:
	    print "Computers chance"
        
	try:
            if player == False:
		pos = move_gen()
	    else:
	        pos = input("Select: ")
           
 
	    if pos <=9 and pos >=1:
                Y = pos/3      
                X = pos%3      
                if X != 0:      
                    X -=1
                else:
                     X = 2      
                     Y -=1
                    
                if map[Y][X] == " ":
                    map[Y][X] = turn
        	    count +=1
	            moved = True
	    	    player = not player
                    done = check_done()

                    if done == False:
                        if turn == "X":
                            turn = "O"
                        else:
                            turn = "X"
                
			            
        except:
            print "You need to add a numeric value"
        

print_board()

