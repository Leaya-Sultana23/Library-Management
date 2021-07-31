import django_filters
from .models import *

class bookFilter(django_filters.FilterSet):
    class Meta:
        model = Book
        fields = ["name"]

class authorFilter(django_filters.FilterSet):
    class Meta:
        model = Author
        fields = ["name"]

class categoryFilter(django_filters.FilterSet):
    class Meta:
        model = Category
        fields =["name"]

class publishFilter(django_filters.FilterSet):
    class Meta:
        model = Publication
        fields = ["name"]