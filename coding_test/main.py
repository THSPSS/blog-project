from tkinter import *
THEME_COLOR = "#375362"

window = Tk()
window.title("Quizzler")
window.config(padx=20,pady=20,bg=THEME_COLOR)
canvas = Canvas(width=340, height=600,bg=THEME_COLOR,highlightthickness=0)
canvas_text = canvas.create_text(260, 10, text="Score :", fill='white',font=30)
canvas.grid(column=1,row=0)
rect = canvas.create_rectangle(30, 50, 300, 500,fill="white")
canvas.grid(column=0,row=1,columnspan=2)
false_img = PhotoImage(file="../quizzler-app-start/images/false.png")
true_img = PhotoImage(file="../quizzler-app-start/images/true.png")
false_button = Button(image=false_img, highlightthickness=0)
true_button = Button(image=true_img, highlightthickness=0)
false_button.grid(column=0, row=2)
true_button.grid(column=1, row=2)


window.mainloop()