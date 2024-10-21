from datetime import date, datetime


def Age(birthdate):
    today = date.today()
    DOB = datetime.strptime(birthdate, '%d/%m/%Y')
    
    age = today.year - DOB.year
    return age



def Gender_encoding(Gender):
    if Gender == 'male':
        Gender = 0
        
    elif Gender == 'female':
        Gender = 1
        
    return Gender


def BMI(Height, Weight):
    Bmi= Weight/ ((Height/100) * (Height/100))
    return Bmi