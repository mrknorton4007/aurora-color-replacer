#!/usr/bin/env python
import os
import sys


class AuroraColorReplacer:

    def __init__(self, theme_name):
        # current dir
        self.base_path = os.getcwd()
        # name of the folder containing the original files
        self.source_folder_name = "_input"
        # name of the folder that will contain the edited files
        self.output_folder_name = "_output"
        # import color replacing rules
        self.theme_rules = self._import_theme(theme_name)
        # check folder structure
        self._integrity_folder_check()

    def _import_theme(self, theme_name):
        # check and import py module with the replace rules
        pass

    def _integrity_folder_check(self):
        # ensure that input/output folders exists
        source_folder = os.path.join(self.base_path, self.source_folder_name)
        output_folder = os.path.join(self.base_path, self.output_folder_name)

        for directory in [source_folder, output_folder]:
            if not os.path.exists(directory):
                # let the script raise an OSError and exit in case
                # user doesnt have the correct permissions.
                os.mkdir(directory)
        return True

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
