###########################################################
## 
##  Aurora Dashboard Color Replacing Script
##  mrknorton4007 - version 1.0
##  Note: this replaces only the 2 variants of aquamarine used for the active elements
## 
###########################################################

## aurora file names
aurora_skin_file = "Aurora_Skin.xui"
aurora_new_file  = "Aurora_Skin_edit.xui"


## original colors (0xff------)
main_color = "0xff33e5a8"      #33e5a8 = aquamarine
secondary_color = "0xff55b696" #55b696 = dark aquamarine

## new colors (0xff------)
replace_main_color = "0xffcc1a57"      #cc1a57 = vivid raspberry
replace_secondary_color = "0xffaa4969" #aa4969 = moderate raspberry


## open files
file_content = open(aurora_skin_file, "r") 
new_content  = open(aurora_new_file, "w")


## for each line
for line in file_content:
	line = line.replace(main_color, replace_main_color)
	line = line.replace(secondary_color, replace_secondary_color)
	new_content.write(line)


## close file
file_content.close()
new_content.close()
