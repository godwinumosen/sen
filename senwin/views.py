from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView,ListView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.urls import reverse
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin  
from .models import SenwinMainPost,SenwinProjectPost,Contactvideo,SenwinLatestPost

'''def home(request):
    return render (request,'senwin/home.html')'''


#The main HomeView page
class HomeView(ListView): 
    model = SenwinMainPost
    template_name = 'senwin/home.html'
    #This model is for the second senwin page
    def get_context_data(self, **kwargs):  
        context = super().get_context_data(**kwargs)
    #the sencon senwin home page
        context['senwin_sencond_home_pages'] = SenwinProjectPost.objects.all()   
        context['senwin_latest_pages'] = SenwinLatestPost.objects.all()  
        return context 

 #The first Senwin post ArticleDetailView page
class ArticleDetailView(DetailView):
    model = SenwinMainPost
    template_name = 'senwin/article_detail.html'
    def ArticleDetailViewDeusmagnuslimited(request, pk): 
        object = get_object_or_404(SenwinMainPost, pk=pk)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
        return render(request, 'article_detail.html', {'detail': object})
    

#The second ArticleDetailView page of deus magnus group
class SecondProjectsDetailView(DetailView):
    model = SenwinProjectPost
    template_name = 'senwin/second_article_detail.html'    
    context_object_name = 'second_projects'
    def SecondProjectsDetailView(request, pk): 
        object = get_object_or_404(SenwinProjectPost, pk=pk)
        return render(request, 'senwin/second_article_detail.htm', {'second_detail': object})
    
#The third ArticleDetailView page of deus magnus groups
class ThirdLatestPostDetailView(DetailView):
    model = SenwinLatestPost
    template_name = 'senwin/third_article_detail.html'    
    context_object_name = 'third_projects'
    def ThirdLatestPostDetailView(request, pk):
        object = get_object_or_404(SenwinLatestPost, pk=pk)
        return render(request, 'senwin/third_article_detail.htm', {'third_detail': object})

#The project class base View page
class Projects(ListView): 
    model = SenwinProjectPost
    template_name = 'senwin/projects.html'

#The project ArticleDetailView page
class ProjectsDetailView(DetailView):
    model = SenwinProjectPost
    template_name = 'senwin/second_article_detail.html'    
    context_object_name = 'second_projects'
    def ProjectsDetailView(request, pk): 
        object = get_object_or_404(SenwinProjectPost, pk=pk)
        return render(request, 'senwin/second_article_detail.htm', {'second_detail': object})

def AboutSenwin(request):
    return render (request,'senwin/about_senwin.html')

# The Contact view been implemented
class ContactView(ListView):
    model = Contactvideo
    template_name = 'senwin/contact_senwin.html'

    def get(self, request):
        videos = Contactvideo.objects.all()
        return render(request, self.template_name, {'object_list': videos,})

    def post(self, request):
        if request.method == 'POST':
            message_name = request.POST['message-name']
            message_email = request.POST['message-email']
            message_subject = request.POST['message-subject']
            message = request.POST['message']
            # Process the form (e.g., send an email)
            messages.success(request, f'Your email was Successfully {message_name}..')
            return render(request, 'senwin/message.html', {'message_name': message_name})
        else:
            # If the form is not valid, render the template again with the form errors
            videos = Contactvideo.objects.all()
            return render(request, self.template_name, {'object_list': videos,})

'''def message (request):
    return render (request, 'senwin/message.html',)'''


