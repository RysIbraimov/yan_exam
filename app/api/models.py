from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from account.models import Author

class PostAbstract(models.Model):
    text = models.TextField(null=True,blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Post(PostAbstract):

    def __str__(self):
        return self.text[:10]

    def get_average_grade(self):
        grades = GradePost.objects.filter(post=self)
        score = sum([g.grade for g in grades])
        if score > 0:
            average = score / len(grades)
            return average
        return 0


class GradePost(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    grade = models.SmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['post', 'author']

class Comment(PostAbstract):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    comment_author = models.CharField(max_length=30,null=True,blank=True)

    def __str__(self):
        return f"{self.text[:10]}"



