from selfwalking.gameinterface import minecraftinterface

mci = minecraftinterface.Win10MinecraftApp()
for x in range(0, 1000):
    keys = mci.get_keys()
    print(keys)

