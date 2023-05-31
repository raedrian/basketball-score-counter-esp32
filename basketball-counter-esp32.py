from machine import Pin
import time
from time import sleep
import mp_i2c_lcd1602
import machine

i2c = I2C(1, sda=Pin(21), scl=Pin(22))

LCD = LCD1602(i2c)


#-----------------BUTTON ASSIGNMENT-----------------
buttona = Pin(14, Pin.OUT)   
buttonm = Pin(13, Pin.OUT)
stopb = Pin(33, Pin.OUT)
playb = Pin(12, Pin.OUT)
resetb = Pin(25, Pin.OUT)
score1 = 0
score2 = 0



print("WELCOME TO BASKETBALL SCORE COUNTER AND TIMER")
LCD.puts("BASKETBALL TIMER",0,0)
LCD.puts("Press 2 to Start",0,1)
sleep(2)


print("Press Button 1 to Reset the Device")
print("Press Button 2 to Start the clock")
print("Press Button 3 to Stop the clock")
print("Press Button 4 to add Team #1 Score")
print("Press Button 5 to add Team #2 Score")
print("\n")


def countdown(time_sec):
  LCD.clear()
  while time_sec:
      if stopb.value() == 1:
        print("\n")
        print("Timer Stopped")
        LCD.puts("Timer Stopped")
        print("\n")
        break
      mins, secs = divmod(time_sec, 60)       
      timeformat = '{:02d}:{:02d}'.format(mins, secs)
      print(timeformat, end='\r')
      LCD.puts("Time:   ",0,0)
      LCD.puts(timeformat,0,1)
      time.sleep(1)
      time_sec -= 1
      
     



while True:
 
  if resetb.value() == 1:
    score1 = 0
    score2 = 0
    print("Scores Reset")
    print(" Team#1 Score = ",score1)
    print(" Team#2 Score = ",score2)
    
    LCD.puts("Team#1:",0,0)
    LCD.puts(score1,0,1)
    
    LCD.puts("Team#2:",8,0)
    LCD.puts(score2,8,1)
    
    print("\n")
    
  
  
  while playb.value() == 0:
    if resetb.value() == 1:
      score1 = 0
      score2 = 0
      LCD.clear()
      print("Scores Reset")
      print(" Team#1 Score = ",score1)
      print(" Team#2 Score = ",score2)
      
      LCD.puts("Team#1:",0,0)
      LCD.puts(score1,0,1)
    
      LCD.puts("Team#2:",8,0)
      LCD.puts(score2,8,1)
      
      
      print("\n")
      sleep(0.5) 
    
    if buttonm.value() == 1:
      score1 = score1 + 1
      
      print(" Team#1 Score = ",score1)
      print(" Team#2 Score = ",score2)
      
      LCD.puts("Team#1:",0,0)
      LCD.puts(score1,0,1)
    
      LCD.puts("Team#2:",8,0)
      LCD.puts(score2,8,1)
      
      print("\n")
      sleep(0.5)  

    elif buttona.value() == 1:
      score2 = score2 + 1
      
      print(" Team#1 Score = ",score1)
      print(" Team#2 Score = ",score2)
      
      LCD.puts("Team#1:",0,0)
      LCD.puts(score1,0,1)
    
      LCD.puts("Team#2:",8,0)
      LCD.puts(score2,8,1)
      
      
      print("\n")
      sleep(0.5)  
  print("Play Button Pressed")
  
  print("\n")
  sleep(0.5)
  
  while stopb.value() == 0:
    countdown(24)
    LCD.clear()
    break
    
  sleep(0.5)
  
  print("Input Score Buttons")
  print(" Team#1 Score = ",score1)
  print(" Team#2 Score = ",score2)
  
  LCD.puts("Team#1:",0,0)
  LCD.puts(score1,0,1)
    
  LCD.puts("Team#2:",8,0)
  LCD.puts(score2,8,1)
  
  
  
  print("\n")






