import os, shutil
current_path = os.getcwd()
file_list = [x for x in os.listdir(current_path)]
file_dict = {'.jpg': 'Image', '.mp4': 'Videos', '.py': 'Scripts'}
file_keys = tuple([x for x in file_dict])
for postfix in file_list:
    if postfix.endswith(file_keys):
        # print(postfix) #checking the files having the file_keys in the current directory 
        try: 
            os.makedirs(file_dict['.'+postfix.split('.')[1]]) #make directory if the directory is not already present
            shutil.move(postfix,file_dict['.'+postfix.split('.')[1]]+'/' + postfix) #move the files in the newly created directory
        except: shutil.move(postfix,file_dict['.'+postfix.split('.')[1]]+'/' + postfix)