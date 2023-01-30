# HomeSecuritySystem

The aim was to create a small reliable system using AI for Home Security.

Packages to be installed:
Install Python from official Website.
pip3 install tensorflow or pip3 install torch 
pip3 install SpeechRecognition
brew install flac
brew install portaudio (further create path for the portaudio)
pip3 install PyAudio
pip3 install gtts
pip3 install numpy
Python3 version: 3.7 and up (Current System 3.10.6)
pip3 install pandas
pip3 install opencv-python

To translate Speech to Text: I have used SpeechRecognition API developed by Google.
To translate Text to Speech: I have used gtts library developed by Google.

Face Recoginition system has been created to detect the user face and store in database. 
This user image can be sent over to the home owner's personal device.

Haarcascade Classifier has been used to detect the user face.

To run:

Step 1: Go to the folder where you have stored the files in Terminal
Step 2: Type - python3 regres.py
Program will start running..
It will ask for the house personal names.
Enter No when finish entering.
Step 3: Say "Hi James"
Step 4: Continue with the process.
