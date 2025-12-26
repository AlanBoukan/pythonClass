import requests
import os
def downloade_mp3():
    url=input("Web site adress:")
    Save_Folder=input("save the folder path:")
    filename=input("The mp3 file name:")
    os.makedirs(Save_Folder, exist_ok=True)
    file_path=os.path.join(Save_Folder,filename)
    response=requests.get(url)
    print(response)

    if response.status_code == 200:
        with open(file_path, "wb") as file:
            file.write(response.content)
        print("download  completed",file_path)
    else:
        print("Failed to download file")
downloade_mp3()