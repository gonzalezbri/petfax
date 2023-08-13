from flask import ( Blueprint, render_template, request,redirect ) 

bp = Blueprint('fact', __name__, url_prefix="/facts")
#
@bp.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
       print(request.form)
       return redirect('/facts')
    
    return 'Thanks for submitting a fun fact!'

#nwe page
@bp.route('/new')
def new(): 
    return render_template('facts/new.html')


