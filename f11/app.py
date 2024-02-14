from flask import Flask, render_template, redirect, abort, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/gugu/<int:num>')
def gugu(num):
    if num <2:
        return redirect('/gugu/2')
    gugu_list = [f'{num} x {i} = {num*i}' for i in range(1,10)]

    # for i in range(1,10):
    #     gugu_list.append(f'{num} x {i} = {num*i}')

    return render_template('gugu.html', gugu_list=gugu_list, num=num)

@app.route('/gugu2/<int:num>')
def gugu2(num):
    if num <2:
        return redirect('/gugu2/2')
    gugu_list = [f'{num} x {i} = {num*i}' for i in range(1,10)]

    # for i in range(1,10):
    #     gugu_list.append(f'{num} x {i} = {num*i}')

    return render_template('gugu2.html', gugu_list=gugu_list, dna=num)

languages = {
    'python': '파이썬',
    'js': '자바스크립트',
    'java': '자바',
}


@app.route('/languages/<name_en>')
def languages_detail(name_en):
    if name_en not in languages:
        abort(404)

    return render_template(
        template_name_or_list='language_detail.html', language=languages[name_en]
    )


#200,  201, 300~302, 400~405
@app.route('/languages/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        en = request.form['en']
        kr = request.form['kr']
        languages[en] = kr
        return redirect(f'/languages/{en}')
    return render_template('create.html')