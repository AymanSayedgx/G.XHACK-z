import telebot
import requests

# هنا ضع رمز الـ Token الخاص بالبوت
API_TOKEN = '7551672172:AAE8b73qo2SYfFugmm1KI5uuDBQLtHOLXOE'
bot = telebot.TeleBot(API_TOKEN)

# دالة بدء التفاعل مع البوت
@bot.message_handler(commands=['start'])
def start(message):
    name = message.from_user.first_name  # الحصول على اسم المستخدم
    welcome_message = f"""
    ╔━━━━━🧟‍♂WELCOME🧟‍♂━━━━━━╗

    🧚𝐇𝐢 {name} 𝐢𝐧 𝐦𝐲 𝐁𝐨𝐭🥶

    🍀𝐒𝐏𝐀𝐌 𝐂𝐀𝐋𝐋ৡ
    🌟𝚜𝚞𝚌𝚌𝚎𝚜𝚜𝚏𝚞𝚕𝚕𝚢 𝚕𝚘𝚐𝚒𝚗🌟
    ♻️ 𝙲𝚑𝚘𝚘𝚜𝚎 𝚝𝚑𝚎 𝚜𝚎𝚛𝚟𝚒𝚌𝚎♻️

    [♻️] 𝗕𝗢𝗧 𝗕𝘆 @x_GX_HACK_x ★👑★
    ادخــل رقـــم الـــهاتف  كدا  01247934567

    زي كده 👇
    01234567890

    ╚━━━━━━━━━👑👑━━━━━━━━━╝
    """
    bot.reply_to(message, welcome_message)

# دالة لمعالجة الرسائل من المستخدم
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    n = message.text  # الرقم المدخل من المستخدم
    url = "https://virs-net.com/spmcall.php"

    payload = {
        'num': n,
        'g-recaptcha-response': "03AFcWeA5UcHhFc6K3_GGAyLq9zrKaDijOtmXGdAmE7KsPw-okdrajCKI1JPz9LStZoHxt9RcoZ-pZHdDZ4-44Cwen_L_IWWKrFPiRvi6TYbxXOM5vCn5jrw10xjLXt-72LVYXqnLQSiCFHhBugGF2A0mfF5vAOgLxT6HEZk7ws9g23K6sUcSPGtH3ZF6iZ3Jw12Fg7sICKdVbfX1RCTPgZVggdVJQnhHGc3CeVu8pEU6ncP3S5t4r8x2PWclPLlpGtmQzmgW8uqJAN4g--vQ7OulY3UHwNIfU3evMjPVuoDfJT1-3Fur1pcU99ZHjfcCPnf7VCdepAXjG2QUnYYj0_KNFGdSg4jVAISlUvRozHtpfzSshdriWuIsLkU4aqqh6JRUttDLYAwxAHhItCF7-JX6P7tyIhGQgleD1DYRrCSoLePlOpeLZRrcwkC6-dhxjS_I-JHuyMo4oClAZMry40gC16LqPoPFCmoys3EJf50pS5Rp2fwscGB3z9YxEVMunATP9AKB9_T4HUotsDzBI4sNMKvEqKHhRgmwlcdRpvbsTkJy4OltYxcwaMb_pDnMX-lnPFMj_CgeEo6tIl5YXXGzfSRqEcEIX6Tk3QCjW9c2HQEbXUcpAU3GJunnKusmrZt3NJBBDzvsT83Im5DgY02qTgZv5lQ1fcHLouh8UXPmsTn30Z5SEasYdylfk1qC8kI1M5Avop9-Nr92zKZdd6ewyXAsM1X8r4nJPwmh0pgP1_bWT7skvIprSBHvfO_ri5NrnP2Vk1R0Y1D6hlh3noevZobIGAT5sk732dgTzeaNj9gGswc7PH-Sj6ZbhFxl_TlacmTffhHfiyxnvkBzINFmnw-doRBfIvx5-G_pIPkKNN49-rvRqqRC8c1udf8GaVs5EngdO2GT72sAG8rGCjwcQE4TGE4IS9GefEb1XLiArNMnZG-JESLvwLkJY7iUGy60yI9i6rOr-GmF1Qv-U4nuz4iBshwX4c_1sjCQeRRZGK9fh64lSuTlMaspj82VSIJn8DnfpXdS1n0JTI3ZOoKQJU9x4-VWPmm1MyIqcrqHNi3WscHZNESph41RG4J9waA0X8NhdzCo5tIJXwuUAHJoHfo7YWAGYg0JuUG-0nb3lYPSUh-rYdhSUoSr_iNco-eV0AgM_Y9eLQx2ugKXTabJrbOuM0FSJyGwfb8DH7T8XciDzjY_1vzV4CWxClvv8dvEUDf9PQ_ECjbeXT98YOxO-kktTtTzIFY1mVwJDpdRsXmAkcBPdK802wxdcsY0bh65xgNsaEHyS7jgesnnh1dzBzImXOYClPe54vnR-DsdU_1WwaCX8Hsn6j_8nFYbIqfYvxkCq6ZMCyY7peVBbOwR4XibV8xPj4ddCGbCF67nAyo2tLDml2YYB952E2UCNxbu7GDATDVSpTmgKZiopfpLeje6i0QwMaoGRB5e74QVkNhQBlKHpjDkX9YDqfrDypw5hB_saIYqr00wCcelqZWLa3Z6MLmSUWNy8UyNDvtsGQlrxxrLB0G5lRnHQNq94MXg9SLWE5MYScSEnZpu51ukw5jHL1UOKSlNEnEovIFKxFM3wSL_WoAEZEPBNeJqkje_573gOyKFFo9TQhPNTrfJOJDAbXS-kGDAiyz6CJe6kF-I-iu4pVnx8DmbiyLiMVQJQwBKqg4OCSDMFOXOuFebdjHzQsJGUVpqdrm6r5KixRB11o3SwgZVvgV9RuLXh6YwYAJHT0ogvBsrKg_Vlg3IlJYwX3_AFdIN07SJWX9CisEJ3aiakm_Ti2FFwl_g_AjrZyGlC5kUkhlgkR81AEhRVS2VK2SZjwrdw1t10mKPJJSJbyBmTkJepXXakGjZ9sI7fTENIUjhVLfpJOlH9YNjlhPwq9yXrU0JI1Zp0561erfbP0hFJzCj7F-dyEyU-i6pTdYg79VA26nt19KdfuBIPapJAhKCU-OKIEJcohi9YHRCQaqBGH6LUFWV5-Qm5ahg7hrvUjP7kBoSnEUzKbWWBp56RFpgQUqSUlYRbB9_XE-n5s3SAaqNQROzi2onMFcbeyGh_LDTnhJMl8fztX9Gq6QbELud8rjViOKXYTB5Zigm-sgBYjEDZRzmJfsVFFDL5wg2Sf4SwSGt-8Ere8fews3WBOjZGsIXctcJbuh0t6N5_A165GmSn9lDSU_xR5ay_79RmSg6ZyXff-7v1EFubTbzY5Z4fALhpqGVFLSlhKFhHJ9_qCKVuYW_7gznfmOOWhfTAqx_bkHxVwj1SzpIIaToLc8zAAeSbxr7Rm5LGW04LPgCk0FXxki-JKEhCCCUfme6IDsWl",
        'submit': ""
    }

    headers = {
        'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36",
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        'Accept-Encoding': "gzip, deflate, br, zstd",
        'cache-control': "max-age=0",
        'sec-ch-ua': "\"Not A(Brand\";v=\"8\", \"Chromium\";v=\"132\", \"Google Chrome\";v=\"132\"",
        'sec-ch-ua-mobile': "?1",
        'sec-ch-ua-platform': "\"Android\"",
        'origin': "https://virs-net.com",
        'upgrade-insecure-requests': "1",
        'sec-fetch-site': "same-origin",
        'sec-fetch-mode': "navigate",
        'sec-fetch-user': "?1",
        'sec-fetch-dest': "document",
        'referer': "https://virs-net.com/spmcall.php?",
        'accept-language': "ar-EG,ar;q=0.9,en;q=0.8",
    }

    # إرسال الطلب
    response = requests.post(url, data=payload, headers=headers)

    # التحقق من استجابة الطلب
    if response.status_code == 200:
        bot.reply_to(message, "تم إرسال الطلب بنجاح!")
    else:
        bot.reply_to(message, "فشل الطلب! يرجى المحاولة لاحقًا.")

# بدء البوت
bot.polling()