# The counter function counts down from start to stop when 
# start is bigger than stop, and counts up from start to stop otherwise. 
# Fill in the blanks to make this work correctly.

def counter(start, stop):
    if start > stop:
        x = [i for i in range(stop,start+1)]
        x.sort(reverse=True)
        return_string = "Counting down:"
        for i in range(len(x)):
            return_string = return_string + " " + str(x[i]) +', '
        return_string = return_string[:-2]
        return return_string
    else:
        y = [i for i in range(start,stop+1)]
        return_string = "Counting up:"
        for i in range(len(y)):
            return_string = return_string + " " + str(y[i]) +', '
        return_string = return_string[:-2]
        return return_string

print(counter(1, 10)) # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
print(counter(2, 1)) # Should be "Counting down: 2,1"
print(counter(5, 5)) # Should be "Counting up: 5"