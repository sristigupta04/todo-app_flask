from flask import Blueprint,render_template,request,redirect,url_for,flash,session
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from app.models import User
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


@auth_bp.route('/register',methods=['GET','POST'])
def register():
    if request.method == "POST":
        username = request.form.get('username')
        password= request.form.get('password')
        email = request.form.get("email")

    existing_user = User.query.filter_by(username= username).first()
    if existing_user:
        flash("user exist")
        return redirect(url_for("auth.register"))
    

    hashed_password = generate_password_hash(password)
    new_user = User(
        username= username,
        password= hashed_password
    )
    db.session.add(new_user)
    db.session.commit()

    flash("regisster successful")
    return redirect(url_for("auth.login"))
return render_template("register.html")