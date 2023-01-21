import sublime
import sublime_plugin

def plugin_loaded():
    print(sublime.version())

def plugin_unloaded():
    print(sublime.channel())

class NiceLogInputHandler(sublime_plugin.TextInputHandler):
    def __init__(self, view):
        self.view = view

    def name(self):
        return "text"

    def placeholder(self):
        return "Text to insert"

    def preview(self, text):
        return ("Selections: {}, Characters: {}"
                .format(len(self.view.sel()), len(text)))

class NiceLogCommand(sublime_plugin.TextCommand):
    def run(self, edit, text):
        # Your code here
        for region in self.view.sel():
            self.view.replace(edit, region, text)

    def input(self, args):
        return NiceLogInputHandler(self.view)
