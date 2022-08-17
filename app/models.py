from django.db import models


class Quiz(models.Model):
    question = models.TextField()
    
    def __str__(self):
        return self.question

class Options(models.Model):
    option = models.TextField()
    question = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.option
