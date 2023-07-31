# CS361

## Dice roll micro service:
### A. How to programmatically REQUEST data:
To initiate the dice roll and request data:

In the Application 1 script, call the function writeRollToDiceFile() to write "roll" to the dice.txt file. This will signal the Application 2 script to read "roll" and roll the dice.

#### Example Call: 
Application 1: write “roll” to dice.txt

Application 2: read “roll” from dice.txt

Application 2: randomly generate the dice roll and write the number to dice.txt

Application 1: read the number from dice.txt


### B. How to programmatically RECEIVE data:
To receive the data (dice number) after the dice has been rolled:

In the Application 1 script, call the function readDiceNumberFromFile() to read the dice number from the dice.txt file. This function will keep checking the file until it receives a valid dice number (not "roll").

### C. UML sequence diagram:
