from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask( __name__ )

app.config[ 'SQLALCHEMY_DATABASE_URI' ] = 'mysql+pymysql://root@localhost/guestbook'
app.config[ 'SQLALCHEMY_TRACK_MODIFICATIONS' ] = False

db = SQLAlchemy( app )


class Comments( db.Model ):
    id = db.Column( db.Integer, primary_key = True )
    name = db.Column( db.String( 20 ) )
    comment = db.Column( db.String( 250 ) )


@app.route( '/' )
def index():
    results = Comments.query.all()
    return render_template( 'index.html', results = results )


@app.route( '/sign' )
def sign():
    return render_template( 'sign.html' )


@app.route( '/process', methods = [ 'POST' ] )
def process():
    name = request.form[ 'name' ]
    comment = request.form[ 'comment' ]
    signature = Comments( name = name, comment = comment )
    db.session.add( signature )
    db.session.commit()
    return redirect( url_for( 'index' ) )


if __name__ == '__main__':
    app.run( debug = True )
