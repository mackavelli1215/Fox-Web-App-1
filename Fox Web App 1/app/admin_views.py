from app import app
from flask import render_template


# Define routing views for Staff Portal
@app.route('/')
def admin_home():
    return render_template('index.html')

@app.route('/admin/dashboard')
def admin_dashboard():
    return render_template('admin/dashboard.html')

