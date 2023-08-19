from django.db import models


NULLABLE = {
    'null': True,
    'blank': True,
}

class Category(models.Model):
    name = models.CharField(max_length=250, verbose_name='Category')
    description = models.TextField(verbose_name='Description')
    # created_at = models.DateTimeField(**NULLABLE, verbose_name='Created At')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Product(models.Model):

    name = models.CharField(max_length=250, verbose_name='Name')
    description = models.TextField(**NULLABLE, verbose_name='Description')
    photo = models.ImageField(upload_to='shop/',**NULLABLE, verbose_name='Photo')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Category')
    price = models.IntegerField(verbose_name='Price')
    date_created = models.DateTimeField(verbose_name='Date Created')
    date_modified = models.DateTimeField(**NULLABLE, verbose_name='Date Modified')

    def __str__(self):
        return f'{self.name} (Price: {self.price}): {self.description}'

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class Contact(models.Model):
    name = models.CharField(max_length=250, verbose_name='Contact name')
    email = models.EmailField(max_length=250, verbose_name='Email')
    message = models.TextField(**NULLABLE, verbose_name='Message')

    def __str__(self):
        return f'{self.name} ({self.email}): {self.message}'

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'