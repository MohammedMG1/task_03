from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {
        "my_list":[ 
            {"restaurant_name": "turkish mishawi",
             "food_type" :"lamb, beaf", 

            },
            {"restaurant_name":"shawrma shamiyah",
             "food_type":"all type of shawrma just pick yours",

            },
            {"restaurant_name":"MG Deserts",
             "food_type":"all type of deserts and coffes",
            },



        ]

    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
        "my_object":{
            "restaurant_name":"MG Deserts",
            "food_type":"all type of deserts and coffes"
            
        }
    }
    return render(request, 'detail.html', context)

