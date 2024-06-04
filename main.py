import turtle, keyboard

keys = [
    'up arrow',
    'down arrow',
    'left arrow',
    'right arrow']

turtle.color('red')

keyboard.add_hotkey(keys[0], lambda: turtle.forward(5))
keyboard.add_hotkey(keys[1], lambda: turtle.back(5))
keyboard.add_hotkey(keys[2], lambda: turtle.left(5))
keyboard.add_hotkey(keys[3], lambda: turtle.right(5))

turtle.exitonclick()