from flask import ( Blueprint, render_template, request ) 

bp = Blueprint('fact', __name__, url_prefix="/facts")
#
@bp.route('/', methods=['POST'])
def index():
    print(request.form)
    return 'Thanks for submitting a fun fact!'

#nwe page
@bp.route('/new')
def new(): 
    return render_template('facts/new.html')