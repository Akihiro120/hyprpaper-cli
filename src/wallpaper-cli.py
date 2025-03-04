#!/usr/bin/env python3
from parser import Parser;
from image_manager import ImageManager;

def main():
    # create a parser instance
    parser = Parser();
    parser.parse_arguments();

    # get the parser arguments
    args = parser.get_args();

    # create a image manager instance
    image_manager = ImageManager();

    # parse the arguments
    if args.add:
        # add a picture
        image_manager.add_picture(args.add);
    if args.display:
        # display images
        images = image_manager.get_image_pool();
        for i, image in enumerate(images):
            print(f"{i + 1}: {image}")
    if args.remove:
        # remove image
        image_manager.remove_picture(args.remove);
    if args.set:
        # set image
        image_manager.set_picture(args.set);
    if args.load:
        # load an instance
        image_manager.load();
    if args.next:
        # next
        image_manager.next_image();
    if args.prev:
        # prev
        image_manager.prev_image();
    if args.togglecycle:
        # cycle
        image_manager.toggle_cycle();
    if args.enablecycle:
        image_manager.enable_cycle();


# entry point
if __name__ == "__main__":
    main();
