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
    image = models.ImageField(upload_to='front_images', default='/media/')
    date_added = models.DateField(auto_now_add=True)
    project_tags = models.ManyToManyField(Tag)

    def to_dict(self):
        project_tags = []
        links = []
        screenshots = []
        for tag in Tag.objects.filter(project=self.id):
            project_tags.append(tag.to_dict())
        for link in Link.objects.filter(project=self.id):
            links.append(link.to_dict())
        for screenshot in Screenshot.objects.filter(project=self.id):
            screenshots.append(screenshot.to_dict())
        return {'id': self.id, 'name': self.name, 'description': self.description, 'image_url': self.image.url,
                'date_added': str(self.date_added), 'links': links, 'screenshots': screenshots,
                'project_tags': project_tags}

    def __str__(self):
        return self.name


class ProjectContrib(Project):
    """
        Model class for contributed project table
    """
    def to_dict(self):
        super(ProjectContrib, self).to_dict()

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
    link = models.URLField(max_length=150, blank=False)
    link_type = models.CharField(max_length=2, choices=LINK_TYPE_CHOICES, default=GITHUB)

    def to_dict(self):
        return {'id': self.id, 'link_type': self.link_type, 'link': self.link}

    def __str__(self):
        return self.project.name + ': ' + self.link_type


class Screenshot(models.Model):
    """
        Model class for Screenshot table
    """
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='screenshots_reference')
    image = models.ImageField(upload_to='screenshots', default='/media/')

    def to_dict(self):
        return {'id': self.id, 'screenshot_url': str(self.image.url)}

    def __str__(self):
        return self.project.name + '_' + str(self.id)
