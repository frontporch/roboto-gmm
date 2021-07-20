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
FILE_TYPES          = ["ttf", "woff", "woff2"]
FONT_STYLE_MAPS     = {
                        "Bold": {
                            "weight": 700
                        },
                        "BoldItalic": {
                            "style": "italic",
                            "weight": 700
                        },
                        "Italic": {
                            "style": "italic"
                        },
                        "Regular": {}
                    }

print("Starting build process...")
if not os.path.exists(OUTPUT_PATH):
    os.mkdir(OUTPUT_PATH)

print(CURRENT_DIR)


def generate_fonts():
    print("FontForge version: " + ff.version())
    print("Python version: " + platform.python_version())
    for name in FONT_NAME_LIST:
        font_name     = FONT_FAMILY_NAME + "-" + name
        print(font_name)
        project_file  = CURRENT_DIR + "/src/" + font_name + ".sfd"
        print(project_file)
        for ext in FILE_TYPES:
            font_file     = OUTPUT_PATH + font_name + "." + ext
            print(font_file)
            _generate_font(project_file, font_file, font_name)


def _generate_font(project_file, font_file, font_name):
    font = ff.open(project_file)
    font.generate(font_file)
    font.close()
    print(datetime.datetime.now().strftime('[%Y-%m-%d %H:%M:%S.%f]')
          + " '" + font_name + "' " + "generated.")


def generate_css():
    print("Generating CSS File")
    declaration = '''@font-face {{
  font-family: Roboto;
  font-style: {style};
  font-display: swap;
  font-weight: {weight};
  src: local("Roboto-GMM"), url("./{font_name}.woff2") format("woff2"),
    url("./{font_name}.woff") format("woff"),
    url("./{font_name}.ttf") format("truetype");
}}
'''
    with open(OUTPUT_PATH + "roboto-gmm.css", "w+") as f:
        for name in FONT_NAME_LIST:
            font_name = FONT_FAMILY_NAME + "-" + name
            style_map = FONT_STYLE_MAPS[name]
            style = style_map.get("style", "normal")
            weight = style_map.get("weight", 400)
            print("writing @font-face for " + font_name)
            f.write(declaration.format(style=style,
                    weight=weight, font_name=font_name))


def main():
    generate_fonts()
    generate_css()


if __name__ == "__main__":
    main()
