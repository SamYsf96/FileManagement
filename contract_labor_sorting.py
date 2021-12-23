import os
import glob
import shutil

community = ["Alura","ILA","ILBS","ILDB","ILHL","ILK","ILL","ILLWR","ILRP","ILS","ILSC","ILSL","ILT","ILWM","IRL"]
vendor_names = ["Ascen Workforce","Clipboard Health","Brightstar Care","ATC Healthcare","Maxim Healthcare","AMX Healthcare","AIT Staffing","Elite Medical Staffing","Intelycare"]
community_qdrive = {'ILA':'Alpharetta', 'Alura':'Alura', 'ILBS':'Bonita Springs', 'ILDB':'Delray', 'ILHL':'Hidden Lakes','IRL':'Ivy Ridge','ILK':'Kenner','ILLWR':'Lakewood Ranch'
                    ,'ILL':'Lewisville', 'ILRP':'Royal Palm', 'ILS':'Sarasota', 'ILSL':'Sugar Land','ILSC':'Sun City','ILT':'Tampa','ILWM':'Windermere'}



def copy_file(file,community_name):
    filedesc = file.split('\\')[-1]
    for i in vendor_names:
        if i in filedesc and filedesc[-12:-9] == '12.':
            name = os.path.basename(file)
            destination = f"Q:\\{community_qdrive[community_name]}\\Executive Director\\Accounting & Finance\\Contract Labor\\12.2021\\Invoices"
            dest = os.path.join(destination,name)
            shutil.copyfile(file,dest)
        elif i in filedesc and filedesc[-12:-9] == '11.':
            name = os.path.basename(file)
            destination = f"Q:\\{community_qdrive[community_name]}\\Executive Director\\Accounting & Finance\\Contract Labor\\11.2021\\Invoices"
            dest = os.path.join(destination,name)
            shutil.copyfile(file,dest)
        elif i in filedesc and filedesc[-12:-9] == '10.':
            name = os.path.basename(file)
            destination = f"Q:\\{community_qdrive[community_name]}\\Executive Director\\Accounting & Finance\\Contract Labor\\10.2021\\Invoices"
            dest = os.path.join(destination,name)
            shutil.copyfile(file,dest)
    

def sort_through_files():
    for i in community:
        PATH = f"Y:\\Accounts Payable\\Invoices Community to Enter\\{i}"
        source = glob.glob(PATH + "/**/*.pdf", recursive=True)
        for f in source:
            copy_file(f,i)


sort_through_files()
