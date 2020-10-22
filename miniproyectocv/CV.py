from flask import Flask, url_for
from jinja2 import Template, Environment, FileSystemLoader
import yaml
file_loader = FileSystemLoader('miniproyectocv\\templates')
env = Environment(loader=file_loader)
app = Flask(__name__)
with open("miniproyectocv/MICV.yaml") as yaml_file:
    miyaml = yaml.load(yaml_file)
@app.route('/CV')
def CV():
    template = env.get_template('CV_.html')
    foto_mia = url_for('static', filename=miyaml['fotografia'])
    return template.render(my_data=miyaml, foto_mia=foto_mia)
@app.route('/')
def Linker():
    template = env.get_template('Linker.html')
    return template.render(my_data=miyaml, links=miyaml['Redes_Sociales'])

if __name__ == '__main__':
    app.run()