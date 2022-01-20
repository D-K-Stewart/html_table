from flask import Flask, render_template
app = Flask(__name__)   

@app.route('/')
def users():
    users = [
    {'first_name' : 'Jerry', 'last_name' : 'Seinfeld'},
    {'first_name' : 'George', 'last_name' : 'Castanza'},
    {'first_name' : 'Cosmo', 'last_name' : 'Kramer'},
    {'first_name' : 'Elaine', 'last_name' : 'Benes'}
    ]

    return render_template('index.html', users=users)








#KEEP THIS AT THE BOTTOM!
if __name__=="__main__":       
    app.run(debug=True)
