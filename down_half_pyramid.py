#Print a downward Half-Pyramid Pattern of Star (asterisk)
def pyramid(num):
    for i in range(num,0,-1):
        for j in range(i-1,0,-1):
            print("*", end=" ")
        print(" ")
          
no_of_lines=int(input())
print("Printing a downward half-pyramid with ",no_of_lines," lines:")
pyramid(no_of_lines+1)
