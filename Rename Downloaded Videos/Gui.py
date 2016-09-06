from Tkinter import *
from ttk import *
import tkMessageBox
import os
import re
import tkMessageBox as messageBox
from functools import partial


class Gui:
    def __init__(self):
        """ Create window set title and styles """
        self.gui = Tk()
        self.gui.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.gui.title(
            "File Renamer 2016 - Slightly Better than 2015 but DEFINITELY worth the upgrade - GIVE ME MONEY!")
        self.gui.iconbitmap("gui.ico")
        self.gui.state("zoomed")
        self.gui.style = Style()
        self.gui.style.theme_use("clam")

        ''' Create Styles '''
        self.gui.style.configure("Test.TFrame", background="white")
        self.gui.style.configure("Test.TLabel", background="#FDFDFD")

        ''' Create Top and Main content Frames and place them'''
        self.top_frame = Frame(self.gui, style="", pad=10)
        self.main_frame = Frame(self.gui, style="", )
        self.top_frame.place(x=0, y=0, relwidth=1.0, height=52)
        self.main_frame.place(x=0, y=55, relwidth=1.0, relheight=1.0)

        ''' Create Buttons and Entry for the Top Frame then place them'''
        self.User_Entry = Entry(self.top_frame)
        self.User_Submit = Button(self.top_frame, command=self.get_folder, text="Submit")
        self.User_Submit.place(relx=0.91, width=80)
        self.User_Entry.place(x=0, y=0, height=30, relwidth=0.9)

        ''' create input and output variables
            output stores all the information to be outputted and the modified data
            input stores all the information from the files it will rename'''
        self.output = []
        self.input = []

        ''' the file types that will be renamed'''
        self.file_types_to_rename = [".mp4", ".mkv", ".avi", ".srt", ".txt"]

        ''' the stuff we remove from files'''
        self.list_of_crap = ["x264-", "x264", "KILLERS", "[ettv]", "ASAP", "EVOLVE", "2HD", "1080p", "720p", "ShAaNiG",
                             "AAC", "BATV", "WEB-DL", "XviD-", "FUM", "AFG", "MGD", "PROPER", "HDTV", "BRrip", "BrRip",
                             "brrip", "BDRip", "BR", "sujaidr", "DTS", "[ETRG]", "INTERNAL", "EXTERNAL", "Sujaidr",
                             "YIFY", "XViD-", "ETRG", "BluRay", "-JYK", "AC3", "YIFY+HI", "tomcat12"]

        ''' variable to store directory in'''
        self.directory = ""

        '''begin running gui'''
        self.redraw()
        self.gui.mainloop()

    def get_folder(self):
        user_inputted_directory = self.User_Entry.get()
        if not user_inputted_directory:
            tkMessageBox.showinfo("Warning", "{} Please Enter A String".format(user_inputted_directory))
        else:
            if os.path.isdir(user_inputted_directory):
                self.directory = user_inputted_directory
                self.update()
            else:
                messageBox.showerror("Error", "Please Select a Valid File Directory")

    def update(self):
        self.get_files(self.directory)
        for all in self.input:
            temp = {"Frame": Frame(self.main_frame, width=self.gui.winfo_width(), height=40, style="Test.TFrame"),
                    "Path": all[0], "RelPath": all[1], "Old": all[2], "New": all[3]}
            temp["LabelPath"] = Label(temp["Frame"], text=temp["RelPath"], style="Test.TLabel")
            temp["LabelOld"] = Label(temp["Frame"], text=temp["Old"], style="Test.TLabel")
            temp["EntryNew"] = Entry(temp["Frame"])
            temp["Submit"] = Button(temp["Frame"], text="Submit", command=partial(self.do_something, len(self.output)))
            temp["EntryNew"].insert(END, temp["New"])
            self.output.append(temp)

    def redraw(self):
        if self.output:
            y_location = 5
            for all in self.output:
                all["Frame"].place(y=y_location, relwidth=1.0, height=40, x=0)
                all["LabelPath"].place(relx=0.05, y=5, relwidth=0.1, height=30)
                all["LabelOld"].place(relx=0.35, y=5, relwidth=0.1, height=30)
                all["EntryNew"].place(relx=0.65, y=5, relwidth=0.1, height=30)
                all["Submit"].place(relx=0.85, y=5, relwidth=0.1, height=30)
                y_location += 45
        else:
            print "waiting for user"
        self.gui.after(1000, self.redraw)

    def run(self):
        self.redraw()
        self.g.mainloop()

    def do_something(self, place):
        self.output[place]["New"] = self.output[place]["EntryNew"].get()
        self.rename(self.output[place]["Path"], self.output[place]["Old"], self.output[place]["New"])

    @staticmethod
    def rename(path, old, new):
        print "{} renamed to {} in the {} folder".format(old, new, path)
        os.rename(os.path.join(path, old), os.path.join(path, new))

    def get_files(self, directory):
        if os.path.isdir(directory):
            for each_thing in os.listdir(directory):
                if os.path.isdir(os.path.join(directory, each_thing)):
                    self.get_files(os.path.join(directory, each_thing))
                elif os.path.isfile(os.path.join(directory, each_thing)):
                    names = self.name_changer(directory, each_thing)
                    self.input.append([directory, os.path.relpath(directory, self.directory), names[1], names[2]])

    def name_changer(self, path, name):
        new = name
        extension = name[-4::1]
        new = new.replace(extension, " ")
        checkseason = re.search("S[0-9][0-9]E[0-9][0-9]", new)
        if checkseason:
            new = new.replace(".", " ")
            findseasonepisodes = re.search("S[0-9][0-9]E[0-9][0-9]", new).start()
            season = re.sub("(?i)s", "Season ", new[findseasonepisodes:findseasonepisodes + 3])
            episode = re.sub("(?i)E", " Episode ", new[findseasonepisodes + 3:findseasonepisodes + 6])

            new = "{}{}{}{}".format(new[0:findseasonepisodes], season, episode, extension)
        else:
            new = new.replace(".", " ")
            for a in self.list_of_crap:
                new = new.replace(a, " ")
            new = re.sub("(19|20)\d{2}", " ", new)
            new = "{}{}".format(new, extension)
        return [path, name, new]

    def on_closing(self):
        if messageBox.askokcancel("Quit", "Do you want to quit?"):
            self.gui.destroy()


x = Gui()
