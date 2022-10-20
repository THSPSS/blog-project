from tkinter import *
CONVERTER = 1.609

def get_miles_and_covert():
    miles = float(input.get())    #type of input will be string so it has to be change to actual number
    km = round(miles * CONVERTER)
    km_number.config(text=f"{km}")




#making screen
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200,height=100)
window.config(padx = 50, pady = 50)


#input box to get miles
input = Entry(width=10)
input.grid(column=1 , row=0)


#print miles on screen
miles_label = Label(text="Miles", font=("Arial", 13))
miles_label.grid(column=2, row=0)
miles_label.config(padx=5)

#put 'is equal to' on screen
is_equal_to_label = Label(text="is equal to", font=("Arial", 13))
is_equal_to_label.grid(column=0, row=1)
is_equal_to_label.config(pady=5)

#put km_number on screen
km_number = Label(text="0", font=("Arial", 13))
km_number.grid(column=1, row=1)


#put 'Km' on screen
km_label = Label(text="Km", font=("Arial", 13))
km_label.grid(column=2, row=1)


#create button on screen
button = Button(text="calculate" ,command=get_miles_and_covert , bd = '5',width=15)
button.grid(column=1,row=2)



window.mainloop()