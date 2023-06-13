def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    if front_is_clear():
        move()
    turn_left()
    if front_is_clear():
        move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()



while not at_goal():
    if wall_on_right() and front_is_clear():
        turn_left()
        if front_is_clear():
            move()
        else:
            turn_right()
            move()
    elif not front_is_clear() and wall_on_right():
        turn_left()
        if front_is_clear():
            move()
        else:
            turn_left()
            move()
    elif not front_is_clear() and not wall_on_right():
        turn_right()
        move()
    elif front_is_clear() and right_is_clear():
        turn_left()
        if not front_is_clear():
            turn_right()
            move()
        else:
            turn_right()
            move()
    else:
        turn_left()
        turn_left()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################