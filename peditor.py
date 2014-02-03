#!/usr/bin/python

from gi.repository import Gtk, GtkSource, GObject
from os.path import abspath, dirname, join

WHERE_AM_I = abspath(dirname(__file__))

class MyApp(object):

	def __init__(self):
		self.builder = Gtk.Builder()
		self.glade_file = join(WHERE_AM_I, "UI.glade")
		GObject.type_register(GtkSource.View)
		self.builder.add_from_file(self.glade_file)
		self.main_window = self.builder.get_object("window1")
		


if __name__ == "__main__":
	try:
		gui = MyApp()
		gui.main_window.show_all()
		Gtk.main()
	except KeyboardInterrupt:
		pass
