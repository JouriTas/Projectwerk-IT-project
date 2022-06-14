# Sprint 2 - 29/04/2022 - 13/05/2022

Script voor de hardware adhv ip-adresseringschema =>

-	Bepalen Vlan's per lokaal  + 1 voor de acces-point switch
-	Switches configureren via ansible
-	Routers => basisconfig router
-	HTML weergave output scripts

# Definition of done

Planning Sprint 2:

-	In het huidig script een berekening maken waarbij we 2 vlan's krijgen als output
	voor zowel de wired alsook de wireless hosts


-	In een YAML bestand de configuratie uitwerken voor de router en de switchen
	en via ansible toepassen, telnet acces
	Testen in packet tracer zowel voor de switch als voor de router
	
	
-	Routers => Basisconfig maken in ansible, zonder vlan's, enkel telnet acces


-	HTML weergave output van de scripts, weergave adressering per device/categorie

# Planning

Vlan-berekening: Daniël en William (done)

Aanzet html-weergave: Jouri (done)

Bijwerken topologie: Jouri (done)

Basisconfig ansible: Jouri (done)

Ansible-script testen in PT, copy/paste config: Jouri (done)

Aanvulling script

	Foutdetectie input (max. 8 lokalen, geldig netwerkadres): Daniël
	
	Vlan-berekening: William (done)
	
	Berekeningen herschrijven
	
		Subnetmask naar /26: William
		
		1 IP-adres per routerpoort: William (done)
	
		1 switch (PoE) voor de APs: William (done)
		
		Netwerkadres: William (done)
	
	Ansible-script genereren
	
	Html-weergave: William (done)
	


