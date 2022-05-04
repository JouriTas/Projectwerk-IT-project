## Creëren van een HTML file vanuit python.

-	Door de f functie toe te passen.

Voorbeeld code:

f = open('Script.html', 'w')

Met bovenstaande verwijzing slagen we de html code op in Script.html
Hierna volgt een html code met de output van ons script in dit geval de output van de print.

Naam geven van de html code, begin en einde markeren door """

html_Script = """<html>
<head>
<title>Title</title>
</head>
<body>
<h2>print ()</h2>
  
<p></p>
  
</body>
</html>
"""

De code/output wegschrijven in de file
f.write(html_Script)

De code afsluiten
f.close()

