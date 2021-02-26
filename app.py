from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from drop_stor import dropbox_view, dropbox_save, show_all_files, dbx, support


app = Flask(__name__)


@app.route('/reply/', methods=['POST'])
def reply():
    media_number = int(request.values['NumMedia'])
    media = request.values.get('MediaContentType0', '')
    
    
    print(media)
    print(user_cell = user_cell = request.values)
    
    
    user_cell = request.values['From']
    
    if user_cell.startswith('whatsapp'):
        user_cell = user_cell.split(':')[1]

    resp = MessagingResponse()
    
    incoming_msg = request.values['Body'].lower()
    if 'hi' in incoming_msg:
            reply = (f"Hi {user_cell}, I am DropBot :). Let me make DropBox backup management easy for you. \n"
                    "\n"
                    "*>> 1 :* Save files.\n"
                    "\n"
                    "*>> 2 :* View Folder.\n"
                    "\n"
                    "*>> 3 :* View files list. \n"
                    "\n"
                    "*>> 4 :* Support.\n"
                    "\n")

    elif incoming_msg == '1':
        reply = (
            f"Upload Videos, Photos & Audios, and I will save them to your DropBox folder.\n"
              )
    elif incoming_msg == '2':
        complete_folder = dropbox_view(user_cell)
        reply = f'Check your backup here: {complete_folder}'

    elif incoming_msg == '3':
        reply = f"Here are your all your files {show_all_files(f'/{str(user_cell)}')}"

    elif incoming_msg == '4':
        reply = support()

    elif media_number > 0:
        if media.startswith('image/'):
            file_url = request.values['MediaUrl0']
            extension = media.split('/')[1]
            dropbox_save(user_cell, file_url, extension)
            reply = 'Your image file has been saved! Press 2 to view it'

        elif media.startswith('audio/'):
            file_url = request.values['MediaUrl0']
            extension = media.split('/')[1]
            dropbox_save(user_cell, file_url, extension)
            reply = 'Your audio file has been saved! Press 2 to view it'

        elif media.startswith('video/'):
            file_url = request.values['MediaUrl0']
            extension = media.split('/')[1]
            dropbox_save(user_cell, file_url, extension)
            reply = 'Your video file has been saved! Press 2 to view it'

        else:
            reply = 'Sorry, file format not accepted.'
    else:
        reply = f"Sorry I do not understand what you said. Please type 'hi' for a menu"

    resp.message(reply)
    return str(resp)


