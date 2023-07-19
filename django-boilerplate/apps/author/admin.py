from django.contrib import admin
from .models import  ( AuthorOccupationModel, AuthorModel, SocialMediaModel,
                     OrdinaryUserModel, BlogPostModel, ContactModel, TagModel, CategoryModel,
                      CommentModel, ReviewModel )

# Register your models here.
admin.site.register(AuthorModel)
admin.site.register(AuthorOccupationModel)
admin.site.register(SocialMediaModel)
admin.site.register(OrdinaryUserModel)
admin.site.register(BlogPostModel)
admin.site.register(ContactModel)
admin.site.register(TagModel)
admin.site.register(CategoryModel)
admin.site.register(CommentModel)
admin.site.register(ReviewModel)

