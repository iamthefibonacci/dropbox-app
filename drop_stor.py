import dropbox
import os

from twilio.twiml.messaging_response import MessagingResponse


dbx = dropbox.Dropbox('4LYbJIbHSy4AAAAAAAAAAZ0bI0AzCPDhhh3SyRkJIOs8fC7jQLE6jiNpxGfL5qPi')


def show_all_files(phone_number):
    all_files=[]
    pending_files=[]
    pending_files=dbx.files_list_folder(phone_number)

    for files in pending_files.entries:
      all_files.append(files.path_lower)

    return all_files


def dropbox_save(phone_number, file_url, extension):
    file_name = file_url[file_url.rfind('/')+1:]
    file_path = f'/{phone_number}/{file_name}.{extension}'
    return dbx.files_save_url(file_path, file_url)


def support():
    return "If you need assistance call +27 00 000 0000 or email us on ineedhelp@dropbot.co.za"


def dropbox_view(phone_number):
    path = f'/{phone_number}'
    folder_url = None
    try:
        link = dbx.sharing_create_shared_link_with_settings(path)
        folder_url = link.url
    except dropbox.exceptions.ApiError as exception:
        if exception.error.is_shared_link_already_exists():
            link = dbx.sharing_get_shared_links(path)
            folder_url = link.links[0].url
    return folder_url