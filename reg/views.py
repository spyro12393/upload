from django.shortcuts import render
import os

# Create your views here.

'''
def main(request):
    # Render the main page

    context = {'like': 'Django 很棒'}
    return render(request, 'reg/reg.html', context)
'''


def main(request):
    if request.method == "POST":

        # print("files:", request.FILES.get("up_file"))
        # print(type(request.FILES.get("up_file")))
        print(type(request.FILES.get("up_file")))

        file_obj = request.FILES.get("up_file")

        print(file_obj.name)

        f1 = open(file_obj.name, "wb")

        for i in file_obj.chunks():
            f1.write(i)
        f1.close()

        hello = "hi"
        os.system("mv " + file_obj.name + ' ~/.jupyter/' + file_obj.name)

    return render(request, "reg/reg.html", locals())
