from flask import Flask, request, render_template
import functions as control
import pygetwindow as gw

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def home():
    service = request.form.get('service')
    match service:
      case 'youtube':
        control.openWebService("https://www.youtube.com.br")
      case 'netflix':
        control.openWebService("https://www.netflix.com/browse")
      case 'bing':
        control.openWebService("https://www.bing.com/search?q=Bing+AI&showconv=1&FORM=hpcodx")
      case 'chatgpt':
        control.openWebService("https://chat.openai.com/auth/login")
      case 'edge':
        control.openSystemService("edge")
      case 'whatsapp':
        control.openSystemService("whatsapp")
      case 'spotify':
        control.openSystemService("spotify")
      case 'vs_code':
        control.openSystemService("visual studio code")
      case 'vs_2022':
        control.openSystemService("visual studio 2022")
      case 'virtualbox':
        control.openSystemService("Oracle VM VirtualBox")
      case 'configs':
        control.openSystemService("configuracoes")
      case 'calculadora':
        control.openSystemService("calculadora")
      
    return render_template('index.html')

if __name__ == '__main__':
  app.run('0.0.0.0', debug = True)