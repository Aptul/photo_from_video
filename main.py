def get_photo_from_video(video, directory, photo_name):
    import cv2
    import os
    cap = cv2.VideoCapture(video)
    total_frames = cap.get(7)


    cap.set(1, int(total_frames/2))
    ret, still = cap.read()
    current_dir = os.getcwd()
    if not os.path.isdir(os.getcwd() + f"/{directory}"):
        os.mkdir(os.getcwd() + f"/{directory}")
    if not os.path.isfile(os.getcwd() + f"/{directory}/{photo_name}"):
        os.chdir(os.getcwd() + "/" + directory)
        cv2.imwrite(f"{photo_name}", still)
        print("non presente")
    else:
        print("presente")
    os.chdir(current_dir)


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

def do_job(video, directory, photo_name):
    get_photo_from_video(video=video, directory=directory, photo_name=photo_name)
    image_cropper(photo=f'{directory}/{photo_name}')
    image_resizer(photo=f'{directory}/{photo_name}')
if __name__ == '__main__':
    import pymongo

    myclient = pymongo.MongoClient('mongodb://admin:password@192.168.1.222:27017')
    mydb = myclient["animes"]
    mytb = mydb["anime_tb"]

    for anime in mytb.find():
        for episodio in anime["episodi"]:
            if "AnimeWorld Server" in episodio.keys():
                try:
                    video = episodio["AnimeWorld Server"]
                    directory = anime["_id"].replace("/", ",|").replace(".", ",.")
                    photo_name = f'{episodio["numero"]}.jpg'

                    do_job(video=video, directory=directory, photo_name=photo_name)

                except Exception as e:
                    print("AnimeWorld Server link non funzionante")
                    print(anime)
                    print(episodio)
                    print(e)
            else:
                print("AnimeWorld Server non presente")
