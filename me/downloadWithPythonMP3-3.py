
import requests
import os
import tkinter as tk
from tkinter import messagebox

def download_mp3():
    url = WebAdress.get()
    save_folder = StorageAdress.get()
    filename = FileName.get()

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

        # پیام موفقیت
        messagebox.showinfo("موفقیت", "دانلود با موفقیت انجام شد!")

    except requests.exceptions.RequestException as e:
        messagebox.showerror("خطا", f"دانلود انجام نشد:\n{e}")


# ---------------- GUI ----------------

root = tk.Tk()
root.title("دانلود فایل")

tk.Label(root, text="آدرس وب سایت:").grid(row=0, column=0)
WebAdress = tk.Entry(root)
WebAdress.grid(row=0, column=1)

tk.Label(root, text="آدرس ذخیره سازی:").grid(row=1, column=0)
StorageAdress = tk.Entry(root)
StorageAdress.grid(row=1, column=1)

tk.Label(root, text="اسم فایل:").grid(row=2, column=0)
FileName = tk.Entry(root)
FileName.grid(row=2, column=1)

tk.Button(root, text="دانلود", command=download_mp3).grid(row=3, column=1)

root.mainloop()

