import os, shutil
FILE_TYPES={"Images":[".jpg",".png",".jpeg"],"Documents":[".pdf",".docx",".txt",".csv"],"Videos":[".mp4",".mkv"],"Audios":[".mp3"],"Codes":[".py",".js"],"Zips":[".zip"]}
def organize_folder(path):
    for file in os.listdir(path):
        fpath=os.path.join(path,file)
        if os.path.isfile(fpath):
            ext=os.path.splitext(file)[1].lower()
            for cat,exts in FILE_TYPES.items():
                if ext in exts:
                    dest=os.path.join(path,cat); os.makedirs(dest,exist_ok=True)
                    shutil.move(fpath,os.path.join(dest,file)); break
            else:
                dest=os.path.join(path,"Others"); os.makedirs(dest,exist_ok=True)
                shutil.move(fpath,os.path.join(dest,file))
organize_folder(input("Enter folder path: ").strip() or os.getcwd())
