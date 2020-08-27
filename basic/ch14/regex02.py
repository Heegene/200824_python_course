import re
import pyperclip

# create E-mail regex --> VERBOSE, X

email_regex = re.compile(r'''(
            [a-zA*Z0-9._%+-]+  # username
            @                  # @
            [a-zA-Z0-9.-]+     # domain
            (\.[a-zA-Z]{2,4}){1,2}    # dot-something
            )''', re.VERBOSE)

def find_match_list():
    text = pyperclip.paste()
    # clipboard에 있는 리스트를 하나씩 꺼내 matches list에 넣음
    matches = []
    print("find_match_list text-> Start")
    print("find_match_list text-> \n", text)
    #email에 있는 List append
    for each in email_regex.findall(text):
        matches.append(each[0])

    print("find_match_list matches => \n", matches)
    return matches

def copy_result_to_clipboard(matches):
    if len(matches) > 0:
        # list 하나하나 개행처리
        pyperclip.copy('\n'.join(matches))
        print("Clipboard에 복사됨")
    else:
        print("매칭되는 패턴이 없음")

def main():
    matches = find_match_list() # 빈 리스트에 return matches를 받아서 리스트 값을 채움
    print("main matches -> \n", matches)
    copy_result_to_clipboard(matches)

main()