from . import db
from werkzeug.security import (generate_password_hash,check_password_hash)
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(int(user_id))

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    username = db.Column(db.String(255), unique = True)
    email = db.Column(db.String(255), unique = True, index = True)
    bio = db.Column(db.String())
    avatar_path = db.Column(db.String())
    password_hash = db.Column(db.String(255))
    posts = db.relationship("Post",
                            backref = "user",
                            lazy = "dynamic")
    comments = db.relationship("Comment",
                                backref = "user",
                                lazy = "dynamic")


    @property
    def password(self):
        raise AttributeError("You cannot read the password attribute")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"User {self.username}"


class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key = True)
    post_title = db.Column(db.String)
    post_content = db.Column(db.Text)
    posted_at = db.Column(db.DateTime)
    post_by = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    comments = db.relationship("Comment", 
                                foreign_keys = "Comment.post_id", 
                                backref = "post", 
                                lazy = "dynamic")

    def save_post(self):
        db.session.add(self)
        db.session.commit()

    def delete_post(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_user_posts(cls,id):
        posts = Post.query.filter_by(user_id = id).order_by(Post.posted_at.desc()).all()
        return posts

    @classmethod
    def get_all_posts(cls):
        return Post.query.order_by(Post.posted_at).all()


class Comment(db.Model):
    __tablename__ = "comments"

    id = db.Column(db.Integer, primary_key = True)
    comment = db.Column(db.String)
    comment_at = db.Column(db.DateTime)
    comment_by = db.Column(db.String)
    like_count = db.Column(db.Integer, default = 0)
    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def delete_comment(cls, id):
        gone = Comment.query.filter_by(id = id).first()
        db.session.delete(gone)
        db.session.commit()

    @classmethod
    def get_comments(cls,id):
        comments = Comment.query.filter_by(post_id = id).all()
        return comments


class Subscribers(db.Model):
    __tablename__ = "subscribers"
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(255), unique = True, index = True)

