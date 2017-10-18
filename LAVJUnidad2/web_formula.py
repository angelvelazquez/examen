from flask import Flask, render_template, request, redirect
from equa import energia

app = Flask(__name__)


@app.route('/')
def hello() -> '302':
    return redirect('/entry')


@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='EXAMEN UNIDAD 2')


@app.route('/exec_equation', methods=['GET', 'POST'])
def execute() -> 'html':
    m = int(request.form['m'])
    c = int(request.form['c'])
    title = 'This is the equation\'s result'
    result = energia(m, c)
    return render_template('result.html',
                           the_title=title,
                           the_m=m,
                           the_c=c,
                           the_result=result, )


if __name__ == '__main__':
    app.run('localhost', 5001, debug=True)
