from django.test import TestCase
from .models import Post, Comment
import datetime
from django.contrib.auth.models import User
# Create your tests here.


class TestPostModel(TestCase):

    def test_post_created(self):
        author = User(username='Jack')
        author.save()
        post = Post.objects.create(
            title='Test title',
            author=author,
            content='Test content',
            created_on=datetime.date.today(),
            status=1
        )
        post.save()
        self.assertTrue(post.status, 1)
        self.assertTrue(post.author, 'Jack')
        self.assertTrue(post.title, 'Test title')
        self.assertTrue(isinstance(post, Post))
        self.assertEqual(str(post), post.title)


class TestCommentModel(TestCase):

    def test_comment(self):
        author = User(username='Jack')
        author.save()
        post = Post.objects.create(
            title='Test title',
            author=author,
            content='Test content',
            created_on=datetime.date.today(),
            status=1
        )
        post.save()
        comment = Comment.objects.create(
            post=post,
            name='Max',
            email='max@testing.com',
            body='Test comment body',
            created_on=datetime.date.today(),
            active=1
        )
        comment.save()

        self.assertTrue(comment.active, 1)
        self.assertTrue(comment.name, 'Max')
        self.assertTrue(comment.body, 'Test comment body')
        self.assertTrue(isinstance(comment, Comment))
        self.assertEqual(
            str(comment), "Comment {} by {}".format(
                comment.body, comment.name))
