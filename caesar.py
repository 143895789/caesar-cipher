def caesar_cipher():
    """
    카이사르 시저 암호화/복호화 함수
    :return: 암호화/복호화된 결과 메시지 (str)
    """
    message = input("메시지를 입력하세요: ")
    key = int(input("암호화/복호화에 사용할 키 값을 입력하세요: "))
    mode = input("암호화: 'encrypt', 복호화: 'decrypt' 중 선택하세요: ")

    result = ''
    if mode == 'encrypt':
        for char in message:
            if char.isalpha():
                if char.isupper():
                    result += chr((ord(char) + key - 65) % 26 + 65)
                else:
                    result += chr((ord(char) + key - 97) % 26 + 97)
            else:
                result += char
    elif mode == 'decrypt':
        for char in message:
            if char.isalpha():
                if char.isupper():
                    result += chr((ord(char) - key - 65) % 26 + 65)
                else:
                    result += chr((ord(char) - key - 97) % 26 + 97)
            else:
                result += char
    return result

cipher_text = caesar_cipher()
print(cipher_text)
