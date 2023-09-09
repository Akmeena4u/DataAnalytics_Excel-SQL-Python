Project Title: "Number Guessing Game "

Project Description:--this is a number guessing game where users log in with a 6-digit alphanumeric ID and guess a randomly generated number within specified 
                      difficulty levels (easy, medium, hard). The game provides feedback, tracks guesses, and offers the option to play again

                     Key Features:-
                           1-User authentication with a 6-digit alphanumeric login ID.
                           2-Multiple difficulty levels (easy, medium, hard) with different number ranges and maximum guess limits.
                           3- Interactive gameplay with user-friendly prompts and feedback.
                           4- Randomly generated target numbers for each game.
                           5-The option to play again and improve guessing skills.
                           6-Input validation to ensure a smooth user experience.


Challenges:-
          challenge 1:- Handling user input validation like correct format of login id and user guess range limitations  
          challenge 2:- Authencity problem :- to make login id more authentic i used a regular expression that demonstrates that ID should be alphanumeric and 6 length only
          Challenge 3:- Play Again issue -- Once a gamer complets game and wants to play again for that i added extra conditions 

          

update  :-
        version 1:- First of all i just asked user to guess number and comapre that number with rendomly genrated number , untill user guesses correctly
        version 2 :- Now to make game little bit harder i added constraints on max number of times an user can gusses to win or guess correctly
        version 3:-  Difficulty level:- Till now there was no difficulty level for gamers all was playing at similiar level so now considering diffrent level of gamers i added difficulty level
                      Now user can select there preferred level of game --Easy , medium , hard
        version 4:- to improve security or to give personalized experience to gamers i added an Login id concept 
        version 5:- to improve security in login id i used regular expression that matches that id should be alphanumeric and 6 lengths 
        version 6:- Play again - to get most time of gamers on application  or to give them another opportunity to play and win fastly i added  play again feature  



Used Modules:- re module , random module 
        
