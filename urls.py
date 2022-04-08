from django.urls import path
from . import views

urlpatterns = [
    # path('snippets/', views.amit),

    
    # path('register/', views.Register.as_view()),

    path('login/', views.Login.as_view()),
     path('snippets/<int:pk>/', views.SnippetDetail.as_view()),

    
]



