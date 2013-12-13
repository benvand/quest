from django.db import models
from django.contrib.auth import get_user_model
#User class is:
User = get_user_model()
# Create your models here.

class Question(models.Model):
    question =          models.CharField(max_length=255)
    explainantion =     models.TextField()
    example =           models.TextField()
    picture =           models.ImageField(upload_to='quest/pictures')
    attached =          models.FileField(upload_to='quest/attachments')
    created =           models.TimeField(auto_now_add=True)
    modified =          models.TimeField(auto_now=True)
    categories =        models.ManyToManyField('Category')
    userid =            models.ForeignKey(User)

    class Meta():
        ordering = ('created',)
        get_latest_by = ('created',)
        verbose_name = 'Forum Post'
        verbose_name_plural = 'Forum Posts'

class Answer(models.Model):
    answer =            models.TextField()
    picture =           models.ImageField(upload_to='quest/pictures')
    attached =          models.FileField(upload_to='quest/attachments')
    created =           models.TimeField(auto_now_add=True)
    modified =          models.TimeField(auto_now=True)
    references =        models.ForeignKey('Answer', null=True,
                            related_name='questionanswerreference')
    userid =            models.ForeignKey(User)
    questionid =        models.ForeignKey('Question')

    class Meta():
        ordering = ('created',)
        get_latest_by = ('created',)
        verbose_name = 'Forum Reply'
        verbose_name_plural = 'Forum Replies'

class Category(models.Model):
    title =             models.CharField(max_length=255)
    keywords =          models.CharField(max_length=1000)
    jobs =              models.TextField()
    created =           models.TimeField(auto_now_add=True)

    class Meta():
        ordering = ('created',)
        get_latest_by = ('created',)
        verbose_name = 'Forum Category'
        verbose_name_plural = 'Forum Categories'

class Vote(models.Model):
    created =           models.TimeField(auto_now_add=True)
    questionid =        models.ForeignKey('Question')
    userid =            models.ForeignKey(User)


    class Meta():
        abstract = True

class UpVote(Vote):
    class Meta():
        ordering = ('created',)
        get_latest_by = ('created',)
        verbose_name = 'Upvote'
        verbose_name_plural = 'Upvotes'

class DownVote(Vote):
    class Meta():
        ordering = ('created',)
        get_latest_by = ('created',)
        verbose_name = 'Downvote'
        verbose_name_plural = 'Downvotes'