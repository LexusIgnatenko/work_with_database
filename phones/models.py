from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля  `id`, `name`, `price`, `image`, `release_date`, `lte_exists` и `slug`.
    id = models.AutoField(primary_key=True, serialize=False)
    name = models.CharField('Название', max_length=50)
    price = models.DecimalField('Стоимость', decimal_places=2, max_digits=10)
    image = models.ImageField('Изображение', upload_to='')
    release_date = models.DateField('Дата выпуска')
    lte_exists = models.BooleanField('LTE', default=False)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    # def __str__(self):
        # return f'{self.name}, {self.price}: {self.image}'