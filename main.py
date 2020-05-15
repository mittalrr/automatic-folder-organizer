import os #,shutil

def createIfNotExists(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def move(folder_name, files):
    for file in files:
        os.replace(file,f"{folder_name}/{file}")
        # shutil.move(file,f"{folder_name}/{file}")

if __name__ == "__main__":
    files=os.listdir()
    files.remove("main.py")
    print("\nfiles :- \n",files)

    imgext=[".png", ".jpg", ".jpeg"] # add more extensions if required so as to move them in Images folder
    images=[file for file in files if os.path.splitext(file)[1].lower() in imgext]
    print("\n\n\nImage Extensions :-\n",imgext,"\n\nImage Files :-\n",images)
    createIfNotExists('Images')
    move("Images", images)
    
    docext = [".txt", ".docx", ".doc", ".pdf"] # add more extensions if required so as to move them in Docss folder
    docs = [file for file in files if os.path.splitext(file)[1].lower() in docext]
    print("\n\n\nDoc Extensions :-\n",docext,"\n\nDoc Files :- \n",docs)
    createIfNotExists('Docs')
    move("Docs", docs)
    
    zipext = [".zip"] # add more extensions if required so as to move them in Zips folder
    zips = [file for file in files if os.path.splitext(file)[1].lower() in zipext]
    print("\n\n\nZip Extensions :-\n",zipext,"\n\nZip Files :-\n",zips)
    createIfNotExists('Zips')
    move("Zips", zips)
    
    mediaext = [".mp4", ".mp3", ".flv", ".mkv"] # add more extensions if required so as to move them in Media folder
    medias = [file for file in files if os.path.splitext(file)[1].lower() in mediaext]
    print("\n\n\nMedia Extensions :-\n",mediaext,"\n\nMedia Files :-\n",medias)
    createIfNotExists('Media')
    move("Media", medias)
    
    createIfNotExists('Others')
    others = []
    allext = imgext + docext + zipext + mediaext # add more extensions if required so as to move them in Others folder
    for file in files:
        exts = os.path.splitext(file)[1].lower()
        if (exts not in allext) and os.path.isfile(file):
            others.append(file)
    print("\n\n\nOther Files :- \n",others)
    
    move("Others", others)