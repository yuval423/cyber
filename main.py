#מגישה :יובל אגמי
#תאריך:15.10.25
#קובץ:main
#

print(" **     ** ")
print(" ****   ****")
print(" *********** ")
print("  ********  ")
print("   ******   ")
print("    ***    ")
print("     *     ")#טוב אתה אמרת להיות יצירתיים בשביל בונוס ואני מפחדת
#  לגעת בקוד אז מקווה שאהבת תלב
import sys#מאפשר לגשת לencrypt / decrypt
from milon import milon#מביא את המילון שהופך מילים למספרים
from milon import reverse_milon#מביא את המילון ההפוך שהופך מספרים למילים
if len(sys.argv) < 2:#בודקת אם הכנסתי encrypt /decrypt
    print("יש להזין מצב הפעלה encrypt או decrypt")
    sys.exit()#יוצאת מהתוכנית אם כן
mode = sys.argv[1]
if mode == 'encrypt':#בודקת אם צריך להצפין את ההודעה
    msg = input("הכנס הודעה להצפנה: ")#מקבלת הודעהלהצפנה
    if len(msg) == 0:#בודקת אם ההודעה ריקה אם כן מוציא אותך מהתוכנית
        print("לא שמת הודעה")
        sys.exit()
    encrypted_text = ""#יוצר מחרוזת שכרגע ריקה

    for letter in msg:#עוברת על כל האותיות והופך אותן אחת אחת למספרים לפי המילון
        encrypted_text += str(milon[letter]) + ','

    with open("encrypted_msg.txt", "w", encoding="utf-8") as file:
        file.write(encrypted_text)#שומר את ההודעה המוצפנת לקובץ

    print("ההודעה נשמרה בקובץ encrypted_msg.txt")# מודיע שההודעה נשמרה

elif mode == 'decrypt':#בודקת אם המשתמש ביקש לפענך הודעה
    with open("encrypted_msg.txt", "r", encoding="utf-8") as file:
        data = file.read()#פותח את הקובץ המוצפן וקורא ממנו תהודעה

    decrypted_text = ""#יוצר מחרוזת ריקה שתכיל את ההודעה אחרי שהיא מפוענחת

    for num in data.split(","):#בודקת אם המספר במילון ממיר אותו לאותיות ואז מכניס אותו להודעה
        if num.isdigit():
            num = int(num)
            if num in reverse_milon:
                decrypted_text += reverse_milon[num]
            else:
                decrypted_text += str(num)
        else:
            decrypted_text += num

    print("ההודעה:")
    print(decrypted_text)#מדפיס תהודעה

else:
    print(" זה לא decrypted או encrypt")#אם הגעתי לכאן כנראה שכתבתי בטעות לא נכון decrypted/ encrypt