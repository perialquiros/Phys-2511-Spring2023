#!/usr/bin/env python
# coding: utf-8

# In[30]:


"""import matplotlib.pyplot as plt
import numpy as np"""

def countWord(word: str, text: str):
    position = 0
    appearances = 0
    chapterID = 0
    pastTableOfContents = False
    pastLetters = False
    chapterAppearances = []
    textInWords = text.split()
    for wordID in range(len(textInWords)):
        textWord = textInWords[wordID]
        if textWord == "Chapter":
            chapterID = textInWords[wordID + 1]
            chapterID = int(chapterID)
            if chapterID == 24 and pastTableOfContents == False:
                pastTableOfContents = True
            elif pastTableOfContents and pastLetters == False:
                pastLetters = True
                chapterAppearances.append(0)
            elif pastTableOfContents == True and pastLetters == True:
                chapterAppearances.append(0)
        if word in textWord and pastLetters == True:
            nextWord = textInWords[wordID + 1]
            for punctuation in [",", ".", "-"]:
                nextWord.replace(punctuation, "")
            appearances += 1
            chapterAppearances[chapterID - 1] += 1
        position += 1
    return [appearances, chapterAppearances]

def countCharacterAppearances(characterList):
    for character in characterList:
        wordToFind = character
        returnedValues = countWord(wordToFind, fileText)
        totalAppearances = returnedValues[0]
        chapterAppearances = returnedValues[1]
        print(str() + str(totalAppearances) +
          " appearances of "  + wordToFind + " in the text.")
        print("Most often appeared in Chapter " + 
              str(chapterAppearances.index(max(chapterAppearances)) + 1))
        allChapterAppearances.append(chapterAppearances)

def checkDead(text=str, chrList=tuple):
    textInWords = text.split()
    talkingAbtChar = False
    deadPeople = ""
    for char in chrList:
        charDead = False    
        for wordID in range(len(textInWords)):
            selectedWord = textInWords[wordID]
            for punctuation in [",", ".", "-"]:
                selectedWord.replace(punctuation, "")
            if selectedWord == char:
                talkingAbtChar = True
            if selectedWord != char and selectedWord in chrList:
                talkingAbtChar = False
            if "died" in selectedWord:
                if talkingAbtChar and charDead == False:
                    deadPeople += char
                    deadPeople += ", "
                    charDead = True
    return deadPeople

def appearancesGraph(allChptApprs=list, chars=tuple):
    for chapterNum in range(24): # For all chapters
        charsThatAppearInThisChapter = []
        apprsPerChar = []
        for charsChptApprs in allChptApprs: # For all sets of appearances
            if charsChptApprs[chapterNum] > 0:
                charsThatAppearInThisChapter.append(chars[allChptApprs.index(charsChptApprs)])
                apprsPerChar.append(charsChptApprs[chapterNum])
        fig, ax = plt.subplots()

        """fruits = ['apple', 'blueberry', 'cherry', 'orange']
        counts = [40, 100, 30, 55]
        bar_labels = ['red', 'blue', '_red', 'orange']
        bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']"""
        
        ax.bar(charsThatAppearInThisChapter, apprsPerChar)

        ax.set_ylabel('Appearances')
        ax.set_title('Appearances in Chapter ' + str(chapterNum + 1))
        #ax.legend(title='Fruit color')

        plt.show()

file = open("frankenstein.txt", "r", encoding="utf-8")
fileText = file.read()
characterList = ("Victor", "creature", "Agatha", "Caroline", "Lacey"
                , "Elizabeth", "Ernest", "Felix", "Henry", "Justine", "William")
pronounList = ("he", "it", "she", "she", "he"
                , "she", "he", "he", "he", "she", "he")
allChapterAppearances = []
countCharacterAppearances(characterList)
appearancesGraph(allChapterAppearances, characterList)
chapterNumber = 0
charactersThatAppearInEachChapter = []
strOfDeadPpl = checkDead(fileText, characterList)
while chapterNumber < 24:
    print("In Chapter " + str(chapterNumber + 1) + ":")
    charactersThatAppearInEachChapter.append([])
    for charChapAppearances in allChapterAppearances:
        if charChapAppearances[chapterNumber] != 0:
            characterIndex = allChapterAppearances.index(charChapAppearances)
            character = characterList[characterIndex]
            charactersThatAppearInEachChapter[chapterNumber].append(character)
            print ("\t" + character + " appears " + str(charChapAppearances[chapterNumber]) + " time(s).")
    chapterNumber += 1
charactersThatMeetVictor = ""
charactersThatMeetCreature = ""
for targetCharacter in characterList:
    printedVictor = False
    printedCreature = False    
    for i in charactersThatAppearInEachChapter:
        if targetCharacter in i and "Victor" in i and printedVictor == False:
            charactersThatMeetVictor += targetCharacter
            charactersThatMeetVictor += ", "
            printedVictor = True
        if targetCharacter in i and "creature" in i and printedCreature == False:
            charactersThatMeetCreature += targetCharacter
            charactersThatMeetCreature += ", "
            printedCreature = True
print(charactersThatMeetVictor + "have met Victor.")
print(charactersThatMeetCreature + "have met creature.")
print(strOfDeadPpl + " have died.")
file.close()


# In[ ]:





# In[ ]:




