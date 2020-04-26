from app import app

@app.route('/')
@app.route('/index')
def index():
    return 'Thanks for using our API. Contact owner for more information'
