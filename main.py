#HW 5

# Course: CMPT 140 Introduction to Computing Science and Programming I
# Instructor: Dr. Herbert H. Tsang
# Description: <Chatbox>
# Due date: < 2020/10/18>

# Author: < WeidongWang >
# Input: < IF ANY >
# Output: < IF ANY >
# I pledge that I have completed the programming assignment independently.
# I have not copied the code from a student or any source.
# I have not given my code to any student.
#
# Sign here: ___<WeidongWang>_______

# Import the turtle package
import turtle
import random
from alphabet import alphabet

myPen = turtle.Turtle()
myPen.hideturtle()
myPen.speed(0)
window = turtle.Screen()
window.bgcolor("#000000")
myPen.pensize(2)

def displayMessage(message,fontSize,color,x,y):
  myPen.color(color)
  message=message.upper()
  
  for character in message:
    if character in alphabet:
      letter=alphabet[character]
      myPen.penup()
      for dot in letter:
        myPen.goto(x + dot[0]*fontSize, y + dot[1]*fontSize)
        myPen.pendown()
        
      x += fontSize
      
    if character == " ":
      x += fontSize
    x += characterSpacing 

#Main Program Starts Here
fontSize = 30
characterSpacing = 5
fontColor = "#FF00FF"

message = "Hello world!"
displayMessage(message,fontSize,fontColor,-190,0)