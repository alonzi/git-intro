# git-intro
uva library workshop on introduction to git and github

## Who am I?
* [Senior Research Data Scientist with the Data Science Institute and UVA Library](https://dsi.virginia.edu/people/peter-alonzi)
* I like to be interrupted with questions! Please jump right in.

## Welcome to the UVA Library
* [Research Data Services](https://data.library.virginia.edu/)
* [Workshop Series](https://data.library.virginia.edu/training/)
  * Data Storage Best Practices (Bill Corey)	Tuesday, 11/6	14:00 – 15:30	Brown 133

## First, some terms

* git - version control software
* github - a for profit company owned by microsoft
* repository - a record of all changes to specified files (aka repo)
* fork - a repo and a pointer to the repo it deviates from

## Second, our goals

1. Everyone has git on their computer in working order
2. Become comfortable with git/github
3. Know how to get help

## Getting Git
* to play along you will need a github account --> https://github.com/

* if on mac/linux you probably already have git
  * go to the terminal and type git
  * if it says: *-bash: git: No such file or directory* (or something similar)
  * goto https://git-scm.com/ and download
  
* if on windows you probably need to get git
  * goto https://git-scm.com/ and download

## Outline
0. Some background
1. Work through the GitHub browser interface
2. Quick show of terminal interface
3. Tips on getting help

### Cartoons
* http://phdcomics.com/comics.php?f=1531
* https://swcarpentry.github.io/2014-06-24-wise-penn/lessons/nelle-git/git.html
* https://xkcd.com/1597/

## A brief history (according to wiki)
* Designed by [Linus Torvalds](https://en.wikipedia.org/wiki/Linus_Torvalds)
* initial release: 7 April 2005
* official repo: https://github.com/git/git
* most recent release (as of writing) 2.19.0 / 10 September 2018; 19 days ago



# Let's Get to It (hopefully everyone is done installing)
* open spyder [it looks like this](spyder.png)
  * text editor
  * variable explorer
  * console
  * control icons
  
## Strings
* A string is a 'string' of characters
  * 'apple'  # letters
  * 'blue42' # letters and numbers
  * 'i am the very model of a modern major general' # spaces are fine
  * '7 hills' # it can even start with a number
  
## Comments
We also introduce comments here, the computer will ignore everything after the '#' symbol. There are other forms but we'll see them later on.

## Variables
You can "save" things as variables. For those curious as to what's going on under the hood...in python a variable is actually just a pointer to the location in memory where the object lives.
* a = 'apple'
  * a is the variable
  * = is the assignment operator
  * 'apple' (a string) is the object assigned to a
  
* *Important Note*: the assignment operator is not like an equals sign
  * a=5
  * a=7
    * totally works, a was just reassigned to point to 7
    
## Functions
* print(a) # this function will show us what a points to
* we know that print is a function because there is no space between print and the "("
* format of a function: name(arguments)
* we say we "call" a function
* *this is super important* in python the way to spot a function is no space before a "(" and a letter or number
  * [python built-in functions](https://docs.python.org/3/library/functions.html)
  * print(...)
  * type(...)
  * pow(...)
  * in an equation you may see 5*(2+3), you won't seet 5(2+3) (try it and see what happens)
  
## Indexing
* for objects with an order you can access individual elements
* [indexing](indexing.png)
* you can also pull out slices
  * syntax [X:Y]
    * starting at X
    * upto but not including Y

## Lists
* represented like functions but with [...]
* there is an order to the items
* the items can be of any type

## Dictionary
* represented like lits but with {...}
* there is no order to items
* items contain two pieces: a key and a value represented key:value and the key must be a string

## loops - used when you want to repeat code
* for loop
  * for X in Y: << code >>
    * X is a new variable created on the spot
    * Y is some preexisting iterable
    * << code >> is a block of code you want to repeat
    * eg: for x in range(10): print(x)

* while loop
  * while Z: << code >>
    * Z is a boolean
    * << code >> is a block of code you want to repeat
    * eg: while i<10: print i; i+=1

## if statements
* example
  * if X: << code A >>
  * else: << code B >>
    * X is a boolean
    * << code A >> is some code
    * << code B >> is some code, could be the same
    


# Import
* *This is the most important topic*
* The import command let's you bring in code from another file and use it
* one example: random number generation
  * import numpy
  * numpy.random.randn()
* There are two steps [info on conda](https://conda.io/docs/user-guide/tasks/manage-pkgs.html) [info on pip](https://pip.pypa.io/en/stable/user_guide/)
  1. install the module, eg: shell]$ conda install numpy
  2. python>>> import numpy

# Scripting vs Programming
It's a matter of modularity. Programs are designed to be modular and work with other programs. Scripts are designed to be single use.



# Ways to Practice
1. Write some code
2. Ask a friend to review it

* Beginning
  * Flip a coin (~10 lines)
  * Play rock, paper, scissors  (~25 lines)
* Intermediate
  * Guess a secret number between 1 and 10. With hints. (~20 lines)
  * Dice rolling program
* Expert
  * Play blackjack
  * Play roulette
