# This makes init run only once
execute if entity @a unless data storage dp_conv:init {"init":true} run function day10:init
execute if entity @a run data merge storage dp_conv:init {"init":true}

# Handles giving credit sign
execute if data storage dp_conv:init {"sign":true} run give @a minecraft:oak_sign{BlockEntityTag:{Text1:'{"text":"Converted to","clickEvent":{"action":"run_command","value":"tellraw @a [\\"\\",{\\"text\\":\\"The command blocks in this map were converted to a datapack using NICO_THE_PRO\'s datapack-converter tool! You can learn more on how it works by clicking \\",\\"color\\":\\"green\\"},{\\"text\\":\\"-> here <-\\",\\"bold\\":true,\\"color\\":\\"dark_green\\",\\"clickEvent\\":{\\"action\\":\\"open_url\\",\\"value\\":\\"https://github.com/rotolonico/Datapack-Converter\\"}}]"},"color":"green"}',Text2:'{"text":"datapack by","color":"green"}',Text3:'{"text":"NICO_THE_PRO","color":"green"}',Text4:'{"text":"[Learn more]","bold":true,"color":"dark_green"}'},display:{Name:'{"text":"Epic Sign :D"}'}}
data merge storage dp_conv:init {"sign":false}

# Handles warnings (if any)
execute if data storage dp_conv:init {"warning_message":true} run tellraw @a {"text":"WARNINGS_PLACEHOLDER","color":"yellow"}
data merge storage dp_conv:init {"warning_message":false}

# Calling commands
execute if data storage dp_conv:day10 {r0_0_auto:1b} run function day10:r0
execute if data storage dp_conv:day10 {r1_0_auto:1b} run function day10:r1
execute if data storage dp_conv:day10 {r0_0_auto:1b} run data merge storage dp_conv:day10 {r0_0_success:0b}
execute if data storage dp_conv:day10 {r0_1_auto:1b} run data merge storage dp_conv:day10 {r0_1_success:0b}
execute if data storage dp_conv:day10 {r0_2_auto:1b} run data merge storage dp_conv:day10 {r0_2_success:0b}
execute if data storage dp_conv:day10 {r1_0_auto:1b} run data merge storage dp_conv:day10 {r1_0_success:0b}
execute if data storage dp_conv:day10 {r1_1_auto:1b} run data merge storage dp_conv:day10 {r1_1_success:0b}
