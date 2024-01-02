## Number Letter Counts

## If all the numbers from 1 to 1000 (inclusive) were written out in words,
## how many letters would be used?

## For example, 342 (three hundred and forty-two) contains 23 letters
## and 115 (one hundred and fifteen) contains 20 letters
## *** NOT including spaces or hyphens ***

NUM_DICT = {
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
    '10': 'ten',
    '11': 'eleven',
    '12': 'twelve',
    '13': 'thirteen',
    '14': 'fourteen',
    '15': 'fifteen',
    '16': 'sixteen',
    '17': 'seventeen',
    '18': 'eighteen',
    '19': 'nineteen',
    '20': 'twenty',
    '30': 'thirty',
    '40': 'forty',
    '50': 'fifty',
    '60': 'sixty',
    '70': 'seventy',
    '80': 'eighty',
    '90': 'ninety',
    '00': 'hundred',
    '000': 'thousand'
}

START = 1
END = 1000

def solve():
    count = 0
    for num in range(START, END+1):
        if len(str(num)) == 1:
            count += len(NUM_DICT[str(num)])
        elif len(str(num)) == 2:
            if str(num)[0] == '1':
                count += len(NUM_DICT[str(num)])
            else:
                if str(num)[0] == '2':
                    count += len(NUM_DICT['20'])
                elif str(num)[0] == '3':
                    count += len(NUM_DICT['30'])
                elif str(num)[0] == '4':
                    count += len(NUM_DICT['40'])
                elif str(num)[0] == '5':
                    count += len(NUM_DICT['50'])
                elif str(num)[0] == '6':
                    count += len(NUM_DICT['60'])
                elif str(num)[0] == '7':
                    count += len(NUM_DICT['70'])
                elif str(num)[0] == '8':
                    count += len(NUM_DICT['80'])
                elif str(num)[0] == '9':
                    count += len(NUM_DICT['90'])

                if str(num)[1] != '0':
                    if str(num)[1] == '1':
                        count += len(NUM_DICT['1'])
                    elif str(num)[1] == '2':
                        count += len(NUM_DICT['2'])
                    elif str(num)[1] == '3':
                        count += len(NUM_DICT['3'])
                    elif str(num)[1] == '4':
                        count += len(NUM_DICT['4'])
                    elif str(num)[1] == '5':
                        count += len(NUM_DICT['5'])
                    elif str(num)[1] == '6':
                        count += len(NUM_DICT['6'])
                    elif str(num)[1] == '7':
                        count += len(NUM_DICT['7'])
                    elif str(num)[1] == '8':
                        count += len(NUM_DICT['8'])
                    elif str(num)[1] == '9':
                        count += len(NUM_DICT['9'])

        elif len(str(num)) == 3:
            count += len(NUM_DICT['00'])
            if str(num)[0] == '1':
                count += len(NUM_DICT['1'])            
            elif str(num)[0] == '2':
                count += len(NUM_DICT['2'])
            elif str(num)[0] == '3':
                count += len(NUM_DICT['3'])
            elif str(num)[0] == '4':
                count += len(NUM_DICT['4'])
            elif str(num)[0] == '5':
                count += len(NUM_DICT['5'])
            elif str(num)[0] == '6':
                count += len(NUM_DICT['6'])
            elif str(num)[0] == '7':
                count += len(NUM_DICT['7'])
            elif str(num)[0] == '8':
                count += len(NUM_DICT['8'])
            elif str(num)[0] == '9':
                count += len(NUM_DICT['9'])

            if str(num)[1] == '0' and str(num)[2] == '0':
                continue
            else:
                ## the BRITISH say "and"
                count += 3
                if str(num)[1] == '0' and str(num)[2] != '0':
                    if str(num)[2] == '1':
                        count += len(NUM_DICT['1'])            
                    elif str(num)[2] == '2':
                        count += len(NUM_DICT['2'])
                    elif str(num)[2] == '3':
                        count += len(NUM_DICT['3'])
                    elif str(num)[2] == '4':
                        count += len(NUM_DICT['4'])
                    elif str(num)[2] == '5':
                        count += len(NUM_DICT['5'])
                    elif str(num)[2] == '6':
                        count += len(NUM_DICT['6'])
                    elif str(num)[2] == '7':
                        count += len(NUM_DICT['7'])
                    elif str(num)[2] == '8':
                        count += len(NUM_DICT['8'])
                    elif str(num)[2] == '9':
                        count += len(NUM_DICT['9'])
                elif str(num)[2] == '0':
                    if str(num)[1] == '1':
                        count += len(NUM_DICT['10'])
                    elif str(num)[1] == '2':
                        count += len(NUM_DICT['20'])
                    elif str(num)[1] == '3':
                        count += len(NUM_DICT['30'])
                    elif str(num)[1] == '4':
                        count += len(NUM_DICT['40'])
                    elif str(num)[1] == '5':
                        count += len(NUM_DICT['50'])
                    elif str(num)[1] == '6':
                        count += len(NUM_DICT['60'])
                    elif str(num)[1] == '7':
                        count += len(NUM_DICT['70'])
                    elif str(num)[1] == '8':
                        count += len(NUM_DICT['80'])
                    elif str(num)[1] == '9':
                        count += len(NUM_DICT['90'])
                    continue
                else:
                    if str(num)[2] == '1':
                        count += len(NUM_DICT['1'])
                    elif str(num)[2] == '2':
                        count += len(NUM_DICT['2'])
                    elif str(num)[2] == '3':
                        count += len(NUM_DICT['3'])
                    elif str(num)[2] == '4':
                        count += len(NUM_DICT['4'])
                    elif str(num)[2] == '5':
                        count += len(NUM_DICT['5'])
                    elif str(num)[2] == '6':
                        count += len(NUM_DICT['6'])
                    elif str(num)[2] == '7':
                        count += len(NUM_DICT['7'])
                    elif str(num)[2] == '8':
                        count += len(NUM_DICT['8'])
                    elif str(num)[2] == '9':
                        count += len(NUM_DICT['9'])



        elif len(str(num)) == 4:
            count += 11

    return count

if __name__ == '__main__':
    num_letter_counts = solve()
    print(num_letter_counts)