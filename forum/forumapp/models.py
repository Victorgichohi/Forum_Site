from django.db import models

# Create your models here.
from dbe.settings import MEDIA_URL

# this is the class for the users profile
class UserProfile(BaseModel):
    avatar = ImageField("Profile Pic", upload_to="images/", blank=True, null=True)

    # get users posts
    posts  = IntegerField(default=0)
    user   = OneToOneField(User, related_name="profile")

    def __unicode__(self):
        return unicode(self.user)

    # increase users post
    def increment_posts(self):
        self.posts += 1
        self.save()
    # get users profile picture
    def avatar_image(self):
        return (MEDIA_URL + self.avatar.name) if self.avatar else None
