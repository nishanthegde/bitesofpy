cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}

def get_all_jeeps(cars=cars):
    """return a comma  + space (', ') separated string of jeep models (original order)"""

    return ", ".join(j for j in cars['Jeep'])


def get_first_model_each_manufacturer(cars=cars):
    """return a list of matching models (original ordering)"""
    first_models = [cars[k][0] for k in cars.keys()]

    return first_models


def get_all_matching_models(cars=cars, grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    grep_list = []

    for k in cars.keys():
        for v in cars[k]:
            if grep.lower() in v.lower():
                grep_list.append(v)

    return grep_list


def sort_car_models(cars=cars):
    """sort the car models (values) and return the resulting cars dict"""
    cars_sorted = {k:sorted(cars[k]) for k in cars.keys()}

    return cars_sorted
