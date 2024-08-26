from random import randint
question_data = [
    {"text": "A slug's blood is green.", "answer": "True"},
    {"text": "The loudest animal is the African Elephant.", "answer": "False"},
    {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
    {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
    {"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to orange"
             "at.",
     "answer": "True"},
    {"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.",
     "answer": "False"},
    {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
    {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
    {"text": "Google was originally called 'Backrub'.", "answer": "True"},
    {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
    {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
    {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]
oof = True
niete = 0
nice = 0
def next_question():
    global ooga, answer, question, niete, question_data,oof,l
    ooga = randint(0, len(question_data)-1)
    question = question_data[ooga]["text"]
    answer = question_data[ooga]["answer"].lower()
    niete += 1
    question_data.remove(question_data[ooga])
def right(like):
    global ooga, answer, question, niete, question_data,oof,l,nice
    if like.lower() == answer:
        print(f"You got it right!\nThe correct answer was: {answer}.\nYour current score is: {niete-nice}/{niete}")
    elif like.lower() == "quit":
        print(f"Your final score was {niete-nice}/{niete}")
        oof=False
    else:
        nice += 1
        print(f"That's wrong.\nThe correct answer was: {answer}.\nYour current score is: {niete - nice}/{niete}")
def say_it():
    global ooga, answer, question, niete, question_data,oof,l
    l = input(f"Q.{niete}: {question} (True/False)?:")
    return l
while oof:
    next_question()
    j = say_it()
    right(like=j)