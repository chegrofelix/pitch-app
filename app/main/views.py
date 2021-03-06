from . import main
from flask import render_template, request, redirect, url_for, abort
from flask_login import login_required, current_user
from ..models import User, Pitch, Comment
from .forms import UpdateProfile, PitchForm, CommentForm
from .. import db, photos
import markdown2

@main.route('/')
def index():
    '''
    Getting the vaious categories we are goin to use
    '''
    categories = [
        'pickup lines',
        'Elevator Pitch',
        'Tech Quotes',
        'Playlists',
        'Extensions',
        'Trends'
        ]

    title = 'Pitch app'
    pitches = Pitch.query.all()

    return render_template('index.html', title = title, pitches = pitches, categories = categories)

@main.route('/user/<uname>')
@login_required
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    pitches_posted = Pitch.query.filter_by(user_id = current_user.id).all()
    return render_template('profile/profile.html', user = user, pitches = pitches_posted)

@main.route('/user/<uname>/update', methods = ['GET', 'POST'])
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

        return redirect(url_for('.profile', uname = user.username))

    return render_template('profile/update.html', form = form)

@main.route('/user/<uname>/update/pic', methods = ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()

    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = 'photos/{}'.format(filename)
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile', uname = uname))

@main.route('/new/pitch', methods = ['GET', 'POST'])
@login_required
def new_pitch():
    form = PitchForm()
    if form.validate_on_submit():
        pitch_title = form.title.data
        pitch_body = form.pitch.data

        pitch_title = markdown2.markdown(pitch_title, extras=["code-friendly", "fenced-code-blocks"])
        pitch_body = markdown2.markdown(pitch_body, extras=["code-friendly", "fenced-code-blocks"])
        new_pitch = Pitch(pitch_title = pitch_title, pitch_body = pitch_body, user = current_user, category =form.category.data, postedBy = current_user.username)
        new_pitch.save_pitch()

    title = 'Pitch app'
    return render_template('pitch/new_pitch.html', title = title, pitch_form = form)

@main.route('/pitch/comment/new/<int:id>', methods = ['GET', 'POST'])
@login_required
def new_comment(id):
    form = CommentForm()
    pitch = Pitch.query.filter_by( id = id).first()

    if form.validate_on_submit():
        title = form.title.data
        comment = form.comment.data

        title = markdown2.markdown(title, extras=["code-friendly", "fenced-code-blocks"])
        comment = markdown2.markdown(comment, extras=["code-friendly", "fenced-code-blocks"])

        new_comment = Comment(title = title, comment = comment, user = current_user, user_pitch = pitch, postedBy = current_user.username)
        new_comment.save_comment()

        return redirect(url_for('.pitch', id = id))

    title = 'Pitch app'

    return render_template('pitch/comment.html', title = title, form = form, pitch = pitch)

@main.route('/pitch/<int:id>')
@login_required
def pitch(id):
    pitch = Pitch.query.filter_by(id = id).first()

    comment = Comment.query.filter_by(pitch_id = pitch.id).all()
    comments = Comment.get_comments(id)
    commentBy = User.query.filter_by(id = Comment.user_id).all()

    return render_template('pitch/pitch.html', pitch = pitch, comment = comment, commentBy = commentBy,  comments = comments, postedBy = current_user.username)
    
@main.route('/pitch/delete/<int:id>')
@login_required
def delete_pitch(id):
    pitch = Pitch.query.filter_by(id=id).first()
    db.session.delete(pitch)
    db.session.commit()
    return redirect(url_for('main.profile', uname=current_user.username))