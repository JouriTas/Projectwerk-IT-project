## Projectwerk-IT-project

# Situatieschets

Odisee is dé co-hogeschool. Samenwerking met bedrijven zit in het DNA van elke opleiding en dienst. Om de link met 
bedrijven te verstevigen wordt een bedrijf als een "vestigingsplaats" voor IT-onderwijs gezien. Studenten kunnen in 
deze "vestigingsplaatsen" (bij-)studeren en nieuwe onderwerpen uitdiepen.

Gelet op een samenwerkingsverband met meer dan 20 verschillende bedrijven is het opzetten van een nieuwe
"vestigingsplaats" een tijdrovende bezigheid. Je team wordt ingeschakeld om deze situatie te optimaliseren via 
deployment services. Vanzelfsprekend dient, naast de software, ook de hardware eenvoudig te worden geconfigureerd. 
De studenten die studeren (en werken) in een "vestigingsplaats"  beschikken over een eigen laptop via het BYOD-programma. 
De focus ligt dus op servers, switches, routers en access-points.

# Vestigingsplaats

Een vestigingsplaats bestaat uit tenminste één lokaal met een switch en een access-point. Elk lokaal vormt een eigen VLAN 
waarbij het access-point geen deel uitmaakt van dit VLAN. Elk access-point vormt een VLAN op zich. Dit vertaalt zich dus in 2 VLAN's per lokaal. 
De switch van het lokaal kan tot 20 tafels voorzien van een netwerkaansluiting (in een opstelling van één netwerkaansluiting per tafel). 
Alle lokalen worden via ethernet (twisted-pair) verbonden met een router. Deze router verzorgt de verbinding met internet. 
Bovendien beschikt elke vestigingsplaats over een eigen Linux Ubuntu Server met een geïnstalleerde en geconfigureerde Moodle ELO. 
De Moodle ELO bevat de lokale cursussen/modules. De gegevens van de studenten worden 's nachts uit de centrale server 
opgevraagd (via een API) en geïmporteerd in de lokale Ubuntu Server. Op deze manier is de toegang voor geregistreerde studenten gegarandeerd. 
Studenten die uitgeschreven zijn worden verwijderd uit de vestigingsplaats. Vanzelfsprekend worden enkel de studenten van een 
specifieke vestigingsplaats geïmporteerd, niet alle studenten van de hogeschool.

