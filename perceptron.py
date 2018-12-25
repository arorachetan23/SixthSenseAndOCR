import random
import numpy as np
import cv2

def sign(a):
	if a>=0:
		return(1)
	else:
		return(-1)	


class Perceptron1:
	weights=np.zeros((2,1))
	lr=0.1

	def __init__(self):

		for i in range(len(self.weights)):
			self.weights[i]=random.randint(-1,1)
			

	#print(weights)		
	def guess(self,input):
		sum=0
		for i in range(len(self.weights)):
			sum+=input[i]*self.weights[i]

		output=sign(sum)
		return(output)	

	def train(self,input,target):
		gues=self.guess(input)
		error=target-gues

		for i in range(len(self.weights)):
			self.weights[i]+=error*input[i]*self.lr


class Point:
	x=0
	y=0
	label=0



	def __init__(self):
		
		self.x=random.randint(0,400)
		self.y=random.randint(0,400)
		if self.x>self.y:
			self.label=-1
		else:
			self.label=1

	



			#self.random_points.append((random_points_x,random_points_y))




pt = [Point() for x in range(100)] # array of class Point

canvas = np.zeros((400,400,3), np.uint8)
for i in range(100):
	x=pt[i].x
	y=pt[i].y
	label=pt[i].label
	#random_points.append((random_points_x,random_points_y))
	#display on canvas
	if label==1:
		cv2.circle(canvas, (x,y), 2, (255,255,255), 6)
	else:
		cv2.circle(canvas, (x,y), 2, (255,0,255), 6)	



c=Perceptron1()
#print(random_points)
trainingIndex=0

while(1):
		

	for i in range(len(pt)):
		input=[pt[i].x,pt[i].y]
		target=pt[i].label

		#c.train(input,target)
		gues=c.guess(input)
		if gues==target:
			cv2.circle(canvas, (pt[i].x,pt[i].y), 2, (255,0,0), 2)
		else:
			cv2.circle(canvas, (pt[i].x,pt[i].y), 2, (255,255,0), 2)
		#print(x)	

		
	training=pt[trainingIndex]
	input=[training.x,training.y]
	target=training.label
	c.train(input,target)
	trainingIndex+=1
	if trainingIndex==len(pt):
		trainingIndex=0
	cv2.imshow("canvas",canvas)
	cv2.waitKey(2)
	




# 	input=np.array([[-1],[0.5]])
# 	
# 	output=c.train(input)

#print(output)

	
#print(c.weights)
