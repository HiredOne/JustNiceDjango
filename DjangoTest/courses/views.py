from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Course
# Create your views here.

#BASE VIEW Class = View

class CourseListView(View):
    # Include class variable for modding data
    template_name = "courses/course_list.html" #ListView
    queryset = Course.objects.all()

    def get_queryset(self):
        return self.queryset

    def get(self, request, *args, **kwargs): # Standard args to be passed in
        # Defining (Overriding) GET method
        context = {'object_list' : self.get_queryset()}
        return render(request, self.template_name, context)

class CourseView(View):
    # Include class variable for modding data
    template_name = "courses/course_detail.html" #DetailView
    def get(self, request, id = None, *args, **kwargs): # Standard args to be passed in
        # Defining (Overriding) GET method
        context = {}
        if id is not None: # Logic purposes
            obj = get_object_or_404(Course, id = id)
            context["object"] = obj
        return render(request, self.template_name, context)
    
    # def post(self, request, *args, **kwargs):
    #     return render(request, 'about.html', {})

#HTTP Methods
def my_fbv(request, *args, **kwargs): # Same as above, but this is an FBV
    print(request.method)
    return render(request, 'about.html', {})