from flask import Blueprint,render_template,request,redirect,url_for,flash,session

auth_bp =Blueprint('auth',__name__)

User_credentials ={
    'username':"admin",
    'password':'1234'
}
@auth_bp.route('/login',methods=['GET','POST'])
def login():
    if request.method =='POST':
        username = request.form.get('username')
        password = request.form.get('password')

    if username == User_credentials['username'] and password == User_credentials['password']:
        session['user'] = username
        flash('login succesful','success')
    else:
        flash('invaild')
    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    session.pop('user',None)
    flash("logout successuful")
    return redirect('login.html')
