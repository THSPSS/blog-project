def put_add_mark(number_list):
    for i in range(0,len(number_list)-1):
        print(f"{number_list[i]}+", end="")



input_number = input("Put number here : ")

number = [int(x) for x in str(input_number)]
sum_number = sum(number)
put_add_mark(number)

print(f"{number[-1]}={sum_number}")
