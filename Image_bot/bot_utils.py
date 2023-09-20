from PIL import ImageFilter, Image


async def make_img_filter(img, filter_name):
    pic = Image.open(img)

    if filter_name == "BLUR":
        new_pic = pic.filter(ImageFilter.BLUR)
        new_pic.save(img)
    elif filter_name == "CONTOUR":
        new_pic = pic.filter(ImageFilter.CONTOUR)
        new_pic.save(img)
    elif filter_name == "DETAIL":
        new_pic = pic.filter(ImageFilter.DETAIL)
        new_pic.save(img)
    elif filter_name == "EDGE ENHANCE":
        new_pic = pic.filter(ImageFilter.EDGE_ENHANCE)
        new_pic.save(img)
    elif filter_name == "EDGE ENHANCE MORE":
        new_pic = pic.filter(ImageFilter.EDGE_ENHANCE_MORE)
        new_pic.save(img)
    elif filter_name == "EMBOSS":
        new_pic = pic.filter(ImageFilter.EMBOSS)
        new_pic.save(img)
    elif filter_name == "FIND EDGES":
        new_pic = pic.filter(ImageFilter.FIND_EDGES)
        new_pic.save(img)
    elif filter_name == "SHARPEN":
        new_pic = pic.filter(ImageFilter.SHARPEN)
        new_pic.save(img)
    elif filter_name == "SMOOTH":
        new_pic = pic.filter(ImageFilter.SMOOTH)
        new_pic.save(img)
    elif filter_name == "SMOOTH MORE":
        new_pic = pic.filter(ImageFilter.SMOOTH_MORE)
        new_pic.save(img)

    return img