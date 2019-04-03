from django.db import models
from django.db.models import Q, Count


class Skill(models.Model):
    name = models.CharField(verbose_name='Nome', max_length=20, blank=False, null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = "Skills"

class Project(models.Model):
    title = models.CharField(verbose_name='Título', max_length=150, blank=False, null=False)
    publication_date = models.DateTimeField(verbose_name='Publicação',auto_now=False, auto_now_add=True, blank=False, null=False)
    end_recruitment = models.DateTimeField(verbose_name='Prazo recrutamento', auto_now=False, auto_now_add=False, blank=False, null=False)
    project_description = models.TextField(verbose_name='Descrição', blank=False, null=False)
    #author = models.ForeignKey(User,verbose_name='Autor', null=True, blank=True, on_delete=models.CASCADE)
    github_link = models.CharField(verbose_name='GitHub', max_length=600, null=False, blank=False)
    contact_link = models.CharField(verbose_name='Contato', max_length=600, null=False, blank=False)
    #mockup = models.ImageField(verbose_name='Mockup', max_length=150, blank=False, null=False)


    def __str__(self):
        return self.title

    def post_total(self):
        return Project.objects  .filter(post__project=self.id).aggregate(Count('id'))['id__count']


    def post_available(self):
        return Project.objects.filter(Q(post__project=self.id), Q(post__availability=True)).aggregate(Count('id'))['id__count']


    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"

class Post(models.Model):
    availability = models.BooleanField(default=True)
    skill = models.ManyToManyField(Skill, verbose_name='Skill', blank=True)
    project = models.ForeignKey(Project, null=True, blank=True, on_delete=models.CASCADE)
    #user = models.ForeignKey()

    def __str__(self):
        return self.project.title

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"



