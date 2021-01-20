#!/bin/python3

import os 
import random

#init
yourScore = 0
computersScore = 0

#its just shorter than os.system
def com(command):
	os.system(command)

#let the computer pick rock, paper, scissors
def computerPick():
	num = random.randrange(3)
	if num == 0:
		pick = "rock"
	elif num == 1:
		pick = "paper"
	elif num == 2:
		pick = "scissors"
	return pick

#pick rock, paper or scissors
def youPick():
	while True:
		pick = input("Rock, paper or scissors: ")
		pick = pick.lower()
		if pick == "rock" or pick == "paper" or pick == "scissors" or pick == "s" or pick == "p" or pick == "r":
			if pick == "r":
				return "rock"
			elif pick == "p":
				return "paper"
			elif pick == "s":
				return "scissors"
			else:
				if pick != "exit":
					return pick
			break
		elif pick == "exit":
			return pick
		else:
			print("Sorry please pick again")
		
#who wins 
def whoWins(yourPick, computersPick):

	global yourScore
	global computersScore	
	
	#if you win
	if yourPick == "rock" and computersPick == "scissors" or yourPick == "r" and computersPick == "scissors":
		print("---You win!---")
		yourScore += 1
		print("Your score is: ", yourScore)
		print("The score from the computer: ", computersScore)
	elif yourPick == "paper" and computersPick == "rock" or yourPick == "p" and computersPick == "rock":
		print("---You win!---")
		yourScore += 1
		print("Your score is: ", yourScore)
		print("The score from the computer: ", computersScore)
	elif yourPick == "scissors" and computersPick == "paper" or yourPick == "s" and computersPick == "paper":
		print("---You win!---")
		yourScore += 1
		print("Your score is: ", yourScore)
		print("The score from the computer: ", computersScore)
	elif yourPick == computersPick:
		print("---DRAW---")
		print("Your score is: ", yourScore)
		print("The score from the computer: ", computersScore)
	else: 
		print("---You lose!---")
		computersScore += 1
		print("Your score is: ", yourScore)
		print("The score from the computer: ", computersScore)
	

#calling everything
com("clear")
while True:
	computersPick = computerPick()
	yourPick = youPick()
	com("clear")
	print("The computer picked: ", computersPick)
	print("You picked: ", yourPick)
	if yourPick == "exit":
		com("clear")
		break
	else:
		whoWins(yourPick, computersPick)