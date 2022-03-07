from flask import Flask, request, render_template

app = Flask(__name__)

app.static_folder = 'static'

@app.route('/')
def ui():
   with open('config/pre.txt','r') as fh:
      x = fh.read()
      print(x)
      if x == 'blue':        
         return render_template('index.html',red='none',blue='block')
      else:
         return render_template('index.html',red='block',blue='none')


@app.route('/red')
def red():
    print ("\nred")
    with open('config/pre.txt','w') as fh:
       fh.write('red')
       fh.close
    return ("nothing")
    


@app.route('/blue')
def blue():
    print ("\nblue")
    with open('config/pre.txt','w') as fh:
       fh.write('blue')
       fh.close
    return ("nothing")

if __name__ == '__main__':
   app.run(debug = True)