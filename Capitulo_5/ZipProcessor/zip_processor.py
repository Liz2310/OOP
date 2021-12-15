"""Superclass for processing generic ZIP files.

Objects to represent the ZIP file and each individual text file come with
the Python standard library.

The pathlib library helps out with file and directory manipulation"""

import sys
import shutil
import zipfile
from pathlib import Path

class ZipProcessor:
    """The class is initialized with the .zip filename,
    and search and replace strings. We create a temporary
    directory to store the unzipped files in, so that
    the folder stays clean"""

    def __init__(self, zipname):
        self.zipname = zipname
        self.temp_directory = Path(f"unzipped-{zipname[:-4]}")

    def process_zip(self):
        """Overall manager method for each of the three steps.
        This method delegates responsibility to other objects.

        We changed the filename property to zipname to avoid
        confusion with the filename local variables inside
        the various methods.

        This new ZipProcessor class doesn't actually define a
        process_files method. If we ran it directly, it would
        raise an exception. Because it isn't meant to run
        directly (cuz it's meant to be inherited), we removed
        the main call at the bottom of the original script."""

        self.unzip_files()
        self.process_files()
        self.zip_files()

    def unzip_files(self):
        self.temp_directory.mkdir()
        with zipfile.ZipFile(self.zipname) as zip:
            zip.extractall(self.temp_directory)

    def zip_files(self):
        with zipfile.ZipFile(self.zipname, "w") as file:
            for filename in self.temp_directory.iterdir():
                file.write(filename, filename.name)
        shutil.rmtree(self.temp_directory)


"""It is now much easier for to write other classes that 
operate on files in a ZIP archive, such as a photo scaler. 
Further, if we ever want to improve or bug fix the zip 
functionality, we can do it for all subclasses at once 
by changing only the one ZipProcessor base class. 
Therefore maintenance will be much more effective."""