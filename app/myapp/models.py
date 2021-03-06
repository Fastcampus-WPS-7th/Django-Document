from django.db import models


# ./manage.py startapp myapp
# 아래 모델들을 admin에 등록
# admin에 로그인 할 유저 생성 (createsuperuser)
# runserver후 admin로그인
class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(
        max_length=100,
        blank=True
    )


class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField(
        blank=True,
        null=True,
    )
    num_stars = models.IntegerField()


class Person(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)

    def __str__(self):
        # 이한영 (PK: 1, 셔츠 사이즈: Medium)
        return '{name} (PK: {pk}, 셔츠 사이즈: {shirt_size}'.format(
            name=self.name,
            pk=self.pk,
            shirt_size=self.get_shirt_size_display(),
        )
