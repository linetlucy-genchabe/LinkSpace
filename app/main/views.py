from email.mime import image
from . import main
from flask import render_template,request,redirect,url_for,abort,flash
from ..models import  User,Comment,Post,Subscribers
from .forms import UpdateProfile,PostForm,CommentForm
from .. import db,photos
from flask_login import login_required,current_user
from ..email import mail_message,welcome_message
from datetime import datetime






@main.route("/", methods = ["GET", "POST"])
def index():
    
    posts = Post.query.order_by(Post.date_posted.desc()).all()
    
    if request.method == "POST":
        new_sub = Subscribers(email = request.form.get("subscriber"))
        db.session.add(new_sub)
        db.session.commit()
        welcome_message("Thank you for subscribing to lynne blog", "email/welcome", new_sub.email)
    return render_template("main/index.html",posts = posts)

@main.route("/post/<int:id>", methods = ["POST", "GET"])
def post(id):
    post = Post.query.filter_by(id = id).first()
  
    
    comments = Comment.query.filter_by(post_id = id).all()
    comment_form = CommentForm()
    comment_count = len(comments)

    if comment_form.validate_on_submit():
        comment = comment_form.comment.data
        comment_form.comment.data = ""
        comment_alias = comment_form.alias.data
        comment_form.alias.data = ""
        if current_user.is_authenticated:
            comment_alias = current_user.username
        new_comment = Comment(comment = comment, comment_at = datetime.now(),comment_by = comment_alias,post_id = id)
        new_comment.save_comment()
        return redirect(url_for("main.post", id = post.id))

    return render_template("main/post.html", post = post,comments = comments,comment_form = comment_form,comment_count = comment_count)



@main.route("/post/new", methods = ["POST", "GET"])
@login_required
def new_post():

    post_form = PostForm()
    if post_form.validate_on_submit():
        post_title = post_form.title.data
        post_form.title.data = ""

        filename = photos.save(post_form.image_file.data)
        path = f'photos/{filename}'


        post_content = post_form.content.data
        post_form.content.data = ""
        user_id = current_user._get_current_object().id

       

        new_post = Post(title = post_title, content = post_content,user_id=current_user._get_current_object().id,image_file=path)
        new_post.save_post()
        subs = Subscribers.query.all()
        for sub in subs:
            mail_message(post_title, "email/subscribers", sub.email, new_post = new_post)
            pass
        return redirect(url_for("main.index", id = new_post.id))
    
    return render_template("main/new_post.html",post_form = post_form)




@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)    
@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)    

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))
    
@main.route('/comment/<int:blog_id>', methods = ['POST','GET'])
def comment(blog_id):
    form = CommentForm()
    post = Post.query.get(blog_id)
    all_comments = Comment.query.filter_by(blog_id = blog_id).all()
    if form.validate_on_submit():
        comment = form.comment.data
        blog_id = blog_id
        new_comment = Comment(comment = comment,blog_id = blog_id)
        new_comment.save_comment()
        return redirect(url_for('.comment', blog_id = blog_id))
    return render_template('main/comment.html', form =form,  post =  post,all_comments=all_comments)

@main.route('/subscribe',methods = ['POST','GET'])
def subscribe():
    email = request.form.get('subscriber')
    new_sub = Subscribers(email = email)
    new_sub.save_subscriber()
    welcome_message("Subscribed to LinkSpace","email/welcome",new_sub.email,new_sub=new_sub)
    flash('Sucessfuly subscribed')
    return redirect(url_for('main.index'))
