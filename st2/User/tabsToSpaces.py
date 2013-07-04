import sublime, sublime_plugin

class TapsToSpaces(sublime_plugin.EventListener):
    def on_pre_save(self, view):
        view.run_command("expand_tabs");
