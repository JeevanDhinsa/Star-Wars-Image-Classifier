import splitfolders

# Input and output folders
input_folder = "star_wars_images"
output = "star_wars_images_processed"

# Splitting images in the folders into training,validation and testing with a 60/20/20 ratio
splitfolders.ratio(input_folder,output, seed = 42, ratio=(.6,.2,.2))

