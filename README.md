# Risk

##### work in progress

## to do
- [ ]  everything



## dutch rambling


CONTINENTEN
	- bijhorende landen
	- aangrenzende landen
	-



SPELER AI
	- 'logisch'



game beurt:

	- versterken
		- player.veroverde_landen.count() / 3 = aantal nieuwe
		  standaardbataljons
		- player.veroverde_continents = aantal nieuwe
		  continent bataljons
		- 5 kaarten: MOET IETS gebeuren
			ja: zoek de beste combi = kaartbataljons
			nee : zoek beste combi = kaartbatalons

		- bijzetten
		- check of opdracht = N bataljons per land, check true
		  ( check wincondition )
	- aanvalbeurt



		LOOP AGAIN
		- bepaal of er aangevallen word (Wil je , ja nee?)
			SKIPS
			-! if aantal bataljons == 1 : skip
			- if max(bataljons in enemy.neighbours) == 1: skip
			-
		- bepaal welk land uit player.neighbours of
		  player.findBestRoute(neighbours) ofzo
		- bepaal of enemy
		- kies hoeveel bataljons gebruik je
			- switch to enemy: kies ook verdediging
		- check hoeveel slachtoffers en haal die van de landen af (
		  en players)

		als een van de landen verliest OF kiest om op te houden:
		check de states van de landen
		check wincondition
		LOOP AGAIN

	- verzet fase
		- check of kan verschuiven,
		- verschuif

	- new player
		
