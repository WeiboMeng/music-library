from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from app.models import db, Artist, Song, User
from werkzeug.security import generate_password_hash, check_password_hash 
import logging

main = Blueprint('main', __name__)
songs = Blueprint('songs', __name__)
ranking = Blueprint('ranking', __name__)
auth = Blueprint('auth', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@songs.route('/songs')
def song():
    """显示歌曲字母范围按钮"""
    ranges = ['A-G', 'H-N', 'O-T', 'U-Z']
    return render_template('songs.html', ranges=ranges)

@ranking.route('/ranking')
def rank():
    top_songs = [
        {"title": "Dynamite", "id": 31},
        {"title": "DDU-DU DDU-DU", "id": 32},
        {"title": "Shake It Off", "id": 11},
        {"title": "Shape of You", "id": 14},
        {"title": "Lemon", "id": 23}
    ]
    
    top_artists = [
        {"name": "Jay Chou", "id": 1},
        {"name": "Taylor Swift", "id": 20},
        {"name": "BTS", "id": 32},
        {"name": "BLACKPINK", "id": 33},
        {"name": "Beyoncé", "id": 12}
    ]
    
    return render_template('ranking.html', top_songs=top_songs, top_artists=top_artists)

@main.route('/regions')
def regions():
    """显示所有地区"""
    regions = ['Mandarin', 'Western', 'Japan', 'Korea']
    return render_template('regions.html', regions=regions)

@main.route('/artists/<region>')
def artists_by_region(region):
    artists = Artist.query.filter_by(region=region).all()
    return render_template('artist.html', artists=artists, region=region)

@main.route('/artist/<int:artist_id>')
def artist_detail(artist_id):
    artist = Artist.query.get_or_404(artist_id)
    source = request.args.get('source', 'regions')
    return render_template('artist_detail.html', artist=artist, source=source)

@songs.route('/select_songs/<range>')
def select_songs(range):
    session['range'] = range

    range_conditions = {
        'A-G': ('A', 'G'),
        'H-N': ('H', 'N'),
        'O-T': ('O', 'T'),
        'U-Z': ('U', 'Z')
    }
    if range in range_conditions:
        start, end = range_conditions[range]
        songs = Song.query.filter(Song.title.between(start, end)).order_by(Song.title).all()
    else:
        songs = []

    return render_template('select_songs.html', songs=songs, range=range)

@songs.route('/song_detail/<int:song_id>')
def song_detail(song_id):
    song = Song.query.get_or_404(song_id)
    source = request.args.get('source', 'songs')
    return render_template('song_detail.html', song=song, source=source)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):
            session['user'] = username
            flash('Login successful!', 'success')
            return redirect(url_for('main.index'))
        else:
            flash('Current username or password is incorrect.', 'error')
    
    return render_template('login.html')


@auth.route('/guest_login', methods=['POST'])
def guest_login():
    session['user'] = 'Guest'
    flash('Login as guest succeeded！', 'success')
    return redirect(url_for('main.index'))

@auth.route('/logout')
def logout():
    session.clear()
    flash('You have logged out.', 'info')
    return redirect(url_for('auth.login'))

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        logging.info(f"Received POST data: username={username}, password={password}, confirm_password={confirm_password}")

        if password != confirm_password:
            flash('Passwords do not match.', 'error')
            return render_template('register.html')

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('Username already exists. Please choose another one.', 'error')
            return render_template('register.html')

        new_user = User(username=username)
        new_user.set_password(password)

        try:
            db.session.add(new_user)
            db.session.commit()
            flash('Registration successful! You can now log in.', 'success')
        except Exception as e:
            db.session.rollback()
            logging.error(f"Database error: {e}")
            flash(f'Error: {str(e)}', 'error')

    return render_template('register.html')