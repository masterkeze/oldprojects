from tkinter import *
from math import *
root=Tk()
root.geometry('+250+150')#Deisign the location the calculator will show
root.title('Calculator')#Name the interface
enter=''
output=''

#The function of number
def click_number(num):
    global enter
    enter = enter + str(num)
    cal_input.configure(text=enter)


# function of calculation symbols, including continuous calculation.
def click_cal(symbol):
    global enter
    global output

    if enter == '':
        enter = output
        output = ''
        cal_output.configure(text=output)
    enter = enter + symbol
    cal_input.configure(text=enter)


#Function of special calculation
def click_special(symbol):
    global enter
    global output

    if enter == '' and ((output.replace('.','')).replace('-','')).isdecimal():
        enter = symbol+'(' + output+')'
        cal_input.configure(text=enter)
        output = ''
        cal_output.configure(text=output)
        return None
    
    enter = enter + symbol +'('
    cal_input.configure(text=enter)

#Function of reciprocal
def Press_reciprocal():
    global enter
    global output

    if enter == '' and ((output.replace('.','')).replace('-','')).isdecimal():
        enter = '1/' + output
        cal_input.configure(text=enter)
        output = ''
        cal_output.configure(text=output)
        return None
    if (enter.replace('.','')+'0').isdecimal():
        enter = '1/' + enter 
    else:
        enter = '1/(' + enter + ')'#special application of reciprocal
    cal_input.configure(text=enter)

#Function of equal symbol
def Press_equal():
    global enter,output
    
    try:
        if enter == '' or output == enter:
            cal_output.configure(text=output)
            return None
        output = str(eval(enter))
        cal_output.configure(text=output)
        enter = ''
    except:
        cal_output.configure(text='Expression error!')

#Function of clear button
def Press_clear():
    global enter,output
    enter = ''
    output = ''
    cal_input.configure(text=enter)
    cal_output.configure(text=output)

#Function of backspace button
def Press_backspace():
    global enter
    try:
        if enter.endswith('sin(') or enter.endswith('tan(') or enter.endswith('cos(') :
            enter = enter[:len(enter)-3]
        elif enter.endswith('sqrt('):
            enter = enter[:len(enter)-4]
        enter = enter[:len(enter)-1]
    except:
        pass
    cal_input.configure(text=enter)



#initial label

cal_input=Label(root, text=enter, width='37', height='3', bg='green', fg='yellow', font='12')
cal_input.grid(columnspan=5)

cal_output=Label(root, text=output, width='37', height='3', bg='yellow', fg='green', font='12')
cal_output.grid(row=1,columnspan=5)

#initial button

#row 1 :   '7'   '8'   '9'   '+'   'Clear'

number_seven=Button(root, text='7',width='7', height='2', command=lambda:click_number(7))
number_seven.grid(row=2, column=0,sticky = 'WE')

number_eight=Button(root, text='8',width='7', height='2', command=lambda:click_number(8))
number_eight.grid(row=2, column=1,sticky = 'WE')

number_nine=Button(root, text='9',width='7', height='2', command=lambda:click_number(9))
number_nine.grid(row=2, column=2,sticky = 'WE')

cal_plus=Button(root, text='+',width='7', height='2', command=lambda:click_cal('+'))
cal_plus.grid(row=2, column=3,sticky = 'WE')

function_clear=Button(root, text='Clear',width='7', height='2', command=Press_clear)
function_clear.grid(row=2, column=4,sticky = 'WE')

#row 2 :   '4'   '5'   '6'   '-'   '('

number_four=Button(root, text='4',width='7', height='2', command=lambda:click_number(4))
number_four.grid(row=3, column=0,sticky = 'WE')

number_five=Button(root, text='5',width='7', height='2', command=lambda:click_number(5))
number_five.grid(row=3, column=1,sticky = 'WE')

number_six=Button(root, text='6',width='7', height='2', command=lambda:click_number(6))
number_six.grid(row=3, column=2,sticky = 'WE')

cal_minus=Button(root, text='-',width='7', height='2', command=lambda:click_cal('-'))
cal_minus.grid(row=3, column=3,sticky = 'WE')

cal_left_bracket=Button(root, text='(',width='7', height='2', command=lambda:click_number('('))
cal_left_bracket.grid(row=3, column=4,sticky = 'WE')

#row 3 :   '1'   '2'   '3'   '*'   ')'

number_one=Button(root, text='1',width='7', height='2', command=lambda:click_number(1))
number_one.grid(row=4, column=0,sticky = 'WE')

number_two=Button(root, text='2',width='7', height='2', command=lambda:click_number(2))
number_two.grid(row=4, column=1,sticky = 'WE')

number_three=Button(root, text='3',width='7', height='2', command=lambda:click_number(3))
number_three.grid(row=4, column=2,sticky = 'WE')

cal_multiply=Button(root, text='*',width='7', height='2', command=lambda:click_cal('*'))
cal_multiply.grid(row=4, column=3,sticky = 'WE')

cal_right_bracket=Button(root, text=')',width='7', height='2', command=lambda:click_number(')'))
cal_right_bracket.grid(row=4, column=4,sticky = 'WE')

#row 4 :   '0'   '.'   '<='   '/'   '='

number_zero=Button(root, text='0',width='7', height='2', command=lambda:click_number(0))
number_zero.grid(row=5, column=0,sticky = 'WE')

number_point=Button(root, text='.',width='7', height='2', command=lambda:click_number('.'))
number_point.grid(row=5, column=1,sticky = 'WE')

function_backspace=Button(root, text='<=',width='7', height='2', command=Press_backspace)
function_backspace.grid(row=5, column=2,sticky = 'WE')

cal_divide=Button(root, text='/',width='7', height='2', command=lambda:click_cal('/'))
cal_divide.grid(row=5, column=3,sticky = 'WE')

cal_equal=Button(root, text='=',width='7', height='2', command=Press_equal)
cal_equal.grid(row=5, column=4,sticky = 'WE')

#row 5 :   'tan'   'cos'   'sin'   'sqrt'   '1/x'

special_tan=Button(root, text='tan',width='7', height='2', command=lambda:click_special('tan'))
special_tan.grid(row=6, column=0,sticky = 'WE')

special_cos=Button(root, text='cos',width='7', height='2', command=lambda:click_special('cos'))
special_cos.grid(row=6, column=1,sticky = 'WE')

special_sin=Button(root, text='sin',width='7', height='2', command=lambda:click_special('sin'))
special_sin.grid(row=6, column=2,sticky = 'WE')

special_sqrt=Button(root, text='sqrt',width='7', height='2', command=lambda:click_special('sqrt'))
special_sqrt.grid(row=6, column=3,sticky = 'WE')

special_reciprocal=Button(root, text='1/x',width='7', height='2', command=Press_reciprocal)
special_reciprocal.grid(row=6, column=4,sticky = 'WE')

root.mainloop()
