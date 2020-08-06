from pydub import AudioSegment
from pydub.playback import play


class Equipment:
    def __init__(self, name, design, description, area_of_effect):
        self.name = name

        # Skin do equipamento
        self.design = design
        # Descrição do que o equipamento faz
        self.description = description
        # Area de efeito e atuação dentro do mapa
        self.area_of_effect = area_of_effect

    # Ativação do equipamento
    def activate(self):
        pass
    
    # Som do equipamento
    def make_noise(self, audio_file_path):
        audio = AudioSegment.from_mp3(audio_file_path)
        play(audio)

    def __str__(self):
        return self.name