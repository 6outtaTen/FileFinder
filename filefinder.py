import kivy
import tkinter.filedialog
kivy.require('1.9.1')
from kivy.config import Config
from kivy import Config
Config.set('graphics', 'multisamples', '0')
Config.set("graphics", "resizable", 0)
from kivy.core.window import Window
from  datetime import datetime
import os
import sys
import kivy
from kivy import graphics
import sys, os, os.path
from os import system, name
from kivy.uix.screenmanager import NoTransition
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import kivy.properties as kypros
from kivy.uix.popup import Popup
from kivy.uix.progressbar import ProgressBar
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
import tkinter as Tk
Tk.Tk().withdraw()




# VARS

try:
    scans_path = os.getcwd() + '\\scans'
    os.mkdir(scans_path)
except FileExistsError:
    pass
else:
    pass


try:
    logs_path = os.getcwd() + '\\logs'
    os.mkdir(logs_path)
except FileExistsError:
    pass
else:
    pass

try:
    config_path = os.getcwd() + '\\config'
    os.mkdir(config_path)
except FileExistsError:
    pass

try:
    single_path = os.getcwd() + '\\scans\\single_scan'
    os.mkdir(single_path)
except FileExistsError:
    pass
else:
    pass

try:
    specific_path = os.getcwd() + '\\scans\\specific_scans'
    os.mkdir(specific_path)
except FileExistsError:
    pass
else:
    pass


try:
    contains_path = os.getcwd() + '\\scans\\contains_scans'
    os.mkdir(contains_path)
except FileExistsError:
    pass
else:
    pass


try:
    contains_path = os.getcwd() + '\\scans\\starts_with_scans'
    os.mkdir(contains_path)
except FileExistsError:
    pass
else:
    pass


try:
    ends_path = os.getcwd() + '\\scans\\ends_with_scans'
    os.mkdir(ends_path)
except FileExistsError:
    pass
else:
    pass


failure = "Scan Failed... No files or folders found."
choice = ""
log_file_path_win = os.getcwd() + "\\scans"
count = 0
err_count = 0

# FUNCTIONS

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

def perform_check():

    md_file = open(f"{os.getcwd()}\\config\\usr_md_choice.txt", "a")
    md_file = open(f"{os.getcwd()}\\config\\usr_md_choice.txt", "r")



    md_file.seek(0)

    if "i" in md_file.read():
        return True

    else:
        return False

def get_logs_num():
    c = 0

    history_log = open(f"{os.getcwd()}\\logs\\history_log.txt", "a")
    history_log = open(f"{os.getcwd()}\\logs\\history_log.txt", "r")



    for line in history_log.readlines():
        str(line) # mock call to shut up Pylint
        c+=1
    return(c)


def invalid_path_or_sequence():
    pop = Popup(title="Invalid path or sequence", content=Label(text="Invalid path or sequence", font_size=18),
    size_hint=(None, None), size=(400, 400))

    pop.open()


def success_pop_up():
    global log_file_path_win
    success = "Done! \nFound " + str(count) + " files/folders" "\nA Log file has been created at "

    pop = Popup(title="Scan Complete!", content=Label(text=success + "\n" + log_file_path_win, font_size=20), size_hint=
    (None, None), size=(1000, 300))

    pop.open()


def fail_pop_up():
    pop = Popup(title="Fail", content=Label(text=failure, font_size=20), size_hint=(None, None), size=(400, 400))

    pop.open()


def check_for_success():
    log_file.seek(0)
    if "i" in log_file.read():
        return True

    else:
        return False


def init_pop_up():
    success = check_for_success()

    if success:
        success_pop_up()
        log_file.close()

    else:
        fail_pop_up()
        log_file.close()



# CLASSES

class ProgBar(BoxLayout):
    pass

class ChoiceWindow(Screen):

    def quit(self):
        pass

    def starts_with_mode(self):
        global choice
        choice = "starts_with"
        print("[DEBUG] Initiated " + choice + " mode")
        return choice

    def contains_mode(self):
        global choice
        choice = "contains"
        print("[DEBUG] Initiated " + choice + " mode")
        return choice

    def ends_with_mode(self):
        global choice
        choice = "ends_with"
        print("[DEBUG] Initiated " + choice + " mode")
        return choice

    def specific_mode(self):
        global choice
        choice = "specific"
        print("[DEBUG] Initiated" + choice + " mode")
        return choice

    def go_to_input(self):
        self.manager.current = "input"
        print("[DEBUG] Go to InputScreen")


class InputWindow(Screen):
    path = kypros.StringProperty()
    sequence = kypros.ObjectProperty(None)
    last_scan = kypros.StringProperty()
    status_one = kypros.StringProperty()
    status_two = kypros.StringProperty()
    current_mode = kypros.StringProperty()

    def mode_init(self):
        global choice
        if choice == "starts_with":
            self.current_mode = "Current search mode: Starts With"
            return self.current_mode

        elif choice == "contains":
            self.current_mode = "Current search mode: Contains"
            return self.current_mode

        elif choice == "ends_with":
            self.current_mode = "Current search mode: Ends With"
            return self.current_mode

        else:
            self.current_mode = "Current search mode: Specific"
            return self.current_mode

    def get_path(self):
        path_tk = tkinter.filedialog.askdirectory()
        return path_tk

    def check_md(self):
        choice_file = open(f"{os.getcwd()}\\config\\usr_md_choice.txt", "a")
        choice_file = open(f"{os.getcwd()}\\config\\usr_md_choice.txt", "r")

        if "i" in choice_file.readlines():
            self.status_one = "Turn OFF"
            self.status_two = "Turn ON"
        else:
            self.status_one = "Turn ON"
            self.status_two = "Turn OFF"

    def reset(self):
        global count
        self.sequence.text = ""
        count = 0
        print("[DEBUG] Reset Complete")


    def init_history(self):
        history_log = open(f"{os.getcwd()}\\logs\\history_log.txt", "r")
        line_count = get_logs_num()
        lines = []

        for line in history_log.readlines():
            lines.append(line)
        try:
            self.last_scan = lines[line_count-1]
        except IndexError:
            self.last_scan ="No last scans"
            print(f"[DEBUG] {self.last_scan}")
            return self.last_scan
        else:
            print(f"[DEBUG] {self.last_scan}")
            return self.last_scan


    def search_starts_with(self, path, sequence):
        print("[DEBUG] Initiated starts_with scan")
        global count, log_file, history_log, err_count


        sep_or_sngl = perform_check()

        if sep_or_sngl:


            count_file = open(f"{os.getcwd()}\\config\\logs_count.txt", "a")
            count_file = open(f"{os.getcwd()}\\config\\logs_count.txt", "r")
            logs_count = 0

            for line in count_file.readlines():
                str(line) # mock call to shut up Pylint
                logs_count+=1

            log_file = open(f'{os.getcwd()}\\scans\\starts_with_scans\\starts_with_scan_results_{logs_count}', 'w+')
            history_log = open(f'{os.getcwd()}\\logs\\history_log.txt', 'a')


        else:
            log_file = open(f"{os.getcwd()}\\scans\\single_scan\\scan_results.txt", "w+")


        for folder, sub_folders, files in os.walk(path):

            for sub_fold in sub_folders:
                if sub_fold.startswith(sequence):
                    count += 1
                    curr_path = os.path.join(folder, sub_fold)
                    print(f'Found! Folder: {sub_fold} \n')
                    try:
                        log_file.write(f'FOLDER: {sub_fold} AT {curr_path} \n')
                    except UnicodeEncodeError:
                        err_count += 1
                        continue
                    else:
                        pass

                else:
                    continue

            for f in files:
                if f.startswith(sequence):
                    count += 1
                    curr_path = os.path.join(folder, f)
                    print(f'\tFound! File: {f} \n')
                    try:
                        log_file.write(f'FILE: {f} AT {curr_path} \n')
                    except UnicodeEncodeError:
                        err_count += 1
                        continue
                    else:
                        pass

        if err_count == 1:
            print(f"[DEBUG] Caught {err_count} UnicodeEncodError")
        else:
            print(f"[DEBUG] Caught {err_count} UnicodeEncode errors")

        date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")


        history_log = open(f"{os.getcwd()}\\logs\\history_log.txt", "a")



        history_log.write(f"""{date} You searched for files/folders that start with "{sequence}" in {path} and got {count} results\n""")
        history_log.close()


        count_file = open(f"{os.getcwd()}\\config\\logs_count.txt", "a")



        count_file.write("DO NOT DELETE ANY OF THE LINES\n")

        init_pop_up()

    def search_contains(self, path, sequence):
        global count, log_file, history_log, err_count
        print("[DEBUG] Initiated contains scan")
        sep_or_sngl = perform_check()

        if sep_or_sngl:


            count_file = open(f"{os.getcwd()}\\config\\logs_count.txt", "a")
            count_file = open(f"{os.getcwd()}\\config\\logs_count.txt", "r")
            logs_count = 0

            for line in count_file.readlines():
                str(line) # mock call to shut up Pylint
                logs_count+=1

            log_file = open(f'{os.getcwd()}\\scans\\contains_scans\\contains_scan_results_{logs_count}', 'w+')
            history_log = open(f'{os.getcwd()}\\logs\\history_log.txt', 'a')

        else:

            log_file = open(f"{os.getcwd()}\\scans\\single_scan\\scan_results.txt", "w+")

        for folder, sub_folders, files in os.walk(path):

            for sub_fold in sub_folders:
                if sequence in sub_fold:
                    count += 1
                    curr_path = os.path.join(folder, sub_fold)
                    print(f'Found! Folder: {sub_fold} \n')
                    try:
                        log_file.write(f'FOLDER: {sub_fold} AT {curr_path} \n')
                    except UnicodeEncodeError:
                        err_count += 1
                        continue
                    else:
                        pass

                else:
                    continue

            for f in files:
                if sequence in f:
                    count += 1
                    curr_path = os.path.join(folder, f)
                    print(f'\t Found! File: {f} \n')
                    try:
                        log_file.write(f'FILE: {f} AT {curr_path} \n')
                    except UnicodeEncodeError:
                        err_count += 1
                        continue
                    else:
                        pass

        if err_count == 1:
            print(f"[DEBUG] Caught {err_count} UnicodeEncodError")
        else:
            print(f"[DEBUG] Caught {err_count} UnicodeEncode errors")

        date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")


        history_log = open(f"{os.getcwd()}\\logs\\history_log.txt", "a")


        history_log.write(f"""{date} You searched for files/folders that contain "{sequence}" in {path} and got {count} results\n""")
        history_log.close()


        count_file = open(f"{os.getcwd()}\\config\\logs_count.txt", "a")
        count_file.write("DO NOT DELETE ANY OF THE LINES\n")


        init_pop_up()


    def search_ends_with(self, path, sequence):
        print("[DEBUG] Initiated ends_with scan")
        global count, log_file, history_log, err_count
        sep_or_sngl = perform_check()
        if sep_or_sngl:

            count_file = open(f"{os.getcwd()}\\config\\logs_count.txt", "a")
            count_file = open(f"{os.getcwd()}\\config\\logs_count.txt", "r")
            logs_count = 0

            for line in count_file.readlines():
                str(line) # mock call to shut up Pylint
                logs_count+=1

            log_file = open(f'{os.getcwd()}\\scans\\ends_with_scans\\ends_with_scan_results_{logs_count}', 'w+')
            history_log = open(f'{os.getcwd()}\\logs\\history_log.txt', 'a')

        else:
            log_file = open(f"{os.getcwd()}\\scans\\single_scan\\scan_results.txt", "w+")

        for folder, sub_folders, files in os.walk(path):

            for sub_fold in sub_folders:
                if sub_fold.endswith(sequence):
                    count += 1
                    curr_path = os.path.join(folder, sub_fold)
                    print(f'Found! Folder: {sub_fold} \n')
                    try:
                        log_file.write(f'FOLDER: {sub_fold} AT {curr_path} \n')
                    except UnicodeEncodeError:
                        err_count += 1
                        continue
                    else:
                        pass

                else:
                    continue

            for f in files:
                if f.endswith(sequence):
                    count += 1
                    curr_path = os.path.join(folder, f)
                    print(f'\t Found! File: {f} \n')
                    try:
                        log_file.write(f'FILE: {f} AT  {curr_path}\n')
                    except UnicodeEncodeError:
                        err_count += 1
                        continue
                    else:
                        pass

        if err_count == 1:
            print(f"[DEBUG] Caught {err_count} UnicodeEncodError")
        else:
            print(f"[DEBUG] Caught {err_count} UnicodeEncode errors")

        date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")


        history_log = open(f"{os.getcwd()}\\logs\\history_log.txt", "a")

        history_log.write(f"""{date} You searched for files/folders that end with "{sequence}" in {path} and got {count} results\n""")
        history_log.close()

        count_file = open(f"{os.getcwd()}\\config\\logs_count.txt", "a")

        count_file.write("DO NOT DELETE ANY OF THE LINES\n")

        init_pop_up()


    def specific_search(self, path, sequence):
        print("[DEBUG] Initiated specific scan")
        global count, log_file, history_log, err_count
        sep_or_sngl = perform_check()
        if sep_or_sngl:


            count_file = open(f"{os.getcwd()}\\config\\logs_count.txt", "a")
            count_file = open(f"{os.getcwd()}\\config\\logs_count.txt", "r")
            logs_count = 0

            for line in count_file.readlines():
                str(line) # mock call to shut up Pylint
                logs_count+=1

            log_file = open(f'{os.getcwd()}\\scans\\specific_scans\\specific_scan_results_{logs_count}', 'w+')
            history_log = open(f'{os.getcwd()}\\logs\\history_log.txt', 'a')

        else:
                log_file = open(f"{os.getcwd()}\\scans\\single_scan\\scan_results.txt", "w+")

        for folder, sub_folders, files in os.walk(path):

            for sub_fold in sub_folders:
                if sub_fold == sequence:
                    count += 1
                    curr_path = os.path.join(folder, sub_fold)
                    print(f'Found! Folder: {sub_fold} \n')
                    try:
                        log_file.write(f'FOLDER: {sub_fold} AT {curr_path} \n')
                    except UnicodeEncodeError:
                        err_count += 1
                        continue
                    else:
                        pass

                else:
                    continue

            for f in files:
                if f == sequence:
                    count += 1
                    curr_path = os.path.join(folder, f)
                    print(f'\t Found! File: {f} \n')
                    try:
                        log_file.write(f'FILE: {f} AT  {curr_path}\n')
                    except UnicodeEncodeError:
                        err_count += 1
                        continue
                    else:
                        pass

        if err_count == 1:
            print(f"[DEBUG] Caught {err_count} UnicodeEncodError")
        else:
            print(f"[DEBUG] Caught {err_count} UnicodeEncode errors")

        date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")


        history_log = open(f"{os.getcwd()}\\logs\\history_log.txt", "a")


        history_log.write(f"""{date} You searched for files/folders named "{sequence}" in {path} and got {count} results\n""")
        history_log.close()


        count_file = open(f"{os.getcwd()}\\config\\logs_count.txt", "a")

        count_file.write("DO NOT DELETE ANY OF THE LINES\n")

        init_pop_up()


    def init_search(self):
        global choice

        if self.path != "" and self.sequence.text != "":

            if choice == "starts_with":
                self.search_starts_with(self.path, self.sequence.text)

            elif choice == "contains":
                self.search_contains(self.path, self.sequence.text)

            elif choice == "specific":
                self.specific_search(self.path, self.sequence.text)

            else:
                self.search_ends_with(self.path, self.sequence.text)

        else:
            global history_log

            history_log = open(f"{os.getcwd()}\\logs\\history_log.txt", "a")

            date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

            history_log.write(f"{date} Scan failed: Incorrect Input\n")
            history_log.close()
            invalid_path_or_sequence()


    def go_back(self):
        self.current_mode = ""
        sm.current = "choice"
        print("[DEBUG] Go to ChoiceScreen")


    def go_to_history(self):
        sm.current = "history"
        print("[DEBUG] Go to HistoryScreen")

    def go_to_settings(self):
        sm.current = "settings"
        print("[DEBUG] Go to SettingsScreen")



class HistoryWindow(Screen):
    if_cleared = kypros.StringProperty()
    last_scan = kypros.StringProperty()
    pop_text = "To view all the scans and their details - Visit the log file at: \n" + os.getcwd() + "\\logs"

    def init_history(self):

        history_log = open(f"{os.getcwd()}\\logs\\history_log.txt", "r")

        line_count = get_logs_num()
        lines = []

        for line in history_log.readlines():
            lines.append(line)
        try:
            self.last_scan = lines[line_count-1]
        except IndexError:
            self.last_scan ="No last scans"
            print(f"[DEBUG] {self.last_scan}")
            return self.last_scan
        else:
            self.last_scan = lines[line_count-1]
            print(f"[DEBUG] {self.last_scan}")
            return self.last_scan


    def clear_history(self):

        history_log = open(f"{os.getcwd()}\\logs\\history_log.txt", "w+")

        self.if_cleared = "All Scan History Has Been Cleared"
        print("[DEBUG] History Cleared")
        history_log.close()


    def history_pop(self):
        pop = Popup(title="Looking for older scan details? ", content=Label(text=self.pop_text, font_size=19), size_hint=(None, None), size=(1000, 300))
        pop.open()

    def go_back(self):
        self.if_cleared = ""
        self.last_scan = ""
        sm.current = "input"
        print("[DEBUG] Go to InputScreen")


class SettingsWindow(Screen):
    del_logs = kypros.StringProperty()
    status_one = kypros.StringProperty()
    status_two = kypros.StringProperty()


    def check_md(self):
        choice_file = open(f"{os.getcwd()}\\config\\usr_md_choice.txt", "r")


        if "i" in choice_file.readlines():
            self.status_one = "Turn OFF"
            self.status_two = "Turn ON"
        else:
            self.status_one = "Turn ON"
            self.status_two = "Turn OFF"


    def delete_logs(self):

        path = "scans\\"
        for root, dirs, files in os.walk(path):
            for file in files:
                os.remove(os.path.join(root, file))

        logs_count = open(f"{os.getcwd()}\\config\\logs_count.txt", "w+")

        self.del_logs = "All scans logs have been deleted"
        print("[DEBUG] Logs removed successfully")


    def update_sep(self):

        self.status_one = "Turn OFF"
        self.status_two = "Turn ON"

    def update_single(self):

        self.status_one = "Turn ON"
        self.status_two = "Turn OFF"

    def go_back(self):
        self.del_logs = ""
        sm.current = "input"
        print("[DEBUG] Go to InputScreen")

    def separate_mode(self):

        choice_file = open(f"{os.getcwd()}\\config\\usr_md_choice.txt", "a")


        choice_file.write("usr_md_choice = separate\n")
        choice_file.write("If none, mode = single")
        print("[DEBUG] Separate Mode Chosen")
        choice_file.close()

    def single_mode(self):

        choice_file = open(f"{os.getcwd()}\\config\\usr_md_choice.txt", "w+")
        print("[DEBUG] Single Mode Chosen")
        choice_file.close()

    def updt_init_first(self):
        if self.status_one == "Turn ON":
            self.update_sep()
            self.separate_mode()

        else:
            self.update_sep()
            self.status_one = "Turn ON"
            self.status_two = "Turn OFF"
            self.single_mode()


    def updt_init_sec(self):
        if self.status_two == "Turn ON":
            self.update_single()
            self.single_mode()
        else:
            self.update_single()
            self.status_one = "Turn OFF"
            self.status_two = "Turn ON"
            self.separate_mode()

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file(resource_path("filefinder.kv"))

sm = ScreenManager(transition=NoTransition())

screens = [ChoiceWindow(name="choice"), InputWindow(name="input"), SettingsWindow(name="settings"),
           HistoryWindow(name="history")]


for screen in screens:
    sm.add_widget(screen)

sm.current = "choice"


class FileFinderApp(App):
    def build(self):
        return sm


if __name__ == "__main__":
    Window.size = (1100, 800)


    history_log = open(f"{os.getcwd()}\\logs\\history_log.txt", "a")
    count_file = open(f"{os.getcwd()}\\config\\logs_count.txt", "a")
    count_file = open(f"{os.getcwd()}\\config\\logs_count.txt", "r")


    logs_count = 0
    for line in count_file.readlines():
        logs_count+=1

    get_logs_num()

    FileFinderApp().run()