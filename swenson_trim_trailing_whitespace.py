# Only strip trailing whitespace from modified lines, or if
# anything from `trim_if_present` is present.
#
# Author: Christopher Swenson (chris@caswenson.com)


from difflib import SequenceMatcher

import sublime, sublime_plugin

snapshots = {}

class SwensonTrimTrailingWhiteSpace(sublime_plugin.EventListener):
  # Load a snapshot of the file.
  def on_load(self, view):
    snapshots[view.id()] = view.substr(sublime.Region(0, view.size()))

  def on_pre_save(self, view):
    settings = sublime.load_settings('Preferences.sublime-settings')
    patterns = settings.get("trim_if_present", [])

    # Trim all whitespace on my files.
    if any(view.find(pattern, 0, sublime.IGNORECASE) for pattern in patterns):
      view.run_command("erase_whitespace", {})
      return

    if view.id() not in snapshots:
      print("No snapshot present to compare")
      return

    # Trim whitespace on any new files.
    old = snapshots[view.id()].split('\n')
    new = view.substr(sublime.Region(0, view.size())).split('\n')
    # Remove the line numbers that were present before.
    new_lines = set(range(len(new)))
    sm = SequenceMatcher(None, old, new)
    for i, j, n in sm.get_matching_blocks():
      for k in range(j, j + n):
        new_lines.remove(k)
    # Trim the whitespace on the new lines:
    if new_lines:
      new_lines = ','.join(str(n) for n in new_lines)
      view.run_command("process_new_lines", dict(new_lines=new_lines))

  # Reload the file into the snapshot after saving.
  def on_post_save(self, view):
    self.on_load(view)

class EraseWhitespaceCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    trailing_white_space = self.view.find_all("[\t ]+$")
    trailing_white_space.reverse()
    for r in trailing_white_space:
      self.view.erase(edit, r)

class ProcessNewLinesCommand(sublime_plugin.TextCommand):
  def run(self, edit, new_lines=""):
    for line_no in new_lines.split(','):
      pt = self.view.text_point(int(line_no), 0)
      old_line = self.view.line(pt)
      new_line_text = self.view.substr(self.view.line(pt)).rstrip()
      self.view.replace(edit, old_line, new_line_text)
