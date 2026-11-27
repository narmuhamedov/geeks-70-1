from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100, 
                             verbose_name='укажите название блога')   
     
    image = models.ImageField(upload_to='blog/', verbose_name='загрузите фото')
    image_2 = models.ImageField(upload_to='blog/', verbose_name='загрузите фото2', null=True)
    
    descripiton = models.TextField(verbose_name='укажите описание блога',
                                    blank=True)
    GENRE = (
        ('Животные', 'Животные'),
        ('Морские обитатели', 'Морские обитатели'),
        ('Домашнии Животные', 'Домашнии Животные')
    )

    video_url = models.URLField(null=True, blank=True,verbose_name='укажите ссылку из youtube')

    genre = models.CharField(max_length=100, choices=GENRE, 
                             default='Животные', 
                             verbose_name='Выберите жанр') 
    
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.title}-{self.genre}'

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'

