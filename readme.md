INPUT

The first line of input represents the size of the room with the base index being <0, 0>.

The rest of the input is data pertaining to the insects that have been deployed. Each insect has two lines of input. The first line gives the insect's position, and the second line is the sequence of commands that tell the insect where to navigate.

Each insect will finish it's navigation sequentially, which means that the second insect wont start moving until the first one has finished moving.


OUTPUT

The output for each insect should be its final coordinates and heading.


SAMPLE INPUT AND OUTPUT

Input:
5 5
1 2 N
LFLFLFLFF
3 3 E
FFRFFRFRRF

Expected output:
1 3 N
5 1 E
