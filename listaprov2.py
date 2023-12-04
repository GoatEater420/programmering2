def byt_ut_a_till_ae(text):
    ny_text = text.replace('a', 'ä')
    return ny_text

text = input("skriv din text: ")

ny_text = byt_ut_a_till_ae(text)

print(ny_text)