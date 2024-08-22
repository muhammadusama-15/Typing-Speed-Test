#Importing relevant libraries
import tkinter as tk
import random


#Getting a random paragraph to check the typing speed
from random_paragraphs import paragraphs
random_paragraph = ""


#Defining a function to give user its typing speed
def user_result():
    window.focus() #To prevent typing after time-out
    user_input = input_text.get("1.0","end-1c") #To get hold of the complete user input
    user_input_list = user_input.split(" ")

    random_paragraph_list = random_paragraph.split(" ")

    #Tracking the number of words typed compared to the sample text
    score = 0
    for i in range(len(random_paragraph_list)):
        for j in range(len(user_input_list)):
            if random_paragraph_list[i].lower() == user_input_list[j].lower(): #Using .lower() so that the case of word won't matter
                if i-j <= 2: #A small gap can occur due to missing of a word or two
                    score += 1
                    pass
    
    #Creating a label to sow the typing speen in words per minute
    result_label = tk.Label(master=frame, text=f"Your typing speed is around {score}-{score+1} words per minute.", fg="green", font=("Calibri",20,"bold"))
    result_label.grid(row=5, column=0, columnspan=2)


#Defining a function to start the test
def start_test():
    global random_paragraph
    random_paragraph = random.choice(paragraphs) #To ggive a new paragrapgh to user everytime test starts
    sample_text_message.config(text=random_paragraph)

    input_text.delete("1.0","end") #To delete everything in the entry text box as the user starts the test

    #Defining the timer functionality
    def update_timer(sec):
        start_test_button.config(text="Try Again") #To allow the user to try again
        input_text.focus()

        if sec == 60:
            timer_label = tk.Label(master=frame, text=f"Remaining: 01:00 ",fg="blue", font=("Calibri",20,"bold"))
        elif sec<10:
            timer_label = tk.Label(master=frame, text=f"Remaining: 00:0{sec} ",fg="blue", font=("Calibri",20,"bold"))
        else:
            timer_label = tk.Label(master=frame, text=f"Remaining: 00:{sec} ",fg="blue", font=("Calibri",20,"bold"))
        timer_label.grid(row=4,column=1)

        if sec > 0:
            sec -= 1
            window.after(1000,lambda:update_timer(sec))
        else:
            user_result()


    #Calling the function to initialize the timer
    update_timer(60)



#Creaing a window to run the program
window = tk.Tk()
window.title("Typing Speed Test")
window.geometry("700x700")

#Creating a frame
frame = tk.Frame(master=window)
frame.pack(padx=10,pady=10)

#Creating widgets
sample_label = tk.Label(master=frame, text="Sample Text:",fg="red",font=("Calibri",20,"bold"))
sample_label.grid(row=0,column=0,columnspan=2)

sample_text_message = tk.Message(master=frame, text="A paragraph will appear as soon as the test is started.", width=600, font=("Calibri",14,"normal"))
sample_text_message.grid(row=1,column=0,columnspan=2,pady=10)

input_label = tk.Label(master=frame, text="Type Below:",fg="green",font=("Calibri",20,"bold"))
input_label.grid(row=2,column=0,columnspan=2)

input_text = tk.Text(master=frame, borderwidth=2, font=("Calibri",14,"normal"),width=65,height=10)
input_text.grid(row=3,column=0,columnspan=2,pady=10)

start_test_button = tk.Button(master=frame, text="Start Test",width=30, bg="light grey",command=start_test)
start_test_button.grid(row=4,column=0)


#Creating a mainloop to continuously run the window
window.mainloop()