
import requests
import os
import tkinter as tk

def download_mp3():
    # url = input("Website address: ")
    # save_folder = input("Save folder path: ")
    # filename = input("MP3 file name: ")
    url=(WebAdress.get())
    save_folder =(StorageAdress.get())
    filename =(fileName.get())

    if not filename.endswith(".mp3"):
        filename += ".mp3"

    os.makedirs(save_folder, exist_ok=True)
    file_path = os.path.join(save_folder, filename)

    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()

        with open(file_path, "wb") as file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)


        print("✅ Download completed:", file_path)

    except requests.exceptions.RequestException as e:
        print("❌ Failed to download file:", e)
    
    


    root = tk.Tk()
    root.title("دانلود فایل")    

    tk.Label(root, text=": ادرس  وب سایت ").grid(row=0, column=0)
    WebAdress = tk.Entry(root)
    WebAdress.grid(row=0, column=1)

    tk.Label(root, text="ادرس ذخیره سازی:").grid(row=1, column=0)
    StorageAdress=tk.Entry(root)
    StorageAdress.grid(row=1, column=1)

    tk.Label(root, text="اسم فایل :").grid(row=2, column=0)
    filename= tk.Entry(root)
    filename.grid(row=3, column=1)
    tk.Button(root, text="دانلود",command=download_mp3).grid(row=4,column=1)
download_mp3()

