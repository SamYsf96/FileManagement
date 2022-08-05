from fileinput import close
from ntpath import join
import os
import glob
import shutil
from tkinter import *
import tkinter
import tkinter.messagebox





community = ["Alura","ILA","ILBS","ILDB","ILHL","ILK","ILL","ILLWR","ILRP","ILS","ILSC","ILSL","ILT","ILWM","IRL"]
vendor_names = ["Ascen Workforce","Clipboard Health","Brightstar Care","ATC Healthcare","Maxim Healthcare","AMX Healthcare","AIT Staffing","Elite Medical Staffing","Intelycare"
                ,"Touchstone Homecare","Nurseio","Coastal Care","A Perfect Choice", "Acute Quality Staffing", "AAA Apartment Staffing", "Myra Winn", "Texas Nursing"]
community_qdrive = {'ILA':'Alpharetta', 'Alura':'Alura', 'ILBS':'Bonita Springs', 'ILDB':'Delray', 'ILHL':'Hidden Lakes','IRL':'Ivy Ridge','ILK':'Kenner','ILLWR':'Lakewood Ranch'
                    ,'ILL':'Lewisville', 'ILRP':'Royal Palm', 'ILS':'Sarasota', 'ILSL':'Sugar Land','ILSC':'Sun City','ILT':'Tampa','ILWM':'Windermere'}
date_range_2021 = ['12.','11.']
date_range_2022 = ['01','02.','03.','04.','05.','06.','07','08','09','10','11','12']



def copy_file(file,community_name):
    filedesc = str(file.split('\\')[-1]).upper()
    for i in vendor_names:
        if i.upper() in filedesc:
            if filedesc[-7:-4] == '.21':
                for j in date_range_2021:
                    if filedesc[-12:-9] == j:
                        name = os.path.basename(file)
                        destination = f"Q:\\{community_qdrive[community_name]}\\Executive Director\\Accounting & Finance\\Contract Labor\\2021\\{j}2021\\Invoices"
                        dest = os.path.join(destination,name)
                        shutil.copyfile(file,dest)
            elif filedesc[-7:-4] == '.22':
                for j in date_range_2022:
                    if filedesc[-12:-9] == j:
                        name = os.path.basename(file)
                        destination = f"Q:\\{community_qdrive[community_name]}\\Executive Director\\Accounting & Finance\\Contract Labor\\2022\\{j}2022\\Invoices"
                        dest = os.path.join(destination,name)
                        shutil.copyfile(file,dest)


def sort_through_files():
    for i in community:
        PATH = f"Y:\\Accounts Payable\\Invoices Community to Enter\\{i}"
        source = glob.glob(PATH + "/**/*.pdf", recursive=True)
        for f in source:
            copy_file(f,i)
    tkinter.messagebox.showinfo("Confirmation", "All Done")


def show_vendors():
    win = Tk()
    win.title("Vendors")
    win.geometry("300x400+10+20")
    canvas = Canvas(win, width=300, height=500)
    canvas.create_text(150, 150, text="\n".join(vendor_names), fill="black", anchor=CENTER)
    canvas.pack()
    close_button = tkinter.Button(win, text="Close", command=win.destroy)
    close_button.place(relx=0.5, rely=0.9, anchor=CENTER)
    close_button.pack()
    win.mainloop()

window = Tk()
window.title('Contract Labor Sorting')
window.geometry("300x200+10+20")
show_vendor_button = tkinter.Button(window, text = "Show Vendors", command=show_vendors)
show_vendor_button.place(relx=0.5,rely=0.1, anchor=CENTER)
copy_vendors_button = tkinter.Button(window, text = "Copy Invoices",command=sort_through_files)
copy_vendors_button.place(relx = 0.5, rely = 0.5, anchor=CENTER)
quit_button = tkinter.Button(window, text="Quit", command=window.destroy)
quit_button.place(relx=0.5, rely=0.9, anchor=CENTER)
window.mainloop()
