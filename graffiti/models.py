from django.contrib.auth import get_user_model
from django.db import models


class Graffiti(models.Model):
    svg_data = models.TextField(
        help_text="SVG markup as text",
        blank=False,
        null=False,
    )
    likes = models.ManyToManyField(
        get_user_model(),
        blank=True,
        related_name="liked_graffiti",
    )
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="graffiti",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.username + " - " + str(self.created_at)

    def likes_count(self):
        """
        Returns the number of likes.
        """
        return self.likes.count()
