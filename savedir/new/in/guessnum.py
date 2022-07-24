numguess = 9
while(True):
    n = 33

    if numguess>0:
        print("choose a number from 1 to 100")
        print("You have", numguess, "number of guesess")
        number=int(input())
        if number>70:
            numguess=numguess-1
            if numguess==0:
                print("game over the number was 33" )
                break
            print("you are so far come down")
            # continue
        elif 70>=number>=40:
            numguess=numguess-1
            if numguess==0:
                print("game over the number was 33" )
                break
            print("you are giving high value come down")
        elif 40>number>=34:
            numguess=numguess-1
            if numguess==0:
                print("game over the number was 33" )
                break
            print("just a little more come down")

        elif number== n:
            print("Congratulation you win!!!!!!!!")
            # numguess=numguess-1
            print("NUmber of guesses =", numguess)
            break
            # if numguess==0:
            #     print("game over the number was 33" )
        elif 13>=number:
            numguess = numguess - 1
            if numguess == 0:
                print("game over the number was 33")
                break
            print("increase your value more")
        elif 23>=number>13:
            numguess = numguess - 1
            if numguess == 0:
                print("game over the number was 33")
                break
            print("increase yur value more")
        elif 32>=number>23:
            numguess = numguess - 1
            if numguess == 0:
                print("game over the number was 33")
                break
            print("increase yur value a bit more you are close")
    # else:
