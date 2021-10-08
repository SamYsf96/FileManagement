import os
import shutil
import glob

path = "Y:\Zip Files"
source = glob.glob(path + "/**/*.xlsx", recursive=True)


def fileMove(file):
    fileDesc = file.split('\\')[-1]
    if "Move-Out" in fileDesc:
        name = os.path.basename(file)
        destination = 'X:\Data_Analytics\Sales report\Yardi reports\Move Out'
        dest = os.path.join(destination, name)
        shutil.move(file, dest)
    elif "Move-In" in fileDesc:
        name = os.path.basename(file)
        destination = 'X:\Data_Analytics\Sales report\Yardi reports\Move In'
        dest = os.path.join(destination, name)
        shutil.move(file, dest)
    elif "12_Month_Rolling" in fileDesc:
        name = os.path.basename(file)
        destination = 'X:\Data_Analytics\Sales report\Yardi reports\Budget'
        dest = os.path.join(destination, name)
        shutil.move(file, dest)
    elif "Average_Daily_Census" in fileDesc and "_2" in fileDesc:
        name = os.path.basename(file)
        destination = 'X:\Data_Analytics\Sales report\Yardi reports\ADC 2'
        dest = os.path.join(destination, name)
        shutil.move(file, dest)
    elif "Average_Daily_Census" in fileDesc and "_2" not in fileDesc:
        name = os.path.basename(file)
        destination = 'X:\Data_Analytics\Sales report\Yardi reports\ADU'
        dest = os.path.join(destination, name)
        shutil.move(file, dest)
    elif "VSL_Resident_Days" in fileDesc:
        name = os.path.basename(file)
        destination = 'Y:\DSSI Transition\Data Uploads\Data Upload templates\Yardi reports'
        dest = os.path.join(destination, name)
        shutil.move(file, dest)
    elif "Unit_Roster" in fileDesc:
        name = os.path.basename(file)
        destination = "Y:\\Projects\M Miller\\Base_data\\Unit Rosters"
        dest = os.path.join(destination, name)
        shutil.move(file, dest)
    elif "Rent_Roll" in fileDesc:
        name = os.path.basename(file)
        destination = 'Y:\Projects\M Miller\Base_data\Rent Rolls'
        dest = os.path.join(destination, name)
        shutil.move(file, dest)

def loop_through_files():
    for f in source:
        fileMove(f)

loop_through_files()
