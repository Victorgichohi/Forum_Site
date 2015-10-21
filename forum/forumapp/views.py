from django.shortcuts import render

# Create your views here.
from dbe.mcbv.list_custom import ListView, ListRelated

from dbe.mcbv.edit import CreateView, UpdateView

# this is just a simple list view displaying the main listing of the forums forums
class Main(ListView):
    list_model    = Forum
    template_name = "forum/list.html"

# this list related view combines the detail and list views
# this  two models are connected by a ForeignKey relationship on the ListView model
# the related_name though needs to be specified.
class ForumView(ListRelated):
    # passes the forum model to the parameter detail model
    detail_model  = Forum
    # passes the thread model to the list model parameter
    list_model    = Thread
    related_name  = "threads"
    # defines what its templates name is
    template_name = "forum.html"


class ThreadView(ListRelated):
    # passes the thread model to the detail model parameter
    detail_model  = Thread
    # passes the post model to this list model parameter
    list_model    = Post
    related_name  = "posts"
    # defines what the template name html is
    template_name = "thread.html"




# ProfileForm is inherited from the standard ModelForm with posts and user fields excluded.
# this is just for editing ones profile
class EditProfile(UpdateView):
    form_model      = UserProfile
    modelform_class = ProfileForm
    success_url     = '#'
    template_name   = "profile.html"

    def modelform_valid(self, modelform):
        """Resize and save profile image."""
        # remove old image if changed
        name = modelform.cleaned_data.avatar
        pk   = self.kwargs.get("mfpk")
        old  = UserProfile.obj.get(pk=pk).avatar

        if old.name and old.name != name:
            old.delete()

        # save new image to disk & resize new image
        self.modelform_object = modelform.save()
        if self.modelform_object.avatar:
            img = PImage.open(self.modelform_object.avatar.path)
            img.thumbnail((160,160), PImage.ANTIALIAS)
            img.save(img.filename, "JPEG")
        return redir(self.success_url)
