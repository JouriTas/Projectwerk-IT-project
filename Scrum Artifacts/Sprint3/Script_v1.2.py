#sprint 3

#uitgezet wegens foutmelding - William
#from distutils.command.config import config
#import re

# nodig voor yaml
# installatie (CLI): pip3 install ruamel.yaml
import sys
import ruamel.yaml
from ruamel.yaml import YAML

# nodig voor html
# installatie (CLI): pip3 install pandas
import pandas as pd

# nodig voor inputcontrole
# installatie: pip3 install regex
import re

def set_dotted(ip_adres):
    ip_adres_split = ip_adres.split(".")
    txt = "{:08b}{:08b}{:08b}{:08b}"
    ip_adres_bin = txt.format(int(ip_adres_split[0]),
      int(ip_adres_split[1]),
      int(ip_adres_split[2]),
      int(ip_adres_split[3]))
    ip_adres_dec = int(ip_adres_bin, 2)
    return ip_adres_dec
  
def get_dotted(ip_adres_dec):
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
    j = i + 1
    subnets.append(nw_dec + 64 * j)
  return subnets
  
# ip-adres valideren
def validate_ip_address(address):
    match = re.match(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", address)

    if bool(match) is False:
        return False

    return True 

#subnetmask ifv aantal adressen
sn_masks_ip = {
    32 : "255.255.255.224",
    64 : "255.255.255.192",
    128 : "255.255.255.128",
    256 : "255.255.255.0"
}

#input

# > netwerkadres

NETADR = 'Er'

while not validate_ip_address(NETADR):
    print("{} is geen geldig netwerkadres".format(NETADR))
    NETADR = input('Voer een netwerkadres in: ')

#test zonder input te vragen
#NETADR = "192.168.0.1"

# > aantal lokalen

LOKALEN = 0

#LOKALEN = 1 tot 8
# Voer maximaal 8 lokalen in en minimum 1 lokaal

while LOKALEN not in range(1, 9): 
  print("U moet 1 - 8 lokalen configureren")
  LOKALEN = int(input('Voer het aantal lokalen in: '))

#subnetmask berekenen
  if LOKALEN == 1:
      sn_mask = sn_masks_ip[32]
  elif LOKALEN == 2:
      sn_mask = sn_masks_ip[64]
  elif LOKALEN in range(2, 5):
      sn_mask = sn_masks_ip[128]
  else:
      sn_mask = sn_masks_ip[256]
      
  #subnet ip-buffer
  #voor latere ip-berekeningen in andere subnets
  #prefix /26
  sn_mod = 64

  # > netwerkadres omzetten naar decimaal
  netadr_dec = set_dotted(NETADR)

  # > basisadres
  basisadres = network(NETADR, sn_mask)

  # > subnets berekenen
  subnets = bereken_subnets(netadr_dec)

  # > te voorzien aantal hosts per lokaal
  aantal_hosts = 20

  # ip-adressen netdevices en vlans berekenen
      
  # > router
  router_ip = get_dotted(subnets[0] + 1)
  #> routerinterfaces
  router_g0 = get_dotted(subnets[0] + 2)
  router_g1 = get_dotted(subnets[0] + 3)
  router_g2 = get_dotted(subnets[0] + 4)
  #> access-pointswitch
  ap_switch_ip = get_dotted(subnets[0] + 5)
  # > backbone switch
  bb_switch_ip = get_dotted(subnets[0] + 6)
  # > server
  server_ip = get_dotted(subnets[0] + 7)
  # > management-vlan
  vlan_man_ip = get_dotted(subnets[0] + 8)
  # > access-point-vlan
  vlan_ap_ip = get_dotted(subnets[0] + 9)
  # > lokaal-vlans
  # > kleine L lijkt op cijfer 1
  vlan_l1_ip = get_dotted(subnets[0] + 10)
  vlan_l2_ip = get_dotted(subnets[0] + 11)
  vlan_l3_ip = get_dotted(subnets[0] + 12)
  vlan_l4_ip = get_dotted(subnets[0] + 13)
  vlan_l5_ip = get_dotted(subnets[0] + 14)
  vlan_l6_ip = get_dotted(subnets[0] + 15)
  vlan_l7_ip = get_dotted(subnets[0] + 16)
  vlan_l8_ip = get_dotted(subnets[0] + 17)

  #netdevices en vlans toewijzen aan lokaal 0

  adressen = {"lokaal0" : {
      "name" : "Serverlokaal",
      "short_name" : "Lokaal0",
      "network_address" : get_dotted(subnets[0]),
      "gateway" : router_ip,
      "rt_int_0" : router_g0,
      "rt_int_1" : router_g1,
      "rt_int_2" : router_g2,
      "ap_switch" : ap_switch_ip,
      "backbone" : bb_switch_ip,
      "server" : server_ip,
      "vlan_man" : vlan_man_ip,
      "vlan_aps" : vlan_ap_ip,
      "vlan_l1" : vlan_l1_ip,
      "vlan_l2" : vlan_l2_ip,
      "vlan_l3" : vlan_l3_ip,
      "vlan_l4" : vlan_l4_ip,
      "vlan_l5" : vlan_l5_ip,
      "vlan_l6" : vlan_l6_ip,
      "vlan_l7" : vlan_l7_ip,
      "vlan_l8" : vlan_l8_ip
      }
  }    

  #ip-adressen extra lokalen
  for i in range(LOKALEN):
      j = i + 1
      h = i
      
  #hosts
      hosts_ip = []
      for i in range(aantal_hosts):
          hosts_ip.append(get_dotted(subnets[h] + 3 + i + j * sn_mod))

  #andere instellingen

      adressen["lokaal{0}_ip".format(j)] = {
      "name" : "Leslokaal {0}".format(j),
      "short_name" : "Lokaal{0}".format(j),
      "network_address" : get_dotted(subnets[j]),
      "gateway" : router_ip,
      "network_mask" : sn_mask,
      "switch" : get_dotted(subnets[h] + 1 + j * sn_mod),
      "ap" : get_dotted(subnets[h] + 2 + j * sn_mod),
      "hosts" : hosts_ip
      }

# > range voor de hosts
# > subnet mask
# > default gateway

# test
# print("Instellingen: ", adressen)

  print("\n".join("{}\t{}".format(x, y) for y, x in adressen.items()))
  
#===playbook===
f = open('dev_config.yaml', 'w')

#lege string om aan te vullen
yaml_output = ""

# router
yaml_output += """enable
configure terminal
hostname R1
enable secret cisco
service password-encryption
banner motd $Authorized access only$
security passwords min-length 10
login block-for 120 attempts 2 within 30
no ip domain-lookup
ip domain-name {domain_name}
crypto key generate rsa
1024

interface g0/0
ip address {g0_ip} {snm}
description server
no shutdown
exit

interface g0/1
ip address {g1_ip} {snm}
description access_points
no shutdown
exit

interface g0/2
ip address {g2_ip} {snm}
description backbone
no shutdown
exit""".format(domain_name = "ccnav6.com", g0_ip = router_g0, g1_ip = router_g1, g2_ip = router_g2, snm = sn_mask)

#switch
yaml_output_switch += """enable
conf terminal
hostname {hostname}
enable secret cisco1234
service password-encryption
no ip domain-lookup

line console 0
password cisco1234
login
logging synchronous
exec-timeout 60
exit

line vty 0 15
password cisco1234
login
logging synchronous
exec-timeout 60
exit
interface vlan 1
ip address {vlan1}
no shutdown

ip default-gateway {gateway}
exit""".format(hostname = "Lokaal0", vlan1 = vlan_l1_ip, gateway = router_ip)


# output wegschrijven
f.write(str(yaml_output))
f.write(str(yaml_output_switch))
f.close()

#===html===
f = open('adressen.html', 'w')

df = pd.DataFrame(adressen)
df = df.fillna(' ').T
html_output = df.to_html()

f.write(html_output)
f.close()
