from django.shortcuts import render

# Create your views here.
from dbe.mcbv.list_custom import ListView, ListRelated

# this is just a simple list view displaying the main listing of the forums forums
class Main(ListView):
    list_model    = Forum
    template_name = "forum/list.html"

# this list serves the threads view
class ForumView(ListRelated):
    # passes the forum model to the parameter detail model
    detail_model  = Forum
    # passes the thread model to the list model parameter
    list_model    = Thread
    related_name  = "threads"
    # defines what its templates name is
    template_name = "forum.html"
