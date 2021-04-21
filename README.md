# Roboto-GMM

This is a branch of the source repository for Roboto: Google’s signature family
of fonts, the default font on Android and Chrome OS, and the
recommended font for Google’s visual language, Material Design.

## Build Process using FontForge

Fontforge is an open source font editor which also has support for Python scripts.

Currently, this script will only generate the fonts but can be expanded later.

Here is a [resource link](https://fontforge.org/docs/scripting/python.html) with details on the Python modules Fontforge supports.

## Windows Requirements

1. Make sure to have Python 2.7 installed on your system.
2. Install [Fontforge](https://fontforge.org/en-US/downloads/) project on your system.
3. Make sure there is an Environment Variable in the `Path` for the folder where the  `ffpython.exe` file is stored.

### To Generate Fonts

```cmd
ffpython.exe .\build.py
```

The font files will be generated in the `build\published` folder.

### Adding Glyphs to Project in FontForge

1. Open the `Roboto-GMM-Regular.sfd` in FontForge.
2. On the File Menu use `View` -> `Go to`
   This will bring up a dialog box to enter the Unicode name.  example `uni2220`
   Click `Ok` and it will highlight the empty glyph location.
3. Double-Click the empty glyph to open the `Glyph Dialog`
4. Inside the Glyph Dialog Box:
   1. Choose `File` --> `Import`
   2. Set the type of file you wish to import and click `Import`
   3. Make any adjustment needed
   4. Click `File` --> `Save`
5. Make sure to `Save` or `Save All` from the main dialog to update the `.sfd` file
6. Please note that saving these files may cause the builds to break if there is a version mismatch
7. If this happens, open each .sdf file in `notepadd++` and change the version in the top line from `3.2` to `3.0`

#### Additional Note:

When creating the glyphs make sure to keep in mind the `Ascent: 1638` and the `Decent: 410` with an overall `Em Size: 2048`.