# Route definitions for Hotel Management System

from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, login_required, logout_user, current_user
from app import app, db
from app.models import User, Team, Room, Meeting, CostLog, Participants_user, Participants_partner, Businesspartner
from app.forms import LoginForm, RegistrationForm, RoomForm, MeetingForm, TeamForm
from datetime import datetime

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password')
    
    return render_template('login.html', form=form)

# Register route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form = RegistrationForm()
    if form.validate_on_submit():
        # Check if username already exists
        if User.query.filter_by(username=form.username.data).first():
            flash('Username already exists')
            return redirect(url_for('register'))
        
        # Check if email already exists
        if User.query.filter_by(email=form.email.data).first():
            flash('Email already exists')
            return redirect(url_for('register'))
        
        # Create new user
        user = User(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data
        )
        db.session.add(user)
        db.session.commit()
        
        flash('Registration successful! Please log in.')
        return redirect(url_for('login'))
    
    return render_template('register.html', form=form)

# Logout route
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

# Index route
@app.route('/')
@login_required
def index():
    return render_template('index.html')

# Book meeting route
@app.route('/book', methods=['GET', 'POST'])
@login_required
def book():
    form = MeetingForm()
    if form.validate_on_submit():
        # Check if room is available
        existing_meetings = Meeting.query.filter(
            Meeting.room_id == form.room.data,
            Meeting.date == form.date.data,
            ((Meeting.start_time < form.end_time.data) & (Meeting.end_time > form.start_time.data))
        ).all()
        
        if existing_meetings:
            flash('Room is not available at the selected time')
            return redirect(url_for('book'))
        
        # Create meeting
        meeting = Meeting(
            title=form.title.data,
            date=form.date.data,
            start_time=form.start_time.data,
            end_time=form.end_time.data,
            description=form.description.data,
            room_id=form.room.data,
            team_id=form.team.data,
            booker_id=current_user.id
        )
        db.session.add(meeting)
        db.session.commit()
        
        # Add booker as participant
        participant = Participants_user(
            meeting_id=meeting.id,
            user_id=current_user.id
        )
        db.session.add(participant)
        db.session.commit()
        
        flash('Meeting booked successfully!')
        return redirect(url_for('index'))
    
    return render_template('book.html', form=form)

# Room availability route
@app.route('/roomavailable', methods=['GET', 'POST'])
@login_required
def roomavailable():
    if request.method == 'POST':
        date = request.form['date']
        start_time = request.form['start_time']
        end_time = request.form['end_time']
        
        # Convert to datetime objects
        date_obj = datetime.strptime(date, '%Y-%m-%d').date()
        start_time_obj = datetime.strptime(start_time, '%H:%M').time()
        end_time_obj = datetime.strptime(end_time, '%H:%M').time()
        
        # Get all rooms
        all_rooms = Room.query.all()
        
        # Get occupied rooms
        occupied_rooms = Meeting.query.filter(
            Meeting.date == date_obj,
            ((Meeting.start_time < end_time_obj) & (Meeting.end_time > start_time_obj))
        ).all()
        
        # Get available rooms
        occupied_room_ids = [meeting.room_id for meeting in occupied_rooms]
        available_rooms = [room for room in all_rooms if room.id not in occupied_room_ids]
        
        return render_template('roomavailablelist.html', rooms=available_rooms, date=date, start_time=start_time, end_time=end_time)
    
    return render_template('roomavailable.html')

# Room occupation route
@app.route('/roomoccupation', methods=['GET', 'POST'])
@login_required
def roomoccupation():
    if request.method == 'POST':
        date = request.form['date']
        
        # Convert to date object
        date_obj = datetime.strptime(date, '%Y-%m-%d').date()
        
        # Get all meetings for the date
        meetings = Meeting.query.filter_by(date=date_obj).all()
        
        return render_template('roomoccupationlist.html', meetings=meetings, date=date)
    
    return render_template('roomoccupation.html')

# Costs route
@app.route('/costs', methods=['GET', 'POST'])
@login_required
def costs():
    if request.method == 'POST':
        meeting_id = request.form['meeting_id']
        amount = request.form['amount']
        description = request.form['description']
        
        # Create cost log
        cost_log = CostLog(
            meeting_id=meeting_id,
            amount=amount,
            description=description
        )
        db.session.add(cost_log)
        db.session.commit()
        
        flash('Cost recorded successfully!')
        return redirect(url_for('costs'))
    
    # Get all meetings
    meetings = Meeting.query.all()
    
    return render_template('costs.html', meetings=meetings)

# Cost check route
@app.route('/costcheck', methods=['GET', 'POST'])
@login_required
def costcheck():
    if request.method == 'POST':
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        
        # Convert to date objects
        start_date_obj = datetime.strptime(start_date, '%Y-%m-%d').date()
        end_date_obj = datetime.strptime(end_date, '%Y-%m-%d').date()
        
        # Get cost logs in date range
        cost_logs = CostLog.query.filter(
            CostLog.date >= start_date_obj,
            CostLog.date <= end_date_obj
        ).all()
        
        # Calculate total cost
        total_cost = sum(log.amount for log in cost_logs)
        
        return render_template('costcheck.html', cost_logs=cost_logs, total_cost=total_cost, start_date=start_date, end_date=end_date)
    
    return render_template('costcheck.html')

# All records route
@app.route('/allrecords')
@login_required
def allrecords():
    # Get all meetings
    meetings = Meeting.query.all()
    
    return render_template('allrecords.html', meetings=meetings)