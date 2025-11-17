#!/usr/bin/env python
"""
given a number example 6 - construct an array like [0,1,2,3,4,5]
write a function to to square each number an the find its sum of squares and average of squares .
make a __block__ to call this function, hardcode the argument to fucntion
Do not use any library function.
"""
print("Module monkey getting set up")
def sqsum(n : int):

    inp_arr = list(range(n))
    out_array = [x**2 for x in inp_arr]

    sq_sum = sum(out_array)
    avg = sq_sum / n

    return n, inp_arr, out_array, sq_sum, avg


if __name__ == "__main__" :
    print(" I am in main program")
    print(sqsum(4))
