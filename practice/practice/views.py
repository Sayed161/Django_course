<<<<<<< HEAD
from django.shortcuts import render
from datetime import datetime
def home(request):
    Student = {'Name': 'Sheikh',
               'ID': 159,
               'class': 'Eight',
               'section': 'A'
               }

    Teacher = {'Name': 'Bongai', 'Expert': 'Youtube', 'salary': 12350}

    data = {'Student': [{'Name': 'Sheikh sayed',
                         'ID': 161,
                         'class': 'Ten',
                         'section': 'C'},
                        {'Name': 'akash Ahmed',
                         'ID': 122,
                         'class': 'five',
                         'section': 'A'}
                        ],
            'teacher': [{'Name': 'Bongai', 'Expert': 'Youtube', 'salary': 12350}, {'Name': 'Chotobhai','Expert': 'Food','salary': 11150}],
            'value': [{'Alpha':['a','b','c']}]
            }
    return render(request, 'home.html', data)


#  { 'Name': 'Sayed',
#         'ID ' : '161',
#         'class': 'Ten',
#         'section' : 'C'
#        },
#        { 'Name': 'Akash',
#         'ID ' : '122',
#         'class': 'five',
#         'section' : 'A'
#
# {
    #        'Name': 'ChotoBhai',
    #        'Expert': 'Food',
    #        'salary': 11150
    #    },}]
=======
from django.shortcuts import render
from datetime import datetime
def home(request):
    Student = {'Name': 'Sheikh',
               'ID': 159,
               'class': 'Eight',
               'section': 'A'
               }

    Teacher = {'Name': 'Bongai', 'Expert': 'Youtube', 'salary': 12350}

    data = {'Student': [{'Name': 'Sheikh sayed',
                         'ID': 161,
                         'class': 'Ten',
                         'section': 'C'},
                        {'Name': 'akash Ahmed',
                         'ID': 122,
                         'class': 'five',
                         'section': 'A'}
                        ],
            'teacher': [{'Name': 'Bongai', 'Expert': 'Youtube', 'salary': 12350}, {'Name': 'Chotobhai','Expert': 'Food','salary': 11150}],
            'value': [{'Alpha':['a','b','c']}]
            }
    return render(request, 'home.html', data)


#  { 'Name': 'Sayed',
#         'ID ' : '161',
#         'class': 'Ten',
#         'section' : 'C'
#        },
#        { 'Name': 'Akash',
#         'ID ' : '122',
#         'class': 'five',
#         'section' : 'A'
#
# {
    #        'Name': 'ChotoBhai',
    #        'Expert': 'Food',
    #        'salary': 11150
    #    },}]
>>>>>>> 5befc92 (little changes)
