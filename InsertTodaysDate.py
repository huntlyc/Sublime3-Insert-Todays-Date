import sublime, sublime_plugin, datetime

class InsertTodaysDateCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        s = sublime.load_settings("InsertTodaysDate.sublime-settings")
        dateFormat = s.get("hdate_format")
        today = datetime.date.today()
        self.view.insert(edit, self.view.sel()[0].begin(), today.strftime(dateFormat))