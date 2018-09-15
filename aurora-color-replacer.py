#!/usr/bin/env python
import os
import sys


class AuroraColorReplacer:

    def __init__(self, theme_name):
        # current dir
        self.base_path = os.path.dirname(os.path.abspath(__file__))
        # name of the folder containing the original files
        self.source_folder_name = "_input"
        # name of the folder that will contain the edited files
        self.output_folder_name = "_output"
        # import color replacing rules
        self.theme_rules = self._import_theme(theme_name)

    def _import_theme(self, theme_name):
        # check and import py module with the replace rules
        pass

    def _get_replaced_line(self, xml_tag):
        # given a xml line, find a matching rule
        pass

    def recolor_line(self, xml_tag):
        # given a xml line, writes the recolored one
        pass

    def recolor_file(self, filename):
        # given a xui file, writes the recolored one
        pass

    def recolor_folder(self):
        # find all source files and recolor them
        source_folder = os.path.join(self.base_path, self.source_folder_name)

        for entry in os.listdir(source_folder):

            # silently ignore gitkeep file
            if entry == '.gitkeep':
                continue

            # not a xui file
            if not entry.endswith(".xui"):
                print("{filename} is not a xui file. Skipped.".format(filename=entry))
                continue

            target_file = os.path.join(source_folder, entry)
            self.recolor_file(target_file)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("Usage: ./SCRIPT_NAME.py THEME_NAME")

    selected_theme_name = sys.argv[1]
    acr = AuroraColorReplacer(theme_name=selected_theme_name)
    acr.recolor_folder()
    sys.exit()
