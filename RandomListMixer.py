import glob
import numpy as np
import tkinter
from tkinter import messagebox

class ListRandomiser(object):
    """Class to collect lists from .txt files and
    generate a random selection."""

    def __init__(self):

        self.generate_list_dict()

    def get_list_paths(self):
        """Pulls the directories for all .txt files in the lists folder"

        Attributes
        ----------
        list_paths : list
            List of the directories for the .txt files.

        """

        self.list_paths = glob.glob("lists/*.txt")
    
    def extract_lists(self):
        """Extracts the raw data in the .txt files and generates lists.

        The .txt files are assumed to be comma seperated with spaces, eg:
        a, b, c, d

        Attributes
        ----------
        lists : dict
            Dictionary of lists with enumerated keys.

        """
        
        self.lists = {}

        for i, path in enumerate(self.list_paths):
            with open(path, "r") as file:
                raw_string = file.read()
                self.lists[i] = raw_string.split(", ")

    def generate_list_dict(self):
        """Wrapper for generating the list dictionary."""

        self.get_list_paths()
        self.extract_lists()
    
    def select_random(self):
        """Randomly selects a single value from each of the lists and
        appends them all into a single string.

        Returns
        -------
        outputs : str
            Concatenated string of random list objects.

        """
        outputs = ""
        for i in self.lists.values():
            outputs += " " + str(i[np.random.randint(0, len(i))])
        
        return outputs


class ApplicationWindow(object):
    """Builds the application window to use for the executable.

    Parameters
    ----------
    title : str
        Title of the popup window.
    size : str
        Size of the popup windows, eg: '400x300'.
    
    Attributes
    ----------
    window : tkinter.Tk
        Popup window object

    """

    def __init__(self, title, size):

        self.window = tkinter.Tk()
        self.window.title(title)
        self.window.geometry(size)
        self.window.resizable(0, 0)
        self.run_application()

    def build_list_command(self):
        """Uses the ListRandomiser class to build the output list."""
        output_text = ListRandomiser().select_random()
        messagebox.showinfo("Randomised List", output_text)
    
    def build_button(self, button_text, command):
        """Generates a button that calls a command.

        Parameters
        ----------
        button_text : str
            Display text on the button.
        command : function/method
            Method or function to call when putton is pressed.

        """

        self.button = tkinter.Button(text=button_text, command=command)
        self.button.pack()
    
    def run_application(self):
        """Builds the window and button."""

        self.build_space()
        self.build_button("Build List", self.build_list_command)
        self.window.mainloop()
    
    def build_space(self):
        """Builds the Label object."""

        self.space = tkinter.Label(self.window, height=2, ).pack()

if __name__ == "__main__":
    ApplicationWindow("List Randomiser", "400x300")