from scrapy import cmdline
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.geometry("320x200")
filePath = tk.StringVar()
tk.Label(root, text="文件路径：").grid(row=0, column=0)
tk.Entry(root, text=filePath).grid(row=0, column=1)
tk.Button(root, text="选择txt文本文件", command=lambda: filePath.set(filedialog.askopenfilename(filetypes=[('TXT', '*.txt')]))).grid(row=0, column=2)
tk.Button(root, text="OK", command=root.quit).grid(row=1, column=1)
root.mainloop()
cmd = "scrapy crawl sou -a fpath="+str(filePath.get())
cmdline.execute(cmd.split())
