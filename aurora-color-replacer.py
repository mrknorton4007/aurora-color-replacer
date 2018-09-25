#!/usr/bin/env python
import os, sys
import importlib

# from themes import MetroColorBlue, MetroColorRed
# from themes import SteamOS


class AuroraColorReplacer:

    def __init__(self, theme_name):
        # current dir
        base_path = os.getcwd()
        # name of the folders containing original and edited files
        source_folder_name = "_input"
        output_folder_name = "_output"
        # their real full paths
        self.source_folder = os.path.join(base_path, source_folder_name)
        self.output_folder = os.path.join(base_path, output_folder_name)
        # import color replacing rules
        self.theme_rules = self._import_theme(theme_name)
        # check folder structure
        self._integrity_folder_check()

    def _import_theme(self, theme_name):
        # check and import py module with the replace rules

        try:
            theme_module = "themes." + theme_name
            selected_theme = importlib.import_module(theme_module)
        except ImportError as ex:
            sys.exit(ex)

        return selected_theme.theme_rules

    def _integrity_folder_check(self):
        # ensure that input/output folders exists

        for directory in [self.source_folder, self.output_folder]:
            if not os.path.exists(directory):
                # let the script raise an OSError and exit in case
                # user doesnt have the correct permissions.
                os.mkdir(directory)
        return True

    def _get_recolored_line(self, xml_tag):
        # given a xml line, find a matching rule
        # or return the original if rule not found

        for rule, value in self.theme_rules.items():
            if xml_tag.startswith(rule[0]+rule[1]):
                return xml_tag.replace(rule[1], value)

        return xml_tag

    def recolor_file(self, filename):
        # given a xui file, writes the recolored one
        source_file = os.path.join(self.source_folder, filename)
        output_file = os.path.join(self.output_folder, filename)

        source_stream = open(source_file, "r")
        output_stream = open(output_file, "w")

        line_replaced = 0
        for line in source_stream:
            new_line = self._get_recolored_line(line)
            output_stream.write(new_line)
            if line != new_line:
                print("Replaced %s with %s." % (line, new_line))
                line_replaced += 1

        source_stream.close()
        output_stream.close()

        print("Replaced %s colors in %s file." % (line_replaced, filename))
        return True

    def recolor_folder(self):
        # find all source files and recolor them

        for entry in os.listdir(self.source_folder):

            # silently ignore gitkeep file
            if entry == '.gitkeep':
                continue

            # not a xui file
            if not entry.endswith(".xui"):
                print("{filename} is not a xui file. Skipped.".format(filename=entry))
                continue

            self.recolor_file(entry)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("Usage: ./SCRIPT_NAME.py THEME_NAME")

    selected_theme_name = sys.argv[1]
    acr = AuroraColorReplacer(theme_name=selected_theme_name)
    acr.recolor_folder()
    sys.exit()
