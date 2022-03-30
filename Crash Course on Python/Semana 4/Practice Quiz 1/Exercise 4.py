# Fill in the gaps in the nametag function so that it uses the format method to return first_name
#  and the first initial of last_name followed by a period. For example, nametag("Jane", "Smith") 
# should return "Jane S."

def nametag(x, y):
    z = [x, y[0]+'.']
    z = ' '.join(z)
    
    return z

print(nametag("Jane", "Smith")) 
# Should display "Jane S." 
print(nametag("Francesco", "Rinaldi")) 
# Should display "Francesco R." 
print(nametag("Jean-Luc", "Grand-Pierre")) 
# Should display "Jean-Luc G." 

def nametag(first_name, last_name):
	return(f"{first_name}, {last_name[0:1]}.")

print(nametag("Jane", "Smith")) 
# Should display "Jane S." 
print(nametag("Francesco", "Rinaldi")) 
# Should display "Francesco R." 
print(nametag("Jean-Luc", "Grand-Pierre")) 
# Should display "Jean-Luc G." 