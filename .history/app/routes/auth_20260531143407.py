from flask import Blueprint,render_template,request,redirect,url_for,flash,session
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
auth_bp =Blueprint('auth',__name__)

 
@auth_bp.route('/login',methods=['GET','POST'])
def login():
    if request.method =='POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username= username).first()
    if user and check_password_hash(user.password,password):
        session['user']= username
        flash('login successful','success')
        return redirect(url_for('tasks.view_tasks'))
    flash("inavild username or passsword ",'danger')
    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    session.pop('user',None)
    flash("logout successuful",'info')
    return redirect(url_for('auth.login'))
