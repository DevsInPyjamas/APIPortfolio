from django.db import models


class Tag(models.Model):
    """
        Model class for Tag table
    """
    tag = models.CharField(max_length=25, blank=False, unique=True)

    def to_dict(self):
        return {'id': self.id, 'tag': self.tag}

    def __str__(self):
        return '{}'.format(self.tag)


class Project(models.Model):
    """
        Model class for Project table
    """
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField()
    image_url = models.ImageField(upload_to='', default='/media/')
    date_added = models.DateField(auto_now_add=True)
    project_tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name


class ProjectContrib(Project):
    """
        Model class for contributed project table
    """
    def __str__(self):
        return self.name


class Link(models.Model):
    """
        Model class for Link table
    """
    GITHUB = 'GH'
    ITCH = 'IO'
    WEB = 'WB'
    LINK_TYPE_CHOICES = (
        (ITCH, 'ITCH.IO'),
        (GITHUB, 'GITHUB'),
        (WEB, 'WEBPAGE')
    )
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='links')
    link = models.CharField(max_length=150)
    link_type = models.CharField(max_length=2, choices=LINK_TYPE_CHOICES, default=GITHUB)

    def __str__(self):
        return self.project.name + ': ' + self.link_type


class Screenshot(models.Model):
    """
        Model class for Screenshot table
    """
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='screenshots_reference')
    image = models.ImageField(upload_to='project_images/screenshots', default='/media/')

    def __str__(self):
        return self.project.name + '_' + str(self.id)