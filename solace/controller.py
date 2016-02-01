from model import InputForm
from flask import Flask, render_template, request
from compute import compute

app = Flask(__name__)

@app.route('/vib1', methods=['GET', 'POST'])
def index():
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        result = compute(form.A.data, form.B.data,
                         form.C.data, form.D.data,
                         form.E.data, form.F.data)
    else:
        result = None

    #return render_template('view_errcheck.html', form=form, result=result)
    return render_template('view_ttl.html', form=form, result=result)

if __name__ == '__main__':
    app.run(debug=True, port=5555)
