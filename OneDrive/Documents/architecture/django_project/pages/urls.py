from django.urls import path
from .views import homePageView
from .views import index,listBooks,show,add,edit,remove,add_with_form
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

router = DefaultRouter()
router.register(r'api/books', BookViewSet, basename='book')

urlpatterns=[
    path('',homePageView,name='home'),
    path('index',index,name="index"),
    path('books',listBooks,name='listBooks'),
    path('<int:book_id>/', show,name='show'),
    path('ajouter_livre/', add ,name='add'),
    path('modifier_livre/', edit,name='edit'),
    path('supprimer_livre/', remove, name='remove'),
    path('ajouter_livre_form/',add_with_form,name='add book form'),
    path('', include(router.urls)),
    ]



