###########################################################
## 
##  Aurora Dashboard Dark Mode Script
##  mrknorton4007 - version 1.0
##  Note: try to make a dark version starting from the Aurora default skin
## 
###########################################################

import re

## aurora file name
aurora_skin_file = "Aurora_Skin.xui"
aurora_new_file  = "Aurora_Skin_edit.xui"


## array of colors (search : replace)
## color format (0xff------) 
colors = {

	"<TextColor>0xff444444</TextColor>" : "<TextColor>0xffebebeb</TextColor>",
	"<TextColor>0xffaaaaaa</TextColor>" : "<TextColor>0xffebebeb</TextColor>",
	"<TextColor>0xffffffff</TextColor>" : "<TextColor>0xffebebeb</TextColor>",


	# "<Prop>0xff0000a7</Prop>" : "<Prop>0xff0000a7</Prop>",
	# "<Prop>0xff0000cf</Prop>" : "<Prop>0xff0000cf</Prop>",
	# "<Prop>0xff0900ef</Prop>" : "<Prop>0xff0900ef</Prop>",
	"<Prop>0xff33e5a8</Prop>" : "<Prop>0xff33e5a8</Prop>", # aquamarine
	"<Prop>0xff444444</Prop>" : "<Prop>0xffebebeb</Prop>",
	"<Prop>0xff55b696</Prop>" : "<Prop>0xff55b696</Prop>", # dark aquamarine
	# "<Prop>0xff7b5f19</Prop>" : "<Prop>0xff7b5f19</Prop>",
	"<Prop>0xffaaaaaa</Prop>" : "<Prop>0xffebebeb</Prop>",
	# "<Prop>0xffb39444</Prop>" : "<Prop>0xffb39444</Prop>",
	# "<Prop>0xffcc9922</Prop>" : "<Prop>0xffcc9922</Prop>",
	"<Prop>0xffdddddd</Prop>" : "<Prop>0xffebebeb</Prop>",
	"<Prop>0xffeeeeee</Prop>" : "<Prop>0xff262626</Prop>",
	"<Prop>0xffffffff</Prop>" : "<Prop>0xff262626</Prop>",


	# "<FillColor>0xff000000</FillColor>" : "<FillColor>0xff000000</FillColor>",
	# "<FillColor>0xff0000a7</FillColor>" : "<FillColor>0xff0000a7</FillColor>",
	"<FillColor>0xff444444</FillColor>" : "<FillColor>0xff161616</FillColor>",
	"<FillColor>0xff55b696</FillColor>" : "<FillColor>0xff55b696</FillColor>", # dark aquamarine
	"<FillColor>0xffaaaaaa</FillColor>" : "<FillColor>0xff161616</FillColor>",
	"<FillColor>0xffcccccc</FillColor>" : "<FillColor>0xff161616</FillColor>",
	"<FillColor>0xffdddddd</FillColor>" : "<FillColor>0xff262626</FillColor>",
	"<FillColor>0xffebebeb</FillColor>" : "<FillColor>0xff262626</FillColor>",
	"<FillColor>0xffffffff</FillColor>" : "<FillColor>0xff262626</FillColor>",


	"<StrokeColor>0xff000000</StrokeColor>" : "<StrokeColor>0xff000000</StrokeColor>",
	"<StrokeColor>0xff0f0f80</StrokeColor>" : "<StrokeColor>0xff666666</StrokeColor>",
	"<StrokeColor>0xff444444</StrokeColor>" : "<StrokeColor>0xff161616</StrokeColor>"
}


## define replace func
# https://stackoverflow.com/questions/8687018/python-string-replace-two-things-at-once/8687035#8687035
def replace_all(repls, str):
	return re.sub('|'.join(re.escape(key) for key in repls.keys()), lambda k: repls[k.group(0)], str)   


## open file
file_content = open(aurora_skin_file, "r") 
new_content  = open(aurora_new_file, "w")


## for each line
for line in file_content:
	line_2 = replace_all(colors, line)
	if line != line_2:
		print "Replaced " + line + " with " + line_2 # for debug only
	new_content.write(line_2)


## close file
file_content.close()
new_content.close()
