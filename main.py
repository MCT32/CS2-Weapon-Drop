from flask import Flask
import keyboard

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def drop():
        keyboard.send("g")
        return '''
            You just made a fuckwit drop his weapon<br>\n
            Use this button to do it again<br>\n
            <button onClick="history.go(0);">FUCK YOU</button>
        '''
    
    return app
