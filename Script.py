import os
from datetime import datetime

path = "C:\\Users\\s_now\\Documents\\Script Folder"

print(os.listdir(path))

for fname in os.listdir(path):
    combined_path = os.path.join(path, fname)
    #print (combined_path)
    modification_time = os.path.getmtime(combined_path)
    #print (modification_time)
    if (fname.endswith(".txt")):
        dt_object = datetime.fromtimestamp(modification_time)
        print (combined_path, dt_object, modification_time)
        
    
    
