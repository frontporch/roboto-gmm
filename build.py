# Build script for the Roboto Font using Fontforge
# If changes are needed to the font, open the font .sfd in FontForge and make them there
# This script currently is only used to generate the font

print("Importing modules...")
import os
import datetime
import platform
import fontforge as ff

print("Setting variables...")
MAIN_DIR            = os.path.dirname(os.getcwd())
CURRENT_DIR         = os.getcwd()
OUTPUT_PATH         = CURRENT_DIR + "/published/"
SCRIPTS_PATH        = CURRENT_DIR
FONT_NAME_LIST      = ["Bold", "BoldItalic", "Italic", "Regular"]
FONT_FAMILY_NAME    = "Roboto-GMM"

print("Starting build process...")
if not os.path.exists(OUTPUT_PATH):
    os.mkdir(OUTPUT_PATH)

print(CURRENT_DIR)

def generate_fonts() :
    print("FontForge version: " + ff.version())
    print("Python version: "+ platform.python_version())
    for name in FONT_NAME_LIST:
        font_name     = FONT_FAMILY_NAME + "-" + name
        print(font_name)
        project_file  = CURRENT_DIR + "/src/" + font_name + ".sfd"
        print(project_file)
        font_file     = OUTPUT_PATH + font_name + ".ttf"
        print(font_file)
        _generate_font(project_file, font_file, font_name)

def _generate_font(project_file, font_file, font_name):
    font = ff.open(project_file)
    font.generate(font_file)
    font.close()
    print(datetime.datetime.now().strftime('[%Y-%m-%d %H:%M:%S.%f]')
          + " '" + font_name + "' " + "generated.")

def main():
    generate_fonts()

if __name__ == "__main__":
    main()