from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()           
drive = GoogleDrive(gauth) 


from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
gauth = GoogleAuth()           
drive = GoogleDrive(gauth)  

debut_pdf="<br>\n<div style=\"text-align: center;\"><iframe src=\"https://drive.google.com/file/d/";

fin_pdf="/preview\" allow=\"autoplay\" width=\"100%\" height=\"500\"></iframe></div>";

debut_pptx="<br>\n<div style=\"text-align: center;\"><iframe src=\"https://docs.google.com/presentation/d/"

fin_pptx = "/embed?start=false&amp;loop=false&amp;delayms=3000\" allowfullscreen=\"true\" mozallowfullscreen=\"true\" webkitallowfullscreen=\"true\" width=\"100%\" height=\"500\" frameborder=\"0\"></iframe></div>"


file_list = drive.ListFile({'q': "'{}' in parents and trashed=false".format('id du dossier a utiliser')}).GetList();
id_list = [];
lien_list_pdf=[];
lien_list_pptx=[];
for file in file_list:
        
        print('title: %s, id: %s, lien:%s' % (file['title'], file['id'],file['webContentLink']));
        if (file['title'][-1]=="f"):
                lien_list_pdf.append(debut_pdf+file['id']+fin_pdf);
        if (file['title'][-1]=="x"):
                lien_list_pptx.append(debut_pptx+file['id']+fin_pptx);

for x in lien_list_pdf:
        print(x)
        print("\n")
for x in lien_list_pptx:
        print(x)
        print("\n")
print(lien_list_pdf);
print("\n\n\n\n\n",lien_list_pdf[3]);
