from django.db import models


# verbose_name지정
# admin에 등록
# migration생성 및 적용
class Manufacturer(models.Model):
    name = models.CharField('제조사명', max_length=50)

    def __str__(self):
        return self.name


class Car(models.Model):
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
        verbose_name='제조사',
    )
    name = models.CharField('모델명', max_length=60)

    def __str__(self):
        # 현대 아반떼 <- 와 같이 출력되도록 처리
        return f'{self.manufacturer.name} {self.name}'
