import dropbox
import os
from dropbox.files import WriteMode
class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

        for root,dirs, files in os.walk(file_from):

            for filename in files:

                local_Path = os.path.join(root,filename)
                
                releative_path=os.path.relpath(local_path,file_from)
                dropbox_path = os.path.join(file_to,releative_path)

                with open(local_path,'rb') as f:
                    dbx.files_upload(f.read(),dropbox_path,mode=WriteMode('overwrite'))

def main():
    access_token = 'sl.AxKmLmEYMoDJ0GeBhmjFomiwEM91hetLO-wJ02brpZD8e2B3FtXqQ1aZEmHMRM03r4009BZrspTkwc7v7-7u4O0B-s8SjMc1aSKLKsexOtsWptFWJD_J6kNNfghAEFfnFx5tUV4'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer : -")
    file_to = input("enter the full path to upload to dropbox:- ") 
    
    transferData.upload_file(file_from, file_to) 
    print("your file has been moved")

main()