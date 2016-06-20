#written by Ran Dubin: randubin@gmail.com
# Please feel free to contribute.
#The code is part of a research project called :I Know What You Saw Last Minute - Encrypted
#HTTP Adaptive Video Streaming Title Classification.
#This is the Chrome YouTube video download crawler.

#Please note, the crawler create a pcap file for each new download and save it to root_path. The download is in automatic mode.
#please use ad block or skip the ad or select the maximum largest  Youtube traffic flow (not recomended)
#This software
#---------------------IMPORTS----------------------------------------------------------

from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
import subprocess
import os.path
#--------------------------------------------------------------------------------------
#---------------------GLOBALS----------------------------------------------------------

tshark_interface_number = "2"
root_path = "C:\\Users\\user\\Desktop\\ranTests\\pcap\\Chrome\\"
chrome_driver_path = "C:\\Python27\\Scripts\\chromedriver.exe"
tshark_path = "C:\\Program Files\\Wireshark\\tshark.exe"
chrome_default_profile = "user-data-dir=C:\\Users\\user\\AppData\\Local\\Google\\Chrome\\User Data\\Default"


# The function recieve a string indicate the requested video quality
def downloadVideo(video_quality, video_name, url, duration_of_the_video):
    t_time = time.strftime("%H_%M_%S")
    funcInFile = "Train"
    # create pcap folder
    if not os.path.exists(root_path):
        os.makedirs(root_path)
    # create video folder
    video_path = root_path + video_name + "\\"
    if not os.path.exists(video_path):
        os.makedirs(video_path)

    # create quality folder
    quality_path = video_path + funcInFile + "\\"
    if not os.path.exists(quality_path):
        os.makedirs(quality_path)
    filename = quality_path + video_name + "_" + funcInFile + t_time + ".pcap"
    tsharkOut = open(filename, "wb")
    tsharkCall = [tshark_path, "-F", "pcap", "-f", "tcp port 443", "-i", tshark_interface_number, "-w",
                  filename]  # 8-fixed line 3 wifi in my pc
    tsharkProc = subprocess.Popen(tsharkCall, stdout=tsharkOut, executable=tshark_path)

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument(chrome_default_profile)
    # If you have problem with using default user profile. Try adding ad block plus crx directly.
    ##chrome_options.add_extension('adblockpluschrome-1.8.10.1352.crx')
    #more information in this link : http://stackoverflow.com/questions/25018286/how-can-i-use-selenium-with-my-normal-browser
    driver = webdriver.Chrome(executable_path=chrome_driver_path, chrome_options=chrome_options)
    wait = WebDriverWait(driver, 100)
    driver.get(url)
    time.sleep(1)

    time.sleep(duration_of_the_video)
    driver.close()
    tsharkProc.kill()


####################################################
# Start multiple downloads
####################################################
def harvest_video(amount, name, url, duration):
    for x in range(0, amount):
        print('run number:', x)
        downloadVideo("Auto", name, url, duration)

BBB_URL = "https://www.youtube.com/watch?v=Z5KLxerq05Y"
BBB_duration = 740
world_largest_zip_line_url = "https://www.youtube.com/watch?v=YcwrRA2BIlw"
world_largest_zip_line_duration = 200
sky_dive_dubay_url = "https://www.youtube.com/watch?v=zFg_mlBFV2c"
sky_dive_dubay_duration = 630
incredible_4K_url = "https://www.youtube.com/watch?v=6pxRHBw-k8M"
incredible_4K_duration = 220
the_advanture_of_life_url = "https://www.youtube.com/watch?v=wTcNtgA6gHs&list=PLSSPBo7OVSZvJtRrcF5CVSjRkmH9eNWA3"
the_advanture_of_life_duration = 260
honey_bees_url = "https://www.youtube.com/watch?v=Cx6eaVeYXOs"
honey_bees_duration = 240
Dreamlapse_UHD_url = "https://www.youtube.com/watch?v=qiBm4AfRcr0"
Dreamlapse_UHD_duration = 240
Homefront_TRAILER_url = "https://www.youtube.com/watch?v=JCPew975Qfc"
Homefront_TRAILER_duration = 170
WILDLIFE_IN_4K_url = "https://www.youtube.com/watch?v=xDMP3i36naA"
WILDLIFE_IN_4K_duration = 210
the_prodigy_nasty_url = "https://www.youtube.com/watch?v=xB_nKpEkILs&index=43&list=PL9tY0BWXOZFvWi6WNdcokF_YvXUxyESRW"
the_prodigy_nasty_duration = 230
diving_with_manta_ray_url = "https://www.youtube.com/watch?v=Mc3NTnoGzwE&index=15&list=PLSSPBo7OVSZvJtRrcF5CVSjRkmH9eNWA3"
diving_with_manta_ray_duration = 110
NIGHT_AT_THE_MUSEUM_3_url = "https://www.youtube.com/watch?v=Hr1fFMp0MqU"
NIGHT_AT_THE_MUSEUM_3_duration = 150
iron_man_3_url = "https://www.youtube.com/watch?v=uBI4nPnQ8jI"
iron_man_3_duration = 130
Oblivion_Trailer_url = "https://www.youtube.com/watch?v=ZokHZXb8QDs"
Oblivion_Trailer_duration = 160
x_men_days_of_future_past_url = "https://www.youtube.com/watch?v=IbiX07HHW3I"
x_men_days_of_future_past_duration = 145
Drone_Footage_Of_Frozen_Niagara_Falls_url = "https://www.youtube.com/watch?v=7PNTuIECZCE"
Drone_Footage_Of_Frozen_Niagara_Falls_duration = 120

the_movie_url = "https://www.youtube.com/watch?v=V5hOm8_3mJA"
the_movie_duration = 152
Hitman_url = "https://www.youtube.com/watch?v=alQlJDRnQkE"
Hitman_duration = 150
mr_Holmes_url = "https://www.youtube.com/watch?v=FJwgItmobFE"
mr_holmes_duration = 80
San_andreass_url = "https://www.youtube.com/watch?v=UN1G4BSyIos"
San_andreass_duration = 142
mad_max_url = "https://www.youtube.com/watch?v=b_4nzm9ICuo"
mad_max_duration = 142
FiveFlights_url = "https://www.youtube.com/watch?v=PreX3h3QYHY"
FiveFlights_duration = 140
Aloha_url = "https://www.youtube.com/watch?v=O3mf_ewjc7s"
Aloha_duration = 150
Pitch_perfect2_url = "https://www.youtube.com/watch?v=TY-u5P9pRwA"
Pitch_perfect2_duration = 150
Fifty_shades_ofGrey_url = "https://www.youtube.com/watch?v=CQERFnGvi_A"
Fifty_shades_ofGrey_duration = 146
Friends_url = "https://www.youtube.com/watch?v=V5hOm8_3mJA"
Friends_duration = 152
Furious_7_url = "https://www.youtube.com/watch?v=k94wBXeauao"
Furious_7_duration = 180
Terrence_Howard_url = "https://www.youtube.com/watch?v=NGheJlDfb08"
Terrence_Howard_duration = 182
THE_LOFT_url = "https://www.youtube.com/watch?v=08JRDC4-kug"
THE_LOFT_duration = 140
Last_Knights_url = "https://www.youtube.com/watch?v=e44QilQbvB0"
Last_Knights_duration = 150
The_Interview_url = "https://www.youtube.com/watch?v=KpyVENBPj5c"
The_Interview_duration = 160
Sex_Tape_url = "https://www.youtube.com/watch?v=JF6IXw86iSQ"
Sex_Tape_duration = 180
Ten_Rules_url = "https://www.youtube.com/watch?v=7McSiK7IrDw"
Ten_Rules_duration = 142
Dom_Hemingway_url = "https://www.youtube.com/watch?v=u1izaIH269E"
Dom_Hemingway_url = 135
Exodus_url = "https://www.youtube.com/watch?v=t-8YsulfxVI"
Exodus_duration = 185
Filth_url = "https://www.youtube.com/watch?v=QH0F0GKkUFE"
Filth_duration = 134
cliff_jumps_url = "https://www.youtube.com/watch?v=Bn09g1bwgDc"
cliff_jumps_duration = 334
Fantastic_Four_url = "https://www.youtube.com/watch?v=cxIldZcUuCk"
Fantastic_Four_duration = 105
Home_Sweet_Hell_url = "https://www.youtube.com/watch?v=UbuvFMvytu4"
Home_Sweet_Hell_duration = 134
Cinderella_url = "https://www.youtube.com/watch?v=Pqk436s9cg4"
Cinderella_duration = 130
TenYears_url = "https://www.youtube.com/watch?v=X9Ku-HJc6yE"
TenYears_duration = 151
#####
Albatross_url = "https://www.youtube.com/watch?v=KQnXnbQCJDo"
Albatross_duration = 111
American_Hustle_url = "https://www.youtube.com/watch?v=BeyUrnU_lZ4"
American_Hustle_duration = 111
Avengers_url = "https://www.youtube.com/watch?v=JAUoeqvedMo"
Avengers_duration = 138
Chinese_url = "https://www.youtube.com/watch?v=LbiIu_EzuWk"
Chinese_duration = 240
CURSE_OF_THE_DRAGON_url = "https://www.youtube.com/watch?v=bMW-ja_Rkdw"
CURSE_OF_THE_DRAGON_duration = 150
Dark_Tide_url = "https://www.youtube.com/watch?v=0ipC-bjnH4A"
Dark_Tide_duration = 110
Das_Keyboard_url = "https://www.youtube.com/watch?v=CjIk1JMjMqU"
Das_Keyboard_duration = 492
Disconnect_url = "https://www.youtube.com/watch?v=gkoM0IbbLiY"
Disconnect_duration = 152
Diversity_and_Inclusion_url = "https://www.youtube.com/watch?v=PnDgZuGIhHs"
Diversity_and_Inclusion_duration = 200
Divorce_url = "https://www.youtube.com/watch?v=vN--jzplDPE"
Divorce_duration = 131
Fast_and_Furious_six_url = "https://www.youtube.com/watch?v=dKi5XoeTN0k"
Fast_and_Furious_six_duration = 202
First_human_url = "https://www.youtube.com/watch?v=0E77j1imdhQ"
First_human_duration = 143
Flyboard_url = "https://www.youtube.com/watch?v=m4Bm3cs9TFo"
Flyboard_duration = 200
Taylor_Swift_url = "https://www.youtube.com/watch?v=QcIy9NiNbmo"
Taylor_Swift_duration = 245
Game_of_Thrones_url = "https://www.youtube.com/watch?v=xZY43QSx3Fk"
Game_of_Thrones_duration = 110
Maleficent_url = "https://www.youtube.com/watch?v=w-XO4XiRop0"
Maleficent_duration = 130
Omer_adam_url = "https://www.youtube.com/watch?v=TmG_OVVYNug"
Omer_adam_duration = 290
Pacific_Rim_url = "https://www.youtube.com/watch?v=5guMumPFBag"
Pacific_Rim_duration = 152
Passion_url = "https://www.youtube.com/watch?v=-YhHeO1BuAI"
Passion_duration = 110
Red_Dawn_url = "https://www.youtube.com/watch?v=nGoe7BdGdlg"
Red_Dawn_duration = 155
Soldiers_of_Fortune_url = "https://www.youtube.com/watch?v=6sVP0axlhc4"
Soldiers_of_Fortune_duration = 135
Tamer_Hosny_url = "https://www.youtube.com/watch?v=U_dGwmcwHxU"
Tamer_Hosny_duration = 600

The_English_Teacher_url = "https://www.youtube.com/watch?v=7LLWTXoHHAY"
The_English_Teacher_duration = 140
The_Man_With_The_Iron_Fists_url = "https://www.youtube.com/watch?v=6FyGHAUpSIQ"
The_Man_With_The_Iron_Fists_duration = 140
Welcome_to_Yesterday_url = "https://www.youtube.com/watch?v=KnGcWVoxftI"
Welcome_to_Yesterday_duration = 160
goproSyberTiger_url = "https://www.youtube.com/watch?v=AZ1jTsQS4EY"
goproSyberTiger = 136
# ---------------new set 31_3_2016---------------
jennifer_lopez_papi_url = "https://www.youtube.com/watch?v=6XbIuSLaCnk"
jennifer_lopez_papi_duration = 325
Friday_Rebecca_Black_url = "https://www.youtube.com/watch?v=kfVsfOSbJY0"
Friday_Rebecca_Black_duration = 227
Pharrell_Williams_Happy_url = "https://www.youtube.com/watch?v=ZbZSe6N_BXs"
Pharrell_Williams_Happy_duration = 246
Nature_Beauty_4K_url = "https://www.youtube.com/watch?v=cqcldOyEYRE"
Nature_Beauty_4K_duration = 147
Katy_Perry_This_Is_How_We_Do_url = "https://www.youtube.com/watch?v=7RMQksXpQSk"
Katy_Perry_This_Is_How_We_Do_duration = 209
Cristiano_Ronaldo_url = "https://www.youtube.com/watch?v=QEnxuWjZgx8"
Cristiano_Ronaldo_duration = 350
Katy_Perry_Birthday_url = "https://www.youtube.com/watch?v=jqYxyd1iSNk"
Katy_Perry_Birthday_duration = 215
Maroon_5_Love_Somebody_url = "https://www.youtube.com/watch?v=MU8B4XDI3Uw"
Maroon_5_Love_Somebody_duration = 238
Meghan_Trainor_All_About_That_Bass_url = "https://www.youtube.com/watch?v=7PCkvCPvDXk"
Meghan_Trainor_All_About_That_Bass_duration = 189
GoPro_Snow_Daze_url = "https://www.youtube.com/watch?v=779OQH4R8Bk"
GoPro_Snow_Daze_duration = 263
Farruko_Obsesionado_url = "https://www.youtube.com/watch?v=lkN51aqPOzU"
Farruko_Obsesionado_duration = 256
Farruko_Lejos_url = "https://www.youtube.com/watch?v=MHl0vbc0Nys"
Farruko_Lejos_duration = 239
Maluma_Borro_Cassette_url = "https://www.youtube.com/watch?v=kkx-7fsiWgg"
Maluma_Borro_Cassette_duration = 247
Sting_Be_Still_url = "https://www.youtube.com/watch?v=Ng4P6FWVdcE"
Sting_Be_Still_duration = 333
CNN_url = "https://www.youtube.com/watch?v=Rrtjh7QmxAQ"
CNN_duration = 211
Bon_Jovi_Always_url = "https://www.youtube.com/watch?v=9BMwcO6_hyA"
Bon_Jovi_Always_duration = 362
Shakira_Whenever_url = "https://www.youtube.com/watch?v=weRHyjj34ZE"
Shakira_Whenever_duration = 197
Enrique_Iglesias_Bailamos_url = "https://www.youtube.com/watch?v=weRHyjj34ZE"
Enrique_Iglesias_Bailamos_duration = 217
Whitney_Houston_When_You_Believe_url = "https://www.youtube.com/watch?v=LKaXY4IdZ40"
Whitney_Houston_When_You_Believe_duration = 297
Diving_in_Bali_url = "https://www.youtube.com/watch?v=WFAY8kSYvOo"
Diving_in_Bali_duration = 350
Don_Omar_Dutty_Love_url = "https://www.youtube.com/watch?v=x622Sqjub-s"
Don_Omar_Dutty_Love_duration = 286
J_Alvarez_Junto_Al_Amanecer_url = "https://www.youtube.com/watch?v=hZ7nZ0lQ7Is"
J_Alvarez_Junto_Al_Amanecer_duration = 269
Michael_Jackson_They_Dont_Care_About_Us_url = "https://www.youtube.com/watch?v=QNJL6nfu__Q"
Michael_Jackson_They_Dont_Care_About_Us_duration = 281
Michael_Jackson_Heal_The_World_url = "https://www.youtube.com/watch?v=QNJL6nfu__Q"
Michael_Jackson_Heal_The_World_duration = 382
Michael_Jackson_Earth_Song_url = "https://www.youtube.com/watch?v=XAi3VTSdTxU"
Michael_Jackson_Earth_Song_duration = 402
_2pac_Changes_url = "https://www.youtube.com/watch?v=uS4CvCGFyqc"
_2pac_Changes_duration = 277
Coolio_Gangsters_Paradise_url = "https://www.youtube.com/watch?v=N6voHeEa3ig"
Coolio_Gangsters_Paradise_duration = 248
Eminem_Sing_For_The_Moment_url = "https://www.youtube.com/watch?v=D4hAVemuQXY"
Eminem_Sing_For_The_Moment_duration = 327
Alerta_Roja_url = "https://www.youtube.com/watch?v=Rg4HQ1RhhYk"
Alerta_Roja_duration = 633
Dear_Mama_url = "https://www.youtube.com/watch?v=Mb1ZvUDvLDY"
Dear_Mama_duration = 280
Yandel_Hasta_Abajo_url = "https://www.youtube.com/watch?v=vMHdvd3XEyU"
Yandel_Hasta_Abajo_duration = 271
Alexis_y_Fido_url = "https://www.youtube.com/watch?v=bMCwoHNm_d4"
Alexis_y_Fido_duration = 264
The_Dictator_interviews_url = "https://www.youtube.com/watch?v=XavOvkiAnZw"
The_Dictator_duration = 488
Warcraft_interviews_url = "https://www.youtube.com/watch?v=-ogw1cSZO0I"
Warcraft_duration = 120
MINIONS_url = "https://www.youtube.com/watch?v=Ut9xi-ep2mg"
MINIONS_duration = 234
Pitbull_Fun_url = "https://www.youtube.com/watch?v=jKbR7u8J5PU"
Pitbull_Fun_duration = 241
Zion_Embriagame_url = "https://www.youtube.com/watch?v=z5xrhePJHsg"
Zion_Embriagame_duration = 225
Cosculluela_url = "https://www.youtube.com/watch?v=iapVc5qaheo"
Cosculluela_duration = 300
INNA_Bad_Boys_url = "https://www.youtube.com/watch?v=6ttobrfMnyQ"
INNA_Bad_Boys_duration = 189
Michael_Jackson_Black_Or_White_url = "https://www.youtube.com/watch?v=F2AitTPI5U0"
Michael_Jackson_Black_Or_White_duration = 382
Democratic_Town_Hall_url = "https://www.youtube.com/watch?v=JRFk0UjRa6k"
Democratic_Town_Hall_duration = 266
BBC_News_url = "https://www.youtube.com/watch?v=JRFk0UjRa6k"
BBC_News_duration = 155
Lenny_Kravitz_American_Woman_url = "https://www.youtube.com/watch?v=UzWHE32IxUc"
Lenny_Kravitz_American_Woman_duration = 260
Akon_Right_Now_url = "https://www.youtube.com/watch?v=vIaH35-MLsk"
Akon_Right_Now_duration = 302
fifty_Cent_In_Da_Club_url = "https://www.youtube.com/watch?v=5qm8PH4xAss"
fifty_Cent_In_Da_Club_duration = 249
Snoop_Dogg_Sensual_Seduction_url = "https://www.youtube.com/watch?v=Y1PVmANeyAg"
Snoop_Dogg_Sensual_Seduction_duration = 243
The_Black_Eyed_Peas_url = "https://www.youtube.com/watch?v=I7HahVwYpwo"
The_Black_Eyed_Peas_duration = 288
Avicii_Waiting_url = "https://www.youtube.com/watch?v=cHHLHGNpCSA"
Avicii_Waiting_duration = 230
Black_Eyed_Peas_Where_Is_The_Love_url = "https://www.youtube.com/watch?v=WpYeekQkAdc"
Black_Eyed_Peas_Where_Is_The_Love_duration = 252
Sola_url = "https://www.youtube.com/watch?v=Nk4N_LGWNA4"
Sola_duration = 216
Cheerleader_url = "https://www.youtube.com/watch?v=jGflUbPQfW8"
Cheerleader_duration = 189
Time_Of_Our_Lives_url = "https://www.youtube.com/watch?v=bTXJQ5ql5Fw"
Time_Of_Our_Lives_duration = 281
Let_It_Go_url = "https://www.youtube.com/watch?v=bTXJQ5ql5Fw"
Let_It_Go_duration = 283
Jungle_Book_url = "https://www.youtube.com/watch?v=HcgJRQWxKnw"
Jungle_Book_duration = 115
Pitbull_Hotel_Room_Service_url = "https://www.youtube.com/watch?v=2up_Eq6r6Ko"
Pitbull_Hotel_Room_Service_duration = 268
Jennifer_Lopez_On_The_Floor_url = "https://www.youtube.com/watch?v=t4H_Zoh7G5A"
Jennifer_Lopez_On_The_Floor_duration = 266
BonBon_url = "https://www.youtube.com/watch?v=9O72RLP5fF4"
BonBon_duration = 216
Robbie_Williams_Supreme_url = "https://www.youtube.com/watch?v=ULTtWUZhD9c"
Robbie_Williams_Supreme_duration = 274
Maroon_5_Sugar_url = "https://www.youtube.com/watch?v=09R8_2nJtjg"
Maroon_5_Sugar_duration = 301
NE_YO_url = "https://www.youtube.com/watch?v=lv5RWCQsZIU"
NE_YO_duration = 276
Eminem_Without_Me_url = "https://www.youtube.com/watch?v=YVkUvmDQ3HY"
Eminem_Without_Me_duration = 299
Freedom_url = "https://www.youtube.com/watch?v=zKKF_vFshMM"
Freedom_duration = 194
El_Perdon_url = "https://www.youtube.com/watch?v=ybm205q7Pd4"
El_Perdon_duration = 207
The_Lazy_Song_url = "https://www.youtube.com/watch?v=fLexgOxsZu0"
The_Lazy_Song_duration = 208
Party_Rock_url = "https://www.youtube.com/watch?v=KQ6zr6kCPj8"
Party_Rock_duration = 375
# -------
j_alvarez_url = "https://www.youtube.com/watch?v=YY33oEDtJv0"
j_alvarez_duration = 245
Justin_Bieber_url = "https://www.youtube.com/watch?v=PfGaX8G0f2E"
Justin_Bieber_duration = 200
Tired_of_Running_url = "https://www.youtube.com/watch?v=4u6DcnNuIPw"
Tired_of_Running_duration = 323
Shakira_Waka_Waka_url = "https://www.youtube.com/watch?v=pRpeEdMmmQ0"
Shakira_Waka_Waka_duration = 210
Taylor_Swift_Bad_Blood_url = "https://www.youtube.com/watch?v=QcIy9NiNbmo"
Taylor_Swift_Bad_Blood_duration = 244
Sia_Chandelier_url = "https://www.youtube.com/watch?v=2vjPBrBU-TM"
Sia_Chandelier_duration = 231
Sevyn_Streeter_Furious_7_url = "https://www.youtube.com/watch?v=6Ugaq6r6sQE"
Sevyn_Streeter_Furious_7_duration = 231
Taylor_Swift_Wildest_Dreams_url = "https://www.youtube.com/watch?v=IdneKLhsWOQ"
Taylor_Swift_Wildest_Dreams_duration = 234
Dubai_Journey_url = "https://www.youtube.com/watch?v=2qDcpq172QU"
Dubai_Journey_duration = 492
Farruko_Hola_Beba_url = "https://www.youtube.com/watch?v=IfPyKwwe5ck"
Farruko_Hola_Beba_duration = 237
How_Deep_Is_Your_Love_url = "https://www.youtube.com/watch?v=EgqUJOudrcM"
How_Deep_Is_Your_Love_duration = 260
Ai_Se_Eu_Te_Pego_url = "https://www.youtube.com/watch?v=hcm55lU9knw"
Ai_Se_Eu_Te_Pego_duration = 164
Teenage_Mutant_Ninja_Turtles_2_url = "https://www.youtube.com/watch?v=vXC31hSkHgc"
Teenage_Mutant_Ninja_Turtles_2_duration = 146

The_Hum_url = "https://www.youtube.com/watch?v=exJlapzPnlc"
The_Hum_duration = 284

bara_bere_url = "https://www.youtube.com/watch?v=gEiqSUzQ1fo"
bara_bere_duration = 164

Humilde_Residencia_url = "https://www.youtube.com/watch?v=ogD8UDiMe1g"
Humilde_Residencia_duration = 198

Lord_Of_The_Lost_url = "https://www.youtube.com/watch?v=eYU4cDG1SAs"
Lord_Of_The_Lost_duration = 324

La_Bomba_url = "https://www.youtube.com/watch?v=Uy7a2ovQwK4"
La_Bomba_duration = 280

Wo_sind_die_Clowns_url = "https://www.youtube.com/watch?v=7J6_YCLj5zg"
Wo_sind_die_Clowns_duration = 206

Hollyweezy_url = "https://www.youtube.com/watch?v=skN5U4dlmrE"
Hollyweezy_duration = 307

Maria_url = "https://www.youtube.com/watch?v=yqFdgJJrzNc"
Maria_duration = 216

HANGOVER_url = "https://www.youtube.com/watch?v=HkMNOlYcpHg"
HANGOVER_duration = 308

GUNMAN_STYLE_url = "https://www.youtube.com/watch?v=ceVlltPBcHg"
GUNMAN_STYLE_duration = 381

# harvest_video(1,"Friends",Friends_url,Friends_duration)
# harvest_video(90,"Furious_7",Furious_7_url,Furious_7_duration)
# harvest_video(100,"Terrence_Howard",Terrence_Howard_url,Terrence_Howard_duration)
# harvest_video(1,"THE_LOFT",THE_LOFT_url,THE_LOFT_duration)
# harvest_video(100,"Last_Knights",Last_Knights_url,Last_Knights_duration)
# harvest_video(100,"The_Interview",The_Interview_url,The_Interview_duration)
# harvest_video(81,"world_largest_zip_line",world_largest_zip_line_url,world_largest_zip_line_duration)
# harvest_video(100,"Sex_Tape",Sex_Tape_url,Sex_Tape_duration)
# harvest_video(29,"Ten_Rules",Ten_Rules_url,Ten_Rules_duration)
# harvest_video(100,"Exodus",Exodus_url,Exodus_duration)

# harvest_video(89,"Fantastic_Four_url",Fantastic_Four_url,Fantastic_Four_duration)
# harvest_video(100,"Home_Sweet_Hell",Home_Sweet_Hell_url,Home_Sweet_Hell_duration)
# harvest_video(35,"Cinderella",Cinderella_url,Cinderella_duration)
# harvest_video(100,"TenYears",TenYears_url,TenYears_duration)
################################################################################################

##################Chrome###########Chrome############################
# harvest_video(1,"Albatross",Albatross_url,Albatross_duration)
# harvest_video(1,"diving_with_manta_ray",diving_with_manta_ray_url,diving_with_manta_ray_duration)

# harvest_video(1,"American_Hustle",American_Hustle_url,American_Hustle_duration)
# harvest_video(1,"Avengers",Avengers_url,Avengers_duration)
# harvest_video(1,"Chinese",Chinese_url,Chinese_duration)
# harvest_video(1,"CURSE_OF_THE_DRAGON",CURSE_OF_THE_DRAGON_url,CURSE_OF_THE_DRAGON_duration)
# ----------------
# harvest_video(1,"Dark_Tide",Dark_Tide_url,Dark_Tide_duration)
# harvest_video(1,"Flyboard",Flyboard_url,Flyboard_duration)
# harvest_video(1,"cliff_jumps",cliff_jumps_url,cliff_jumps_duration)
# harvest_video(1,"Taylor_Swift",Taylor_Swift_url,Taylor_Swift_duration)
# harvest_video(1,"diving_with_manta_ray",diving_with_manta_ray_url,diving_with_manta_ray_duration)
##############################Download videos that are not in the DB###################################################





# harvest_video(100,"Das_Keyboard",Das_Keyboard_url,Das_Keyboard_duration)
# harvest_video(98,"Disconnect",Disconnect_url,Disconnect_duration)
# harvest_video(89,"Diversity_and_Inclusion",Diversity_and_Inclusion_url,Diversity_and_Inclusion_duration)
# harvest_video(100,"Divorce",Divorce_url,Divorce_duration)
# harvest_video(35,"Fast_and_Furious_six",Fast_and_Furious_six_url,Fast_and_Furious_six_duration)
# harvest_video(100,"First_human",First_human_url,First_human_duration)
###################################################################################33
# test data single download of titles which are not found  in DB
# harvest_video(1,"SyberTiger",goproSyberTiger_url,goproSyberTiger)
# harvest_video(1,"Game_of_Thrones",Game_of_Thrones_url,Game_of_Thrones_duration)
# harvest_video(1,"Maleficent",Maleficent_url,Maleficent_duration)
# harvest_video(1,"Omer_adam",Omer_adam_url,Omer_adam_duration)
# harvest_video(1,"Pacific_Rim",Pacific_Rim_url,Pacific_Rim_duration)
# harvest_video(1,"Passion",Passion_url,Passion_duration)
# harvest_video(1,"Red_Dawn",Red_Dawn_url,Red_Dawn_duration)
# harvest_video(1,"Tamer_Hosny",Tamer_Hosny_url,Tamer_Hosny_duration)
# harvest_video(1,"The_English_Teacher",The_English_Teacher_url,The_English_Teacher_duration)
# harvest_video(1,"The_Man_With_The_Iron_Fists",The_Man_With_The_Iron_Fists_url,The_Man_With_The_Iron_Fists_duration)
# harvest_video(1,"Welcome_to_Yesterday",Welcome_to_Yesterday_url,Welcome_to_Yesterday_duration)
# harvest_video(1,"The_movie",the_movie_url,the_movie_duration)
# harvest_video(1,"Hitman",Hitman_url,Hitman_duration)
# harvest_video(1,"San_andreass",San_andreass_url,San_andreass_duration)
# harvest_video(1,"Mr_Holmes",mr_Holmes_url,mr_holmes_duration)
# harvest_video(1,"Mad_max",mad_max_url,mad_max_duration)
# harvest_video(1,"FiveFlights",FiveFlights_url,FiveFlights_duration)
# harvest_video(1,"Pitch_perfect2",Pitch_perfect2_url,Pitch_perfect2_duration)
# harvest_video(1,"Fifty_shades_ofGrey",Fifty_shades_ofGrey_url,Fifty_shades_ofGrey_duration)

# harvest_video(1,"Drone_Footage_Of_Frozen_Niagara_Falls",Drone_Footage_Of_Frozen_Niagara_Falls_url,Drone_Footage_Of_Frozen_Niagara_Falls_duration)
# harvest_video(1,"x_men_days_of_future_past",x_men_days_of_future_past_url,x_men_days_of_future_past_duration)
# harvest_video(1,"Oblivion_Trailer",Oblivion_Trailer_url,Oblivion_Trailer_duration)
# harvest_video(1,"iron_man_3",iron_man_3_url,iron_man_3_duration)
# harvest_video(1,"NIGHT_AT_THE_MUSEUM_3",NIGHT_AT_THE_MUSEUM_3_url,NIGHT_AT_THE_MUSEUM_3_duration)
# harvest_video(1,"the_prodigy_nasty",the_prodigy_nasty_url,the_prodigy_nasty_duration)
# harvest_video(1,"WILDLIFE_IN_4K",WILDLIFE_IN_4K_url,WILDLIFE_IN_4K_duration)
# harvest_video(1,"Homefront_TRAILER",Homefront_TRAILER_url,Homefront_TRAILER_duration)
# harvest_video(1,"Dreamlapse_UHD",Dreamlapse_UHD_url,Dreamlapse_UHD_duration)
# harvest_video(1,"honey_bees",honey_bees_url,honey_bees_duration)
# harvest_video(1,"the_advanture_of_life",the_advanture_of_life_url,the_advanture_of_life_duration)
# harvest_video(1,"incredible_4K",incredible_4K_url,incredible_4K_duration)
# ----new 60 uploads from 31_3_2016--------------------------------
# harvest_video(17,"Party_Rock",Party_Rock_url,Party_Rock_duration)
# harvest_video(100,"The_Lazy_Song",The_Lazy_Song_url,The_Lazy_Song_duration)
# harvest_video(100,"El_Perdon",El_Perdon_url,El_Perdon_duration)#4harvest_video(1,"Freedom",Freedom_url,Freedom_duration,typeClick,QulityType,bType)#4
# harvest_video(100,"Eminem_Without_Me",Eminem_Without_Me_url,Eminem_Without_Me_duration)#4
# harvest_video(100,"NE_YO",NE_YO_url,NE_YO_duration)#4
# harvest_video(100,"Maroon_5_Sugar",Maroon_5_Sugar_url,Maroon_5_Sugar_duration)#4
# harvest_video(40,"Robbie_Williams_Supreme",Robbie_Williams_Supreme_url,Robbie_Williams_Supreme_duration)#4
# harvest_video(74,"BonBon",BonBon_url,BonBon_duration)#4
# harvest_video(16,"Jennifer_Lopez_On_The_Floor",Jennifer_Lopez_On_The_Floor_url,Jennifer_Lopez_On_The_Floor_duration)#4
# harvest_video(4,"Pitbull_Hotel_Room_Service",Pitbull_Hotel_Room_Service_url,Pitbull_Hotel_Room_Service_duration)#4
# harvest_video(100,"Jungle_Book",Jungle_Book_url,Jungle_Book_duration)#4
# harvest_video(100,"fifty_Cent_In_Da_Club",fifty_Cent_In_Da_Club_url,fifty_Cent_In_Da_Club_duration)#4
# harvest_video(100,"Snoop_Dogg_Sensual_Seduction",Snoop_Dogg_Sensual_Seduction_url,Snoop_Dogg_Sensual_Seduction_duration)#4
# harvest_video(100,"The_Black_Eyed_Peas",The_Black_Eyed_Peas_url,The_Black_Eyed_Peas_duration)#4
# harvest_video(100,"Avicii_Waiting",Avicii_Waiting_url,Avicii_Waiting_duration)#4
# harvest_video(100,"Black_Eyed_Peas_Where_Is_The_Love",Black_Eyed_Peas_Where_Is_The_Love_url,Black_Eyed_Peas_Where_Is_The_Love_duration)#4
# harvest_video(100,"Sola",Sola_url,Sola_duration)#4
# harvest_video(6,"Cheerleader",Cheerleader_url,Cheerleader_duration)#4
# harvest_video(30,"Time_Of_Our_Lives",Time_Of_Our_Lives_url,Time_Of_Our_Lives_duration)#4
# harvest_video(77,"Let_It_Go",Let_It_Go_url,Let_It_Go_duration)#4
# harvest_video(100,"Akon_Right_Now",Akon_Right_Now_url,Akon_Right_Now_duration)#4
# harvest_video(18,"Lenny_Kravitz_American_Woman",Lenny_Kravitz_American_Woman_url,Lenny_Kravitz_American_Woman_duration)#4
# harvest_video(100,"Democratic_Town_Hall",Democratic_Town_Hall_url,Democratic_Town_Hall_duration)#4
# harvest_video(1,"Michael_Jackson_Black_Or_White",Michael_Jackson_Black_Or_White_url,Michael_Jackson_Black_Or_White_duration)#4harvest_video(1,"INNA_Bad_Boys",INNA_Bad_Boys_url,INNA_Bad_Boys_duration,typeClick,QulityType,bType)#4
# harvest_video(6,"Cosculluela",Cosculluela_url,Cosculluela_duration)#4
# harvest_video(100,"Zion_Embriagame",Zion_Embriagame_url,Zion_Embriagame_duration)#4
# harvest_video(100,"Pitbull_Fun",Pitbull_Fun_url,Pitbull_Fun_duration)#4
# harvest_video(100,"MINIONS",MINIONS_url,MINIONS_duration)#4
# harvest_video(100,"Warcraft",Warcraft_interviews_url,Warcraft_duration)#4
# harvest_video(100,"Ali_G_NBA_interviews",The_Dictator_interviews_url,The_Dictator_duration)#4
# harvest_video(14,"Alexis_y_Fido",Alexis_y_Fido_url,Alexis_y_Fido_duration)#4
# harvest_video(5,"Yandel_Hasta_Abajo",Yandel_Hasta_Abajo_url,Yandel_Hasta_Abajo_duration)#4
##harvest_video(100,"Alerta_Roja",Alerta_Roja_url,Alerta_Roja_duration)#4ran-- this is too long!! TODO replace!
# harvest_video(26,"Eminem_Sing_For_The_Moment",Eminem_Sing_For_The_Moment_url,Eminem_Sing_For_The_Moment_duration)#4
# harvest_video(25,"Coolio_Gangsters_Paradise",Coolio_Gangsters_Paradise_url,Coolio_Gangsters_Paradise_duration)#4
# harvest_video(1,"_2pac_Changes",_2pac_Changes_url,_2pac_Changes_duration)#4
# harvest_video(4,"Michael_Jackson_Earth_Song",Michael_Jackson_Earth_Song_url,Michael_Jackson_Earth_Song_duration)#4
# harvest_video(1,"Michael_Jackson_Heal_The_World",Michael_Jackson_Heal_The_World_url,Michael_Jackson_Heal_The_World_duration)#4
# harvest_video(4,"Michael_Jackson_They_Dont_Care_About_Us",Michael_Jackson_They_Dont_Care_About_Us_url,Michael_Jackson_They_Dont_Care_About_Us_duration)#4
# harvest_video(9,"J_Alvarez_Junto_Al_Amanecer",J_Alvarez_Junto_Al_Amanecer_url,J_Alvarez_Junto_Al_Amanecer_duration)#4
# harvest_video(8,"Don_Omar_Dutty_Love",Don_Omar_Dutty_Love_url,Don_Omar_Dutty_Love_duration)#4
# harvest_video(3,"Diving_in_Bali",Diving_in_Bali_url,Diving_in_Bali_duration)#4
# harvest_video(99,"Whitney_Houston_When_You_Believe",Whitney_Houston_When_You_Believe_url,Whitney_Houston_When_You_Believe_duration)#4
# harvest_video(100,"Enrique_Iglesias_Bailamos",Enrique_Iglesias_Bailamos_url,Enrique_Iglesias_Bailamos_duration)#4
# harvest_video(55,"Shakira_Whenever",Shakira_Whenever_url,Shakira_Whenever_duration)#4
# harvest_video(28,"Bon_Jovi_Always",Bon_Jovi_Always_url,Bon_Jovi_Always_duration)#4
# harvest_video(100,"CNN",CNN_url,CNN_duration)#4
# harvest_video(70,"Sting_Be_Still",Sting_Be_Still_url,Sting_Be_Still_duration)#4
# harvest_video(16,"Farruko_Obsesionado",Farruko_Obsesionado_url,Farruko_Obsesionado_duration)#4
# harvest_video(33,"GoPro_Snow_Daze",GoPro_Snow_Daze_url,GoPro_Snow_Daze_duration)#4
# harvest_video(100,"Meghan_Trainor_All_About_That_Bass",Meghan_Trainor_All_About_That_Bass_url,Meghan_Trainor_All_About_That_Bass_duration)#4
# harvest_video(84,"Katy_Perry_Birthday",Katy_Perry_Birthday_url,Katy_Perry_Birthday_duration)#4
# harvest_video(13,"Cristiano_Ronaldo",Cristiano_Ronaldo_url,Cristiano_Ronaldo_duration)#4
# harvest_video(62,"Katy_Perry_-_This_Is_How_We_Do",Katy_Perry_This_Is_How_We_Do_url,Katy_Perry_This_Is_How_We_Do_duration)#4
# harvest_video(1,"Nature_Beauty_4K",Nature_Beauty_4K_url,Nature_Beauty_4K_duration)#4
# harvest_video(62,"Pharrell_Williams_Happy",Pharrell_Williams_Happy_url,Pharrell_Williams_Happy_duration)#4
# harvest_video(23,"Friday_-_Rebecca_Black",Friday_Rebecca_Black_url,Friday_Rebecca_Black_duration)#4
# harvest_video(10,"jennifer_lopez_papi",jennifer_lopez_papi_url,jennifer_lopez_papi_duration)#4
# -------------
# harvest_video(15,"Teenage_Mutant_Ninja_Turtles_2",Teenage_Mutant_Ninja_Turtles_2_url,Teenage_Mutant_Ninja_Turtles_2_duration)#4
# harvest_video(36,"The_Hum",The_Hum_url,The_Hum_duration)#4
# harvest_video(36,"bara_bere",bara_bere_url,bara_bere_duration)
# harvest_video(100,"Humilde_Residencia",Humilde_Residencia_url,Humilde_Residencia_duration)
# harvest_video(18,"Lord_Of_The_Lost",Lord_Of_The_Lost_url,Lord_Of_The_Lost_duration)
# harvest_video(49,"La_Bomba",La_Bomba_url,La_Bomba_duration)
# harvest_video(8,"Wo_sind_die_Clowns",Wo_sind_die_Clowns_url,Wo_sind_die_Clowns_duration)
# harvest_video(3,"Hollyweezy",Hollyweezy_url,Hollyweezy_duration)
# harvest_video(8,"Maria",Maria_url,Maria_duration)
# harvest_video(47,"HANGOVER",HANGOVER_url,HANGOVER_duration)
# harvest_video(38,"GUNMAN_STYLE",GUNMAN_STYLE_url,GUNMAN_STYLE_duration)
harvest_video(2, "j_alvarez", j_alvarez_url, j_alvarez_duration)  # 4
# harvest_video(1,"Justin_Bieber",Justin_Bieber_url,Justin_Bieber_duration)#4
# harvest_video(55,"Tired_of_Running",Tired_of_Running_url,Tired_of_Running_duration)#4
# harvest_video(99,"Shakira_Waka_Waka",Shakira_Waka_Waka_url,Shakira_Waka_Waka_duration)#4
# harvest_video(100,"Taylor_Swift_Bad_Blood",Taylor_Swift_Bad_Blood_url,Taylor_Swift_Bad_Blood_duration)#4
# harvest_video(100,"Sia_Chandelier",Sia_Chandelier_url,Sia_Chandelier_duration)#4
# harvest_video(100,"Sevyn_Streeter_Furious_7",Sevyn_Streeter_Furious_7_url,Sevyn_Streeter_Furious_7_duration)#4
# harvest_video(100,"Taylor_Swift_Wildest_Dreams",Taylor_Swift_Wildest_Dreams_url,Taylor_Swift_Wildest_Dreams_duration)
# harvest_video(100,"Dubai_Journey",Dubai_Journey_url,Dubai_Journey_duration)
# harvest_video(100,"Farruko_Hola_Beba",Farruko_Hola_Beba_url,Farruko_Hola_Beba_duration)
# harvest_video(100,"How_Deep_Is_Your_Love",How_Deep_Is_Your_Love_url,How_Deep_Is_Your_Love_duration)
# harvest_video(100,"Ai_Se_Eu_Te_Pego",Ai_Se_Eu_Te_Pego_url,Ai_Se_Eu_Te_Pego_duration)

