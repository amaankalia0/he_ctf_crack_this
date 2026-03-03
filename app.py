from flask import Flask, request, render_template_string, redirect, url_for

app = Flask(__name__)

# Login page template
LOGIN_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>SecureLogin Portal</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 400px; margin: 100px auto; padding: 20px; }
        .login-form { background: #f5f5f5; padding: 30px; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
        input { width: 100%; padding: 10px; margin: 10px 0; border: 1px solid #ddd; border-radius: 4px; }
        button { width: 100%; padding: 12px; background: #007bff; color: white; border: none; border-radius: 4px; cursor: pointer; }
        button:hover { background: #0056b3; }
        .hint { color: #666; font-size: 12px; margin-top: 10px; }
        .error { color: red; margin-top: 10px; }
    </style>
</head>
<body>
    <div class="login-form">
        <h2>Corporate Login Portal</h2>
        <form method="POST">
            <input type="email" name="email" placeholder="Email" value="admin@company.com" readonly>
            <input type="password" name="password" placeholder="Password" required>
            <button type="submit">Login</button>
        </form>
        <div class="hint">
            Email: admin@company.com<br>
            Password: Contact IT department for access<br><br>
            <!--<small style="color: #999; font-size: 10px;">
                Debug Info: %@ :?E6C?2==J 24466D @C 3JA2DD E96 2FE96?E:42E:@? AC@46DD )x\\?E6C?2=x244@DD ?665 E@ 36 25565 :? E96 A24<6E
            </small>-->
        </div>
        {% if error %}
        <div class="error">{{ error }}</div>
        {% endif %}
    </div>
</body>
</html>
'''

# Success page template with flag
SUCCESS_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Welcome - Internal Portal</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 600px; margin: 50px auto; padding: 20px; }
        .success { background: #d4edda; padding: 20px; border-radius: 8px; border: 1px solid #c3e6cb; }
        .flag { background: #fff3cd; padding: 15px; margin: 20px 0; border-radius: 4px; border: 1px solid #ffeaa7; font-family: monospace; }
    </style>
</head>
<body>
    <div class="success">
        <h2>🎉 Access Granted!</h2>
        <p>Welcome to the internal corporate portal.</p>
        <div class="flag">
            <strong>FLAG:</strong> CTF{h3ad3r_byp4ss_1s_34sy_wh3n_y0u_kn0w_h0w}
        </div>
        <p>Congratulations! You successfully bypassed the authentication by adding the correct header.</p>
    </div>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template_string(LOGIN_TEMPLATE)
    
    # Check for the secret header that bypasses authentication
    if request.headers.get('X-Internal-Access') == 'true':
        return render_template_string(SUCCESS_TEMPLATE)
    
    # Normal login logic (will always fail since no valid password exists)
    email = request.form.get('email')
    password = request.form.get('password')
    
    if email == 'admin@company.com' and password:
        # Always fail normal login
        error = "Invalid credentials. Contact IT department for assistance."
        return render_template_string(LOGIN_TEMPLATE, error=error)
    
    error = "Please fill in all fields."
    return render_template_string(LOGIN_TEMPLATE, error=error)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)