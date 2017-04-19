import pickle


# import charModel as CM

def getModel():
	model=pickle.load( open( "../models/charModel.p", "rb" ) )
	print(model)
	return model