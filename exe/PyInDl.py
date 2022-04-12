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
root = Tk()
root.title("instagram post saver")
root.geometry("400x300")
root.resizable(0,0)
root.config(bg="#121212")
#end of app page
inputfourm = Entry(root, width=30) #input post form(entery)
userinput = Entry(root, width=30)
passinput = Entry(root, width=30)
#download function
def pdl():
    link = inputfourm.get()  #get link from entery
    def download():
        if 'https://www.instagram.com/p/' in link: #check link
            try:
                username = userinput.get()
                if username == "0":
                    username = "pythondlapp"
                    password = "Ab66416670"
                else:
                    username = userinput.get()
                    password = passinput.get()
                location = filedialog.askdirectory()
                os.chdir(location)
                #set download location
                plink = link.replace('https://www.instagram.com/p/', '')
                plink = plink.replace('/', '')  
                #link to short code
                print(f"short code is {plink}")
                L = instaloader.Instaloader()
                L.login(username, password) 
                post = instaloader.Post.from_shortcode(L.context, plink)
                L.download_post(post, target=plink)
                messagebox.showinfo("complete", "download is complete")
                #download
            except:
                messagebox.showerror("eror", "مشکل در ادرس پست. (اگر ادرس درست است از رمز و پسوورد خودتان استفاده کنید)")
        else:
            messagebox.showerror("error", "ادرس پست مطعلق به اینستاگرام") #bad url error
    threading.Thread(target=download).start()  #download with exiting app
def creator():
    print("created by M.Sython")
    print("python 3.10")
    print("https://github.com/Msython")
    print("t.me/MSython")
#end of download function
#app opjects
posttext = Label(root, text="لینک پست", bg="#121212", fg="white") #text
usertext = Label(root, text="نام کاربری", bg="#121212", fg="white")
passtext = Label(root, text="پسوورد", bg="#121212", fg="white")
defulttext = Label(root, text="برای استفاده از یوزر و پسوورد پیشفرض 0 را وارد کنید", bg="#121212", fg="white", font=("arial", 10, "bold"))
posttext.grid(row=0, column=0, padx=10, pady=10) #text grid
usertext.grid(row=1, column=0, padx=10, pady=10) #text grid
passtext.grid(row=2, column=0, padx=10, pady=10) #text grid
defulttext.grid(row=3, column=1, padx=10, pady=10)
inputfourm.grid(row=0, column=1) #input post fourm grid
userinput.grid(row=1, column=1) 
passinput.grid(row=2, column=1)
dlbtn = Button(root, text="دانلود", bg="#121212", fg="white", borderwidth=5, command=pdl) #download buttun
crbtn = Button(root, text="سازنده : M.Sython", bg="#121212", fg="white", borderwidth=5, command=creator) #creator buttun
exitbtn = Button(root, text="خروج", bg="#121212", fg="white", borderwidth=5, command=root.destroy) #exit buttun
dlbtn.place(relx=0.3, rely=0.7, anchor="c") #download button gride
crbtn.place(relx=0.8, rely=0.7, anchor="c") #creator buttun gride
exitbtn.place(relx=0.5, rely=0.9, anchor="c") #download buttun gride
root.mainloop() #end of app