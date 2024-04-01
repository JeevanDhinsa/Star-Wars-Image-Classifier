import splitfolders

input_folder = "star_wars_images"
output = "star_wars_images_processed"

splitfolders.ratio(input_folder,output, seed = 42, ratio=(.6,.2,.2))

