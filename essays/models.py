from django.db import models
'''from generators.models import Generator'''


class EssayArticle(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField(blank=True)

    def __str__(self):
        return self.title


class CuratedSlashdot(models.Model):
    title = models.CharField(max_length=256)
    introduction = models.TextField(blank=True)
    # description =  # shared with generators Model
    # tarot_card_image =  # shared with generators Model
    # galileo_content =  # shared with generators Model
    # f_loss_content =  # shared with generators Model
    conclusion = models.TextField(blank=True)
    # content_changes_logged =  # shared with this Model

    def __str__(self):
        return self.title


class CuratedWatchtower(models.Model):
    title = models.CharField(max_length=256)
    introduction = models.TextField(blank=True)
    # description =  # shared with generators Model
    # tarot_card_image =  # shared with generators Model
    # st_paul_content =  # shared with generators Model
    conclusion = models.TextField(blank=True)
    # content_changes_logged =  # shared with this Model

    def __str__(self):
        return self.title


class ContentChanges(models.Model):
    title = models.CharField(max_length=256)
    content_changes_logged = models.TextField(
        blank=True, help_text="Please use line space for bullet points")

    def __str__(self):
        return self.title

    def log_to_bullets(self):
        return self.content_changes_logged.split('\r\n')


# ContentChanges(models.Model).log_to_bullets(self)
