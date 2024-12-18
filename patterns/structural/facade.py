class AudioConverter:
    def convert_file(self, file, format):
        return "converted_file." + format

class AudioMetadata:
    def extract_metadata(self, file):
        return {"title": "song", "artist": "artist"}

class AudioPlayer:
    def play_file(self, file):
        print(f"Playing {file}")

class AudioFacade:
    def __init__(self):
        self.converter = AudioConverter()
        self.metadata = AudioMetadata()
        self.player = AudioPlayer()

    def play_audio(self, file, format):
        converted = self.converter.convert_file(file, format)
        metadata = self.metadata.extract_metadata(converted)
        self.player.play_file(converted)
        return metadata

facade = AudioFacade()
metadata = facade.play_audio("song.mp3", "wav")
print(metadata)