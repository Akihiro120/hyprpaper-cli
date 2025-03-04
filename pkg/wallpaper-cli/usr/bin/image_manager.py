import json;
import os;
import subprocess;
import time;
import threading;

class ImageManager:
    IMAGE_POOL_DIRECTORY = "~/.config/wallpaper-cli/config.json"
    image_pool = [];
    current_index = 0;
    cycle = False;
    cycle_enable = False;

    def __init__(self):
        # load the image pool
        self.load_image_pool();

    """
    Toggle cycle
    """
    def toggle_cycle(self):
        # toggle and save
        self.cycle = not self.cycle;
        self.save_image_pool();

    def enable_cycle(self):
        # toggle
        self.cycle_enable = not self.cycle_enable;
        self.save_image_pool();

    """
    Load
    """
    def load(self):
        # load the swww daemon
        subprocess.run([
            "swww-daemon"
        ], check=True);
        self.set_picture(self.current_index);

    """
    Set the current picture by index
    """
    def set_picture(self, index):
        # set the index
        if index-1 < len(self.image_pool):
            self.current_index = index-1;
            path = os.path.expanduser(self.image_pool[self.current_index]);

            # load the image using swww
            subprocess.run([
                "swww", "img", path,
                "--transition-type", "fade",
                "--transition-duration", "1.0"
            ]); 
            self.save_image_pool();
            return;
        
        print("Index out of bounds.");

    """
    Add a new picture to the image pool.
    """
    def add_picture(self, image_path):
        # add and save the image pool
        # first check if the image is valid
        if os.path.isfile(image_path):
            if image_path not in self.image_pool:
                self.image_pool.append(image_path);
                self.save_image_pool();
                return;
        else:
            print(f"{image_path} does not exist at directory");
            return;
        print(f"{image_path} already exists.");

    """
    Remove a picture from the image pool by index.
    """
    def remove_picture(self, index):
        # remove the picture from the image_pool 
        if index-1 < len(self.image_pool):
            del self.image_pool[index-1];
            self.save_image_pool();
            return;

        print("Picture index doesn't exist.");

    """
    Save the image pool to directory
    """
    def save_image_pool(self):
        # save the json file
        path = os.path.expanduser(self.IMAGE_POOL_DIRECTORY);
        with open(path, "w") as file:
            # make the json
            data = {"paths": self.image_pool, "index": self.current_index, "cycle": self.cycle, "cycle-enable": self.cycle_enable};
            json.dump(data, file, indent=4);

    """
    Load the image pool from directory
    """
    def load_image_pool(self):
        # load the json
        path = os.path.expanduser(self.IMAGE_POOL_DIRECTORY);
        try: 
            with open(path, "r") as file:
                info = json.load(file);
                self.image_pool = info["paths"];
                self.current_index = info["index"];
                self.cycle = info["cycle"];
                self.cycle_enable = info["cycle-enable"]

        # the file doesnt exist
        except FileNotFoundError:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w") as file:
                json.dump({"paths": [], "index": 0, "cycle": False, "cycle-enable": False}, file, indent=4);
            
            # load an empty image_pool
            self.image_pool = [];
            self.current_index = 0;
        
    """
    Load the next image in the pool
    """
    def next_image(self):
        self.current_index = (self.current_index + 1) % len(self.image_pool)-1;
        self.set_picture(self.current_index);

    """
    Load the prev image in the pool
    """
    def prev_image(self):
        self.current_index = (self.current_index - 1) % len(self.image_pool)-1;
        self.set_picture(self.current_index);


    """
    Get the image pool
    """
    def get_image_pool(self):
        return self.image_pool;
