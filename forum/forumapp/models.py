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

# this is the class which defines all the posts
class Post(BaseModel):
    # the title is set to a maximum length of 60
    title   = CharField(max_length=60)
    # the date the post was created is added too
    created = DateTimeField(auto_now_add=True)
    # this foreign key is used to get the name of the user who created the post.
    creator = ForeignKey(User, blank=True, null=True)
    # this thread also has a foreign key property and gets the posts of all the users then displays them
    thread  = ForeignKey(Thread, related_name="posts")
    # the body which shows all the threads is set to a maximum length of 10000,reducing that soon
    body    = TextField(max_length=10000)

    # this orders the posts by the date they were created
    class Meta:
        ordering = ["created"]

    # this gets the user who created that post,displays the title and shows that particular users thread of posts
    def __unicode__(self):
        return u"%s - %s - %s" % (self.creator, self.thread, self.title)

    # The short() method will be used in “Last Post” columns in forum and thread listings;
    def short(self):
        created = self.created.strftime("%b %d, %I:%M %p")
        return u"%s - %s\n%s" % (self.creator, self.title, created)

    #  profile_data() is used where user data is shown on the right side of each post in thread view.
    def profile_data(self):
        p = self.creator.profile
        return p.posts, p.avatar
