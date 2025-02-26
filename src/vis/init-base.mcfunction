# Text that shows once on conversion complete
tellraw @a ["",{"text":"Commands successfully converted to a datapack!","color":"green"},{"text":"\n"},{"text":"- - - - - - - - - - - - - - -","color":"dark_green"},{"text":"\n"},{"text":"This message will not pop up again, it only shows that the converter has worked!\nIt's not mandatory, but feel free to credit me (","color":"green"},{"text":"NICO_THE_PRO","color":"dark_green"},{"text":") anywhere in your map, if this tool helped you.","color":"green"},{"text":"\n"},{"text":"[Click here]","color":"dark_green","clickEvent":{"action":"run_command","value":"/data merge storage dp_conv:init {\"sign\":true}"}},{"text":" to get a sign that you can put anywhere in the map to let more people know about this tool :).","color":"green"},{"text":"\n\n"},{"text":"Made with <3 by NICO_THE_PRO","color":"dark_green"}]
execute if data storage dp_conv:init "warnings" run tellraw @a ["",{"text":"- - - - - - - - - - - - - - -","bold":true,"color":"yellow"},{"text":"\n\u26a0", "color":"yellow"},{"text":" WARNING ","bold":true,"color":"gold"},{"text":"\u26a0\n", "color":"yellow"},{"text":"Some commands that got converted were modifying blocks/data at coordinates in the selected conversion area.\n Check out this file for more info:\n","color":"gold"},{"text":"/Users/hutchinsp01/Projects/personal/world/datapacks/day10/warnings.txt","color":"yellow"}]

# Initial states of the command blocks (storing if they started out active/inactive, successful/unsuccessful)
data merge storage dp_conv:day10 {"r0_0_auto":0b}
data merge storage dp_conv:day10 {"r0_1_auto":1b}
data merge storage dp_conv:day10 {"r0_2_auto":1b}
data merge storage dp_conv:day10 {"r1_0_auto":0b}
data merge storage dp_conv:day10 {"r1_1_auto":1b}