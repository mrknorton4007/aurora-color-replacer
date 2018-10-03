# Aurora Color Replacer Script
Considering .xui files are basically .xml files, this script helps you replace
colors of Aurora_Skin files. Tested on Aurora 0.5b and 0.6b but should work
on future versions too.

### Requirements
- Python 2.7+ or Python 3+
- Aurora original skin files

Aurora skin files should be in .xui format. Use the XDK to convert them
from .xur to .xui (and convert back to .xur once you're done).

### How-to
Download this project on your PC, then copy the original skin files you want
to edit (remember, in .xui format) inside the `_input` folder.

For sure you will need the `Aurora_Skin.xui` file. Other files like
`Aurora_Loading.xui` (for example) depends on what you want to achieve.

Once you're ready, run the Python script using the command

    py.exe ./aurora-color-replacer.py THEME_NAME

where `THEME_NAME` is the name of the file that contains the theme you want
to use. You can see the available themes under the `themes` folder.

Example:

    py.exe ./aurora-color-replacer.py MetroColorRed

You will then find the color-edited files inside the `_output` folder. Remember
to convert them back to .xur format before building your final .xzp skin file.

### Custom themes
Inside this repository you will find some ready-to-use themes created by me
during these years. Check the relative threads on the RealModScene forum here:
- [Metro Colors](https://www.realmodscene.com/index.php?/topic/4656-skin-aurora-metro-colors) 
- [SteamOS](https://www.realmodscene.com/index.php?/topic/4701-skin-aurora-steamos/) 

You can obviously create your own custom themes by simply adding a new .py file
inside the `themes` folder. Use the other themes as example for the file structure.

Theme files consist in a single variable called `theme_rules` containing
a Python dictionary where elements are in the following format:

    ('<PROPRIETY_NAME>', 'ORIGINAL_ARGB_COLOR'): 'NEW_ARGB_COLOR',

Example:

    ('<FillColor>', '0xff33e5a8'): '0xffcc1a57',

Colors are in hexadecimal ARGB (0xAARRGGBB) so `0xffcc1a57` in the example
is `#cc1a57` with 100% opacity.

If no-matching rules are found for an element, in your theme it will keep
the original color. Themes files should only contains colors you want to replace.

### Image files
As a final note, keep in mind that this script does a lot of work for you
but not all.

Some "scenes" may still need your revision after you applied this script.
There are also some .png files that compose the final skin and most likely
you will need to edit them.
