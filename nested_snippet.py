import sublime
import sublime_plugin

class InsertBestCompletionOrGotoNextField(sublime_plugin.TextCommand):
  def run(self, edit, exact = False, default = "\t",
    completion_command = 'insert_best_completion', fallback = False):

    text = self._get_text()

    self.view.run_command(completion_command, {'exact': exact, 'default': ''})

    modified_text = self._get_text()
    selections = self._get_selections()

    if text == modified_text:
      if fallback:
        return self.run(edit, exact, default, 'insert_best_completion', False)

      self.view.run_command('next_field')
      if selections == self._get_selections():
        self.view.run_command('insert', {'characters': default})

  def _get_text(self):
    return self.view.substr(sublime.Region(0, min(self.view.size(),
      1024*1024*5)))

  def _get_selections(self):
    selections = ''

    for sel in self.view.sel():
      selections += str(sel.a) + ':' + str(sel.b)

    return selections