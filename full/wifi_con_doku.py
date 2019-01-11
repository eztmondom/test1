import network
sta_if = network.WLAN(network.STA_IF); sta_if.active(True)
sta_if.connect("TP-LINK_Docu_Team", "dokuwifi1234")