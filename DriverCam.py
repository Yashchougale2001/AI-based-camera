import numpy
from pygame import mixer
import time
import datetime
import cv2
from tkinter import *
import tkinter.messagebox
root=Tk()
root.geometry("500x570")
root.resizable(False,False)
frame = Frame(root, relief=RIDGE, borderwidth=2)
frame.pack(fill=BOTH,expand=1)
root.title('Driver Cam')
frame.config(background='light blue')
label = Label(frame, text="Driver Cam",bg='light blue',font=('Times 35 bold'))
label.pack(side=TOP)
filename = PhotoImage(file="demo.png")
background_label = Label(frame,image=filename)
background_label.pack(side=TOP)

def hel():
   help(cv2)

def Contri():
   tkinter.messagebox.showinfo("Contributors","\n1.Mayur Kadam\n2. Abhishek Ezhava \n3. Rajendra Patil \n")


def anotherWin():
   tkinter.messagebox.showinfo("About",'Driver Cam version v1.0\n Made Using\n-OpenCV\n-Numpy\n-Tkinter\n In Python 3')
                                    
   

menu = Menu(root)
root.config(menu=menu)

subm1 = Menu(menu)
menu.add_cascade(label="Tools",menu=subm1)
subm1.add_command(label="Open CV Docs",command=hel)

subm2 = Menu(menu)
menu.add_cascade(label="About",menu=subm2)
subm2.add_command(label="Driver Cam",command=anotherWin)
subm2.add_command(label="Contributors",command=Contri)



def exitt():
   exit()


def detect():
   capture = cv2.VideoCapture(0)
   face_cascade = cv2.CascadeClassifier('cascade/haarcascade_frontalface_default.xml')
   smile_cascade = cv2.CascadeClassifier('cascade/haarcascade_smile.xml')

   while True:
         _, frame = capture.read()
         frame1 =cv2.flip(frame,1)
         ori_frame = frame1.copy()
         gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
         face = face_cascade.detectMultiScale(gray, 1.3, 5)
         for x, y, w, h in face:
            cv2.rectangle(frame1, (x,y),(x+w, y+h), (0.255,255),2)
            face_roi = frame1[y:y+h, x:x+w]
            gray_roi = gray[y:y+h, x:x+w]
            smile = smile_cascade.detectMultiScale(gray_roi, 1.3, 25)
            for x1, y1, w1, h1 in smile:
                  cv2.rectangle(face_roi, (x1, y1), (x1+w1, y1+h1), (0, 0, 255), 2)
                  save_img()
         cv2.imshow('Cam Start',frame1)
         if cv2.waitKey(10) == ord('q'):
            destroy()
            break
            
         def save_img():
            time_stamp = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
            file_name = f'selfie-{time_stamp}.png'
            cv2.imwrite(file_name, ori_frame)
            # cv2.imwrite('sel22.png',ori_frame)

         def destroy():
            capture.release()
            cv2.destroyAllWindows()
            

def webrec():
   capture =cv2.VideoCapture(0)
   fourcc=cv2.VideoWriter_fourcc(*'XVID') 
   op=cv2.VideoWriter('Sample1.avi',fourcc,11.0,(640,480))
   while True:
      ret,frame=capture.read()
      gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
      cv2.imshow('frame',frame)
      op.write(frame)
      if cv2.waitKey(1) & 0xFF ==ord('q'):
         break
   op.release()
   capture.release()
   cv2.destroyAllWindows()   

def webdet():
   capture =cv2.VideoCapture(0)
   face_cascade = cv2.CascadeClassifier('lbpcascade_frontalface.xml')
   eye_glass = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
   

   while True:
       ret, frame = capture.read()
       gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
       faces = face_cascade.detectMultiScale(gray)
    

       for (x,y,w,h) in faces:
           font = cv2.FONT_HERSHEY_COMPLEX
           cv2.putText(frame,'Face',(x+w,y+h),font,1,(250,250,250),2,cv2.LINE_AA)
           cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
           roi_gray = gray[y:y+h, x:x+w]
           roi_color = frame[y:y+h, x:x+w]
        
          
           eye_g = eye_glass.detectMultiScale(roi_gray)
           for (ex,ey,ew,eh) in eye_g:
              cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

       
       cv2.imshow('frame',frame)
       if cv2.waitKey(1) & 0xff == ord('q'):
          break
   capture.release()
   cv2.destroyAllWindows()

def webdetRec():
   capture =cv2.VideoCapture(0)
   face_cascade = cv2.CascadeClassifier('lbpcascade_frontalface.xml')
   eye_glass = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
   fourcc=cv2.VideoWriter_fourcc(*'XVID') 
   op=cv2.VideoWriter('Sample2.avi',fourcc,9.0,(640,480))

   while True:
       ret, frame = capture.read()
       gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
       faces = face_cascade.detectMultiScale(gray)
    

       for (x,y,w,h) in faces:
           font = cv2.FONT_HERSHEY_COMPLEX
           cv2.putText(frame,'Face',(x+w,y+h),font,1,(250,250,250),2,cv2.LINE_AA)
           cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
           roi_gray = gray[y:y+h, x:x+w]
           roi_color = frame[y:y+h, x:x+w]
        
          

           eye_g = eye_glass.detectMultiScale(roi_gray)
           for (ex,ey,ew,eh) in eye_g:
              cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
       op.write(frame)
       cv2.imshow('frame',frame)
       if cv2.waitKey(1) & 0xff == ord('q'):
          break
   op.release()      
   capture.release()
   cv2.destroyAllWindows()

   
def alert():
   mixer.init()
   alert=mixer.Sound('beep-07.wav')
   alert.play()
   time.sleep(0.1)
   alert.play()   
   
def blink():
   capture =cv2.VideoCapture(0)
   face_cascade = cv2.CascadeClassifier('lbpcascade_frontalface.xml')
   eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
   blink_cascade = cv2.CascadeClassifier('CustomBlinkCascade.xml')

   while True:
      ret, frame = capture.read()
      gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
      faces = face_cascade.detectMultiScale(gray)

      for (x,y,w,h) in faces:
         font = cv2.FONT_HERSHEY_COMPLEX
         cv2.putText(frame,'Face',(x+w,y+h),font,1,(250,250,250),2,cv2.LINE_AA)
         cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
         roi_gray = gray[y:y+h, x:x+w]
         roi_color = frame[y:y+h, x:x+w]

         eyes = eye_cascade.detectMultiScale(roi_gray)
         for(ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

         blink = blink_cascade.detectMultiScale(roi_gray)
         for(eyx,eyy,eyw,eyh) in blink:
            cv2.rectangle(roi_color,(eyx,eyy),(eyx+eyw,eyy+eyh),(255,255,0),2)
            alert()
      cv2.imshow('frame',frame)
      if cv2.waitKey(1) & 0xFF ==ord('q'):
          break

      def save_img():
             time_stamp = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
             file_name = f'selfie-{time_stamp}.png'
             cv2.imwrite(file_name, ori_frame)
             cv2.imwrite('sel22.png',ori_frame)
  
   capture.release()
   cv2.destroyAllWindows()

but1=Button(frame,padx=5,pady=5,width=39,bg='white',fg='black',relief=GROOVE,command=web,text='Open Cam',font=('helvetica 15 bold'))
but1.place(x=5,y=104)

but2=Button(frame,padx=5,pady=5,width=39,bg='white',fg='black',relief=GROOVE,command=webrec,text='Open Cam & Record',font=('helvetica 15 bold'))
but2.place(x=15,y=150)

but3=Button(frame,padx=5,pady=5,width=39,bg='white',fg='black',relief=GROOVE,command=webdet,text='Open Cam & Detect',font=('helvetica 15 bold'))
but3.place(x=5,y=250)

but4=Button(frame,padx=5,pady=5,width=39,bg='white',fg='black',relief=GROOVE,command=webdetRec,text='Detect & Record',font=('helvetica 15 bold'))
but4.place(x=5,y=322)

but5=Button(frame,padx=5,pady=5,width=39,bg='white',fg='black',relief=GROOVE,command=blink,text='Detect Eye Blink & Record With Sound',font=('helvetica 15 bold'))
but5.place(x=5,y=400)

but5=Button(frame,padx=5,pady=5,width=5,bg='orange',fg='black',relief=GROOVE,text='EXIT',command=exitt,font=('helvetica 15 bold'))
but5.place(x=210,y=478)

root.mainloop()