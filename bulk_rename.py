from tkinter import Tk, Label, Button, Text, Entry, Checkbutton, IntVar
from tkinter import N, E, W, NW, END

import os
import re

class BulkRename:
    def __init__(self, master):
        self.master = master
        master.title("SDL Rename Tool")

        self.filenames_label = Label(master, text="Old paths:")
        self.filenames_label.grid(row=1, padx=10, sticky=W)

        self.newname_label = Label(master, text="New name:")
        self.newname_label.grid(row=1, column=2, padx=10, sticky=W)

        self.filenames = Text(master, width=50, height=10)
        self.filenames.grid(row=2, padx=10, pady=10, rowspan=2)

        self.newname = Entry(master)
        self.newname.grid(row=2, column=2, padx=10, pady=10, sticky=N)

        self.create_new_dir = IntVar()

        self.newdir = Checkbutton(master, text="Create new dir?", variable=self.create_new_dir)
        self.newdir.grid(row=3, column=2, padx=10, pady=10, sticky=NW)

        self.go = Button(master, text='Rename', command=self.batch_rename)
        self.go.grid(row=4, pady=10, columnspan=3)

        self.copyright = Label(master, text='Created by Stardust Labs')
        self.copyright.grid(row=5, column=2, sticky=E)

        self.status = Label(master, text='Ready')
        self.status.grid(row=5, sticky=W)

    def retrieve(self):
        return self.filenames.get('1.0', END).replace('"', '').split('\n')

    def rename(self, old, new, abspath, newdir=False):
        if newdir:
            oldpath = abspath.split('\\')
            oldpath.pop()
            oldpath.pop()
            oldpath = '\\'.join(oldpath) + '\\'
            oldname = oldpath + old
        else:
            oldname = abspath + old
        newname = abspath + new
        os.rename(oldname, newname)

    def get_filetype_from_address(self, file):
        filetype = file.split('\\')
        filetype = filetype[len(filetype)-1].split('.')
        filetype = filetype[len(filetype)-1]
        return filetype

    def get_filename_from_address(self, file):
        file = file.split('\\')
        return file[len(file)-1]

    def get_abspath_from_address(self, file):
        file = file.split('\\')
        file.pop()
        return '\\'.join(file)+'\\'

    def batch_rename(self):
        try:
            input_array = self.retrieve()
            input_array.pop()
            new_name = self.newname.get()

            counter = 1
            if self.create_new_dir.get():
                for file in input_array:
                    if counter == 1:
                        self.status.configure(text='Creating directory {}'.format(new_name))
                        abspath = self.get_abspath_from_address(file)
                        newdir = abspath + new_name + '\\'
                        os.mkdir(newdir)
                        self.status.configure(text='{} created'.format(new_name))
                    filetype = self.get_filetype_from_address(file)
                    abspath = self.get_abspath_from_address(file) + new_name + '\\'
                    file = self.get_filename_from_address(file)
                    new = new_name + ' ' + str(counter) + '.' + filetype
                    self.status.configure(text='Renaming {} to {}'.format(file, new))
                    self.rename(file, new, abspath, newdir=True)
                    counter += 1
            else:
                for file in input_array:
                    filetype = self.get_filetype_from_address(file)
                    abspath = self.get_abspath_from_address(file)
                    file = self.get_filename_from_address(file)
                    new = new_name + ' ' + str(counter) + '.' + filetype
                    self.status.configure(text='Renaming {} to {}'.format(file, new))
                    self.rename(file, new, abspath)
                    counter += 1
            self.status.configure(text='Files renamed')
        except:
            self.status.configure(text='Error')
        

root = Tk()
gui = BulkRename(root)
root.mainloop()
