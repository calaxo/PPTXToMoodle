
#crer dossier dans drive et y meter un pptx



from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth() 
drive = GoogleDrive(gauth)

parent = "id du dossier a utliser"


file_metadata = {
  'title': 'cours1',
  'parents': [{'id': parent}],
  'mimeType': 'application/vnd.google-apps.folder'
}

folder = drive.CreateFile(file_metadata)
folder.Upload()

parent_id = folder['id']

# file_list = drive.ListFile({'q': "'{}' in parents and trashed=false".format(parent)}).GetList()
# for file in file_list:
# 	print('title: %s, id: %s' % (file['title'], file['id']))
entries = os.listdir('input')
upload_file_list = entries
for upload_file in upload_file_list:
	gfile = drive.CreateFile({'parents': [{'id': parent_id}],'title': upload_file})
	# Read file and set it as the content of this instance.
	gfile.SetContentFile("input/"+upload_file)
	gfile.Upload() # Upload the file.
