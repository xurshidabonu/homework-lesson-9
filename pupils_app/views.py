from django.shortcuts import render

# Create your views here.


pupils_list=[
    {"id":1,"Ism": "Shukurjonova Xurshidabonu", "masala1": 10, "masala2": 10, "masala3": 10},
    {"id":2,"Ism": "Abdujabborov Muhammadsaid", "masala1": 10, "masala2": 10, "masala3": 10},
    {"id":3,"Ism": "Yusufjon Muhammadov", "masala1": 9, "masala2": 5, "masala3": 9},
    {"id":4,"Ism": "Nurbek Doniyorov", "masala1": 8, "masala2": 6, "masala3": 8},
    {"id":5,"Ism":"Boburmirzo Muhammadov", "masala1": 10, "masala2": 4, "masala3": 7},
    {"id":6,"Ism": "Fazliddin Asomov", "masala1": 9, "masala2": 3, "masala3": 9},
    {"id":7,"Ism": "O'rolov Asadbek", "masala1": 10, "masala2": 6, "masala3": 6},
    {"id":8,"Ism": "Murodjon Azimov", "masala1": 7, "masala2": 7, "masala3": 7},
    {"id":9,"Ism": "O'taboyeva Lobaroy", "masala1": 10, "masala2": 6, "masala3": 9},
    {"id":10,"Ism": "Elbek Eliboyev", "masala1": 9, "masala2": 8, "masala3": 9}
]

def pupils(request):
    return render(request,'pupils_list.html',context={'pupils':pupils_list})


def pupil_info(request,pk):
    return render(request,"pupil_info.html",context={'pupil':pupils_list[pk-1]})






