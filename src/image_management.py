from PIL import Image

if __name__ == '__main__':
    mac = Image.open('박지옷.png')
    #mac.size
    #mac.filename
    #mac.format_description

    #   Cropping images
    #mac.show()
    new = Image.open('박지3.jpg')
    print(mac.size)
    x = 228
    y = 10
    w = 428
    h = 230
    new = new.crop((x, y, w, h))
    computer = mac.crop((x,y,w,h))
    mac.paste(im=computer, box=(500,0))
    #mac.show()
    #   mac.resize(()) can resize the image

    #   Color transparency
    red = Image.open('red_color.jpg')
    blue = Image.open('blue_color.png')
    rgba = blue.convert("RGBA")
    datas = rgba.getdata()
    #   put alpha decides the transparency
    blue.putalpha(255)
    red.putalpha(128)
    #red.show()
    blue.paste(im=red, box=(0, 0), mask=red)
    blue.show()
    #   it should return purple


