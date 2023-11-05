# OpenDoctoratePy

It's a pity that DoctoratePy is no longer maintained. Therefore, this repo aims to continue the support of this project for newer versions of the game.

Python server implementation of a certain anime tower defense game. This repo is for the CN TapTap Version.

Discord: [https://discord.com/invite/SmuB88RR5W](https://discord.com/invite/SmuB88RR5W)

## Currently tested emulator to be working

1. MuMu Player X (aka MuMu Player 12) (**recommended**)

2. LDPlayer9 (usable, but **NOT** recommended)

## How To

### MuMu Player X (aka MuMu Player 12)

[https://www.mumuglobal.com/faq/system-requirement-mumu-player-x.html](https://www.mumuglobal.com/faq/system-requirement-mumu-player-x.html)

[https://a11.gdl.netease.com/MuMuInstaller_12.0.0.6_12beta-gw-offline_all_1666787400.exe](https://a11.gdl.netease.com/MuMuInstaller_12.0.0.6_12beta-gw-offline_all_1666787400.exe)

1. Enable root permission in MuMu Player's settings (adb connection should be enabled by default, therefore no need to enable it manually).
2. Start MuMu Player X (aka MuMu Player 12).
3. Run `setup_requirements.bat`, and success can be indicated from `"Press enter to exit..."`.
4. Run `start_local_server.bat`, and the window should stay open if no error occurs.
5. Run `start_frida-server.bat`, and the window should stay open if no error occurs.
6. Run `start_frida-hook.bat`. It should automatically open up the game. The window should stay open if no error occurs.

### LDPlayer9

[https://ldcdn.ldmnq.com/download/package/LDPlayer9.0.exe](https://ldcdn.ldmnq.com/download/package/LDPlayer9.0.exe)

1. Enable root permission and adb connection in LDPlayer9's settings.
2. Start LDPlayer9.
3. Run `setup_requirements.bat`, and success can be indicated from `"Press enter to exit..."`.
4. Run `start_local_server.bat`, and the window should stay open if no error occurs.
5. Run `start_frida-server.bat`, and the window should stay open if no error occurs.
6. Run `start_frida-hook.bat`. It should automatically open up the game. The window should stay open if no error occurs.

## Changing contengency contract season
Change the value of key `selectedCrisis` in `config\config.json` to whatever you want. The avaiable seasons are under `data\crisis`.

## Customizing indivual operators level, potentials, skill ranks and others
Customize each operator indivually by adding new info in `customUnitInfo` key in `config\config.json`. You can find <operator_key_name> from [here](https://raw.githubusercontent.com/Kengxxiao/ArknightsGameData/master/zh_CN/gamedata/excel/character_table.json). By default, all characters will have max level, max potentials, max mastery.

- `favorPoint` - Trust points (25570 is 200% Trust) [link to exact point to %](https://gamepress.gg/arknights/core-gameplay/arknights-guide-operator-trust)
- `mainSkillLvl` - Skill Rank (Put mastery at 0 if this is lower than 7)
- `potentialRank` - 0-5
- `evolvePhase` - 0 - E0, 1 - E1, 2 - E2
- `skills` - Mastery level for each skill starting from S1.

### Format
```
"<operator_key_name>": {
    "favorPoint": 25570,
    "mainSkillLvl": 7,
    "potentialRank": 2,
    "level": 50, 
    "evolvePhase": 1,
    "skills": [1, 0]
}
```

## Customizing support unit
Customize the support unit list by changing the unit info in `assistUnit` key in `config\config.json`. All characters info can be found [here](https://raw.githubusercontent.com/Kengxxiao/ArknightsGameData/master/zh_CN/gamedata/excel/character_table.json).

- `charId` - key of the character
- `skinId` - skinId of the character (Skin List can be found [here](https://raw.githubusercontent.com/Kengxxiao/ArknightsGameData/master/zh_CN/gamedata/excel/skin_table.json))
- `skillIndex` - Skill Index of the support unit (Index starts from 0).

Note: Characters stats and skill masteries are based on the above parameters.

### Format
```
{
    "charId": "char_350_surtr",
    "skinId": "char_350_surtr@it#1",
    "skillIndex": 2
}
```

## TODO
- [ ] Add more info about mods
- [ ] Add a UI for easy editing
