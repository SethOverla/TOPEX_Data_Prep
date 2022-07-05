from asyncore import close_all
from encodings import utf_8
from genericpath import exists
from importlib.resources import path
import pandas as pd
import os.path

# Identifying our variables, user_path being the Desktop of the current user and in_file representing the included sample file stored on the desktop. The 'Desktop' term can be swapped for another location i.e. 'Documents'.
user_path = os.path.join(os.path.expanduser('~'), 'Desktop')
in_file = os.path.join(user_path, 'Topex_Sample_File.csv')

# Calling panda to read our sample input file and create a dataframe.
df = pd.read_csv(in_file)

# This step is creating a multi-step loop that indexes each row iteration in our sample file. The first step searches for a "TOPEX_Output folder and creates one if there isn't one found. This is repeated for the actively indexed row "Course_Name" column as a sub folder with in the TOPEX_Output folder. After the folder is identified/created, the loop creates a utf_8 encoded text file of the "Comment" column based on the actively indexed row value.
for index, row in df.iterrows():
    out_folder = os.path.join(user_path, 'TOPEX_Output', row['Course_Name'])

    # Creating the path for the folders if they do not exist. The loop will continue if they do exist.
    if not os.path.exists(out_folder):
        os.makedirs(out_folder)

    # Creating the utf-8 encoded files within their respective folders and named by their unique identifiers.
    with open(os.path.join(out_folder, row["Comment_ID"] + ".txt"), "w") as out_file:
        out_file.write(row["Comment"])

# Confirmation message that the script has completed.
print('The export has completed.')

exit()
