from __future__ import unicode_literals
import youtube_dl
import tkinter as tk

def dn():
    a = chk.get()
    if a == 1:
        yt = link.get()
        ydl_opts = {
           'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
                }],
            }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            try:
                ydl.download([yt])
            except:
                import tkinter.messagebox as m
                m.showerror('ERROR', 'ERROR, Link may invalid.')
    else:
        yt = link.get()
        ydl_opts = {}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            try:
                ydl.download([yt])
            except:
                import tkinter.messagebox as m
                m.showerror('ERROR', 'ERROR, Link may invalid.')     

def clear():
    link.delete(0, "end")
    link.insert(0, "")
root = tk.Tk()
root.resizable(False, False)
root.title('YT Vid Downloader')
link = tk.Entry(root, text='Link')
link.grid(row=0)
b = tk.Button(root, text='Download', command=dn)
b.grid(row=1, column=0)
chk = tk.IntVar()
cbox = tk.Checkbutton(root, text='Download MP3',variable=chk, onvalue=1, offvalue=0)
cbox.grid(row=1, column=2)
b1 = tk.Button(root, text='Clear', command=clear)
b1.grid(row=1, column=1)
root.mainloop()