__author__ = '13123035 - Jordan Harman'
import os
import re

video_location = 0

folder = raw_input("Enter Folder Location")

file_types_to_rename = [".mp4", ".mkv", ".avi", ".srt"]

text_to_remove = ["x264-", "x264", "KILLERS", "[ettv]", "ASAP", "EVOLVE", "2HD", "1080p", "720p", "ShAaNiG", "AAC",
                  "BATV", "WEB-DL", "XviD-", "FUM", "AFG", "MGD", "PROPER", "HDTV", "BRrip", "BrRip", "brrip", "BDRip",
                  "BR", "sujaidr", "DTS", "[ETRG]", "INTERNAL", "EXTERNAL", "Sujaidr", "YIFY", "XViD-", "ETRG",
                  "BluRay",
                  "-JYK", "AC3", "YIFY+HI", "tomcat12", "[YTS AG]"]

if video_location is 0:
    video_location = folder

elif os.path.exists(video_location):
    video_location = video_location

else:
    exit("Location does not exist")


def recursive_rename(path):
    for each_folder in os.listdir(path):
        if os.path.isdir(os.path.join(path, each_folder)):
            recursive_rename(os.path.join(path, each_folder))
        elif os.path.isfile(os.path.join(path, each_folder)):
            extension = each_folder[-4::1]
            if extension in file_types_to_rename:
                rename_process(path, each_folder, extension)
            else:
                if not os.path.exists(
                        os.path.join(os.path.join(os.path.expanduser("~"), "Desktop"), "Files To Remove")):
                    os.makedirs(os.path.join(os.path.join(os.path.expanduser("~"), "Desktop"), "Files To Remove"))
                os.rename(os.path.join(path, each_folder), os.path.join(
                    os.path.join(os.path.join(os.path.expanduser("~"), "Desktop"), "Files To Remove"), each_folder))


def rename_process(path, name, extension):
    new = name
    new = new.replace(extension, " ")

    m = re.search("S[0-9][0-9]E[0-9][0-9]", new)
    if m:
        new = new.replace(".", " ")
        x = re.search("S[0-9][0-9]E[0-9][0-9]", new).start()
        season = re.sub("(?i)s", "Season ", new[x:x + 3])
        episode = re.sub("(?i)E", " Episode ", new[x + 3:x + 6])

        new = "{}{}{}{}".format(new[0:x], season, episode, extension)

    else:
        new = new.replace(".", " ")
        for a in text_to_remove:
            new = new.replace(a, " ")
        new = re.sub("(19|20)\d{2}", " ", new)
        new = "{}{}".format(new, extension)

    rename(path, name, new)


def rename(path, old, new):
    os.rename(os.path.join(path, old), os.path.join(path, new))


recursive_rename(video_location)
