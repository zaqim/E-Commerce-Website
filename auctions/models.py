from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    watchlist=models.ManyToManyField('Auction',blank=True,related_name="users")

class Category(models.Model):
    name = models.CharField(max_length=64)
    def __str__(self):
        return self.name

class Auction(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="auctions_user")
    title = models.CharField(max_length=32)
    description = models.TextField(max_length=1024)
    starting_bid = models.IntegerField()
    bid = models.ForeignKey('Bid', on_delete=models.CASCADE,null=True)
    category = models.ManyToManyField(Category, blank= True,related_name="auctions_category")
    url = models.CharField(max_length=128)
    def __str__(self):
        return f"{self.user.username}: {self.title}"

class Bid(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="bids_user")
    amount = models.IntegerField()
    def __str__(self):
        return f"{self.user.username} {self.amount}"

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="comments_user")
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE,related_name="comments")
    comment = models.TextField(max_length=1024)
    def __str__(self):
        return f"{self.user.username} {self.auction.title}: {self.comment}"