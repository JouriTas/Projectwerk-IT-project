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
    return ip_adres_dec
  
  def get_dotted(self, ip_adres_dec):
    # van decimaal naar binair
    txt = "{:032b}"
    ip_adres_bin = txt.format(ip_adres_dec)
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
    
#basisadres berekenen obv IP & subnetmask
def network(ip, mask):

    network = ''

    iOctets = ip.split('.')
    mOctets = mask.split('.')

    network = str( int( iOctets[0] ) & int(mOctets[0] ) ) + '.'
    network += str( int( iOctets[1] ) & int(mOctets[1] ) ) + '.'
    network += str( int( iOctets[2] ) & int(mOctets[2] ) ) + '.'
    network += str( int( iOctets[3] ) & int(mOctets[3] ) )

    return network

# berekenen van de subnets
def bereken_subnets(nw_dec):
  subnets = [nw_dec]
  for i in range(LOKALEN):
    subnets.append(nw_dec + 64 * i+1)
  return subnets

#subnetmask ifv aantal adressen
sn_masks_ip = {
    32 : "255.255.255.224",
    64 : "255.255.255.192",
    128 : "255.255.255.128",
    256 : "255.255.255.0"
}

#input

# > netwerkadres
print('Voer een netwerkadres in: ')
NETADR = raw_input()
#test zonder input te vragen
#NETADR = "192.168.0.1"
#geldigheid testen

# > aantal lokalen
print('Voer het aantal lokalen in: ')
LOKALEN = int(raw_input())
#test zonder input te vragen
#LOKALEN = 1

# berekeningen

#subnetmask berekenen
if LOKALEN == 1:
    sn_mask = sn_masks_ip[32]
elif LOKALEN == 2:
    sn_mask = sn_masks_ip[64]
elif LOKALEN in range(2, 5):
    sn_mask = sn_masks_ip[128]
else:
    sn_mask = sn_masks_ip[256]

# > netwerkadres omzetten naar decimaal
netadr_dec = IP_Adres().set_dotted(NETADR)

# > basisadres
basisadres = network(NETADR, sn_mask)

# > aantal benodigde hosts
hosts = LOKALEN * 20

# >> 1 (server) + 1 (router) + aantal lokalen * (20 (hosts) + 1 (switch) + 1 (access point)) + 1 backbone switch indien >4 lokalen
# > subnets berekenen
subnets = bereken_subnets(netadr_dec)

# ip-adressen toewijzen

# > 1: router
router_ip = IP_Adres().get_dotted(subnets[0] + 1)
# > 2: backbone switch
bb_switch_ip = IP_Adres().get_dotted(subnets[0] + 2)
# > 3: server
server_ip = IP_Adres().get_dotted(subnets[0] + 3)
# > 4: switch lokaal 1
switch1_ip = IP_Adres().get_dotted(subnets[0] + 4)
# > 5: access point lokaal 1
ap1_ip = IP_Adres().get_dotted(subnets[0] + 5)
# > 6: hosts lokaal 1
hosts1_ip = {}
for i in range(hosts):
    hosts1_ip["host{0}".format(i)] = IP_Adres().get_dotted(subnets[0] + 6 + i)

# > ip-adres per netwerkdevices
nwd_ip = {
    "Router" : router_ip,
    "Backbone switch" : bb_switch_ip,
    "Server" : server_ip,
    "Switch 1": switch1_ip,
    "Access Point 1": ap1_ip
}

#ip-adressen lokaal 2
#for i in LOKALEN
#    nwd_ip["Switch 2"] : IP_Adres().get_dotted(subnets[1] + 1)
#    nwd_ip["Access Point 2"] : IP_Adres().get_dotted(subnets[1] + 2)
#    for i in range(hosts):
#        hosts2_ip["host{0}".format(i)] = IP_Adres().get_dotted(subnets[0] + 3 + i)      

# output

# > range voor de hosts
# > subnet mask
# > default gateway

# prints voor tests
print("IP-adressen netwerkdevices: ", nwd_ip)
print("IP-adressen hosts lokaal 1: ", hosts1_ip)
print("Het subnetmask is: ", sn_mask)
print("De default gateway is: ", nwd_ip["Router"])