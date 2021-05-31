from tkinter import *
window = Tk()
# Функции
def POR():
    if T0.get() == str(0) and T01.get() == str(0) and T1.get() == str(1) and T2.get() == str(2) and T3.get() == str(3) and T4.get() == str(4) and T5.get() == str(5) and T6.get() == str(6):
        T0['bg'] = 'green'
        T01['bg'] = 'green'
        T1['bg'] = 'green'
        T2['bg'] = 'green'
        T3['bg'] = 'green'
        T4['bg'] = 'green'
        T5['bg'] = 'green'
        T6['bg'] = 'green'
    else:
        T0['bg'] = 'red'
        T01['bg'] = 'red'
        T1['bg'] = 'red'
        T2['bg'] = 'red'
        T3['bg'] = 'red'
        T4['bg'] = 'red'
        T5['bg'] = 'red'
        T6['bg'] = 'red'

def RNR():
    if K1.get() == str(3) and K2.get() == str(2) and K3.get() == str(1) and K4.get() == str(2) and K5.get() == str(1) and K6.get() == str(1) and K7.get() == str(2):
        K1['bg'] = 'green'
        K2['bg'] = 'green'
        K3['bg'] = 'green'
        K4['bg'] = 'green'
        K5['bg'] = 'green'
        K6['bg'] = 'green'
        K7['bg'] = 'green'
    else:
        K1['bg'] = 'red'
        K2['bg'] = 'red'
        K3['bg'] = 'red'
        K4['bg'] = 'red'
        K5['bg'] = 'red'
        K6['bg'] = 'red'
        K7['bg'] = 'red'
# Сука пиши интерфейсы нормально
window.resizable(width= False, height= False)
window.geometry('1000x400')
window.title('Химиические элементы')
#window.iconbitmap('./icon.ico')
labeT1 =Label(text="H     O ",fg="orange",font='arial 30',width=20,height=1)
labeT2 =Label(text="  \   // ",fg="orange",font='arial 30',width=20,height=1)
labeT3 =Label(text="C",fg="orange",font='arial 30',width=20,height=1)
labeT4 =Label(text="|",fg="orange",font='arial 30',width=20,height=1)
labeT5 =Label(text="C - C -C - C - C -C -C - OH",fg="orange",font='arial 30',width=20,height=1)
labe2 =Label(text="ВВЕДИТЕ КОЭФФИЦИЕНТЫ И ПОРЯДОК ЭЛЕМЕНТОВ",fg="black",font='arial 15',width=70,height=1)
# КНОПКА ПРОВЕРКИ
button1 = Button(window, text = 'ПРОВЕРИТЬ ПОРЯДОК',bg = 'orange',width=20,height=1,command=POR)
button2 = Button(window, text = 'ПРОВЕРИТЬ КОЭФФИЦИЕНТ',bg = 'orange',width=25,height=1,command=RNR)
# КНОПКИ ПОРЯДКА
T0 = Entry(window,fg="yellow", bg="blue", width=1,font='arial 14')
T01 = Entry(window,fg="yellow", bg="blue", width=1,font='arial 14')
T1 = Entry(window,fg="yellow", bg="blue", width=1,font='arial 14')
T2 = Entry(window,fg="yellow", bg="blue", width=1,font='arial 14')
T3 = Entry(window,fg="yellow", bg="blue", width=1,font='arial 14')
T4 = Entry(window,fg="yellow", bg="blue", width=1,font='arial 14')
T5 = Entry(window,fg="yellow", bg="blue", width=1,font='arial 14')
T6 = Entry(window,fg="yellow", bg="blue", width=1,font='arial 14')
# КНОПКА КОЭФФИЦЕНТА
K1 = Entry(window,fg="yellow",bg="purple", width=1,font='arial 14')
K2 = Entry(window,fg="yellow", bg="purple", width=1,font='arial 14')
K3 = Entry(window,fg="yellow", bg="purple", width=1,font='arial 14')
K4 = Entry(window,fg="yellow", bg="purple", width=1,font='arial 14')
K5 = Entry(window,fg="yellow", bg="purple", width=1,font='arial 14')
K6 = Entry(window,fg="yellow", bg="purple", width=1,font='arial 14')
K7 = Entry(window,fg="yellow", bg="purple", width=1,font='arial 14')
#Упаковка
labe2.pack()
labeT1.pack()
labeT2.place(x=265, y=70)
labeT3.place(x=265,y =100)
labeT4.place(x=265,y=145)
labeT5.place(x=369,y= 190)
T0.place(x=390,y=180)
T01.place(x=455,y=180)
T1.place(x=516,y=110)
T2.place(x=508,y=180)
T3.place(x=572,y=180)
T4.place(x=637,y=180)
T5.place(x=690,y=180)
T6.place(x=742,y=180)
button1.place(y=200)
button2.place(y=250)
K1.place(x=390,y=230)
K2.place(x=455,y=230)
K3.place(x=508,y=230)
K4.place(x=572,y=230)
K5.place(x=637,y=230)
K6.place(x=690,y=230)
K7.place(x=742,y=230)
#THE END
window.mainloop()
