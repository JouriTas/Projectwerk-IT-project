# VLANs

VID	Name		IP-address	Default gateway     
1	Default		-		-                   
10	Management	x.x.x.4		router   						           
20	APs		x.x.x.5		router												
21	Lokaal 1	x.x.x.6		router (via backbone sw)
22	Lokaal 2	x.x.x.7		router (via backbone sw)
28	Lokaal 8	x.x.x.13	router (via backbone sw)

IP-adressen: worden berekend in script obv basisadres. 1-3 zijn echter al bezet door router, backbone switch en server. 
Apart subnet voor deze drie + de vlans is misschien nodig, want ze staan nu allemaal in hetzelfde subnet als lokaal 1.

# Interfaces

Interface	VLAN	Mode
G0/0		10	trunk
G0/1		20	access
G0/2		21-28	access
G0/3
