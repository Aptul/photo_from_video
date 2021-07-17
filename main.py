def get_photo_from_video(video):
    import cv2
    cap = cv2.VideoCapture(video)
    total_frames = cap.get(7)


    cap.set(1, int(total_frames/2))
    ret, still = cap.read()
    cv2.imwrite(f'./frame.jpg', still)

    return 'frame.jpg'

def image_cropper(photo):
    from PIL import Image

    img = Image.open(photo)
    width, height = img.size
    #NOTA: LA PRIMA DIMENSIONE E' QUELLA DI SINISTRA, POI ALTO, DESTRA, BASSP
    img_cropped = img.crop((0.075 * width, 0, width*0.925, 0.85 * height))

    img_cropped.save(photo)

def image_resizer(photo):
    from PIL import Image

    img = Image.open(photo)
    img.thumbnail((400, 400))
    img.save(photo)


get_photo_from_video(video="https://server5.streamingaw.online/DDL/ANIME/MairimashitaIruma-kun2/MairimashitaIruma-kun2_Ep_14_SUB_ITA.mp4")
image_cropper(photo='frame.jpg')
image_resizer(photo='frame.jpg')