                            # TO-DO LIST

'''
    A To-Do List application is a useful project that helps users manage
    and organize their tasks efficiently. This project aims to create a
    command-line or GUI-based application using Python, allowing
    users to create, update, and track their to-do lists
'''

from tkinter import *
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        tasks.append(task)
        update_listbox()
        task_entry.delete(0, END)
    else:
        messagebox.showwarning("Error", "You must enter a task.")

def remove_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        tasks.pop(selected_task_index[0])
        update_listbox()
    else:
        messagebox.showwarning("Error", "You must select a task to remove.")
        
def delete_all_tasks():  
    message_box = messagebox.askyesno('Delete All', 'Are you sure?')  
    if message_box == True:    
        while(len(tasks) != 0):    
            tasks.pop()   
        update_listbox() 

def update_listbox():
    listbox.delete(0, END)
    for task in tasks:
        listbox.insert(END, task)
    
def exitApp():
    root.destroy()
        
        
        
root = Tk()
root.geometry("700x300")
root.title("To-Do List")
root.config(bg="green")

tasks = []

frame = Frame(root)
frame.pack()

label = Label(frame, width=10, bg='#D4AC0D', text="TO-DO-LIST")
label.pack(side=LEFT, padx=5, pady=5)

task_entry = Entry(frame, width=50, bg='light blue')
task_entry.pack(side=LEFT, padx=5, pady=5)

add_button = Button(frame, text="Add Task", command=add_task, bg='#D4AC0D')
add_button.pack(side=LEFT, padx=5, pady=5)

remove_button = Button(frame, text="Remove Task", command=remove_task, bg='#D4AC0D')
remove_button.pack(side=LEFT, padx=5, pady=5)

delete_all = Button(frame, text="Delete All", command=delete_all_tasks, bg='#D4AC0D')
delete_all.pack(side=LEFT, padx=5, pady=5)

listbox = Listbox(root, width=60, height=15)
listbox.pack(padx=5, pady=5)

exit_button = Button(frame, text="Exit/Close", command=exitApp, bg='#D4AC0D')
exit_button.pack(side=LEFT, padx=5, pady=5)

root.mainloop()