from zip_processor import ZipProcessor

"""This inherits its ZIP processing abilities from 
the parent class. We first import the base class and 
make ZipReplace extend that class. Then, we use super() 
to initialize the parent class. 

The find_replace method is still here, but we renamed it 
process_files so the parent class can call it from 
its management interface."""

class ZipReplace(ZipProcessor):
    """Program that does a find-and-replace action for
    text files stored in a compressed ZIP file"""

    def __init__(self, filename, search_string, replace_string):
        super().__init__(filename) #sends the filename so that the superclass can save it as zip name and make the temp directory
        self.search_string = search_string
        self.replace_string = replace_string

    def process_files(self):
        """Perform a search and replace on all files in the
        temporary directory"""

        for filename in self.temp_directory.iterdir():
            with filename.open() as file:
                contents = file.read()
            contents = contents.replace(self.search_string,self.replace_string)
            with filename.open("w") as file:
                file.write(contents)