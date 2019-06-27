# Making a Game of IT - Day 4

<!-- TOC -->

- [Functions](#functions)
- [Jumping around (platforming)](#jumping-around-platforming)
- [Angle shooting](#angle-shooting)
- [Interacting with an NPC](#interacting-with-an-npc)
- [NPC Movement](#npc-movement)

<!-- /TOC -->

## Functions

We've been using Python's built-in functions like `str()`, `input()`, `len()`, and `print()`.
Python's `def` keyword --- followed by the intended name of your function, its arguments inside parentheses, and a colon ---lets us create our own.
The indented code block under the `def` line constitutes the body of the function... it's executed every time the function is called.
After we `def` the function we call it by its name followed by a set of parentheses with the arguments it needs inside.
In this first example, the function `hello_world()` takes no arguments.

```python3
def hello_world():
  print("Hello world!")

hello_world()
```

In this next example, we see how functions can access variables from outside their code block.

```python3
name = "Rear Admiral Grace Brewster Murray Hopper"

def hello_person():
  print("Hello", name)

hello_person()

name = "Dr. Alan Mathison Turing"

hello_person()
```

However, functions can't _change_ variables outside their code block

```python3
name = "Rear Admiral Grace Brewster Murray Hopper"

def name_change():
  name = "inside name"

name_change()

print(name)
```

Variables inside functions override variables from outside functions.

```python3
name = "Scarlin Hernandez"

def hello_person():
  name = "inside name"
  print("Hello", name) # This should print 'inside name'

hello_person()

print("Outside", name) # This should print 'Scarlin Hernandez'
```

This function takes one argument.

```python3
def hello_person(name):
  print("Hello", name)

hello_person("Dr. Mark E. Dean")

hello_person("Dr. Alan Mathison Turing")
```

This function takes two arguments.

```python3
def repeat_hello(n, name):
  for i in range(n):
    print("Hello, name, i)

repeat_hello(1, "Katherine Johnson")

repeat_hello(7, "Roy L. Clay, Sr.")
```

Functions can use the `return` keyword to halt and give a value back to the caller.

```python3
def oh_hai(name):
  return "oh, hai " + name
  print("do more stuff")    # This isn't executed because it comes after the return

result = oh_hai("Dr. Fei-Fei Li")
print(result)
```

Why are functions useful?
1. re-use of code inside the function (you have to type less code)
2. compartmentalize code so that high-level structure of your program is easier to follow
3. experiment with/test individual components of your program

## Jumping around (platforming)

The example game shown below is a simple platformer where players control sparty
with the goal of reaching the giant coin in the top right corner of the screen.

**To run this game you will need the [coin.png](/media/coin.png) and [sparty.png](/media/Sparty.png) files!**

{% include codeinclude.html file='sparty-platformer/platformer.py' %}

## Angle shooting

{% include codeinclude.html file='pointer.py' %}

## Interacting with an NPC

...comming soon...

## NPC Movement

...comming soon...
