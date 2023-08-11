

# PROGRAMMING AND ALGIRITHMS 2
# NAME = Rahul Kumar Thakur
# STUDENT ID = 220135
# COURSEWORK ASSIGNMENT = 1
#                         MENU DRIVEN PORT SCANNER

from tkinter import *
import customtkinter as rt
import socket
from tkinter import messagebox

rt.set_appearance_mode("dark")

window = rt.CTk()
window.title("Port Scanner")
window.geometry("670x480")
window.iconbitmap('C:\\Users\\rahul\Downloads\\bug.ico') # Adding icon to title bar.

name_entry = None  # Initialize these variables at the beginning
occupation_entry = None
address_entry = None

def nw():
    global name_entry, occupation_entry, address_entry  # Declare these variables as global

    root = rt.CTk()
    root.geometry("220x200")
    root.iconbitmap('C:\\Users\\rahul\\Downloads\\bug.ico')
    root.title("Data Entry")

    # Create labels and entry fields
    name_label = rt.CTkLabel(root, text="Enter name:")
    name_label.pack()

    name_entry = rt.CTkEntry(root)
    name_entry.pack()

    occupation_label = rt.CTkLabel(root, text="Enter occupation:")
    occupation_label.pack()

    occupation_entry = rt.CTkEntry(root)
    occupation_entry.pack()

    address_label = rt.CTkLabel(root, text="Enter address:")
    address_label.pack()

    address_entry = rt.CTkEntry(root)
    address_entry.pack()

    # Create a save button
    save_button = rt.CTkButton(root, text="Save to File", command=save_to_file)  # Remove the parentheses
    save_button.pack()

    root.mainloop()

def save_to_file():
    global name_entry, occupation_entry, address_entry  # Declare these variables as global

    name = name_entry.get()
    occupation = occupation_entry.get()
    address = address_entry.get()

    if name and occupation and address:
        with open('Question2.txt', 'a') as file:
            file.write(f'Name: {name}\n')
            file.write(f'Occupation: {occupation}\n')
            file.write(f'Address: {address}\n')

        messagebox.showinfo("Success", "Data has been saved to the file.")
    else:
        messagebox.showerror("Error", "Please fill in all fields.")

def Window_Third():

    for widget in window.winfo_children():
        widget.destroy()
    text_area = rt.CTkTextbox(window)
    text_area.configure(width=415, height=230)
    text_area.pack(pady=46)
    text_area.configure(font=("Arial", 15))

def Window_Two():
    for widget in window.winfo_children():
        widget.destroy()

    text2 = rt.CTkLabel(window, text="Your scanning options are:",
                        font=('Helvetica', 19, 'bold'))
    text2.pack(pady=4)

    single_port_button = rt.CTkButton(
        window, text="single port scan", command=fourth_window, font=('Helvetica', 15))

    single_port_button.pack(pady=15)

    multi_port_button = rt.CTkButton(
        window, text="Multi ports Scan ", command=fifth_window, font=('Helvetica', 15))

    multi_port_button.pack(pady=15)

    range_port_button = rt.CTkButton(
        window, text="Range Scan", command=sixth_window, font=('Helvetica', 15))

    range_port_button.pack(pady=15)

    all_port_button = rt.CTkButton(window, text="scan all the ports of the given target",
                                   command=seventh_window, font=('Helvetica', 15))
    all_port_button.pack(pady=15)

    back = rt.CTkButton(window, text="Home Page",
                        command=first, font=('Helvetica', 15))
    back.pack(pady=15)

    exit_button = rt.CTkButton(
        window, text="Exit the program", command=terminate, font=('Helvetica', 15))
    exit_button.pack(pady=15)


def first():
    for widget in window.winfo_children():
        widget.destroy()

    text1 = rt.CTkLabel(window, text="Programming and Algorithms 2",
                        font=('Baguet Script', 45, 'bold'))
    text1.pack(pady=30)

    text1 = rt.CTkLabel(window, text="Port Scanner & User Info Entry",
                        font=('Dreaming Outloud Script Pro', 34, 'bold'))
    text1.pack(pady=12)

    text2 = rt.CTkLabel(window, text="Created by Rahul Kumar Thakur",
                        font=('MV Boli', 20, 'italic'))
    text2.pack(pady=4)

    mymenu = Menu(window)
    m = Menu(mymenu, tearoff=0)
    # m.add_command(label="new text file", command=ntf)
    m.add_command(label="Saving User info", command=nw)
    m.add_command(label="Single Port Scan", command=Window_Two)
    m.add_separator()
    m.add_command(label="Close", command=quit)
    window.config(menu=mymenu)
    mymenu.add_cascade(label="Options", menu=m)

first()


def singleportinput(ip_entry, port_entry, root):
    '''The function is used for scanning the single port of the
    given target through the user input.'''

    open_number = 0
    close_number = 0

    target = ip_entry.get()
    port = port_entry.get()

    if target == "" and port == "":
        messagebox.showerror('Error', "entry field can not be empty")

    else:
        open_number = 0
        close_number = 0

        if target.count(".") != 3 or port.isdigit() == False:
            messagebox.showerror(
                'Error', "Please enter a valid IP address and port number")
        else:
            text_area = rt.CTkTextbox(window)
            text_area.configure(width=400, height=250)
            text_area.pack(pady=46)
            text_area.configure(font=("Arial", 15))

            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = s.connect_ex((target, int(port)))
            if result == 0:
                text_area.insert(
                    rt.END, f"[-] The port {port} is open on {target}\n")
                open_number += 1

            else:
                text_area.insert(
                    rt.END, f"[-] The port {port} is closed on {target}\n")
                close_number += 1

            text_area.insert(rt.END, "\n")
            text_area.insert(
                rt.END, f"[-] The closed ports are {close_number} and open ports are {open_number}\n")
            text_area.insert(rt.END, "\n")
            text_area.insert(rt.END, "\n")
            text_area.insert(rt.END,
                             f"Scanning the singleport {port} of ip address {target} was successful !!!\n")

            s.close()
            back = rt.CTkButton(window, text="Take me back", command=Window_Two,
                                font=('Arial', 15))
            back.pack(pady=15)

            exit_button = rt.CTkButton(
                window, text="Exit the program", command=terminate, font=('Helvetica', 15))
            exit_button.pack(pady=15)

            root.destroy()


def fourth_window():

    root = rt.CTk()
    root.geometry("200x150")
    root.iconbitmap('C:\\Users\\rahul\Downloads\\bug.ico')
    for widget in window.winfo_children():
        widget.destroy()
    ip_label = rt.CTkLabel(root, text="IP Address:")
    ip_label.pack()

    ip_entry = rt.CTkEntry(root)
    ip_entry.pack()

    port_label = rt.CTkLabel(root, text="Port:")
    port_label.pack()

    port_entry = rt.CTkEntry(root)
    port_entry.pack()

    submit_button = rt.CTkButton(
        root, text="Submit", command=lambda: singleportinput(ip_entry, port_entry, root))
    submit_button.pack()

    root.mainloop()


def multiportinput(ip_entry, port_entry, root):
    '''The function is used for scanning the list of ports of the given target.'''
    print('\n')

    target = ip_entry.get()
    port_one = port_entry.get()

    if target == "" and port_one == "":
        messagebox.showerror('Error', "entry field can not be empty")

    else:
        open_number = 0
        close_number = 0

        if target.count(".") != 3:
            messagebox.showerror(
                'Error', "Please enter a valid IP address and port number")
        else:
            text_area = rt.CTkTextbox(window)
            text_area.configure(width=443, height=300)
            text_area.pack(pady=46)
            text_area.configure(font=("Arial", 15))

            ports_collection = port_one.replace(" ", ",")
            ports = ports_collection.split(',')

    # convert all elements to int
            ports = [int(i) for i in ports]
    # sort the ports using bubble sort
            for i in range(len(ports)):
                for j in range(0, len(ports)-i-1):
                    if ports[j] > ports[j+1]:
                        # sorting the range in ascending order using bubble sort
                        ports[j], ports[j+1] = ports[j+1], ports[j]

     # scan ports
            for port in ports:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                result = s.connect_ex((target, port))
                if result == 0:
                    text_area.insert(
                        rt.END, f"[-] The port {port} is open on {target}\n")
                    text_area.insert(rt.END, "\n")
                    open_number += 1
                else:
                    text_area.insert(
                        rt.END, f"[-] The port {port} is closed on {target}\n")
                    text_area.insert(rt.END, "\n")
                    close_number += 1

            text_area.insert(
                rt.END, f"[-] The closed ports are {close_number} and open ports are {open_number}\n")
            text_area.insert(rt.END, "\n")
            text_area.insert(rt.END, "\n")
            text_area.insert(rt.END,
                             f"Scanning the multiports {ports} of ip address {target} was successful !!!\n")

            s.close()
            back = rt.CTkButton(window, text="Take me back", command=Window_Two,
                                font=('Helvetica', 15))
            back.pack(pady=15)

            exit_button = rt.CTkButton(
                window, text="Exit the program", command=terminate, font=('Helvetica', 15))
            exit_button.pack(pady=15)

            root.destroy()


def fifth_window():

    root = rt.CTk()
    root.geometry("320x190")
    root.iconbitmap('C:\\Users\\rahul\Downloads\\bug.ico')
    for widget in window.winfo_children():
        widget.destroy()
    ip_label = rt.CTkLabel(root, text="IP Address:")
    ip_label.pack()

    ip_entry = rt.CTkEntry(root)
    ip_entry.pack()

    port_label = rt.CTkLabel(
        root, text="Port: Enter multiple ports seperated by ','")
    port_label.pack()

    port_entry = rt.CTkEntry(root)
    port_entry.pack()

    submit_button = rt.CTkButton(
        root, text="Submit", command=lambda: multiportinput(ip_entry, port_entry, root))
    submit_button.pack()

    root.mainloop()


def rangeportinput(ip_entry, port_entry, root):
    '''The function is used to scan the range of ports of the given target.'''
    print('\n')
    target = ip_entry.get()
    port_one = port_entry.get()

    if target == "" and port_one == "":
        messagebox.showerror('Error', "entry field can not be empty")

    else:
        op = 0
        cp = 0

        if target.count(".") != 3:
            messagebox.showerror(
                'Error', "enter a valid IP and port!")
        else:
            text_area = rt.CTkTextbox(window)
            text_area.configure(width=400, height=240)
            text_area.pack(pady=46)
            text_area.configure(font=("Arial", 15))
            ports_collection = port_one.replace(" " and ",", "-")
            ports = ports_collection.split('-')

        # Convert the ports to a list of integers
            ports = list(map(int, ports))
            swap = False

            for i in range(len(ports)):

                for j in range(len(ports)-1):

                    if ports[j] > ports[j+1]:

                        # Swap the ports
                        temp = ports[j]
                        ports[j] = ports[j+1]
                        ports[j+1] = temp
                        swap = True
                if swap == False:
                    break

    # helps to scan ports in ascending manner
            for i in range(int(ports[0]), int(ports[1])+1):
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                result = s.connect_ex((target, i))
                if result == 0:
                    text_area.insert(
                        rt.END, f"[-] The port {i} is open on {target}\n")
                    text_area.insert(rt.END, "\n")
                    op += 1
                else:
                    text_area.insert(
                        rt.END, f"[-] The port {i} is closed on {target}\n")
                    text_area.insert(rt.END, "\n")

                    cp += 1

                s.close()
            text_area.insert(
                rt.END, f"[-] The closed ports are {cp} and open ports are {op}\n")

            text_area.insert(rt.END, "\n")
            text_area.insert(rt.END, "\n")
            text_area.insert(rt.END,
                             f"Scanning the ports of specific range of user choice of ip address {target} was successful !!!\n")
            back = rt.CTkButton(window, text="Take me back", command=Window_Two,
                                font=('Helvetica', 15))
            back.pack(pady=15)

            exit_button = rt.CTkButton(
                window, text="Exit the program", command=terminate, font=('Helvetica', 15))
            exit_button.pack(pady=15)

            root.destroy()


def sixth_window():

    root = rt.CTk()
    root.geometry("320x190")
    root.iconbitmap('C:\\Users\\rahul\Downloads\\bug.ico')
    for widget in window.winfo_children():
        widget.destroy()
    ip_label = rt.CTkLabel(root, text="IP Address:")
    ip_label.pack()

    ip_entry = rt.CTkEntry(root)
    ip_entry.pack()

    port_label = rt.CTkLabel(
        root, text="Port: Enter range of ports seperated by '-'")
    port_label.pack()

    port_entry = rt.CTkEntry(root)
    port_entry.pack()

    submit_button = rt.CTkButton(
        root, text="Submit", command=lambda: rangeportinput(ip_entry, port_entry, root))
    submit_button.pack()

    root.mainloop()


def allportscan(ip_entry, root):
    '''The function is used to scan all the ports of the given target.'''
    print('\n')

    target = ip_entry.get()
    if target == "":
        messagebox.showerror('Error', "entry field can not be empty")
    else:
        op = 0
        cp = 0
        if target.count(".") != 3:
            messagebox.showerror(
                'Error', "Please enter a valid IP address and port number")
        else:
            text_area = rt.CTkTextbox(window)
            text_area.configure(width=379, height=210)
            text_area.pack(pady=46)
            text_area.configure(font=("Arial", 15))

            for port in range(1, 65536):
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                result = s.connect_ex((target, port))
                if result == 0:
                    text_area.insert(
                        rt.END, f"[-] The port {port} is open on {target}\n")
                    text_area.insert(rt.END, "\n")

                    op += 1

                else:
                    text_area.insert(
                        rt.END, f"[-] The port {port} is closed on {target}\n")
                    text_area.insert(rt.END, "\n")

                    cp += 1
                s.close()
                text_area.insert(rt.END, "\n")
                text_area.insert(rt.END, "\n")
                text_area.insert(rt.END,
                                 f"Scanning the ports of specific range of user choice of ip address {target} was successful !!!\n")
                back = rt.CTkButton(window, text="Take me back", command=Window_Two,
                                    font=('Helvetica', 15))
                back.pack(pady=15)

                exit_button = rt.CTkButton(
                    window, text="Exit the program", command=terminate, font=('Helvetica', 15))
                exit_button.pack(pady=15)
                root.destroy()


def seventh_window():

    root = rt.CTk()
    root.geometry("220x150")
    root.iconbitmap('C:\\Users\\rahul\Downloads\\bug.ico')
    for widget in window.winfo_children():
        widget.destroy()
    ip_label = rt.CTkLabel(
        root, text="IP Address: Enter IP address of your choice")
    ip_label.pack()

    ip_entry = rt.CTkEntry(root)
    ip_entry.pack()

    submit_button = rt.CTkButton(
        root, text="Submit", command=lambda: allportscan(ip_entry, root))
    submit_button.pack()

    root.mainloop()


def terminate():
    exit()
window.mainloop()