
from django.urls import path
from . import views
from .views import HomeView,ArticleDetailView,SecondProjectsDetailView,ContactView,Projects
from .views import ProjectsDetailView,ThirdLatestPostDetailView,SubPictureDetailView
from .views import SecondSubPictureDetailView

urlpatterns = [
    #path('', views.home, name='home'),
    path('', HomeView.as_view(), name="home"),
    path('home/', HomeView.as_view(), name='home'),
    path('projects/', Projects.as_view(), name='projects'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name="detail"),
    path('article2/<int:pk>/', SecondProjectsDetailView.as_view(), name="second_detail"),
    path('sub_picture/<int:pk>/', SubPictureDetailView.as_view(), name="sub_detail"),
    path('second_sub_picture/<int:pk>/', SecondSubPictureDetailView.as_view(), name="second_sub_detail"),
    path('article3/<int:pk>/', ThirdLatestPostDetailView.as_view(), name="third_detail"),
    path('project_article/<int:pk>/', ProjectsDetailView.as_view(), name="project_article"),
    path('about_senwin/', views.AboutSenwin, name='about_senwin'),
    path('contact_senwin/', ContactView.as_view(), name='contact_senwin'),
    #path('message/', views.message, name='message'),
]