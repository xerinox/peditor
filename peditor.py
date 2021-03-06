#!/usr/bin/python

from gi.repository import Gtk, GtkSource, GObject
from os.path import abspath, dirname, join

class Gui(object):

	def __init__(self):
		self.builder = Gtk.Builder()
		self.glade_file = join(abspath(dirname(__file__)), "UI.glade")
		GObject.type_register(GtkSource.View)
		self.builder.add_from_file(self.glade_file)

		self.main_window = self.builder.get_object("window1")
		self.main_window.connect("delete-event", Gtk.main_quit)
		self.main_window.show_all()
		


if __name__ == "__main__":
	try:
		Gui()
		Gtk.main()
	except KeyboardInterrupt:
		pass
