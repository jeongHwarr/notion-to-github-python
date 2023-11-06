import re
import zipfile
import os
import glob
import time
import shutil

posts_folder_path='_posts'# set post_folder path
images_folder_path=os.path.join('assets','images') # set image folder path

exported_zip_reg="*.zip"

zip_files = glob.glob(os.path.join(posts_folder_path, "*.zip"), recursive=False)


def imgNameTransform(text):
    text = re.sub(' ', '_', text)
    text = re.sub('%20', '_', text)
    return text.lower()

def cleanText(text):
    text = re.sub('[=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', '', text)
    text = re.sub(' ', '_', text)
    text = re.sub('-', '_', text)
    return text.lower()


for file in zip_files:
    zipfile.ZipFile(file).extractall()

    zf = zipfile.ZipFile(file, 'r')
    content_files = zf.namelist()

    md_file = [i for i in content_files if ".md" in i][0]

    # open md_file
    with open(md_file, "r", encoding="utf-8") as txt:
        lines = txt.read().splitlines()

        # -----------------------[Meta Data]-------------------
        # The first head data is recognized as a title.
        for index, line in enumerate(lines):
            if "# " in line:
                meta_title = line.replace("# ",'')
                clean_title = cleanText(meta_title)
                del lines[index]
                break

        meta_date = time.strftime('%Y-%m-%d %H:%M:%S +0009')
        file_name = time.strftime('%Y-%m-%d')+"-%s"%clean_title
        file_name = input("Enter a file name [Default:%s]\nIf you press enter, the default value is set as the filename.\n" %file_name) or file_name
        
        meta_title = input("Enter a Title [Default:%s]\nIf you press enter, the default value is set as the title.\n" %meta_title) or meta_title
        print("Title: %s"%meta_title)  
        meta_subtitle = input("Enter a subtitle: ")
        meta_categories = input("Enter categories: ")
        meta_tags = re.sub(' *, *', ',', input("Enter tags (ex: dog,cat): ")).split(",")
        meta_date = time.strftime('%Y-%m-%d %H:%M:%S') +" +0900"

        # put meta data
        lines.insert(0, "---")
        lines.insert(1, "title: \"%s\""%meta_title)
        lines.insert(2, "subtitle: %s"%meta_subtitle)
        lines.insert(3, "categories: %s"%meta_categories)
        lines.insert(4, "date: %s"%meta_date)
        lines.insert(5, "tags:")
        for index, tag in enumerate(meta_tags):
            lines.insert(6+index, "  - %s"%tag)
        lines.insert(7+index, "---")



        # -----------------------[Image]---------------------------
        images = [i for i in content_files if i != md_file]
        if len(images):
            ori_img_dir = os.path.split(images[0])[0]

            # change names of image files
            for image in images:
                new_img_name = imgNameTransform(os.path.basename(image))
                os.rename(image, os.path.join(ori_img_dir,new_img_name))

            # move images
            new_image_dir = os.path.join(images_folder_path, file_name)
            shutil.move(ori_img_dir, new_image_dir)


            # edit a md file (edit image path)
            for idx, line in enumerate(lines):
                find_img_content = re.search('!\[(.+)]\((.+)/(.+?)\)',line)
                if find_img_content:
                    img_path = find_img_content.group(2)
                    img_name = find_img_content.group(3)
                    line = line.replace(img_path, "/"+new_image_dir.replace(os.sep,"/"))
                    lines[idx] = line.replace(img_name, imgNameTransform(img_name))

    os.remove(md_file)
    zf.close()
    with open(os.path.join(posts_folder_path,file_name+".md"),"w", encoding="utf-8") as f:
        for line in lines:
            f.write("%s\n" % line)


    while(True):
        is_delete = input("\nComplete. Do you want to delete the compressed file?\n(%s)\nEnter y or n: "%file).lower()
        if is_delete=='y':
            os.remove(file)
            break
        elif is_delete=='n':
            break

    print("Completed successfully.")

