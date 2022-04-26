#libraries: er zou een bestaan om met IP-adressen te werken, nog niet getest
from IPy import IP

#sprint 1
#class voor conversie van IP-formaat
class IP_Adres:
  def __init__(self):
    self._decimaal = 0

  def set_dotted(self, ip_adres):
    ip_adres_split = ip_adres.split(".")
    txt = "{:08b}{:08b}{:08b}{:08b}"
    ip_adres_bin = txt.format(int(ip_adres_split[0]),
      int(ip_adres_split[1]),
      int(ip_adres_split[2]),
      int(ip_adres_split[3]))
    ip_adres_dec = int(ip_adres_bin, 2)
    self._decimaal = ip_adres_dec
  
  def get_dotted(self):
    # van decimaal naar binair
    txt = "{:032b}"
    ip_adres_bin = txt.format(self._decimaal)
    # 4 groepjes 8 bit uit binair
    groep_1 = ip_adres_bin[0:8]
    groep_2 = ip_adres_bin[8:16]
    groep_3 = ip_adres_bin[16:24]
    groep_4 = ip_adres_bin[24:32]
    # binair -> decimaal per groep, scheiden door een punt
    txt = "{}.{}.{}.{}"
    ip_adres = txt.format(int(groep_1, 2),
      int(groep_2, 2),
      int(groep_3, 2), 
      int(groep_4, 2))
    return ip_adres
  
  def set_decimal(self, decimaal):
    self._decimaal = decimaal
    
  def get_decimal(self):
    return self._decimaal

#input

# > netwerkadres
print('Voer een netwerkadres in: ')
NETADR = input()
#geldigheid testen met IPy; exception indien ongeldig
IP(NETADR)

# > aantal lokalen
print('Voer het aantal lokalen in: ')
LOKALEN = int(input())

# berekeningen

#subnetmask berekenen
sub_mask = LOKALEN * 32
sub_mask = "255.255.255.sub_mask"

# > netwerkadres omzetten naar decimaal/binair
netadr_dec = ip_adres.set_decimal(NETADR)

# > basisadres

# > aantal benodigde hosts

# >> 1 (server) + 1 (router) + aantal lokalen * (20 (hosts) + 1 (switch) + 1 (access point)) + 1 backbone switch indien >4 lokalen
# > subnet mask

# ip-adressen toewijzen

# > 1: router
# > 2: backbone switch
# > 3: server
# > 4: switches
# > 5: access points
# > 6: hosts

# output

# > ip-adres per device
# > range voor de hosts
# > subnet mask
# > default gateway
