# Installation

Hey, I have included both questions in this repository.

-   Question 1 is created with Vue.js framework. No library used. There is a readme file in the calendar folder to explain how to run the code with `yarn`.
-   Question 2 is solved with Python 3. Therefore you need Python 3 to run the code as well as a library called [NumPy](https://numpy.org/) to install Pythin 3 run on mac `brew install pyrhon` and to install [NumPy](https://numpy.org/) run `pip3 install numpy`.
-   There is a `input.txt` file in the pizzerias folder to test the code. You are free to modify that, as you wish.
-   To see the result of question 2 simply run `python3 index.py` in `pizzerias` folder.

1. Write down your thoughts on how would you approach this problem briefly.

-   Between Bellman Ford's Algorithm, Dijkstra's Algorithm and Floyd–Warshall's Algorithm. I chose Dijkstra’s Algorithm because it is very efficient in finding the shortest path from one node to every other node within the same graph data structure.

2. Code down the solution with a language of your choice.

-   I did in Python 3

3. What is the complexity of your approach? Can we do better?

-   The processing time can be improved by avoiding blind search. The principle behind Dijkstra's method technique is that given the shortest path between each of a given nodes, there must be another node. The code is developed on the discussed logic to determine the shortest path. The approach can further be improved by introducing an algorithm that works on the negative edges as well.

## Question 1

Please create a web page that displays a calendar in grid form, like the output from the UNIX cal command.

We don’t expect you to preserve the formatting or titles as per this image - you can decide how you want to display those - but you must display the dates in a week-by-week grid form and the current day should be highlighted. The calendar implementation has to be your own (DO NOT use existing solutions such as Datepicker). The code must be easily runnable.

You’re free to use whatever framework you like. This should be made under the assumption that your calendar will be rendered in multiple locations across an app.

## Question 2

After a long deferment, the mayor of Z-city has allowed pizzerias to be opened in town. Pizzerias used to be unlawful because of health reasons (according to the mayor). The city is big, and suddenly there are pizzerias everywhere.

We can imagine the city like a matrix with NxN squares, where every square represents one block of the city. Every pizzeria only delivers pizza to the nearby blocks. Specifically, every pizzeria delivers pizza to every block that is at most R blocks away from block the pizzeria's location. Distance is determined by the minimum number of blocks that the delivery guy must take if he is going East/West or North/South (moving diagonally is forbidden in Z-city). For example, let's say that N=5 and a pizzeria is located at the block (3, 3). It can deliver to a 2 block distance at most. The following map shows where the given pizzeria delivers pizzas.

00X00

0XXX0

XXXXX

0XXX0

00X00

Mr. Little Z loves pizza, so he wants to move to the block where he can have the greatest selection of pizzas (the block that has the maximum number of pizzerias delivering to it).

Help Mr. Little Z find that maximum. In other words, if he moves to the block with the greatest selection of pizzas, how many pizzerias will be able to deliver to his block?

## INPUT

The first line of the standard input contains the two numbers N and M, and both numbers are on the interval [1, 1000]. The number N represents the dimension of the city in blocks (the city has NxN blocks). M is the number of pizzerias in the city. The following M lines contain information about each pizzeria, given by the three numbers X, Y, R. The numbers X and Y represent the block where the pizzeria is located, (1 <= X, Y <= N) and the number R represents the maximum distance that the given pizzeria's delivery guy will travel to deliver pizza (1 <= R <= 100).

## OUTPUT

Write one number to the standard output that represents the number of pizzerias that deliver pizzas to the block with the greatest selection of pizzas.

Input:
5 2

3 3 2

1 1 2

Output:
2

## Explanation

The first pizzeria delivers pizzas to the following blocks:

00X00

0XXX0

XXXXX

0XXX0

00X00

and the second one:

00000

00000

X0000

XX000

XXX00

So the number of pizzerias that deliver pizzas to each block is:

00100

01110

21111

12110

11200

So the maximum number is 2.
