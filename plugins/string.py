import os, json, time, asyncio, sys, shutil, heroku3, random, requests
from asyncio.exceptions import TimeoutError
from pyrogram import filters, Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon.tl.functions.channels import EditPhotoRequest, CreateChannelRequest
from telethon.errors import PhoneNumberInvalidError, PhoneCodeInvalidError, PhoneCodeExpiredError, FloodWaitError,SessionPasswordNeededError, PasswordHashInvalidError
from time import time
from asyncio import get_event_loop
from git import Repo
from bot import Bot as bot
import tracemalloc
tracemalloc.start()

@bot.on_message(filters.command('start') & filters.private)
async def start(Bot, message: Message):
    id = message.chat.id
    video = "https://telegra.ph/file/d5707c8ab5ea69f990d81.mp4"
    text = f"<b>🇦🇿 Salam {message.from_user.first_name} Mən 𝙵𝚊𝚜𝚝𝚄𝚜彡𝚛𝙱𝚘𝚝 üçün yaradılmışam\n✅ Qurulum başlatmaq üçün /fast yazın.\n🖥️ Qurulum Haqda İzah Üçün /qurulum.yazın.\nℹ️ Heroku Apikey Üçün /apikey yazın.</b>"
    await Bot.send_video(id, video, text)
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("📢 Rəsmi Kanal", url=f"https://t.me/thefastresmi")], [InlineKeyboardButton("🇦🇿 Mental Kanal", url=f"https://t.me/MentalGameResmi")], [InlineKeyboardButton("👨🏻‍🔧 Support", url=f"https://t.me/TheFastSup")], [InlineKeyboardButton("🖥️ Məni Yaradan", url=f"https://t.me/FUBOwnerr")]])
    await message.reply(text = text, reply_markup = reply_markup, quote = True, disable_web_page_preview = True)

@bot.on_message(filters.command('apikey') & filters.private)
async def apikey(Bot, message: Message):
    id = message.chat.id
    img = "https://telegra.ph/file/3597be721e735cdbc3eda.jpg"
    text = f"<b>Salam 👋 {message.from_user.first_name}\n✅ Heroku [ApiKey]'i şəkildə göstərilmiş qaydada ala bilərsiniz.</b>"
    await Bot.send_video(id, img, text)

@bot.on_message(filters.command('qurulum') & filters.private)
async def qurulum(Bot, message: Message):
    id = message.chat.id
    video = "https://telegra.ph/file/b24d465f20ac51e09232e.mp4"
    text = f"<b>@SakoRobot 'a Start ver, botun cavab verməyin gözlə\n(əgər botdan cavab gəlməsə, 5 dəqiqə sonra yenidən yoxla,\nqurulum olduqda bot işləmir.\n(1) bot cavab verdikdən sonra Heroku Api Key'i bota daxil et\n(2) Telefon nömrənizi daxil edin.\n(İ) Nümunə: +995551234567\n(3) Telegrama gələn 5 rəqəmli kodu Daxil edin.\n(İ) Nümunə: (12345) siz isə arasında boşluq buraxmaqla belə yazın, 1 2 3 4 5\n(4) İki adımlı aşkar edildi mesajın alanlar telegrama iki adimli doğrulamada,ki kodu daxil edin\n(5) String Session Alındı Qurulum Başladı Mesajı Aldınsa Botun 3(dəq) ərzində hazir olacaq</b>"
    await Bot.send_video(id, video, text)

def rm_r(path):
    if not os.path.exists(path):
        return
    if os.path.isfile(path) or os.path.islink(path):
        os.unlink(path)
    else:
        shutil.rmtree(path)

@Client.on_message(filters.private & ~filters.forwarded & filters.command('fast'))
async def husu(bot, msg):
    loop = get_event_loop()
    user_id = msg.chat.id
    aid = 17202681
    ash = "ef4d6e4de6f924085a01988b1bc751f0"
    api_msg = await bot.ask(user_id, "(i) **Fast Userbot Qurulumu başlayır**\n\n__(i) Zəhmət olmasa heroku API keyinizi daxil edin__", filters=filters.text)
    api = api_msg.text
    heroku_conn = heroku3.from_key(api)
    try:
        heroku_conn.apps()
    except:
        await msg.reply("ℹ️ **Heroku Api Key Yanlış!**")
        return
    await msg.reply("✅ **Herokuya Giriş Uğurlu!**")

    # Telegram Prosesləri #
    phone_number_msg = await bot.ask(user_id, "📞 **İndi isə' telefon nömrənizi daxil edin.\n(i) Nümunə:** `+994551234567`", filters=filters.text) 
    phone_number = phone_number_msg.text
    client = TelegramClient(StringSession(), 17202681, "ef4d6e4de6f924085a01988b1bc751f0")
    await client.connect()
    try:
        code = await client.send_code_request(phone_number)
    except PhoneNumberInvalidError:
        await msg.reply("❗ **Telefon nömrəsi yanlış!**.\n\n✨ Yenidən başlat /fast")
        return
    try:
        phone_code_msg = await bot.ask(user_id, "**📲 Hesaba Kod Göndərildi.\nℹ️ Rəqəmlərin arasına boşluq buraxmaqla yaz.\n📟 Kod belə olur👉** '12345' **siz isə belə göndərin:** `1 2 3 4 5`\n\n✅ [Koda Baxmaq Üçün Daxil Ol](https://t.me/+42777)", filters=filters.text, timeout=600)
    except TimeoutError:
        await msg.reply("⌛ **Verilən vaxt limi sona çatdı**\n\n❗ Yenidən başlat /fast")
        return
    phone_code = phone_code_msg.text.replace(".", "")
    try:
        await client.sign_in(phone_number, phone_code, password=None)
    except PhoneCodeInvalidError:
        await msg.reply("❗ **Deyəsən botu başqa biri üçün qurursan.\n\n🪐 Kodu yönləndirməməsini və ss atmasını istəyin.\n\n🔁 Artıq bu kod keçərsiz olduğundan, qurulumu yenidən başladı .** /fast")
        return
    except PhoneCodeExpiredError:
        await msg.reply("❗ **Doğrulama kodununun müddəti başa çatıb. Qurulumu yenidən başlat.** /fast")
        return
    except SessionPasswordNeededError:
        try:
            two_step_msg = await bot.ask(user_id, "**🙈 Hesabınızda iki addımlı doğrulama aşkar edildi.\n✍🏻 Zəhmət olmasa iki addımlı kodu daxil edin.**", filters=filters.text, timeout=300)
        except TimeoutError:
            await msg.reply("**⌛ Vaxt limiti 5 dəqiqəyə çatdı. Zəhmət olmasa qurulumu yenidən başlat.** /fast")
            return
        try:
            password = two_step_msg.text
            await client.sign_in(password=password)
        except PasswordHashInvalidError:
            await two_step_msg.reply("🤔 **İki adımlı doğrulamanı.\nℹ️ Yanlış daxil etdin.\n✅ Yenidən başlat** /fast", quote=True)
            return
    string = client.session.save()
    await client.send_message("me", "🗽 **Fast UserBot Avtomatik Mesaj\n\n💠 Salam Hesabınıza ⚡️ Fast Userbot qurursunuz. Userbotu qurarkən @TheFastSup qrup və @TheFastPlugin kanalına avtomatik olaraq əlavə olunursunuz.\n\n💎 Fast​ UserBotu şeçdiyiniz üçün təşəkkürlər\n\n🆘Support Üçün Və İş Birliyi Üçün @FUBOwnerr**")
    Qrup = await client(CreateChannelRequest(title='🇦🇿Fast Botlog', about="Bu Qrupdan Çıxmayın!", megagroup=True))
    Qrup = Qrup.chats[0].id
    foto = await client.upload_file(file='FastLog.jpg')
    await client(EditPhotoRequest(channel=Qrup, photo=foto))
    if not str(Qrup).startswith("-100"):
        Qrup = int(f"-100{str(Qrup)}")
    await client.disconnect()
    await msg.reply("(✓) StringSession alındı!")

    appname = "karabakhuserbot" + str(time() * 1000)[-4:].replace(".", "") + str(random.randint(0,500))
    try:
        heroku_conn.create_app(name=appname, stack_id_or_name='container', region_id_or_name="eu")
    except requests.exceptions.HTTPError:
        await msg.reply("**🤦🏻‍♂️ Herokuda 5 tətbiq aşkar edildi.\nℹ️ tətbiq silməklə bağlı @TheFastSup dan kömək istəyə bilərsiniz.\n✅ Yenidən Quruluma Başla.** /fast")
        return

    await bot.send_message(-1001718954263, "✅ Mən quruluma Başladım.")

    await msg.reply("(i) 𝙵𝚊𝚜𝚝𝚄𝚜彡𝚛𝙱𝚘𝚝 Deploy edilir...\n(Bu müddət maksimum 200 saniyə çəkir)")
    if os.path.isdir("./fastuserbot/"):
        rm_r("./fastuserbot/")
    repo = Repo.clone_from("https://github.com/fastuserbot/fastuserbot", "./fastuserbot/", branch="main")
    app = heroku_conn.apps()[appname]
    giturl = app.git_url.replace("https://", "https://api:" + api + "@")
    if "heroku" in repo.remotes:
        remote = repo.remote("heroku")
        remote.set_url(giturl)
    else:
        remote = repo.create_remote("heroku", giturl)
    try:
        remote.push(refspec="HEAD:refs/heads/master", force=True)
    except Exception as e:
        await msg.reply(f"❌ Xəta baş verdi: {e}")

    app.install_addon(plan_id_or_name='062a1cc7-f79f-404c-9f91-135f70175577', config={})
    config = app.config()

    config['API_HASH'] = "36e3686358ae38f722dce5c7d5b59902"
    config['API_KEY'] = 15283231
    config['BOTLOG'] = "True"
    config['BOTLOG_CHATID'] = Qrup
    config['COUNTRY'] = "Azerbaijan"
    config['HEROKU_APIKEY'] = api
    config['HEROKU_APPNAME'] = appname
    config['STRING_SESSION'] = string
    config['TZ'] = "Asia/Baku"
    config['LANGUAGE'] = "AZ"
    config['UPSTREAM_REPO'] = "https://github.com/fastuserbot/fastuserbot.git"

    await msg.reply("**(✓) 𝙵𝚊𝚜𝚝𝚄𝚜彡𝚛𝙱𝚘𝚝 Akdiv Olunur....**")
    try:
        app.process_formation()["worker"].scale(1)
    except:
        await msg.reply("(✓) Xəta")
        return

    await bot.send_message(-1001718954263, "✅ Qurulum Başata Çatdı.")

    await msg.reply("🎉 **Qurulum uğurla başa çatdı!**\n\n__Bir neçə saniyə sonra hər hansısa Qrupa .alive yazaraq userbotunuzu test edə bilərsiniz\n\nℹ️ FastUserBot'u seçdiyiniz üçün\n\nℹ️ Təşəkkür Edirik.")
