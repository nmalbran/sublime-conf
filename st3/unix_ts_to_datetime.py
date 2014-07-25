import sublime, sublime_plugin
import datetime

'''
Convert a unix timestamp to a readable datetime string according to FORMAT.
It does nothing if not a valid timestamp.
Example:
    input: 1406216630
    output: "Thu 24/07/2014 15:43:50 UTC"
'''

FORMAT = '"%a %d/%m/%Y %H:%M:%S UTC"'

class UnixTsToDatetimeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            if region.empty():
                continue
            text = self.view.substr(region)

            if not self._is_int(text):
                continue

            replacement = self._timestamp_to_userfriendly_datetime(text)
            if replacement:
                self.view.replace(edit, region, replacement)
            else:
                continue

    def _timestamp_to_userfriendly_datetime(self, timestamp):
        try:
            return datetime.datetime.utcfromtimestamp(int(timestamp)).strftime(FORMAT)
        except OSError as e:
            return False

    def _is_int(self, test):
        try:
            int(test)
        except ValueError as e:
            return False
        else:
            return True
