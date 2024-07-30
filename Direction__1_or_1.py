
# Using a for loop, write a program that:
# -	Reads a list of values from the user.
# -	Reads a sorting direction from the user (1 or -1)
# -	If direction is 1, sort the list from smallest to largest. If -1 do the opposite. The sorting must be done using the Selection Sort algorithm.
# -	Print the sorted list.

Data=input("Enter an Integer: ").split()
n=len(Data)
for i in range(n):
    Data[i]=int(Data[i])

marker=n
direction=int(input("Enter 1 for Ascending order and -1 for Descending: "))
for i in range(n):
    Largest=max(Data[0:marker])
    smallest=min(Data[0:marker])
    ilar=Data.index(Largest,0,marker)
    ismal=Data.index(smallest,0,marker)
    if direction==1:
        Data[ilar],Data[marker-1]=Data[marker-1],Data[ilar]
    elif direction==-1:
        Data[ismal],Data[marker-1]=Data[marker-1],Data[ismal]
    else:
        print("Not a valid input!")
    marker=marker-1
print (Data)
