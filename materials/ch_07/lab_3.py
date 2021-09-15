# BMI CALCULATOR

def calculate_bmi(w, h, mode=1):
    if mode == 1:
        bmi = w / (h ** 2)
    elif mode == 2:
        bmi = (w / (h ** 2)) * 703
    else:
        bmi = None
    return bmi


def meaning_bmi(bmi):
    if bmi < 18.5:
        meaning = 'Under-weight'
    elif 18.5 <= bmi and bmi < 25:
        meaning = 'Normal'
    elif 25 <= bmi and bmi < 30:
        meaning = 'Over-weight'
    else:
        meaning = 'Obesity'
    return meaning


'''
mode 1: kg/m
mode 2: lb/in
'''

# mode = int(input('Choose mode (1=kg/m, 2=lb/in): '))
# weight = float(input('Enter your weight: '))
# height = float(input('Enter your height: '))
# bmi = calculate_bmi(weight, height, mode)

# w_unit = {1:'kg', 2:'lb'}
# h_unit = {1:'m', 2:'in'}
# print(f'Weight = {weight} {w_unit[mode]}, Height = {height} {h_unit[mode]} --> BMI = {bmi:.2f} --> {meaning_bmi(bmi)}')