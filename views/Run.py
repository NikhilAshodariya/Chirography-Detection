# from views import charRecognition


import sys
# importing file
sys.path.insert(0, '../views')

import charRecognition as cr
# from charRecognition import Application


import tkinter as tk
import pygubu

class NikhilApp:	

	def show_Screen(self):
		self.root=tk.Tk()
		# print(dir(cr))
		self.obj=cr.Application(self.root)


		self.root.mainloop()

	def get_Model(self):
		model=lM.getModel()
		return model

# app=NikhilApp()	
# app.show_Screen()
# show_Screen()











