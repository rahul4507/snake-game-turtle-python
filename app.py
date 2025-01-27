from flask import Flask, render_template, redirect, url_for, flash
import subprocess

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flash messages

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route to play the game
@app.route('/play')
def play():
    try:
        # Run the Python game script and wait for it to complete
        result = subprocess.run(['python', 'main.py'], check=True)
        flash("Game completed successfully!", "success")
    except subprocess.CalledProcessError as e:
        flash(f"An error occurred while running the game: {e}", "error")
    except Exception as e:
        flash(f"Unexpected error: {e}", "error")
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
