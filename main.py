import os 
Folders = os.listdir("NewF")
for i in Folders:
    print(i)
    print(os.listdir(f"NewF/{i}"))