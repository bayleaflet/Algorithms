# Original Author: BJC
# Date of Last Edit: 10/01/2023
# This is a game function that tests the users on the power of two. It follows
# a particular format in which the user does not have to enter an exact answer,
# rather the user rounds to the nearest whole number, such as 2^16= 64k.
# It also tells the user the time to completion

import random
import time

# Create a list of unique powers of 2 from 0 to 49
powers_of_2 = [2 ** i for i in range(50)]

indices = list(range(50))
random.shuffle(indices)


start_time = time.time()
correct_answers = 0

for index in indices:
    power = powers_of_2[index]
    question = f'What is 2 ** {index}? '
    answer = input(question)
    incorrect_attempts = 0
    answer_suffix = ''


    while incorrect_attempts < 2:

        try:
            # If power greater than 9, split number, go through this different proocess.
            if index > 9:
                power_str = str(index)
                digits = [int(digit) for digit in power_str] #Converts back into digits [2,3]
                first_digit = digits[0]
                second_digit = digits[1]

                if first_digit == 1:
                    answer_suffix = "k"
                    # end should be k
                if first_digit == 2:
                    answer_suffix = "m"
                    # end should be m
                if first_digit == 3:
                    answer_suffix = "b"
                    # End should be b
                if first_digit == 4:
                    answer_suffix = "t"
                    # end should be t
                user_answer = answer
                correct_answer = str(2 ** second_digit) + answer_suffix
                if user_answer == correct_answer:
                    correct_answers +=1
                    print("Correct!")
                    break
                else:
                    incorrect_attempts += 1

                    if incorrect_attempts < 2:
                        answer = input(f'Wrong! Try again ({2 - incorrect_attempts} attempts left): ')
                    #else:
                        #print(f'Sorry, the correct answer is {correct_answer}.')

            user_answer = int(answer)
            if user_answer == (2 ** powers_of_2.index(power)):
                correct_answers += 1
                print("Correct!")
                break
            else:
                incorrect_attempts += 1
                if incorrect_attempts < 2:
                    answer = input(f'Wrong! Try again ({2 - incorrect_attempts} attempts left): ')
                else:
                    print(f'Sorry, the correct answer is {correct_answer}.')
        except ValueError:
            answer = input('Please enter a valid integer: ')

end_time = time.time()
total_time = round(end_time - start_time)

print(f'Your total time was {total_time} seconds.')
print(f'You answered {correct_answers} out of 50 questions correctly.')
