import os

print(os.getcwd())

f = open('story.txt', 'w')

for i in range(3):
    sentence = input(f"{i + 1}번 문장을 입력하세요: ")
    f.write(sentence + '\n')

f.close()

f = open('story.txt', 'r')

story = f.read()
print(story)

f.close()