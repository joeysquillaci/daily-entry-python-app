import tkinter as tk
import time
from tkinter import messagebox


class MyGUI:

    def __init__(self):

        self.root = tk.Tk()

        # Simple Label
        self.label = tk.Label(
            self.root, text='Daily Entry', font=('Arial', 18))
        self.label.pack(padx=10, pady=10)

        # Simple textbox
        self.textbox = tk.Text(self.root, height=5, font=('Arial', 16))
        self.textbox.pack(padx=10, pady=10)

        # Simple button
        self.button = tk.Button(self.root, text='Submit Entry', font=(
            'Arial', 18), command=self.writeToFile)
        self.button.pack(padx=10, pady=10)

        # Call on_closing() if user clicks the X at the top right of the window
        self.root.protocol('WM_DELETE_WINDOW', self.on_closing)

        # Run mainloop()
        self.root.mainloop()

    # Function getting the checkbox state and doing proper function based on if it's checked or not

    def writeToFile(self):

        # Prints out the self.check_state variable, will be 0 or 1 depending on if box is checked
        # print(self.check_state.get())

        print(self.textbox.get('1.0', tk.END))

        moment = time.strftime('%b-%d-%Y', time.localtime())

        w = open('entries/diary-' + moment + '.txt', mode="wt")
        w.write(self.textbox.get('1.0', tk.END))
        w.close()

    # Function verifying if user really wants to quit
    def on_closing(self):

        # If we click yes, this will return 1
        if messagebox.askyesno(title='Quit?', message='Do you really want to quit?'):
            self.root.destroy()


MyGUI()
