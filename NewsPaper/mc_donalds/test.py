

каким будет код метода update_rating(), согласно данного условия: метод update_rating()
модели Author, обновляет рейтинг текущего автора - user_id, метод принимает в качестве аргумента только self.
Он равен суммарному рейтингу - rating каждой статьи автора - author_id = user_id модели Post, умноженному на 3;
class Author(models.Model):  # наследуемся от класса Model
    user_id = models.OneToOneField('User')
    user_rating = models.IntegerField(default = 0)


class Post(models.Model):
    author_id = models.ForeignKey('Author')
    article_or_news = models.BooleanField(default = False)
    date_and_time = models.DateTimeField(auto_now_add = True)
    many_to_many_relation = models.ManyToManyField('Category', through = 'PostCategory')
    title =  models.CharField(max_length = 255)
    text_article_or_news = models.TextField()
    rating = models.IntegerField(default = 0)


    def update_rating(self):
        total_rating = 0
        for post in self.post_set.all():
            total_rating += post.rating
        self.user_rating = total_rating * 3
        self.save()