# SRC: https://www.hackerrank.com/challenges/the-minion-game/problem


# Functions
def substring_count(string, sub):
    count = start = 0
    while True:
        start = string.find(sub, start) + 1
        if start > 0:
            count += 1
        else:
            return count


def get_player_score(string, player, letters):
    # Calculate player score as per HR instructions
    results = 0

    # For each valid player letter
    for letter in letters:

        # Get the leftmost index of the letter in the string
        start = string.index(letter)

        # Temp value to calculate points on
        _string = string[start:]

        # Parse the string letter by letter
        while len(_string):
            # Add score
            results += substring_count(string, _string)

            # Drop one letter from right
            _string = _string[:-1]

        # Reset word to original
        _string = string

    return player, results


def minion_game(string):
    score = []
    vowels = ('A', 'E', 'I', 'O', 'U')

    # Get valid starting letters for both players
    # Stu gets points for words starting with a consonant
    # Kev gets points for words starting with a vowel
    starters_s = sorted(set([l for l in string if l not in vowels]))
    starters_k = sorted(set([l for l in string if l in vowels]))

    score.append(get_player_score(string, player='Stuart', letters=starters_s))
    score.append(get_player_score(string, player='Kevin', letters=starters_k))

    # Check if draw
    if len(set([i[1] for i in score])) == 1:
        print('Draw')
    else:
        winner = sorted(score, reverse=True, key=lambda x: x[1])[0]
        print(f"{winner[0]} {winner[1]}")

# main()
if __name__ == '__main__':
    s = input()
    minion_game(s)
