# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1pAoTM4FGdq61G0sdl6iWDMOH8RkAXo7a
"""

import pandas as pd
baza={
    "FISH":[ "azizibloyev hojiakbar", "mamadaliyev zikrullo", "yusubov temur", "mizahamidov jaloliddin", "raxmonov begizod", "qambarov samandar", "qambarova gulxayo", "obitjonova dilfuza", "madaminjonov baxtiyor", "yunusuva mohizar"  ],
    "YOSHI":[ '19', '19', '19', '19', '19', '19', '19', '19', '19', '19'],
    "MAKTABI":[ '1-maktab', '2-maktab', '3-maktab', '4-maktab', '5-maktab', '6-maktab','7-maktab', '8-maktab', '9-maktab', '10-maktab'  ],
    "JINSI":[ 'ogil bola', 'ogil bola', 'ogil bola', 'ogil bola', 'ogil bola', 'ogil bola', 'qiz bola', 'qiz bola', 'ogil bola', 'qiz bola' ],
    "MAZILI":[ 'fargona', 'andijon', 'buxoro', 'samarqand', 'namangan', 'margilon', 'xarazm', 'toshkent', 'nuks', 'jizzax'  ]
}
db=pd.DataFrame(baza)
print(db)

filtr=db[(db['JINSI']=="qiz bola") & (db['MAZILI']=='jizzax')]
print(filtr)

filtr=db[(db['JINSI']=="qiz bola"]
print(filtr)