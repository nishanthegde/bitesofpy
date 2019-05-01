MIN_DRIVING_AGE = 18

def allowed_driving(name, age):

    if age >=  MIN_DRIVING_AGE:
        allowed_driving = 'is allowed to drive' 
    else:
        allowed_driving = 'is not allowed to drive'

    print(f'{name} {allowed_driving}')