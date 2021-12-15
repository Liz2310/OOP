"""A media player might need to load an AudioFile object and then play it.

   However, the process of decompressing and extracting an audio file is
   different for different types of files.

   It is possible to use inheritance with polymorphism to simplify the design.
   Each type of file can be represented by a different subclass of AudioFile.

   Each of these would have a play() method that would be implemented differently
   for each file to ensure that the correct extraction procedure is followed.

   The media player object would never need to know which subclass of AudioFile it is
   referring to; it just calls play() and polymorphically lets the object take care
   of the actual details of playing."""
import abc
class MediaLoader(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def play(self):
        pass

    @property
    @abc.abstractmethod
    def ext(self):
        pass

    @classmethod
    def __subclasshook__(cls, C):
        if cls is MediaLoader:
            attrs = set(dir(C))
            if set(cls.__abstractmethods__) <= attrs:
                return True
        return NotImplemented

class AudioFile:
    """The __init__ method in the parent class is able to access the ext class variable from different subclasses.

       The fact that the AudioFile parent class doesn't actually store a reference to the ext variable doesn't stop
       it from being able to access it on the subclass.

       Plus, each subclass of AudioFile implements play() in a different way.
       The details of decompressing the audio file are encapsulated."""

    def __init__(self, filename):
        if not filename.endswith(self.ext):
            raise Exception("Invalid file format")
        self.filename = filename


class MP3File(AudioFile):
    ext = "mp3"

    def play(self):
        print(f"playing {self.filename} as mp3")


class WavFile(AudioFile):
    ext = "wav"

    def play(self):
        print(f"playing {self.filename} as mp3")

class OggFile(AudioFile):
    ext = "ogg"

    def play(self):
        print(f"playing {self.filename} as mp3")

class FlacFile:

    def __init__(self, filename):
        if not filename.endswith(".flac"):
            raise Exception("Invalid file format")
        self.filename = filename

    def play(self):
        print(f"playing {self.filename} as flac")

class Wav(MediaLoader):
    """Since the Wav class fails to implement the abstract attributes in the
       MediaLooader ABC, it is not possible to instantiate that class. """
    pass

class Ogg(MediaLoader):
    """Supplies both attributes, so it instantiates cleanly."""
    ext = " .ogg"
    def play(self):
        pass



# flac_file = FlacFile("Lmao.flac")
# print(flac_file.play())

# mp3_object = MP3File("lol.mp420")
# mp3_object2 = MP3File("lmao.mp3")
#
# print(mp3_object.play())
# print(mp3_object2.play())

# x = Wav() #TypeError: Can't instantiate abstract class Wav with abstract methods ext, play
