import argparse;

VERSION = 1.0;
class Parser:
    parser: argparse.ArgumentParser;

    """
    create the parsing arguments
    """
    def parse_arguments(self):
        self.parser = argparse.ArgumentParser(description="A CLI tool for SWWW for wallpapers");
        # create the parser
        self.parse_version_argument();
        self.parse_add_argument();
        self.parse_remove_argument();
        self.parse_get_images_arguments();
        self.parse_load();
        self.parse_set();
        self.parse_nextprev();
        self.parse_cycle();

    """
    parse for cycling
    """
    def parse_cycle(self):
        # parse next
        self.parser.add_argument(
            "--togglecycle",
            action="store_true",
            help="Toggle wallpaper cycling"
        );
        # parse next
        self.parser.add_argument(
            "--enablecycle",
            action="store_true",
            help="Enable wallpaper cycling feature"
        );

    """
    parse for next and prev
    """
    def parse_nextprev(self):
        # parse next
        self.parser.add_argument(
            "--next",
            action="store_true",
            help="Loads the next image"
        );
        # parse prev
        self.parser.add_argument(
            "--prev",
            action="store_true",
            help="Loads the previous image"
        );

    """
    parse setting a wallpaper based on index
    """
    def parse_set(self):
        self.parser.add_argument(
            "--set",
            type=int,
            help="Set a picture from the image pool by index"
        );

    """
    parse loading
    """
    def parse_load(self):
        # parse loading
        self.parser.add_argument(
            "--load",
            action="store_true",
            help="Load an instance of SWWW, and prepare"
        );

    """
    parse for getting the version
    """
    def parse_version_argument(self): 
        # parse get version 
        self.parser.add_argument(
            "--version", 
            action="version", 
            version="Wallpaper-cli version: " + str(VERSION), 
            help="Get the current version of Wallpaper-cli"
        );
    
    """
    parse for adding an image
    """
    def parse_add_argument(self):
        # parse add file
        self.parser.add_argument(
            "--add",
            type=str,
            help="Add a new picture to the image pool"
        );

    """
    parse for removing image
    """
    def parse_remove_argument(self):
        # parse remove file
        self.parser.add_argument(
            "--remove",
            type=int,
            help="Remove a picture from the image pool by index"
        );

    """
    parse get images
    """
    def parse_get_images_arguments(self):
        self.parser.add_argument(
            "--display",
            action="store_true",
            help="display images in the pool"
        );

    """
    return the parser arguments
    """
    def get_args(self):
        # parse the arguments
        args = self.parser.parse_args();
        return args;
