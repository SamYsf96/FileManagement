import os
import glob
import shutil

community = ["Alura","ILA","ILBS","ILDB","ILHL","ILK","ILL","ILLWR","ILRP","ILS","ILSC","ILSL","ILT","ILWM","IRL"]
vendor_names = ["Ascen Workforce","Clipboard Health","Brightstar Care","ATC Healthcare","Maxim Healthcare","AMX Healthcare","AIT Staffing","Elite Medical Staffing","Intelycare"
                ,"Touchstone Homecare"]
community_qdrive = {'ILA':'Alpharetta', 'Alura':'Alura', 'ILBS':'Bonita Springs', 'ILDB':'Delray', 'ILHL':'Hidden Lakes','IRL':'Ivy Ridge','ILK':'Kenner','ILLWR':'Lakewood Ranch'
                    ,'ILL':'Lewisville', 'ILRP':'Royal Palm', 'ILS':'Sarasota', 'ILSL':'Sugar Land','ILSC':'Sun City','ILT':'Tampa','ILWM':'Windermere'}
date_range_2021 = ['12.','11.','10.','09.']
date_range_2022 = ['01.','02.','03.','04']



def copy_file(file,community_name):
    filedesc = file.split('\\')[-1]
    for i in vendor_names:
        if i in filedesc:
            if filedesc[-7:-4] == '.21':
                for j in date_range_2021:
                    if filedesc[-12:-9] == j:
                        name = os.path.basename(file)
                        destination = f"Q:\\{community_qdrive[community_name]}\\Executive Director\\Accounting & Finance\\Contract Labor\\{j}2021\\Invoices"
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


sort_through_files()
