#***************************Imports******************
import tkinter as tk
import time
import threading

#**********************Global Variables****************
start_time = None
update_thread = None
pause_time = None
current_state = -1

#****************************Functions****************
def update_elapsed_time(label) :

    global start_time, pause_time
    while True :
        elapsed_time = time.time() - start_time
        if(current_state == -1) :
            start_time = None
            pause_time = None
            elapsed_time_label["text"] = "0:0:0:0"
            break
        elif (current_state == 1) :
            if(pause_time == None) :
                label["text"] = f" {int((elapsed_time) / 60**2) % 24} : {int((elapsed_time) / 60) % 60} : { int(elapsed_time) % 60} : {int((elapsed_time) * 1000) % 1000}"
                pause_time = time.time()
        elif (current_state == 0) :
            label["text"] = f" {int((elapsed_time) / 60**2) % 24} : {int((elapsed_time) / 60) % 60} : { int(elapsed_time) % 60} : {int((elapsed_time) * 1000) % 1000}"

    print("Thread Closed")

def start_stopwatch() :
    """Starts the stopwatch"""

    global start_time, update_thread, current_state, pause_time
    
    if(current_state != 0) :
        current_state = 0
        if(pause_time != None) :
            start_time += time.time() - pause_time
            pause_time = None
        else :
            start_time = time.time()
        if (update_thread == None or update_thread.is_alive() == False) :
            update_thread = threading.Thread(target=update_elapsed_time, args=(elapsed_time_label,),daemon=True)
            update_thread.start()

    print(threading.active_count())

def stop_stopwatch() :
    """Stops the measuring of elapsed time"""

    global current_state
    current_state = -1

def pause_stopwatch() :
    """Pauses the stopwatch"""

    global current_state
    current_state = 1

#****************************Script Commands****************

#Creating the main window
main_window = tk.Tk()
main_window.geometry("800x600")
main_window.title("Stopwatch")
main_window.resizable(False, False)

#Creating a frame for the elapsed time display label
gui_frame = tk.Frame(main_window, width=200,height=50, borderwidth=2, relief="sunken")
gui_frame.place(relx = 0.5 - (100 / 800), rely= 0.5 - (25 / 600))
gui_frame.grid_propagate(False)
gui_frame.update_idletasks()

#Creating a label to display the elapsed time
elapsed_time_label = tk.Label(gui_frame, text="0:0:0:0", font=("Agency FB", 26), fg="red")
rel_sz = (elapsed_time_label.winfo_width() / 100, elapsed_time_label.winfo_height() / 100)
elapsed_time_label.grid(row=0,column=0)

#Creating a frame for the buttons
button_frame = tk.Frame(main_window, width=300, height=50)
button_frame.grid_propagate(False)
button_frame.place(relx=0.5-(150/800),rely=0.5 + (25/600) + (20/600))
for i in range(0,10) :
    button_frame.grid_columnconfigure(i, minsize=20)

#Creating the buttons
start_button = tk.Button(button_frame, text="Start",command=start_stopwatch)
start_button.grid(row=0, column=3)
stop_button = tk.Button(button_frame, text="Stop", command= stop_stopwatch)
stop_button.grid(row=0, column=5)
pause_button = tk.Button(button_frame, text="Pause", command=pause_stopwatch)
pause_button.grid(row=0, column = 7)

#Rendering the gui
main_window.mainloop()
