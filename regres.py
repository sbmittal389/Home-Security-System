import speech_recognition as sr
from gtts import gTTS
from transformers import pipeline, Conversation
import os
import numpy as np
import pandas as pd
import cv2

class ai_model():
	def __init__(self, name):
		print("Starting..", name)
		self.name = name

	def s_to_t(self):																			#Speech to Text func
		recognizer = sr.Recognizer()
		with sr.Microphone() as src:
			print("listening..")
			recognizer.adjust_for_ambient_noise(src)
			a = recognizer.listen(src)
			try:
				self.text = recognizer.recognize_google(a)										#Translating the speech into text format using recognizer
				print(self.text)
			except:
				print("Sorry! Did not understand what you said:(")

	def t_to_s(self, text):																		#Text to speech conversion func
		speaker = gTTS(text=text, lang="en", slow=False, tld="co.in")							#language = English, tld(speech voice) = indian
		speaker.save("res.mp3")
		os.system("afplay res.mp3")																#afplay is used for Mac users, for Windows replace it with 'start'
		os.remove("res.mp3")

	def wakingUp(self, text):
		if self.name in text.lower():
			return True
		else:
			return False

def introToai(ai):
	ai.t_to_s("Hi, I am your HouseKeeper James")
	ai.t_to_s("Please set up your System")

def house_mates(ai):
	ai.t_to_s("Enter the names of People living in the house")
	names_house = []
	while True:
		name_s = input("Enter the name (enter 'No' if no name):")
		names_house.append(name_s)
		if name_s.lower() == 'no':
			break
	df = pd.DataFrame(names_house)
	df.to_csv('housemates.csv', index = False)

def face_detect(user_name):																		#function to detect user face
	web_cam = cv2.VideoCapture(0)
	face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
	face_data = []
	cnt = 0
	while True:
		ret, frame = web_cam.read()
		if ret:
			gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
			faces= face_cascade.detectMultiScale(frame, 1.3, 5)
			if(len(faces) == 0):
				continue

			for face in faces:
				x,y,w,h = face
				cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 255), 2)
				cv2.rectangle(gray, (x, y), (x+w, y+h), (0, 255, 255), 2)

				face_section = frame[y-10:y+h+10, x-10:x+w+10]
				face_section = cv2.resize(face_section, (100,100))
				if cnt%10 == 0:
					print("taking picture")
					face_data.append(face_section)
					cnt+=1


			cv2.imshow(user_name, frame)
		
		else:
			break

		if  cv2.waitKey(1) & 0xFF == ord('q'):
			break

	face_data = np.array(face_data)
	face_data = face_data.reshape((face_data.shape[0], -1))
	np.save("./"+user_name+".npy", face_data)
	web_cam.release()
	cv2.destroyAllWindows()


ai = ai_model(name="james")

introToai(ai)
house_mates(ai)

housemate_list = pd.read_csv('housemates.csv')

while True:
	print("To notify the owner, Please say 'Hi James'")
	ai.s_to_t()

	if ai.wakingUp(ai.text) is True:
		res = "Hi I am James the house keeper, Please tell me your name"
		ai.t_to_s(res)
		ai.s_to_t()
		face_detect(ai.text)
		ai.t_to_s("I have updated the Owner about you")

	elif any(i in ai.text for i in ["thank", "thanks", "bye", "thank you", "thank you for helping", "no thank you"]):
		res = np.random.choice(["Welcome!", "Anytime!", "No Problem!"])
		ai.t_to_s(res)
		break