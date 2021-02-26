# Drop-Bot
 
Dropbox App is WhatsApp chatbot that will help you to save media from your phone to 
a dropbox file.
It uses Dropbox APIs, NGROK, Flask, Twilio and Python
1. To test, download repository to you machine: https://github.com/mcwilton/dropbox-app.git
2. Install Python and configure the environment
3. Register and get a free trial account with Twilio
4. Run Ngrok.exe, and run this command: ngrok http 5000
5. Copy the webhook with https:// and past that in your Twilio whatsapp sandbox
6. Run the requirements file to install the dependancies: pip install -r requirements.txt
7. Run this command: set FLASK_APP=app.py
8. To run your script: python -m flask run
9. Test the bot and have fun


For an already installed demo, 
1. Save this number +1 (415) 523-886 as Dropbot.
1. Send a whatsapp message to this number: join here-mathematics
2. You are ready to test. Type Hi

***Demo is running on AWS.