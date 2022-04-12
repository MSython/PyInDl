#M.Sython14
#import librarys
from tkinter import messagebox 
from tkinter import filedialog
from tkinter import *
import os
import threading
import instaloader #pip install instaloader
#end of import
#create app page
root = Tk()  #create app
root.title("instagram post saver") #app title
root.geometry("400x300") #app window size
root.resizable(0,0) 
root.config(bg="#121212") #app bg
#end of app page
inputfourm = Entry(root, width=30) #input post form(entery) 
userinput = Entry(root, width=30) #get user
passinput = Entry(root, width=30) #get pass
#download function
def pdl():
    link = inputfourm.get()  #get link from entery
    def download():
        if 'https://www.instagram.com/p/' in link: #check link
            try:
                username = userinput.get() #get username
                if username == "0": #defult mode
                    username = "pythondlapp" #defult user
                    password = "Ab66416670" #defult pass
                else: #accunt mode
                    username = userinput.get()
                    password = passinput.get()
                location = filedialog.askdirectory() #select dirctory
                os.chdir(location)
                #set download location
                plink = link.replace('https://www.instagram.com/p/', '') 
                plink = plink.replace('/', '')  
                #link to short code
                print(f"short code is {plink}") #accept ShortCode
                L = instaloader.Instaloader() #download value
                L.login(username, password)  #user pass
                post = instaloader.Post.from_shortcode(L.context, plink) #download post value
                L.download_post(post, target=plink) # complete download
                messagebox.showinfo("complete", "download is complete") #show complete messege
                #download
            except:
                messagebox.showerror("eror", "check the shortcode of post. (or use accunt mode)")
        else:
            messagebox.showerror("error", "URL is wrong! not for instagram") #bad url error
    threading.Thread(target=download).start()  #download with exiting app
def creator():  #show program info
    print("created by M.Sython") #me :)
    print("python 3.10")
    print("https://github.com/Msython") #my github
    print("t.me/MSython") #my telegram
#end of download function
#app opjects
posttext = Label(root, text="postlink", bg="#121212", fg="white") #text
usertext = Label(root, text="username", bg="#121212", fg="white") 
passtext = Label(root, text="password", bg="#121212", fg="white")
defulttext = Label(root, text="type 0 to user to use without accunt mode", bg="#121212", fg="white", font=("arial", 10, "bold"))
posttext.grid(row=0, column=0, padx=10, pady=10) #text grid
usertext.grid(row=1, column=0, padx=10, pady=10) #text grid
passtext.grid(row=2, column=0, padx=10, pady=10) #text grid
defulttext.grid(row=3, column=1, padx=10, pady=10)
inputfourm.grid(row=0, column=1) #input post fourm grid
userinput.grid(row=1, column=1) 
passinput.grid(row=2, column=1)
dlbtn = Button(root, text="download", bg="#121212", fg="white", borderwidth=5, command=pdl) #download buttun
crbtn = Button(root, text="Created By : M.Sython", bg="#121212", fg="white", borderwidth=5, command=creator) #creator buttun
exitbtn = Button(root, text="exit", bg="#121212", fg="white", borderwidth=5, command=root.destroy) #exit buttun
dlbtn.place(relx=0.3, rely=0.7, anchor="c") #download button gride
crbtn.place(relx=0.8, rely=0.7, anchor="c") #creator buttun gride
exitbtn.place(relx=0.5, rely=0.9, anchor="c") #download buttun gride
root.mainloop() #end of app
