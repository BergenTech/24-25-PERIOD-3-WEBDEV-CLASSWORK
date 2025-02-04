from django.shortcuts import render
import random
def index(request):
    person = {'name':'Alex Smith',
              'title': 'Designer, Developer, Freelancer'}
    person2 = {'name':'John Doe',
              'title': 'Engineer, Author, Photographer'}
    people = ['Camila', 'Jared', 'Julien', ' Andrew', 'Grace']
    random_person = random.choice(people)
    
    return render(request,'index.html',{'name':random_person,'title':'student'})