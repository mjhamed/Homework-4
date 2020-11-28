#Mohamed Hamed
#1644926

def get_age():
    age = int(input())
    if age >= 18 and age <= 75:
        return age
    else:
        raise ValueError('Invalid age.')

def fat_burning_heart_rate(age):
    calculation = ((70/100) * (220 - age))
    return calculation

if __name__ == '__main__':
    try:
        age = get_age()
        print('Fat burning heart rate for a',age,'year-old:',fat_burning_heart_rate(age),'bpm')
    except ValueError as upp:
        print(upp)
        print('Could not calculate heart rate info.\n')
