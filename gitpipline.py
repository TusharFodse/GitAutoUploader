import tkinter as tk
import os
import subprocess
from tkinter import filedialog
from github import Github
from plyer import notification


Token="Enter Your Token (Classic)"

root=tk.Tk()
root.geometry("600x400")
file_contet=[]

def open_dir():
    file_path=filedialog.askdirectory(initialdir="C:\\")
    print(repo_name.get())
    reponame=repo_name.get()
   
    print(file_path)
    print(type(file_path))
    directory=os.listdir(file_path)
    print(directory)
    
    g=Github(Token)
    user=g.get_user()
    print(user)
    repo=user.create_repo(
        name=reponame,
        private=False
    )
    print(f"Repositry created at {repo}")
    os.chdir(file_path)
    try:
        subprocess.run(["git","init"])
        subprocess.run(["git","remote","add",".",f"https://github.com/User Name/{reponame}"])#User Name
        print("Adding files, committing, and pushing to GitHub...")
        subprocess.run(["git", "add", "."])
        subprocess.run(["git", "commit", "-m", "Initial commit"])
        subprocess.run(["git", "branch", "-M", "main"]) 
        subprocess.run(["git", "push", "-u", "origin", "main"])
        print("Repositry created")
        notification.notify(title="Repositry Creted",message="You Created Repositry", timeout=2)
    except:
        print("Problem is occor "+Exception)
        

    


repo_name=tk.StringVar()



repo_label=tk.Label(root,text="Repositry Name")
repo_label.pack(padx=20)
repo_inp=tk.Entry(root,textvariable=repo_name)
repo_inp.pack(padx=20)

button=tk.Button(root,text="Open Git",command=open_dir)
button.pack(padx=20)




root.mainloop()