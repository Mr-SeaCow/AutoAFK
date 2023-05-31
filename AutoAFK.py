from activities import *
import customtkinter
import threading
import sys
import configparser
import os
from datetime import datetime,timezone

currenttime = datetime.now()
currenttimeutc = datetime.now(timezone.utc)
cwd = (os.path.dirname(__file__) + '\\')
config = configparser.ConfigParser()
config.read('settings.ini')
customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

version = "0.8.6"

#Main Window
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("AutoAFK - v" + version)
        self.geometry(f"{800}x{600}")
        self.wm_iconbitmap(cwd + 'img\\auto.ico')

        # configure grid layout (4x4)
        self.grid_rowconfigure((0, 1, 2), weight=0)
        self.grid_columnconfigure((0, 1, 2), weight=0)

        # Dailies Frame
        self.dailiesFrame = customtkinter.CTkFrame(master=self, height=260, width=180)
        self.dailiesFrame.place(x=10, y=20)
        # Dailies button
        self.dailiesButton = customtkinter.CTkButton(master=self, text="Run Dailies", command=lambda: threading.Thread(target=dailiesButton).start())
        self.dailiesButton.place(x=30, y=35)
        # Arena Battles
        self.arenaLabel = customtkinter.CTkLabel(master=self.dailiesFrame, text='Arena Battles', fg_color=("gray86", "gray17"))
        self.arenaLabel.place(x=10, y=55)
        self.arenaEntry = customtkinter.CTkEntry(master=self.dailiesFrame, height=20, width=30)
        self.arenaEntry.insert('end', config.get('DAILIES', 'arenabattles'))
        self.arenaEntry.place(x=130, y=60)
        # Fast Rewards
        self.fastrewardsLabel = customtkinter.CTkLabel(master=self.dailiesFrame, text='Fast Rewards', fg_color=("gray86", "gray17"))
        self.fastrewardsLabel.place(x=10, y=85)
        self.fastrewardsEntry = customtkinter.CTkEntry(master=self.dailiesFrame, height=20, width=30)
        self.fastrewardsEntry.insert('end', config.get('DAILIES', 'fastrewards'))
        self.fastrewardsEntry.place(x=130, y=90)
        # Shop Refresh
        self.shoprefreshLabel = customtkinter.CTkLabel(master=self.dailiesFrame, text='Shop Refreshes', fg_color=("gray86", "gray17"))
        self.shoprefreshLabel.place(x=10, y=115)
        self.shoprefreshEntry = customtkinter.CTkEntry(master=self.dailiesFrame, height=20, width=30)
        self.shoprefreshEntry.insert('end', config.get('DAILIES', 'shoprefreshes'))
        self.shoprefreshEntry.place(x=130, y=120)
        # # Twisted Realm
        # self.twistedRealmLabel = customtkinter.CTkLabel(master=self.dailiesFrame, text='Twisted Realm?', fg_color=("gray86", "gray17"))
        # self.twistedRealmLabel.place(x=10, y=150)
        # self.twistedRealmCheckbox = customtkinter.CTkCheckBox(master=self.dailiesFrame, text=None, onvalue=True, offvalue=False, command=self.Update)
        # if bool(config.getboolean('DAILIES', 'twistedRealm')):
        #     self.twistedRealmCheckbox.select()
        # self.twistedRealmCheckbox.place(x=130, y=150)
        # # Solo Bounties
        # self.soloBountiesLabel = customtkinter.CTkLabel(master=self.dailiesFrame, text='Dispatch Bounties?', fg_color=("gray86", "gray17"))
        # self.soloBountiesLabel.place(x=10, y=180)
        # self.soloBountiesCheckbox = customtkinter.CTkCheckBox(master=self.dailiesFrame, text=None, onvalue=True, offvalue=False, command=self.Update)
        # if bool(config.getboolean('BOUNTIES', 'dispatchsolo')):
        #     self.soloBountiesCheckbox.select()
        # self.soloBountiesCheckbox.place(x=130, y=180)

        # Activities button
        self.activitiesButton = customtkinter.CTkButton(master=self, text="Select Activities", fg_color=["#3B8ED0", "#1F6AA5"], width=120, command=self.open_activitywindow)
        self.activitiesButton.place(x=40, y=170)
        # Shop button
        self.dailiesShopButton = customtkinter.CTkButton(master=self, text="Shop Options", fg_color=["#3B8ED0", "#1F6AA5"], width=120, command=self.open_shopwindow)
        self.dailiesShopButton.place(x=40, y=207)
        # Advanced button
        self.advancedButton = customtkinter.CTkButton(master=self, text="Advanced", fg_color=["#3B8ED0", "#1F6AA5"], width=120, command=self.open_advancedwindow)
        self.advancedButton.place(x=40, y=244)
        # self.portEntry = customtkinter.CTkEntry(master=self.dailiesFrame, height=20, width=30)
        # self.portEntry.insert('end', config.get('DAILIES', 'shoprefreshes'))
        # self.portEntry.place(x=40, y=250)

        # PvP Frame
        self.arenaFrame = customtkinter.CTkFrame(master=self, height=100, width=180)
        self.arenaFrame.place(x=10, y=290)

        # PvP button
        self.arenaButton = customtkinter.CTkButton(master=self.arenaFrame, text="Run PvP Tickets", command=lambda: threading.Thread(target=ticketBurn).start())
        self.arenaButton.place(x=20, y=15)
        # PvP Entry
        self.pvpLabel = customtkinter.CTkLabel(master=self.arenaFrame, text='How many battles', fg_color=("gray86", "gray17"))
        self.pvpLabel.place(x=10, y=60)
        self.pvpEntry = customtkinter.CTkEntry(master=self.arenaFrame, height=20, width=40)
        self.pvpEntry.insert('end', config.get('ARENA', 'arenabattles'))
        self.pvpEntry.place(x=130, y=60)

        # Push Frame
        self.pushFrame = customtkinter.CTkFrame(master=self, height=180, width=180)
        self.pushFrame.place(x=10, y=400)

        # Push Button
        self.pushButton = customtkinter.CTkButton(master=self.pushFrame, text="Auto Push", command=lambda: threading.Thread(target=push).start())
        self.pushButton.place(x=20, y=15)
        # Push Entry
        self.pushLabel = customtkinter.CTkLabel(master=self.pushFrame, text='Where to push?', fg_color=("gray86", "gray17"))
        self.pushLabel.place(x=10, y=50)
        self.pushLocationDropdown = customtkinter.CTkComboBox(master=self.pushFrame,  values=["Campaign"], width=160)
        self.pushLocationDropdown.place(x=10, y=80)
        # Push Formation
        self.pushLabel = customtkinter.CTkLabel(master=self.pushFrame, text='Which formation?', fg_color=("gray86", "gray17"))
        self.pushLabel.place(x=10, y=110)
        self.pushFormationDropdown = customtkinter.CTkComboBox(master=self.pushFrame, values=["1st", "2nd", "3rd", "4th", "5th"], width=80)
        self.pushFormationDropdown.set(config.get('PUSH', 'formation'))
        self.pushFormationDropdown.place(x=10, y=140)
        # Push Duration
        # self.pushLabel = customtkinter.CTkLabel(master=self.pushFrame, text='Check for Victory every:', fg_color=("gray86", "gray17"))
        # self.pushLabel.place(x=10, y=150)
        # self.pushDurationDropdown = customtkinter.CTkEntry(master=self.pushFrame, width=50)
        # self.pushDurationDropdown.insert('end', config.get('PUSH', 'victoryCheck'))
        # self.pushDurationDropdown.place(x=120, y=150)
        # Quit button
        # self.quitButton = customtkinter.CTkButton(master=self, text="Quit", fg_color=["#1111FF", "#1F6AFF"], command=lambda: threading.Thread(target=abortAllTasks).start())
        # self.quitButton.place(x=10, y=650)

        # Textbox Frame
        self.textbox = customtkinter.CTkTextbox(master=self, width=580, height=560)
        self.textbox.place(x=200, y=20)
        self.textbox.configure(text_color='white', font=('Arial', 14))
        self.textbox.tag_config("error", foreground="red")
        self.textbox.tag_config('warning', foreground='yellow')
        self.textbox.tag_config('green', foreground='lawngreen')
        self.textbox.tag_config('blue', foreground='cyan')
        self.textbox.insert('end', 'Welcome to AutoAFK!\n')
        self.textbox.insert('end', 'The tool is still in Beta so bugs and stability are being worked on, if you find any please report on Github or Discord (Jc#4631)\n\n')
        sys.stdout = STDOutRedirector(self.textbox)

        # Configure windows so we can reference them
        self.shop_window = None
        self.activity_window = None
        self.advanced_window = None

    def Update(self):
        if self.twistedRealmCheckbox.get() == 1:
            config.set('DAILIES', 'twistedRealm', 'True')
        else:
            config.set('DAILIES', 'twistedRealm', 'False')

        with open('settings.ini', 'w') as configfile:
            config.write(configfile)

    def open_advancedwindow(self):
        if self.advanced_window is None or not self.advanced_window.winfo_exists():
            self.advanced_window = advancedWindow(self)  # create window if its None or destroyed
            self.advanced_window.focus()
        else:
            self.advanced_window.focus()  # if window exists focus it

    def open_shopwindow(self):
        if self.shop_window is None or not self.shop_window.winfo_exists():
            self.shop_window = shopWindow(self)  # create window if its None or destroyed
            self.shop_window.focus()
        else:
            self.shop_window.focus()  # if window exists focus it

    def open_activitywindow(self):
        if self.activity_window is None or not self.activity_window.winfo_exists():
            self.activity_window = activityWindow(self)  # create window if its None or destroyed
            self.activity_window.focus()
        else:
            self.activity_window.focus()  # if window exists focus it

# Shop Window
class activityWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("250x600")
        self.title('Activity Selection')
        self.attributes("-topmost", True)

        # Activity Frame
        self.activityFrame = customtkinter.CTkFrame(master=self, width=235, height=580)
        self.activityFrame.place(x=10, y=10)
        self.label = customtkinter.CTkLabel(master=self.activityFrame, text="Activities:", font=("Arial", 15, 'bold'))
        self.label.place(x=20, y=5)

        # AFK Rewards Collect
        self.collectRewardsLabel = customtkinter.CTkLabel(master=self.activityFrame, text='Collect AFK Rewards 2x', fg_color=("gray86", "gray17"))
        self.collectRewardsLabel.place(x=10, y=40)
        self.collectRewardsCheckbox = customtkinter.CTkCheckBox(master=self.activityFrame, text=None, onvalue=True, offvalue=False, command=self.activityUpdate)
        self.collectRewardsCheckbox.place(x=200, y=40)
        # Mail Collect
        self.collectMailLabel = customtkinter.CTkLabel(master=self.activityFrame, text='Collect Mail', fg_color=("gray86", "gray17"))
        self.collectMailLabel.place(x=10, y=70)
        self.collectMailCheckbox = customtkinter.CTkCheckBox(master=self.activityFrame, text=None, onvalue=True, offvalue=False, command=self.activityUpdate)
        self.collectMailCheckbox.place(x=200, y=70)
        # Companion Points Collect
        self.companionPointsLabel = customtkinter.CTkLabel(master=self.activityFrame, text='Send/Receive Companion Points', fg_color=("gray86", "gray17"))
        self.companionPointsLabel.place(x=10, y=100)
        self.companionPointsCheckbox = customtkinter.CTkCheckBox(master=self.activityFrame, text=None, onvalue=True, offvalue=False, command=self.activityUpdate)
        self.companionPointsCheckbox.place(x=200, y=100)
        # Send Mercs
        self.lendMercsLabel = customtkinter.CTkLabel(master=self.activityFrame, text='Auto lend mercs?', fg_color=("gray86", "gray17"))
        self.lendMercsLabel.place(x=40, y=130)
        self.lendMercsCheckbox = customtkinter.CTkCheckBox(master=self.activityFrame, text=None, onvalue=True, offvalue=False, command=self.activityUpdate)
        self.lendMercsCheckbox.place(x=200, y=130)
        # Fast Rewards
        # self.fastRewardsLabel = customtkinter.CTkLabel(master=self.activityFrame, text='Fast Rewards', fg_color=("gray86", "gray17"))
        # self.fastRewardsLabel.place(x=10, y=160)
        # self.fastrewardsEntry = customtkinter.CTkEntry(master=self.activityFrame, height=20, width=25)
        # self.fastrewardsEntry.insert('end', config.get('DAILIES', 'fastrewards'))
        # self.fastrewardsEntry.place(x=200, y=160)
        # Attempt Campaign battle
        self.attemptCampaignLabel = customtkinter.CTkLabel(master=self.activityFrame, text='Attempt Campaign', fg_color=("gray86", "gray17"))
        self.attemptCampaignLabel.place(x=10, y=190)
        self.attemptCampaignCheckbox = customtkinter.CTkCheckBox(master=self.activityFrame, text=None, onvalue=True, offvalue=False, command=self.activityUpdate)
        self.attemptCampaignCheckbox.place(x=200, y=190)
        # Handle Team Bounties
        self.teamBountiesLabel = customtkinter.CTkLabel(master=self.activityFrame, text='Dispatch Team Bounties', fg_color=("gray86", "gray17"))
        self.teamBountiesLabel.place(x=10, y=220)
        self.teamBountiesCheckbox = customtkinter.CTkCheckBox(master=self.activityFrame, text=None, onvalue=True, offvalue=False, command=self.activityUpdate)
        self.teamBountiesCheckbox.place(x=200, y=220)
        # Handle Solo Bounties
        self.soloBountiesLabel = customtkinter.CTkLabel(master=self.activityFrame, text='Dispatch Solo Bounties', fg_color=("gray86", "gray17"))
        self.soloBountiesLabel.place(x=40, y=250)
        self.soloBountiesCheckbox = customtkinter.CTkCheckBox(master=self.activityFrame, text=None, onvalue=True, offvalue=False, command=self.activityUpdate)
        self.soloBountiesCheckbox.place(x=200, y=250)
        # Arena Battles
        # self.arenaBattleLabel = customtkinter.CTkLabel(master=self.activityFrame, text='Arena Battles', fg_color=("gray86", "gray17"))
        # self.arenaBattleLabel.place(x=10, y=280)
        # self.arenaBattleEntry = customtkinter.CTkEntry(master=self.activityFrame, height=20, width=30)
        # self.arenaBattleEntry.insert('end', config.get('DAILIES', 'arenabattles'))
        # self.arenaBattleEntry.place(x=200, y=280)
        # Collect Gladiator Coins
        self.gladiatorCollectLabel = customtkinter.CTkLabel(master=self.activityFrame, text='Collect Gladiator Coins', fg_color=("gray86", "gray17"))
        self.gladiatorCollectLabel.place(x=10, y=310)
        self.gladiatorCollectCheckbox = customtkinter.CTkCheckBox(master=self.activityFrame, text=None, onvalue=True, offvalue=False, command=self.activityUpdate)
        self.gladiatorCollectCheckbox.place(x=200, y=310)
        # Fountain of Time
        self.fountainOfTimeLabel = customtkinter.CTkLabel(master=self.activityFrame, text='Collect Fountain of Time', fg_color=("gray86", "gray17"))
        self.fountainOfTimeLabel.place(x=10, y=340)
        self.fountainOfTimeCheckbox = customtkinter.CTkCheckBox(master=self.activityFrame, text=None, onvalue=True, offvalue=False, command=self.activityUpdate)
        self.fountainOfTimeCheckbox.place(x=200, y=340)
        # Kings Tower
        self.kingsTowerLabel = customtkinter.CTkLabel(master=self.activityFrame, text='Attempt King\'s Tower', fg_color=("gray86", "gray17"))
        self.kingsTowerLabel.place(x=10, y=370)
        self.kingsTowerCheckbox = customtkinter.CTkCheckBox(master=self.activityFrame, text=None, onvalue=True, offvalue=False, command=self.activityUpdate)
        self.kingsTowerCheckbox.place(x=200, y=370)
        # Collect Inn gifts
        self.collectInnLabel = customtkinter.CTkLabel(master=self.activityFrame, text='Collect Inn Gifts', fg_color=("gray86", "gray17"))
        self.collectInnLabel.place(x=10, y=400)
        self.collectInnCheckbox = customtkinter.CTkCheckBox(master=self.activityFrame, text=None, onvalue=True, offvalue=False, command=self.activityUpdate)
        self.collectInnCheckbox.place(x=200, y=400)
        # Battle Guild Hunts
        self.guildHuntLabel = customtkinter.CTkLabel(master=self.activityFrame, text='Battle Guild Hunts', fg_color=("gray86", "gray17"))
        self.guildHuntLabel.place(x=10, y=430)
        self.guildHuntCheckbox = customtkinter.CTkCheckBox(master=self.activityFrame, text=None, onvalue=True, offvalue=False, command=self.activityUpdate)
        self.guildHuntCheckbox.place(x=200, y=430)
        # Store Purchases
        self.storePurchasesLabel = customtkinter.CTkLabel(master=self.activityFrame, text='Make Store Purchases', fg_color=("gray86", "gray17"))
        self.storePurchasesLabel.place(x=10, y=460)
        self.storePurchasesCheckbox = customtkinter.CTkCheckBox(master=self.activityFrame, text=None, onvalue=True, offvalue=False, command=self.activityUpdate)
        self.storePurchasesCheckbox.place(x=200, y=460)
        # Twisted Realm
        self.twistedRealmLabel = customtkinter.CTkLabel(master=self.activityFrame, text='Attempt Twisted Realm', fg_color=("gray86", "gray17"))
        self.twistedRealmLabel.place(x=10, y=490)
        self.twistedRealmCheckbox = customtkinter.CTkCheckBox(master=self.activityFrame, text=None, onvalue=True, offvalue=False, command=self.activityUpdate)
        self.twistedRealmCheckbox.place(x=200, y=490)
        # Collect Quests
        self.collectQuestsLabel = customtkinter.CTkLabel(master=self.activityFrame, text='Collect Daily/Weekly Quests', fg_color=("gray86", "gray17"))
        self.collectQuestsLabel.place(x=10, y=520)
        self.collectQuestsCheckbox = customtkinter.CTkCheckBox(master=self.activityFrame, text=None, onvalue=True, offvalue=False, command=self.activityUpdate)
        self.collectQuestsCheckbox.place(x=200, y=520)
        # Collect Free Merchant Deals
        self.collectMerchantsLabel = customtkinter.CTkLabel(master=self.activityFrame, text='Collect Merchant Deals/Nobles', fg_color=("gray86", "gray17"))
        self.collectMerchantsLabel.place(x=10, y=550)
        self.collectMerchantsCheckbox = customtkinter.CTkCheckBox(master=self.activityFrame, text=None, onvalue=True, offvalue=False, command=self.activityUpdate)
        self.collectMerchantsCheckbox.place(x=200, y=550)

        activityBoxes = ['collectRewards', 'collectMail', 'companionPoints', 'lendMercs', 'attemptCampaign', 'teamBounties', 'soloBounties',
                      'gladiatorCollect', 'fountainOfTime', 'kingsTower', 'collectInn', 'guildHunt', 'storePurchases', 'twistedRealm',
                         'collectQuests', 'collectMerchants']
        for activity in activityBoxes:
            if config.getboolean('DAILIES', activity):
                self.__getattribute__(activity+'Checkbox').select()

    def activityUpdate(self):
        activityBoxes = ['collectRewards', 'collectMail', 'companionPoints', 'lendMercs', 'attemptCampaign', 'teamBounties', 'soloBounties',
                      'gladiatorCollect', 'fountainOfTime', 'kingsTower', 'collectInn', 'guildHunt', 'storePurchases', 'twistedRealm',
                         'collectQuests', 'collectMerchants']
        for activity in activityBoxes:
            if self.__getattribute__(activity + 'Checkbox').get() == 1:
                config.set('DAILIES', activity, 'True')
            else:
                config.set('DAILIES', activity, 'False')
        with open('settings.ini', 'w') as configfile:
            config.write(configfile)


# Shop Window
class shopWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("200x400")
        self.title('Shop Options')
        self.attributes("-topmost", True)

        # Shop Frame
        self.shopFrame = customtkinter.CTkFrame(master=self, width=180, height=380)
        self.shopFrame.place(x=10, y=10)
        self.label = customtkinter.CTkLabel(master=self.shopFrame, text="Shop Purchases:", font=("Arial", 15, 'bold'))
        self.label.place(x=20, y=5)
        # Dim Frame
        self.dimFrame = customtkinter.CTkFrame(master=self, width=180, height=380)
        self.dimFrame.place(x=210, y=10)
        self.label = customtkinter.CTkLabel(master=self.dimFrame, text="Dim Gear:", font=("Arial", 15, 'bold'))
        self.label.place(x=20, y=5)


        # Shards
        self.shardsLabel = customtkinter.CTkLabel(master=self.shopFrame, text='Shards', fg_color=("gray86", "gray17"))
        self.shardsLabel.place(x=10, y=40)
        self.shardsCheckbox = customtkinter.CTkCheckBox(master=self.shopFrame, text=None, onvalue=True, offvalue=False, command=self.shopUpdate)
        self.shardsCheckbox.place(x=130, y=40)
        # Cores
        self.coresLabel = customtkinter.CTkLabel(master=self.shopFrame, text='Cores', fg_color=("gray86", "gray17"))
        self.coresLabel.place(x=10, y=70)
        self.coresCheckbox = customtkinter.CTkCheckBox(master=self.shopFrame, text=None, onvalue=True, offvalue=False, command=self.shopUpdate)
        self.coresCheckbox.place(x=130, y=70)
        # Timegazer
        self.timegazerLabel = customtkinter.CTkLabel(master=self.shopFrame, text='Timegazer Card', fg_color=("gray86", "gray17"))
        self.timegazerLabel.place(x=10, y=100)
        self.timegazerCheckbox = customtkinter.CTkCheckBox(master=self.shopFrame, text=None, onvalue=True, offvalue=False, command=self.shopUpdate)
        self.timegazerCheckbox.place(x=130, y=100)
        # Bait
        self.baitsLabel = customtkinter.CTkLabel(master=self.shopFrame, text='Baits', fg_color=("gray86", "gray17"))
        self.baitsLabel.place(x=10, y=130)
        self.baitsCheckbox = customtkinter.CTkCheckBox(master=self.shopFrame, text=None, onvalue=True, offvalue=False, command=self.shopUpdate)
        self.baitsCheckbox.place(x=130, y=130)
        # Dust Gold
        self.dust_goldLabel = customtkinter.CTkLabel(master=self.shopFrame, text='Dust (gold)', fg_color=("gray86", "gray17"))
        self.dust_goldLabel.place(x=10, y=160)
        self.dust_goldCheckbox = customtkinter.CTkCheckBox(master=self.shopFrame, text=None, onvalue=True, offvalue=False, command=self.shopUpdate)
        self.dust_goldCheckbox.place(x=130, y=160)
        # Dust Diamonds
        self.dust_diamondLabel = customtkinter.CTkLabel(master=self.shopFrame, text='Dust (diamonds)', fg_color=("gray86", "gray17"))
        self.dust_diamondLabel.place(x=10, y=190)
        self.dust_diamondCheckbox = customtkinter.CTkCheckBox(master=self.shopFrame, text=None, onvalue=True, offvalue=False, command=self.shopUpdate)
        self.dust_diamondCheckbox.place(x=130, y=190)
        # Elite Soulstone
        self.elite_soulstoneLabel = customtkinter.CTkLabel(master=self.shopFrame, text='Elite Soulstone', fg_color=("gray86", "gray17"))
        self.elite_soulstoneLabel.place(x=10, y=220)
        self.elite_soulstoneCheckbox = customtkinter.CTkCheckBox(master=self.shopFrame, text=None, onvalue=True, offvalue=False, command=self.shopUpdate)
        self.elite_soulstoneCheckbox.place(x=130, y=220)
        # Elite Soulstone
        self.superb_soulstoneLabel = customtkinter.CTkLabel(master=self.shopFrame, text='Superb Soulstone', fg_color=("gray86", "gray17"))
        self.superb_soulstoneLabel.place(x=10, y=250)
        self.superb_soulstoneCheckbox = customtkinter.CTkCheckBox(master=self.shopFrame, text=None, onvalue=True, offvalue=False, command=self.shopUpdate)
        self.superb_soulstoneCheckbox.place(x=130, y=250)
        # Silver Emblems
        self.silver_emblemLabel = customtkinter.CTkLabel(master=self.shopFrame, text='Silver Emblems', fg_color=("gray86", "gray17"))
        self.silver_emblemLabel.place(x=10, y=280)
        self.silver_emblemCheckbox = customtkinter.CTkCheckBox(master=self.shopFrame, text=None, onvalue=True, offvalue=False, command=self.shopUpdate)
        self.silver_emblemCheckbox.place(x=130, y=280)
        # Gold Emblems
        self.gold_emblemLabel = customtkinter.CTkLabel(master=self.shopFrame, text='Gold Emblems', fg_color=("gray86", "gray17"))
        self.gold_emblemLabel.place(x=10, y=310)
        self.gold_emblemCheckbox = customtkinter.CTkCheckBox(master=self.shopFrame, text=None, onvalue=True, offvalue=False, command=self.shopUpdate)
        self.gold_emblemCheckbox.place(x=130, y=310)
        # PoE
        self.poeLabel = customtkinter.CTkLabel(master=self.shopFrame, text='PoE (gold)', fg_color=("gray86", "gray17"))
        self.poeLabel.place(x=10, y=340)
        self.poeCheckbox = customtkinter.CTkCheckBox(master=self.shopFrame, text=None, onvalue=True, offvalue=False, command=self.shopUpdate)
        self.poeCheckbox.place(x=130, y=340)

        checkboxes = ['shards', 'cores', 'timegazer', 'baits', 'dust_gold', 'dust_diamond', 'elite_soulstone',
                      'superb_soulstone', 'silver_emblem', 'gold_emblem', 'poe']
        for box in checkboxes:
            if config.getboolean('SHOP', box):
                self.__getattribute__(box+'Checkbox').select()

    def shopUpdate(self):
        checkboxes = ['shards', 'cores', 'timegazer', 'baits', 'dust_gold', 'dust_diamond', 'elite_soulstone',
                      'superb_soulstone', 'silver_emblem', 'gold_emblem', 'poe']
        for box in checkboxes:
            if self.__getattribute__(box+'Checkbox').get() == 1:
                config.set('SHOP', box, 'True')
            else:
                config.set('SHOP', box, 'False')
        with open('settings.ini', 'w') as configfile:
            config.write(configfile)

class advancedWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("200x200")
        self.title('Advanced Options')
        self.attributes("-topmost", True)

        # Activity Frame
        self.advancedFrame = customtkinter.CTkFrame(master=self, width=180, height=180)
        self.advancedFrame.place(x=10, y=10)
        self.label = customtkinter.CTkLabel(master=self.advancedFrame, text="Advanced Options:", font=("Arial", 15, 'bold'))
        self.label.place(x=20, y=5)

        # Port Entry
        self.portLabel = customtkinter.CTkLabel(master=self.advancedFrame, text='Port:', fg_color=("gray86", "gray17"))
        self.portLabel.place(x=10, y=40)
        self.portEntry = customtkinter.CTkEntry(master=self.advancedFrame, height=25, width=60)
        self.portEntry.insert('end', config.get('ADVANCED', 'port'))
        self.portEntry.place(x=50, y=40)

        # Save button
        self.advanceSaveButton = customtkinter.CTkButton(master=self.advancedFrame, text="Save", fg_color=["#3B8ED0", "#1F6AA5"], width=120, command=self.advancedSave)
        self.advanceSaveButton.place(x=30, y=140)

    def advancedSave(self):
        if self.portEntry.get() != config.get('ADVANCED', 'port'):
            config.set('ADVANCED', 'port', self.portEntry.get())

        with open('settings.ini', 'w') as configfile:
            config.write(configfile)
        config.read('settings.ini')  # to load the new value into memory

# Will change the dropdown to only include open towers
# May cause issues with timezones..
def setUlockedTowers():
    days = {1:["Campaign", "King's Tower", "Lightbringer"],
    2:["Campaign", "King's Tower", "Mauler Tower"],
    3:["Campaign", "King's Tower", "Wilder Tower", "Celestial Tower"],
    4:["Campaign", "King's Tower", "Graveborn Tower", "Hypogean Tower"],
    5:["Campaign", "King's Tower", "Lightbringer Tower", "Mauler Tower", "Celestial Tower"],
    6:["Campaign", "King's Tower", "Wilder Tower", "Graveborn Tower", "Hypogean Tower"],
    7:["Campaign", "King's Tower", "Lightbringer Tower", "Wilder Tower", "Mauler Tower", "Graveborn Tower", "Hypogean Tower", "Celestial Tower"]}
    for day, towers in days.items():
        if currenttimeutc.isoweekday() == day:
            app.pushLocationDropdown.configure(values=towers)

def abortAllTasks():
    for thread in threading.enumerate():
        if thread.name != 'MainThread':
            print(thread.name)
            thread.join()

def buttonState(state):
    app.dailiesButton.configure(state=state)
    app.arenaButton.configure(state=state)
    app.pushButton.configure(state=state)

def ticketBurn():
    if app.pvpEntry.get() != config.get('ARENA', 'arenabattles'):
        config.set('ARENA', 'arenabattles', app.pvpEntry.get())

    with open('settings.ini', 'w') as configfile:
        config.write(configfile)

    buttonState('disabled')
    connect_device()
    # TS_Battle_Stastistics()
    handleArenaOfHeroes(config.getint('ARENA', 'arenabattles'))
    buttonState('normal')
    print('')
    return

def dailiesButton():
    if app.arenaEntry.get() != config.get('DAILIES', 'arenabattles'):
        config.set('DAILIES', 'arenabattles', app.arenaEntry.get())
    if app.fastrewardsEntry.get() != config.get('DAILIES', 'fastrewards'):
        config.set('DAILIES', 'fastrewards', app.fastrewardsEntry.get())
    if app.shoprefreshEntry.get() != config.get('DAILIES', 'shoprefreshes'):
        config.set('DAILIES', 'shoprefreshes', app.shoprefreshEntry.get())

    with open(cwd + 'settings.ini', 'w') as configfile:
        config.write(configfile)

    buttonState('disabled')
    dailies()
    print('')
    buttonState('normal')
    return

def dailies():
    connect_device()
    if bool(config.getboolean('DAILIES', 'collectrewards')) is True:
        collectAFKRewards()
    if bool(config.getboolean('DAILIES', 'collectmail')) is True:
        collectMail()
    if bool(config.getboolean('DAILIES', 'companionpoints')) is True:
        collectCompanionPoints(mercs=bool(config.getboolean('DAILIES', 'lendmercs')))
    if (int(app.fastrewardsEntry.get()) > 0):
        collectFastRewards(int(app.fastrewardsEntry.get()))
    if bool(config.getboolean('DAILIES', 'attemptcampaign')) is True:
        attemptCampaign()
    if bool(config.getboolean('DAILIES', 'teambounties')) is True:
        handleBounties()
    if (int(app.pvpEntry.get()) > 0):
        handleArenaOfHeroes(int(app.arenaEntry.get()))
    if bool(config.getboolean('DAILIES', 'gladiatorcollect')) is True:
        collectGladiatorCoins()
    if bool(config.getboolean('DAILIES', 'fountainoftime')) is True:
        collectFountainOfTime()
    if bool(config.getboolean('DAILIES', 'kingstower')) is True:
        handleKingsTower()
    if bool(config.getboolean('DAILIES', 'collectinn')) is True:
        collectInnGifts()
    if bool(config.getboolean('DAILIES', 'guildhunt')) is True:
        handleGuildHunts()
    shopPurchases(int(app.shoprefreshEntry.get()))
    if bool(config.getboolean('DAILIES', 'twistedrealm')) is True:
        handleTwistedRealm()
    if bool(config.getboolean('DAILIES', 'collectquests')) is True:
        collectQuests()
    if bool(config.getboolean('DAILIES', 'collectmerchants')) is True:
        clearMerchant()
    printGreen('\nDailies done!')
    return

def push():
    if app.pushFormationDropdown.get() != config.get('PUSH', 'formation'):
        config.set('PUSH', 'formation', app.pushFormationDropdown.get())

    with open(cwd + 'settings.ini', 'w') as configfile:
        config.write(configfile)

    connect_device()
    buttonState('disabled')
    formationstr = str(config.get('PUSH', 'formation'))[0:1]

    if app.pushLocationDropdown.get() == 'Campaign':
        printBlue('Auto-Pushing Campaign using the ' + str(config.get('PUSH', 'formation') + ' formation'))
        while 1:
            pushCampaign(formation=int(formationstr), duration=int(config.get('PUSH', 'victoryCheck')))
    else:
        printBlue('Auto-Pushing Tower using using the ' + str(config.get('PUSH', 'formation') + ' formation'))
        openTower(app.pushLocationDropdown.get())
        while 1:
            pushTower(formation=int(formationstr), duration=int(config.get('PUSH', 'victoryCheck')))

class IORedirector(object):
    def __init__(self, text_widget):
        self.text_space = text_widget

class STDOutRedirector(IORedirector):
    def write(self, string):
        timestamp = '[' + datetime.now().strftime("%H:%M:%S") + '] '
        # Very hacky implementation, we scan first 3 characters for colour tag, if found we apply the textbox tag
        # and print the string minus the first 3 characters
        entry = string[0:3]
        if entry == 'ERR':
            self.text_space.insert('end', timestamp + string[3:], 'error')
        elif entry == 'WAR':
            self.text_space.insert('end', timestamp + string[3:], 'warning')
        elif entry == 'GRE':
            self.text_space.insert('end', timestamp + string[3:], 'green')
        elif entry == 'BLU':
            self.text_space.insert('end', timestamp + string[3:], 'blue')
        else:
            self.text_space.insert('end', string)
        self.text_space.see('end')
    def flush(self):
        sys.stdout.flush()

if __name__ == "__main__":
    app = App()
    setUlockedTowers()
    app.mainloop()

# Coloured text for the console
def printError(text):
    print('ERR' + text)

def printGreen(text):
    print('GRE' + text)

def printWarning(text):
    print('WAR' + text)

def printBlue(text):
    print('BLU' + text)