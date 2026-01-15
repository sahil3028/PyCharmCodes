import zipfile
import pathlib

def zipCreate(filePaths,destDir):

    dest=pathlib.Path(destDir,'compressed.zip')
    with zipfile.ZipFile(dest,'w') as archive:
        for file_path in filePaths:
            file_path=pathlib.Path(file_path)
            archive.write(file_path,arcname=file_path.name)