

from flask import *
from database import *


public=Blueprint("public",__name__)


@public.route('/')
def home_page():

    return render_template('index.html')


@public.route('/login',methods=['get','post'])
def login():

    if 'login' in request.form:
        uname=request.form['uname']
        password=request.form['pwd']

        qry="select * from login where username='%s' and password ='%s'"%(uname,password)
        res=select(qry)

        if res:
            session['login_id']=res[0]['login_id']

            if res[0]['user_type']=='admin':
                return ("<script>alert('login successfull');window.location='/admin_home'</script>")
        else:
            return ("<script>alert('Invalid Username or Password ');window.location='/login'</script>")

    return render_template('login.html')