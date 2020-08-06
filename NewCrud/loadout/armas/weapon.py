from pydub import AudioSegment
from pydub.playback import play

class Weapon():
    def __init__(self, name, accuracy, damage, muzzle, barrel, laser, optic, ammunition, reload_speed):
        self.name = name
        self.accuracy = accuracy
        self.damage = damage
        self.muzzle = muzzle
        self.barrel = barrel
        self.laser = laser
        self.optic = optic
        self.ammunition = ammunition
        self.reload_speed = reload_speed

    def fire(self):
        pass

    def reload(self):
        pass

    def make_noise(self, audio_file_path):
        audio = AudioSegment.from_mp3(audio_file_path)
        play(audio)

    def __str__(self):
        return self.name