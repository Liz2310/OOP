from PIL import Image
from zip_processor import ZipProcessor

"""All we do is open each file (assuming that it is an image; 
it will unceremoniously crash if a file cannot be opened or 
isn't an image), scale it, and save it back. The ZipProcessor 
class takes care of the zipping and unzipping without any 
extra work on our part."""

class ScaleZip(ZipProcessor):
    def process_files(self):
        '''Scale each image in the directory to 640x480'''
        for filename in self.temp_directory.iterdir():
            im = Image.open(str(filename))
            scaled = im.resize((640, 480))
            scaled.save(filename)

if __name__ == "__main__":
    ScaleZip(*sys.argv[1:4]).process_zip()