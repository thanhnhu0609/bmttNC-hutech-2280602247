from flask import Flask, render_template, request, json
from Cipher.Caesar import CeasarCipher

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/caesar")
def caesar():
    return render_template('caesar.html')

@app.route("/encrypt", methods=['POST'])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    Caesar = CeasarCipher()
    encrypted_text = Caesar.encrypt_text(text, key)
    return f"text: {text}<br/>key:{key}<br/>enrypted text:{encrypted_text}"

@app.route("/decrypt", methods=['POST'])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyPlain'])
    Caesar = CeasarCipher()
    decrypted_text = Caesar.decrypt_text(text, key)
    return f"text: {text}<br/>key:{key}<br/>derypted text:{decrypted_text}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)