# virtual-notepad
<p>
In “Virtual Notepad” the user will wave in front of the camera i.e make gestures and try to write something in the air. The system will detect the text the user is trying to draw. First it will detect the gesture with the movement of a bottle cap held in the hand and then with that captured gesture it will generate an image using openCV and with the help of the image generated it will recognize the text. The gesture detection part will be performed using openCV while text recognition part will be based on CNN(Convolutional Neural Networks) and RNN(Recurrent Neural Network).
</p><br>
<p>
I have implemented a graphical user interface for a user with options to start and close the notepad . When notepad is started a user is presented with an interface for drawing and a paint interface where the gesture is being printed simultaneously. The interface has 5 buttons as described below-

1)Clear All- On selecting this button by bottle cap gesture the interface screen is cleared and you can start again from scratch.

2)Blue- This button will change the color of our marker with blue color and it is the default marker color.

3)Green- This button will change the color of our marker with green color.

4)Red- This button will change the color of our marker with red color

5)Save- On selecting this button the current text on the paint interface is saved as an image to be passed to our model for text extraction. This will also work when we will close program<br><br>
<br><br><img src="virtual notepad/HTR/doc/vn.png" width=600 height=300/>
