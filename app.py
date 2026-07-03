import os
import resend
from dotenv import load_dotenv
from flask import Flask, render_template, request

load_dotenv()

if not os.getenv("RESEND_API_KEY"):
    raise EnvironmentError("RESEND_API_KEY is missing")

resend.api_key = os.getenv("RESEND_API_KEY")

# This calculates the exact absolute path to your 'contacts' folder
base_dir = os.path.dirname(os.path.abspath(__file__))
contacts_path = os.path.join(base_dir, 'contact')

# Force Flask to use the precise path regardless of your terminal location
app = Flask(__name__, template_folder=contacts_path, static_folder=contacts_path)

# --- CONFIGURATION ---
CLIENT_COMPANY_EMAIL = "client-company@example.com" 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        # 1. Grab data out of the HTML form fields
        visitor_name = request.form.get('name')
        visitor_email = request.form.get('email')
        visitor_message = request.form.get('message')
        
        # 2. Package the data and hand it off to Resend
        try:
            email = resend.Emails.send({
                "from": "Website Contact Form <noreply@yourclientsdomain.com>",
                "to": [CLIENT_COMPANY_EMAIL],
                "subject": f"New Contact Form Submission from {visitor_name}",
                "reply_to": visitor_email,
                "html": f"""
                    <h3>New Message Received</h3>
                    <p><strong>Name:</strong> {visitor_name}</p>
                    <p><strong>Email:</strong> {visitor_email}</p>
                    <p><strong>Message:</strong></p>
                    <p style="white-space: pre-wrap; background: #f4f4f4; padding: 15px; border-radius: 5px;">{visitor_message}</p>
                """
            })
            
            # 3. Return a success state to the browser
            return "<h3>Thank you! Your message has been sent successfully.</h3>"
            
        except Exception as e:
            print(f"Error sending email via Resend: {e}")
            return "<h3>There was a problem sending your message. Please try again later.</h3>", 500

if __name__ == '__main__':
    app.run(debug=True)