from PIL import Image

if __name__ == '__main__':
    image = Image.open("word_matrix.png")
    #   1015, 559
    keys = Image.open("word_key.png")
    #   505 251
    keys = keys.resize((1015, 559))
    keys.putalpha(200)
    image.paste(keys, (0,0), keys)
    image.show()