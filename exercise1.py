N=int(input("Please enter a number="))
def sum_odd_numbers(x):
    sum_odd=0
    for i in range (1,x+1):
        if i%2!=0:
            sum_odd +=i
    return sum_odd
def average_even_numbers(x):
    average_even=0
    even_counter=0
    for i in range (1,x+1):
        if i%2==0:
            average_even +=i
            even_counter +=1
    average_even=average_even/even_counter
    return average_even
print("The sum of odd numbers=",sum_odd_numbers(N))
print("The average of even numbers=",average_even_numbers(N))