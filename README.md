# PUZZLEPREFIX

# Search Bitcoin puzzles by prefix and range

Private keys are generated randomly in keyspace 20000000000000000:3ffffffffffffffff 

The private keys are converted into their respective public keys to address. If an key that start with **13zb1hQb** is find it will save the result in an text file **win.txt**

And also, you can change the range of the puzzle inside the script. Example:

low  = **0x40000000000000000**

high = **0x7ffffffffffffffff**

Don't forget to change the address prefix:

if n.startswith(**'1BY8GQb'**):
