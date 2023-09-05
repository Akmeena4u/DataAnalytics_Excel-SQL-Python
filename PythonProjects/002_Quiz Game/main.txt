project Description :-
            This project is a simple quiz application that begins when a user enters an Application ID, ensuring that the ID is a 6-digit alphanumeric value. 
            If the ID is valid, the user is welcomed to the objective round placement quiz. The program then prompts the user to start the quiz and calculates 
            their score based on their answers to a set of predefined questions. Finally, it provides feedback on the number of correct answers and
            the percentage of correct responses out of the total questions attempted. This project demonstrates basic input validation, user interaction, and scoring in a Python-based quiz application.



Challenges   :--
          c1:- Case Sensitivity problem -- user answering questions correctly but still my program showing  them incorrect answer because of case sensitivity of program so to solve this problem i have used .lower() function. 
          c2:- Authencity problem :- to application id more authentic i used a regular expression that demonstrates that ID should be alphanumeric and 6 length only

Upgradaions  :--
          version 1:- makes a simple quiz that was have 5 questions and at last shows total score
          version 2 :- Here i have increased number of questions to 10 
          version 3 :- to make this quiz more intractive i have added a applications id statement 
          version 4:- to improve security in application id i used regular expression that matches that id should be alphanumeric and 6 lengths 
          version 5:- in last i shows that if score is greater than 7 u are selected 

Used Modules :-
         m1:- regular expression module -- re
