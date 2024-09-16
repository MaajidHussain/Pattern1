def pattern(n):
    if n%2!=0 or n<=0:
        print("Please enter a positive even number as input!")
    
    top_bottom_row=str(n)*n
    #prints the top row
    print(top_bottom_row)
    
    middle_rows=str(n) + str(n-1)*(n-2) + str(n)
    for i in range(n-2):
        #prints the middle rows
        print(middle_rows)
    #prints the bottom row
    print(top_bottom_row)
    
# Take n=number=4 as example..
number=int(input("Enter a positive even number: "))
pattern(number)