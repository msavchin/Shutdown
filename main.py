import tkinter as tk
import os
import platform
import tkinter.messagebox as messagebox


def shutdown():
    time = int(time_entry.get()) * 60
    if time:
        current_platform = platform.system().lower()
        if current_platform == 'windows':
            exit_code = os.system(f"shutdown /s /t {time}")
            if exit_code == 0:
                messagebox.showinfo("Info", "The system will shut down in " + str(int(time_entry.get())) + " minutes")
            else:
                messagebox.showerror("Error", "The shutdown process has already been initiated")
        elif current_platform == 'linux':
            os.system(f"shutdown -h +{time}")
        elif current_platform == 'darwin':
            os.system(f"shutdown -h +{time}")
        else:
            messagebox.showerror("Error", "Unsupported platform")
    else:
        messagebox.showerror("Error", "Enter the required time")


def cancel_shutdown():
    current_platform = platform.system().lower()
    if current_platform == 'windows':
        os.system("shutdown /a")
    elif current_platform == 'linux':
        os.system("shutdown -c")
    elif current_platform == 'darwin':
        os.system("shutdown -c")
    elif current_platform == 'android':
        os.system("adb shell am start -n com.android.settings/.Settings")
    else:
        messagebox.showerror("Error", "Unsupported platform")


root = tk.Tk()
root.geometry("300x300")
root.resizable(False, False)
root.title("Shutdown App")
root.configure(bg="#202225")

time_label = tk.Label(root, text="Enter time in minutes:", font=('Arial', 12), bg="#202225", fg="white")
time_label.pack()

time_entry = tk.Entry(root, font=('Arial', 12), bg="#36393F", fg="white", insertbackground='white', borderwidth=0,
                      highlightthickness=0)
time_entry.place(relx=.5, rely=.3, anchor="center", width=200, height=30)
time_entry.insert(0, "Time")
time_entry.bind("<FocusIn>", lambda args: time_entry.delete('0', 'end'))

submit_button = tk.Button(root, text="Submit", font=('Arial', 12), bg="#7289DA", fg="white", command=shutdown,
                          borderwidth=0, highlightthickness=0, relief="solid", highlightcolor="white",
                          highlightbackground="white", activebackground="#7289DA", activeforeground="white", bd=2)
submit_button.place(relx=.5, rely=.5, anchor="center", width=200, height=30)

cancel_button = tk.Button(root, text="Cancel", font=('Arial', 12), bg="red", fg="white", command=cancel_shutdown,
                          borderwidth=0, highlightthickness=0, relief="solid", highlightcolor="white",
                          highlightbackground="white", activebackground="red", activeforeground="white", bd=2)
cancel_button.place(relx=.5, rely=.7, anchor="center", width=200, height=30)

root.mainloop()
