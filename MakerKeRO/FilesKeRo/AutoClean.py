import os
import glob
import asyncio
import time
from pyrogram import Client, filters

#تم برمجه الكود بواسطه المطور كيرو @Y_J_J_J
#انت يكسمك خد الملف بس قول مين عمله
last_cleanup_time = 0
async def delete_temp_files():
    global last_cleanup_time
    while True:
        await asyncio.sleep(100) 
        current_time = time.time()
        if current_time - last_cleanup_time >= 100:
#//=================================EDITED BY Https://t.me/Y_J_J_J ========================================//
            cache = os.path.realpath("/")
            down_dir = os.listdir(cache)
            pth = os.path.realpath(".")
    
        if down_dir:
            for file in down_dir:
                os.remove(os.path.join(cache, file))

#//=================================EDITED BY Https://t.me/Y_J_J_J ========================================//
            downloads = os.path.realpath("downloads")
            down_dir = os.listdir(downloads)
            pth = os.path.realpath(".")
    
        if down_dir:
            for file in down_dir:
                os.remove(os.path.join(downloads, file))
#//=================================EDITED BY Https://t.me/Y_J_J_J ========================================//            
            files_to_delete = glob.glob("*.webm") + glob.glob("*.jpg") + glob.glob("*.png")
            for file_path in files_to_delete:
                os.remove(file_path)

            last_cleanup_time = current_time
            print("تم حذف الملفات بنجاح .Dev @Y_J_J_J")


asyncio.ensure_future(delete_temp_files())

