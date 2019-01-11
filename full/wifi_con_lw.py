import network
sta_if = network.WLAN(network.STA_IF); sta_if.active(True)
sta_if.connect("LW Access Point", "!LW!AP+wireless2012")