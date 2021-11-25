from msilib.schema import ComboBox
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import push_up as pu
import cv2

#create Tkinter or GUI
main = Tk()
main.geometry('400x400+700+300')
main.title('Fill Out')
#Create Title 
Label(text = 'กรุณาเลือกข้อมูล หรือ กรอกข้อมูลให้ถูกต้อง', font = 100).place(x = 95, y = 15)
Label(text = '''      Please select the information 
      or Fill out the information correctly.''',
      font = 100).place(x = 55, y = 45)

#Create Sex
cb1 = StringVar(value = 'Select Gender')
ttk.Combobox(textvariable = cb1, values = ('Men', 'Woman'), width = 15, height = 20).place(y = 95, x = 150)
Label(text = 'เพศ (Gender)', font = 30).place(y = 95, x = 30)

#Create Weight
cb2 = StringVar()
Label(text = 'น้ำหนัก (Weight)', font = 100).place(y = 140, x = 30)
Entry(textvariable = cb2, width = 20).place(y = 140, x = 150)

#Create Height
cb3 = StringVar()
Label(text = 'ส่วนสูง (Height)', font = 100).place(y = 180, x = 30)
Entry(textvariable = cb3, width = 20).place(y = 180, x = 150)


#Create Age
cb4 = StringVar()
Label(text = 'อายุ (Age)', font = 100).place(y = 220, x = 30)
Entry(textvariable = cb4, width = 20).place(y = 220, x = 150)


#Create Exercise
cb5 = StringVar(value = 'Select Exrecise')
ttk.Combobox(textvariable = cb5, values = ('ไม่ได้ออกกำลังกายเลย', 
                                           'ออกกำลังกายเบาๆ 1-3 วันต่อสัปดาห์',
                                           'ออกกำลังกายปานกลาง 3-5 วันต่อสัปดาห์',
                                           'ออกกำลังกายหนัก 6-7 วันต่อสัปดาห์',
                                           'ออกกำลังกายอย่างหนักเป็นประจำ'),
                                           width = 30, height = 100).place(y = 270, x = 175)
Label(text = 'ออกกำลัง ครั้งต่อสัปดาห์', font = 30).place(y = 270, x = 30)

#Create Workout 
cb6 = StringVar(value = 'Select Gender')
ttk.Combobox(textvariable = cb6, values = ('Push_up', 'Pull_up'), width = 15, height = 20).place(y = 305, x = 150)
Label(text = 'เพศ (Gender)', font = 30).place(y = 305, x = 30)


#create Destroy
def destroy():
    main.destroy()
Button(text = 'Close Program', command = destroy, height = 2).place(y = 350, x = 50)

#create BMI and BMR
def BMI(x, y, z):
    b = int(x) / 100
    c = int(y) / (b**2)
    if cb1.get() == 'Men':
        a = 66 + (13.7 * int(y)) + (5 * int(x)) - (6.8 * int(cb4.get()))
        if z == 'ไม่ได้ออกกำลังกายเลย':
            a *= 1.2
        elif z == 'ออกกำลังกายเบาๆ 1-3 วันต่อสัปดาห์':
            a *= 1.375
        elif z == 'ออกกำลังกายปานกลาง 3-5 วันต่อสัปดาห์':
            a *= 1.55
        elif z == 'ออกกำลังกายหนัก 6-7 วันต่อสัปดาห์':
            a *= 1.7
        elif z == 'ออกกำลังกายอย่างหนักเป็นประจำ':
            a *= 1.9
    if cb1.get() == 'Woman':
        a = 665 + (9.6 * int(y)) + (1.8 * int(x)) - (4.7 * int(cb4.get()))
        if z == 'ไม่ได้ออกกำลังกายเลย':
            a *= 1.2
        elif z == 'ออกกำลังกายเบาๆ 1-3 วันต่อสัปดาห์':
            a *= 1.375
        elif z == 'ออกกำลังกายปานกลาง 3-5 วันต่อสัปดาห์':
            a *= 1.55
        elif z == 'ออกกำลังกายหนัก 6-7 วันต่อสัปดาห์':
            a *= 1.7
        elif z == 'ออกกำลังกายอย่างหนักเป็นประจำ':
            a *= 1.9
    return c, a
#create Infomation()
def infomation():
    try:
        def destroyinfo():
            info.destroy()
        z, y = BMI(cb3.get(), cb2.get(), cb5.get())
        info = Tk()
        info.geometry('400x400+700+300')   
        info.title('Information')
        Label(info, text = 'Information', font = 20).pack()
        Label(info, text = 'ข้อมูลต่างๆ', font = 20).pack()
        Label(info, text = '', font = 20).pack()
        Label(info, text = 'BMI', font = 20).pack()
        Label(info, text = '%.2f'%z, font = 20).pack()
        if z < 18.50:
            Label(info, text = 'น้ำหนักน้อย / ผอม', font = 5).pack()
        elif z >= 18.5 and z <= 22.9:
            Label(info, text = 'ปกติ (สุขภาพดี)', font = 20).pack()
        elif z >= 23 and z <= 24.90:
            Label(info, text = 'ท้วม / โรคอ้วนระดับ 1', font = 20).pack()
        elif z >= 25 and z <= 29.90:
            Label(info, text = 'อ้วน / โรคอ้วนระดับ 2', font = 20).pack()
        else:
            Label(info, text = 'อ้วนมาก / โรคอ้วนระดับ 3', font = 20).pack()
        Label(info, text = '', font = 20).pack()
        Label(info, text = '', font = 20).pack()
        Label(info, text = 'BMR', font = 20).pack()
        Label(info, text = '%.2f'%y, font = 20).pack()
        Label(info, text = 'ควรได้รับ แคลอรี่ต่อวัน', font = 20).pack()
        Button(info, text = 'Close Program', font = 20, command = destroyinfo).pack()
        info.mainloop()
    except:
        messagebox.showerror('Error', 'Not Number or Not complete')
Button(text = 'Show Information', command = infomation, height = 2).place(y = 350, x = 150)
                                                                          
                                                                          
                                                                          
                                                                          
#create next
def info():
    if cb6.get() == 'Push_up':
        pu.workout()
Button(text = 'Next', command = info, height = 2, width = 10).place(y = 350, x = 264)







main.mainloop()