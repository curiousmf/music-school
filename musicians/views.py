from django.shortcuts import render, get_object_or_404
from musicians.models import Student


# Create your views here.
def show_start_page(request):
    context = {'students' : Student.objects.all()}
    return render(request,
                  'index.html',
                  context=context)

def new_student(request):
    if request.method == "POST":
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        age = request.POST.get('age')
        course = request.POST.get('course')
        instrument = request.POST.get('instrument')
        progress = request.POST.get('progress')
        payment = request.POST.get('payment')

        Student.objects.create(name = name,
                               surname = surname,
                               age = age,
                               course = course,
                               instrument = instrument,
                               progress = progress,
                               payment = payment
        )

    return render(request, 'nstudent.html')


def edit_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)

    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        age = request.POST.get('age')
        course = request.POST.get('course')
        instrument = request.POST.get('instrument')
        progress = request.POST.get('progress')
        payment = request.POST.get('payment')

        
        student.name = name
        student.surname = surname
        student.age = age
        student.course = course
        student.instrument = instrument
        student.progress = progress
        student.payment = payment

        student.save() 
    

    return render(request, 'estudent.html')