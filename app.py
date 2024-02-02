from flask import Flask
import telegram
# Create the application instance
app = Flask(__name__)

TOKEN ='6806178452:AAHwxFmry9CVNlCXP-1IhKHMR3MyGDFEBgM'
bot = telegram.Bot(TOKEN)
chat_id = '620642951'

# route for index page
@app.route('/', methods=['POST'])
def index():
    print('index page')
    bot.send_message(chat_id=chat_id, text='Hello World!!!')
    return 'index page'
if __name__=="__main__":
    app.run(debug=True)