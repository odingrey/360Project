import glob
import os
import re

def find_unhidden(path):
	return glob.glob(os.path.join(path, '*'))

def find_images(path):
	contents = os.listdir(path)
	contents = [i for i in contents if re.search('.*(.jpg|.png|.JPG|.PNG)', i)]
	return contents

def convert_brightness(brightness):
	return ((brightness + 100)/100)   # converts brightness level from caman to PIL

