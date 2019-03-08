# John works at a clothin store. He has a large pile of socks that he must pair by color for sale.
# Given an array of integers representing the color of each sock, determine how many pais of socks
# with maching colors there are.

# For example, htere are sock with colors. There is one pair of color and one of color. Tere are three
# odd socks left, one of each color, the numbers of pairs is...

# Function description.
# Complete the sockMerchant function in the editor below. It must return an integer representing the 
# number of matching pairs of socks that are available.
# sockMerchant hast the following parameter(s):
#     - n: the number of socks in the pile.
#     - ar: the colors of each sock.

# Sample input:
#     - n = 9.
#     - ar = 10 20 20 10 10 30 50 10 20

def sockMerchant(n, ar):
    print (n)
    out = ar.split(' ')
    print(out)

sockMerchant(9, '10 20 10 20 10 50 10 10')