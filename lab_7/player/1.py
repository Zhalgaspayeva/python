import pygame as pg
import os

pg.init()

# Класс отвечает за звуковой файл и соответствующее изображения 
class SOUND:
    # Инициализирую
    def __init__(self, path_to_sound, path_to_photo):
        self.sound = pg.mixer.Sound('music/' + path_to_sound)
        self.photo = pg.image.load('assets/sound_images/' + path_to_photo)
        self.is_playing = True
    # Установка изображений на экране
    def placePhoto(self, screen):
        self.photo = pg.transform.scale(self.photo, (300, 300))
        screen.blit(self.photo, (250, 98))
path_to_sound = os.listdir('music/') # Путь к звуковым файлам (список музыки)
path_to_photo = os.listdir('assets/sound_images/') # Путь к изображениям (список изображений)
path_to_sound.sort()
path_to_photo.sort()

path_to_photo.pop(path_to_photo.index('.DS_Store'))
path_to_sound.pop(path_to_sound.index('.DS_Store'))
sounds = []

# Создание экземпляров класса Sound
for i in zip(path_to_photo, path_to_sound):
    print(i)
    print(i[0])
    sound = SOUND(path_to_photo=i[0], path_to_sound=i[1]) # Передачи соответствующих путей к файлам 
    sounds.append(sound) # Связала песни с их изображениями

screen = pg.display.set_mode((800, 600))

# Задний фон
BACKGROUND = pg.image.load('assets/bg.png').convert()
screen.blit(BACKGROUND, (0, 0))
sound_index = 0
sounds[0].sound.play()
sounds[0].placePhoto(screen) 

while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
        # Плей и пауза, предыдущая песня, следующая песня
        if pg.mouse.get_pressed()[0]:
            print(pg.mouse.get_pos())
            if 441 <= pg.mouse.get_pos()[1] <= 490 and 376 <= pg.mouse.get_pos()[0] <= 425:
                if sounds[sound_index].is_playing:
                    pg.mixer.pause()
                    sounds[sound_index].is_playing = False
                else:
                    pg.mixer.unpause()
                    sounds[sound_index].is_playing = True
            elif 322 <= pg.mouse.get_pos()[0] <= 363 and 445 <= pg.mouse.get_pos()[1] <= 486:
                pg.mixer.stop()
                sound_index -= 1
                sounds[sound_index + 1].is_playing = True
                if(sound_index == -1):
                    sound_index = len(sounds) - 1
                sounds[sound_index].sound.play()
                sounds[sound_index].placePhoto(screen)
            elif 438 <= pg.mouse.get_pos()[0] <= 479 and 446 <= pg.mouse.get_pos()[1] <= 487:
                pg.mixer.stop()
                sound_index += 1
                sounds[sound_index - 1].is_playing = True
                if(sound_index == len(sounds)):
                    sound_index = -1
                sounds[sound_index].sound.play()
                sounds[sound_index].placePhoto(screen)
    pg.display.flip()