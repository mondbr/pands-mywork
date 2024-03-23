# Quiz.py
# variable types of the variables in the code
# author: Monika Dabrowska
# TBC

number_of_questions = 5
average_age = 23.4
debug_mode = True
name = "Joe"
ages = []
months = ("Jan", "Feb", "Mar")
book = {}
stuff = [ 12, "Fred", False, {}]
someone = dict(firstname="joe")
me = {
    "firstName": "Monika",
    "studying": [{
        "courseName": "programming",
        "semester": 1
    }, {
        "courseName": "Data Representation",
        "semester": 2
    }
    ]
} 



variables = [number_of_questions, average_age, debug_mode, name, ages, months, book, stuff, someone, me]


for variable in variables:
    print(type(variable))

    ### END
