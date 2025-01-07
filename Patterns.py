# def pattern_1 ():
#     rows=int(input("Enter number of rows: "))
#     i=0
    
#     while i<rows:
#         j=rows
#         while j>0:
#             print("*", end=" ")
#             j=j-1
#         print("\n")
#         i=i+1

# pattern_1()


def pattern_2 ():
    rows=int(input("Enter number of rows: "))
    i=0
    t=rows
    while i<rows:
        j=t
        while j>0:
            print("*", end=" ")
            j=j-1
        print("\n")
        i=i+1
        t=t-1

pattern_2()
