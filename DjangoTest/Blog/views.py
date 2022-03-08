from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import (
        CreateView,
        DetailView,
        ListView,
        UpdateView,
        ListView,
        DeleteView
)

from .models import Article
from .forms import ArticleModelForm
# Create your views here.

# Create the view as a class and pass the default view in as an arg
# Override the template_name variable with the location where the template
# is actually stored

# Class based view corresponds to the generic view passed in

class ArticleCreateView(CreateView):
    template_name = 'articles/article_create.html'
    form_class = ArticleModelForm # Include this if using custom model forms
    queryset = Article.objects.all() # <appName>/<modelName>_list.html

    def form_valid(self, form): # Override test validation of form
        print(form.cleaned_data) # See inputs given
        return super().form_valid(form) # Original form validation
    
    # If the model has a get_absolute_url mtd, the bottom is not necessary
    # This part is to set the URL for Django to return to after the obj is
    # created
    
    # success_url = '/' # Either override this var
    # def get_success_url(self): # Or override this mtd
    #     return '/'

class ArticleUpdateView(UpdateView):
    template_name = 'articles/article_create.html'
    form_class = ArticleModelForm # Include this if using custom model forms
    queryset = Article.objects.all() # <appName>/<modelName>_list.html

    # Define this method to tell Django how to get the object to be updated
	# Use this if kwargs are used in the extension (dynamic routing) 
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id = id_)

    def form_valid(self, form): # Override test validation of form
        print(form.cleaned_data) # See inputs given
        return super().form_valid(form) # Original form validation

class ArticleListView(ListView):
    template_name = 'articles/article_list.html'
    queryset = Article.objects.all() # <appName>/<modelName>_list.html

class ArticleDetailView(DetailView):
    template_name = 'articles/article_detail.html'
    queryset = Article.objects.all() # <appName>/<modelName>_list.html

    # Define this method to tell Django how to get the object for display
	# Use this if kwargs are used in the extension (dynamic routing) 
    def get_object(self): # Create (Override) this mtd to get obj to display
        id_ = self.kwargs.get("id") # Get id of obj
        return get_object_or_404(Article, id = id_) # Retrieve from DB

class ArticleDeleteView(DeleteView):
    template_name = 'articles/article_delete.html'
    queryset = Article.objects.all() # <appName>/<modelName>_list.html

    # Define this method to tell Django how to get the object for display
	# Use this if kwargs are used in the extension (dynamic routing) 
    def get_object(self): # Create (Override) this mtd to get obj to display
        id_ = self.kwargs.get("id") # Get id of obj
        return get_object_or_404(Article, id = id_) # Retrieve from DB
    
    def get_success_url(self):
        return reverse('Blog:article-list')