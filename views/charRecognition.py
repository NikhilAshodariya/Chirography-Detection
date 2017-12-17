import tkinter as tk
import pygubu
import numpy as np
from PIL import Image, ImageDraw
import sys
# importing file
sys.path.insert(0, '../views')
sys.path.insert(0, '../controller')

import imageEdit as IE
import loadModel


class Application:
	def __init__(self,master):
		print('This is the window')
		self.master=master
		
		# create builder
		self.builder = builder = pygubu.Builder()

		# Loading UI file
		builder.add_from_file('../views/CR.ui')

		# create a widget, using master as parent
		self.mainWindow = builder.get_object('CharRecognition',master)

		# getting objects
		self.get_object()

		# creating canvas image
		self.create_Canvas_Image()

		# connect callbacks
		builder.connect_callbacks(self)


	def get_object(self):
		self.canvas=self.builder.get_object('drawCanvas',self.master)
		self.canvas.bind('<B1-Motion>', lambda event: self.paintPoint(event.x, event.y, thickness = 10))
		
		self.create_Canvas_Image()

		temp=self.builder.get_object('innerFrame',self.master) # temp is a frame 

		self.clearButton=self.builder.get_object('clear',temp)
		self.predictButton=self.builder.get_object('predict',temp)
		self.predictedTextLabel=self.builder.get_object('predictedText',temp)

	
	def paintPoint(self, x, y,thickness = 0,color     = '#FFFFFF'):
		a, b   = x - thickness, y - thickness
		c, d   = x + thickness, y + thickness
		points = [a, b, c, d]
		self.canvas.create_oval(points, fill = color)
		# self.canvas.line((a,b),(c,d), fill = color)
		
		self.imageDraw.ellipse (points, color)
		# self.imageDraw.line ((a,b),(c,d))
		
		# self.imageDraw.ellipse (points, color)

	def on_click_clear(self):
		''' Quit Button Callback'''
		self.canvas.delete('all')
		self.create_Canvas_Image()
		self.predictedTextLabel.config(text=" ")


		# self.master.quit()

	def create_Canvas_Image(self):
		width=self.canvas.winfo_width()
		height=self.canvas.winfo_height()
		color='#000000'
		self.image     = Image.new('RGB', (width, width), color)
		self.imageDraw = ImageDraw.Draw(self.image)
		# self.image.thumbnail((28,28), Image.BICUBIC) #(28,28) is the size of image




	def on_click_predict(self):
		# img=self.create_Canvas_Image()

		# self.imageDraw.convert('RGB')
		# print(self.imageDraw)

		# print(self.canvas.find_all())
		self.image.thumbnail((28,28), Image.BICUBIC) #(28,28) is the size of image
		array = np.array(self.image)
		# array=np.reshape(array, (1, array.size))

		# array=np.array(self.imageDraw.getdata()).reshape(pic.size[0], pic.size[1], 3)

		# print('array = ',array)
		
		img=self.image.convert('RGB')
		img=IE.grayscale(img)
		imgArr=np.asarray(img)
		imgArr=imgArr.flatten()

		# img=Image.fromarray(arrimg)

		# # arr=IE._image_to_input(img)
		# arr=arrimg.flatten()
		# arr   = np.reshape(arr, (1, arr.size))
		# self.arr=arr
		# # print(self.arr)

		ans=loadModel.getModel().predict(imgArr)
		self.predictedTextLabel.config(text=ans[0])
		print(ans)
		pass

