from random import randint

player = input()
computer = randint(0,2)

if computer == 0:
    computer = "bua"
if computer == 1:
    computer = "keo"
if computer == 2:
    compurter = "bao"


if player == "keo" and computer == "keo":
        print("draw")

if player == "la" and computer== "la":
        print("draw")

if player == "dam"
    if computer== "dam"
        print("draw")
 
        
if player == "keo"
    if computer== "la"
        print("win")
if player == "la"
    if computer== "dam"
        print("win")
if player == "dam"
    if computer== "keo"
        print("win")
        
        
if player == "dam"
    if computer== "la"
        print("loss")
if player == "la"
    if computer== "keo"
        print("loss")
if player == "keo"
    if computer== "dam"
        print("loss")
    