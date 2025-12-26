def download_mp3():
    urls = WebAdress.get().splitlines()   # multiple URLs
    save_folder = StorageAdress.get()

    os.makedirs(save_folder, exist_ok=True)

    for url in urls:
        url = url.strip()
        if not url:
            continue

        filename = url.split("/")[-1]     # auto filename from URL

        if not filename.endswith(".mp3"):
            filename += ".mp3"

        file_path = os.path.join(save_folder, filename)

        try:
            response = requests.get(url, stream=True)
            response.raise_for_status()

            with open(file_path, "wb") as file:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        file.write(chunk)

        except requests.exceptions.RequestException as e:
            messagebox.showerror("خطا", f"دانلود انجام نشد:\n{e}")
            return

    messagebox.showinfo("موفقیت", "تمام فایل‌ها با موفقیت دانلود شدند!")
