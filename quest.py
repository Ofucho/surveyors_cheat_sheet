def check_even():
    n = int(input("enter number: "))

    if n % 2 != 0:
        print("weird")
    elif (2 < n > 5) % 2 == 0:
        print("not weird")
    elif (6 < n > 20) % 2 == 0:
        print("weird")
    elif n > 20 % 2 == 0:
        print("Not weird")
    return n


# check_even()

def mean(some_list):
    the_mean = sum(some_list) / len(some_list)
    return the_mean


# print(mean(list(range(1,11))[-5:]))

# some_string = input("Say my name: ")
# # text_me = ('Another one %s!' % some_string.capitalize())
# print(f"Hello {some_string.capitalize()}")


def my_list():
    the_list = list(range(5, 30, 5))
    return the_list[0::4]


# print(my_list())

def even_odd(n):
    if n % 2 == 0:
        return 'even'
    else:
        return 'odd'


# x = int(input('Enter any number: '))
# print(even_odd(x))

def check_max():
    # x = range(4)

    b = [int(input('Enter number: ')) for each in range(4)]
    # l1 = [each for each in b if each in []]

    # for i in x:
    #     user_input = int(input('Enter number: '))
    #     b.append(user_input)
    # for each in b:
    #     if each not in l1:
    #         l1.append(each)
    # print(b)
    # print(l1)
    return max(b)


# print(check_max())


def dms2dd(degrees, minutes, seconds):
    dd = float(degrees) + float(minutes) / 60 + float(seconds) / (60 * 60);
    return dd


# t = input('Enter angle separated by space: ')
# a = tuple(float(x) for x in t.split())
# angle_decimal = dms2dd(a[0],a[1],a[2]).__round__(3)
# print(angle_decimal)

def dd2dms(deg):
    d = int(deg)
    md = abs(deg - d) * 60
    m = int(md)
    sd = (md - m) * 60
    return d, m, sd.__round__(3)


# print(dd2dms(dms2dd(a[0],a[1],a[2])))
"""
def phone_number(namba):
    if the_phone[0:2] == '07':
        return the_phone.replace('0','+254',1)
    elif the_phone[0:2] == '01':
        return the_phone.replace('0','+254',1)
    elif the_phone[0:1] == '7':
        return '+254' + namba
    elif the_phone[0:4] == '+254':
        return the_phone
    else:
        return 'enter a valid number'


the_phone = input('ENTER PHONE NUMBER: ')
# print(phone_number(the_phone))
"""


def greetings():
    first_name = input("Enter your first name: ")
    sir_name = input("Enter your sir name: ")
    greeting_card = f'Hello {first_name.capitalize()} {sir_name.capitalize()}'
    return greeting_card


# print(greetings())

def valid_email():
    while True:
        email_address = input('Enter your email address: ')
        at_sign = email_address.find('@')
        dot = email_address.find('.')
        if at_sign != -1 and dot != -1:
            break
        else:
            print('Please enter a valid email address')
            continue
    return email_address


# valid_email()


def phonenumber():
    phone_no = int(input('Enter phone number: '))
    while phone_no != int:
        continue
    else:
        valid_phone_no = f'{phone_no}'
        if valid_phone_no[0] == '7':
            return '+254' + valid_phone_no
        elif valid_phone_no[0] == '1':
            return '+254' + valid_phone_no


# print(phonenumber())

def validate_name():
    while True:
        name = input('Enter your full name: ')
        has_digit = any(map(str.isdigit, name))
        if has_digit is True:
            print('Please enter name without digits')
            continue
        else:
            break
    return name


# print(validate_name())


# details = [valid_email(), phonenumber(), validate_name()]
# print(details)


def largestinlist(x):
    # x = []
    for t in range(3):
        user_input = int(input('Enter a number: '))
        x.append(user_input)
        x.sort()
    print(x)
    y = 'a multiple of 4'
    if x[-1] % 4 == 0:
        print(x[-1], f'{y}')
    else:
        print(x[-1], f'is not {y}')
    return x


# largestinlist(x=[])

def grading_system(n):
    if 79 < n <= 100:
        print('A')
    elif 60 <= n <= 79:
        print('B')
    elif 49 < n <= 59:
        print('C')
    elif 40 < n <= 49:
        print('D')
    elif 0 <= n <= 40:
        print('E')
    else:
        print("Please enter a valid grade")
    return n


# grading_system(n=float(input('Enter grade: ')))
def area_triangle(b, h, co=0.5):
    area = co * b * h
    return area


# base = float(input('Enter base of triangle: '))
# height = float(input('Enter height of triangle: '))
# print(area_triangle(base,height))

def age(years):
    while years > 1:
        return years * 365
    else:
        return 'Age can not be 0'


# print(age(int(input('Enter your age: '))))


def speed_warning(speed):
    demerit = 0
    if 0 < speed <= 70:
        return 'OK'
    elif speed > 70:
        for each in list(range(75, 360, 5)):
            demerit += 1
            if speed == each:
                print(f'Your speed is {speed}km/h', f'\nPoints : {demerit}')
                if demerit > 12:
                    print('Your licence has been suspended')


# speed_warning(float(input('Enter speed: ')))


# temps = [234,678,438,345,763,23]
# new_temp = [temp / 10 for temp in temps]
# print(new_temp)

# user_name = input('Enter your full name: ')
# user_mail = input('Enter your email address: ')
# user_phone = input('Enter your phone number: ')

# speed = int(input('Enter speed: '))
# if 0 < speed <= 70:
#     print('okay')
# elif speed == range(75, 135, 5):
#     points = 0
#     for s in speed:
#         points += 1
#     print(speed, ',','points: ', points)

def chitchat(smalltalk):
    question_tags = ('how', 'when', 'which', 'what', 'who')
    if smalltalk.startswith(question_tags):
        return f'{smalltalk.capitalize()}?'
    else:
        return f'{smalltalk.capitalize()}.'


# print(chitchat(input('Say Something: ')))
results = []


# while True:
#     user_input = input('Say Something: ')
#     if user_input == "\end":
#         break
#     else:
#         results.append(chitchat(user_input))
# print('\n'.join(results))

def login(a, b):
    if a != 'admin@mail.com' and b != 'Admin@123':
        return 'Forgot Password??'
    else:
        return 'Login Successfull'


# email_address = input('Enter your email address: ')
# password = input('Enter your password: ')
#
# print(login(email_address, password))

# num=int(input("enter speed of car"))
# if num <=70 :
#     print("okay")
# else:
#     fastspeed= ((num -70)//5)
#     if fastspeed <=12:
#         print("Demerit points: " , fastspeed)
#     else:
#         print("Licence is suspended")

def stars():
    n = int(input("enter num"))
    for i in range(1, n + 1):
        print("*" * i)


# stars()


y = [each * each for each in range(1, 7).__reversed__()]
print(y)
