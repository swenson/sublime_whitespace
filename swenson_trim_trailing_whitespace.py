# Only strip trailing whitespace from modified lines.
# (Unless I own the file.)
#
# I suggest you modify the patterns line below to include your own email
# addresses.
#
# Author: Christopher Swenson (chris@caswenson.com)


from difflib import SequenceMatcher

import sublime, sublime_plugin

patterns = ['swenson@simple.com', 'chris@caswenson.com']
snapshots = {}

class SwensonTrimTrailingWhiteSpace(sublime_plugin.EventListener):
  # Load a snapshot of the file.
  def on_load(self, view):
    snapshots[view.id()] = view.substr(sublime.Region(0, view.size()))

  def on_pre_save(self, view):
    # Trim whitespace on any new files.
    old = snapshots[view.id()].split('\n')
    new = view.substr(sublime.Region(0, view.size())).split('\n')
    # Remove the line numbers that were present before.
    new_lines = set(range(len(new)))
    sm = SequenceMatcher(None, old, new)
    for i, j, n in sm.get_matching_blocks():
      for k in xrange(j, j + n):
        new_lines.remove(k)
    # Trim the whitespace on the new lines:
    if new_lines:
      edit = view.begin_edit()
      for line_no in new_lines:
        pt = view.text_point(line_no, 0)
        old_line = view.line(pt)
        new_line_text = view.substr(view.line(pt)).rstrip()
        view.replace(edit, old_line, new_line_text)
      view.end_edit(edit)

    # Trim all whitespace on my files.
    if any(view.find(pattern, 0, sublime.IGNORECASE) for pattern in patterns):
      trailing_white_space = view.find_all("[\t ]+$")
      trailing_white_space.reverse()
      edit = view.begin_edit()
      for r in trailing_white_space:
          view.erase(edit, r)
      view.end_edit(edit)

  # Reload the file into the snapshot after saving.
  def on_post_save(self, view):
    self.on_load(view)
