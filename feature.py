from flask import Flask
from flask import render_template

FAI=Flask(__name__)

@FAI.route('/htmlpage')
def htmlpage():
    return render_template('htnl.html')

if __name__=='__main__':
    FAI.run(debug=True)