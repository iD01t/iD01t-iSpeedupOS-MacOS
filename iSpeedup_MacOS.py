import subprocess
import tkinter as tk
import webbrowser
from PIL import ImageTk, Image

def execute_command(command):
    print(f"Executing command: {command}")
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    output = stdout.decode('utf-8') + stderr.decode('utf-8')
    return output

def passwords_off():
    output = execute_command("sudo bash pass.sh")
    print(output)
    output_box.insert(tk.END, "All OS Passwords are Disabled!\n")
    output_box.insert(tk.END, output + "\n")

def install_deps():
    output = execute_command("sudo nvram StartupMute=%01")
    print(output)
    output_box.insert(tk.END, "iSpeedup OS Dependencies installed!\n")
    output_box.insert(tk.END, output + "\n")

def install_heavy():
    output = execute_command("sudo bash heavy.sh")
    print(output)
    output_box.insert(tk.END, "Heavy Login Wallpaper is turned OFF!\n")
    output_box.insert(tk.END, output + "\n")

def install_remote():
    output = execute_command("sudo bash remote.sh")
    print(output)
    output_box.insert(tk.END, "Remote Access turned ON!\n")
    output_box.insert(tk.END, output + "\n")

def disable_lock():
    output = execute_command("sudo bash screen.sh")
    print(output)
    output_box.insert(tk.END, "Lock Screen is turned OFF!\n")
    output_box.insert(tk.END, output + "\n")

def install_updates():
    output = execute_command("sudo bash updates.sh")
    print(output)
    output_box.insert(tk.END, "Computer Updates are turned OFF!\n")
    output_box.insert(tk.END, output + "\n")

def install_motion():
    output = execute_command("sudo bash motion.sh")
    print(output)
    output_box.insert(tk.END, "Reduce Motion & Transparency are OFF!\n")
    output_box.insert(tk.END, output + "\n")

def performance_mode():
    output = execute_command("sudo bash performance.sh")
    print(output)
    output_box.insert(tk.END, "Performance mode is turned ON!\n")
    output_box.insert(tk.END, output + "\n")

root = tk.Tk()
root.title('')

frame = tk.Frame(root, width="788", height="444")
frame.pack(fill=tk.BOTH, expand=True)

bg_image = Image.open("background.png")
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = tk.Label(frame, width="788", height="444", image=bg_photo, bg="black")
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

cButton1 = tk.Button(frame, text="Turn OFF Startup Chime", command=install_deps, background="black", foreground="black", highlightbackground="black", highlightcolor="black")
cButton1.place(x=10, y=340)

cButton2 = tk.Button(frame, text="    Disable Passwords     ", command=passwords_off, background="black", foreground="black", highlightbackground="black", highlightcolor="black")
cButton2.place(x=595, y=380)

cButton3 = tk.Button(frame, text=" Motion & Transparency ", command=install_motion, background="black", foreground="black", highlightbackground="black", highlightcolor="black")
cButton3.place(x=205, y=380)

cButton4 = tk.Button(frame, text=" Enable Remote Access ", command=install_remote, background="black", foreground="black", highlightbackground="black", highlightcolor="black")
cButton4.place(x=595, y=340)

cButton7 = tk.Button(frame, text=" Disable screen locking ", command=disable_lock, background="black", foreground="black", highlightbackground="black", highlightcolor="black")
cButton7.place(x=403, y=380)

cButton8 = tk.Button(frame, text="      Disable Updates      ", command=install_updates, background="black", foreground="black", highlightbackground="black", highlightcolor="black")
cButton8.place(x=403, y=340)

link = tk.Label(root, text="Made by @iD01t_Dev", background="black", foreground="white", font=('Helvetica', 10), cursor="hand2")
link.place(x=668, y=425)

def open_link(event):
    webbrowser.open("https://www.youtube.com/watch?v=DKVB_CtU8XQ")

link.bind("<Button-1>", open_link)

cbeginExploit2 = tk.Button(frame, text="   Disable Heavy Login    ", command=install_heavy, background="black", foreground="black", highlightbackground="black", highlightcolor="black")
cbeginExploit2.place(x=205, y=340)

cbeginExploit3 = tk.Button(frame, text="    Performance Mode    ", command=performance_mode, background="black", foreground="black", highlightbackground="black", highlightcolor="black")
cbeginExploit3.place(x=10, y=380)

link = tk.Label(root, text="v0.1", background="black", foreground="white", font=('Helvetica', 10), cursor="hand2")
link.place(x=15, y=425)

def open_link(event):
    webbrowser.open("(link unavailable)")

link.bind("<Button-2>", open_link)



output_box = tk.Text(frame, width=107, height=7, background="black", foreground="white")
output_box.place(x=15, y=228)

root.geometry("788x444")
root.resizable(False, False)
root.eval('tk::PlaceWindow . center')
root.iconphoto(False, tk.PhotoImage(file='bootlogo (1).png'))

root.mainloop()


