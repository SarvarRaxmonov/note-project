from django.db import models
from phone_field import PhoneField


class RequiredFieldsModel(models.Model):
    name = models.CharField(max_length=30, blank=False, default=None)
    email = models.EmailField()
    phone_number = PhoneField(blank=True, help_text='Contact phone number')

    class Meta:
        abstract = True

class TagModel(models.Model):
    tag_name = models.CharField(max_length=400, blank=False)

    def __str__(self):
        return self.tag_name
class CategoryModel(models.Model):
    category_name = models.CharField(max_length=500,blank=False)
    photo_of_category = models.ImageField(upload_to="images_of_categories", blank=False)

    def __str__(self):
        return self.category_name

class SocialMediaModel(models.Model):
    link = models.CharField(max_length=1000)
    photo_of_link = models.ImageField(upload_to="image_of_link", blank=False)
    social_media_name = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.social_media_name

class AuthorOccupationModel(models.Model):
    job_title = models.CharField(max_length=12)

    def __str__(self):
        return self.job_title

class AuthorModel(RequiredFieldsModel):
    Address = models.CharField(max_length=300, blank=True, default=None)
    social_media_links = models.ForeignKey(SocialMediaModel, on_delete=models.CASCADE)
    occupation = models.ForeignKey(AuthorOccupationModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class OrdinaryUserModel(RequiredFieldsModel):
    def __str__(self):
       return self.name


class BlogPostModel(models.Model):
    author = models.ForeignKey(AuthorModel, on_delete=models.CASCADE)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=900)
    date_time = models.DateTimeField(auto_now_add=True)
    view_count = models.IntegerField(default=0,null=False)
    hashtag = models.ForeignKey(TagModel, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images_of_author_posts", blank=True)
    video = models.FileField(upload_to="videos_of_author_posts", blank=True)
    blog_text = models.TextField(default="None")

    def __str__(self):
        return self.title

class CommentModel(models.Model):
    name = models.ForeignKey(OrdinaryUserModel, on_delete=models.CASCADE, blank=True)
    comment = models.CharField(max_length=1000,blank=True)
    post_id = models.ForeignKey(BlogPostModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.name.name
class ReviewModel(models.Model):
    review_score = models.IntegerField()
    post_id  = models.ForeignKey(BlogPostModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.post_id.title
    



class ContactModel(RequiredFieldsModel):
    subject = models.CharField(max_length=400,blank=False)
    text = models.TextField(default="None")

    def __str__(self):
        return self.name







