from django.urls import path
from .import views

urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    path('base/',views.base,name='base'),
    path('register/',views.register,name='register'),
    path('login/',views.loginpage,name='login'),
    path('logout/',views.logoutpage,name='logout'),
    path('book/',views.book,name='book'),
    path('addbook/',views.addBook,name='addbook'),
    path('updatebook/<str:pk>/',views.updateBook,name='updatebook'),
    path('deletebook/<str:pk>/',views.deleteBook,name='deletebook'),
    path('author/',views.author,name='author'),
    path('addauthor/',views.addAuthor,name='addauthor'),
    path('updateauthor/<str:pk>/',views.updateAuthor,name='updateauthor'),
    path('deleteauthor/<str:pk>/',views.deleteAuthor,name='deleteauthor'),
    path('category/',views.category,name='category'),
    path('addcategory/',views.addCategory,name='addcategory'),
    path('updatecategory/<str:pk>/',views.updateCategory,name='updatecategory'),
    path('deletecategory/<str:pk>/',views.deleteCategory,name='deletecategory'),
    path('publication/',views.publication,name='publication'),
    path('addpub/',views.addPublication,name='addpub'),
    path('updatepublication/<str:pk>/',views.updatePublication,name='updatepublication'),
    path('deletepublication/<str:pk>/',views.deletePublication,name='deletepublication'),
    path('transaction/',views.transaction,name='trans'),
    path('student/',views.student,name='student'),
    path('teacher/',views.teacher,name='teacher')
]


