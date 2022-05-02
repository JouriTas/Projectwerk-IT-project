# Sprint 2 - 29/04/2022 - 13/05/2022

Script voor de hardware adhv ip-adresseringschema =>

-	Bepalen Vlan's per lokaal  + 1 voor de acces-point switch
-	Switches configureren via ansible
-	Routers => basisconfig router
-	HTML weergave output scripts

# Definition of done

Planning Sprint2:

-	In het huidig script een berekening maken waarbij we 2 vlan's krijgen als output
	voor zowel de wired alsook de wireless hosts


-	In een YAML bestand de configuratie uitwerken voor de router en de switchen
	en via ensible toepassen, telnet acces
	Testen in packet tracer zowel voor de switch als voor de router
	
	
-	Routers => Basisconfig maken in ansible, zonder vlan's, enkel telnet acces


-	HTML weergave output van de scripts, weergave adressering per device/categorie

# Planning

Vlan-berekening: Daniël en William

Aanzet html-weergave: Jouri

Bijwerken topologie: Jouri

Basisconfig ansible

Aanvulling script

	Foutdetectie input
	
	Vlan-berekening
	
	Berekeningen herschrijven
	
		1 IP-adres per routerpoort
	
		1 switch (PoE) voor de APs
		
		Max. 8 lokalen
	
	Ansible-script genereren


