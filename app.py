from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)

API_URL = 'http://127.0.0.1:5000/api/livros'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        titulo = request.form.get('titulo')
        autor = request.form.get('autor')

        response = requests.post(API_URL, json={'titulo':titulo, 'autor': autor})
    
    response = requests.get(API_URL)
    if response.status_code == 200:
        livros = response.json()
    else:
        livros = []

    return render_template('index.html', livros=livros)

@app.route('/delete/<int:id>')
def delete(id):
    requests.delete(f'{API_URL}/{id}')
    return redirect('/')

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update (id):
    if request.method == 'POST':
        titulo = request.form['titulo']
        autor =request.form['autor']
        requests.put(
            f' {API_URL}/{id}',
            json={'titulo' : titulo, 'autor' : autor}
        )
        return  redirect('/')
        
    response = requests.get(f'{API_URL}/{id} ')
    if response.status_code == 200:
        livro = response.json()
    else:
        livro = {}

    return render_template('update.html', livro=livro)

if __name__ == '__main__':
    app.run(port=5001, debug=True)

