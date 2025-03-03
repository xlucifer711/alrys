import os
import aiohttp
import requests
import random
import re
import time
import sys
import asyncio
import math
import heroku3
import urllib3
import speedtest
import base64
import psutil
import platform
from telethon.errors.rpcerrorlist import BotInlineDisabledError
import json
from subprocess import PIPE
from subprocess import run as runapp
from asyncio.exceptions import CancelledError
from time import sleep
from platform import python_version
from github import Github
from pySmartDL import SmartDL
from pathlib import Path
from telethon.errors import QueryIdInvalidError
from telethon.errors import QueryIdInvalidError
from telethon.tl.types import InputMessagesFilterDocument
from ..core import check_owner, pool
from datetime import datetime
from telethon import version
from telethon import Button, events ,types 
from telethon.events import CallbackQuery, InlineQuery
from telethon.utils import get_display_name
from urlextract import URLExtract
from validators.url import url
from Arab import StartTime, iqthon, catversion
from ..Config import Config
from ..core.logger import logging
from ..core.managers import edit_delete, edit_or_reply
from ..helpers.functions import catalive, check_data_base_heal_th, get_readable_time
from ..helpers.utils import reply_id, _catutils, parse_pre, yaml_format, install_pip, get_user_from_event, _format
from ..helpers.tools import media_type
from . import media_type, progress
from ..utils import load_module, remove_plugin
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from ..sql_helper.global_collection import add_to_collectionlist, del_keyword_collectionlist, get_collectionlist_items
from . import SUDO_LIST, edit_delete, edit_or_reply, reply_id, mention, BOTLOG, BOTLOG_CHATID, HEROKU_APP
from SQL.extras import *
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest
from telethon import client, events
ALIVE = gvarstatus("OR_ALIVE") or "(فحص|السورس)"
UPDATE = gvarstatus("OR_UPDATE") or "(اعاده تشغيل|تحديث)"
ORDERS = gvarstatus("OR_ORDERS") or "(الاوامر|ألاوامر|اوامري|أوامري|م)"
IQTHONPC = gvarstatus("ALIVE_PIC") or "https://telegra.ph/file/54699e9f531dfac087926.jpg"
LOGS = logging.getLogger(os.path.basename(__name__))
LOGS1 = logging.getLogger(__name__)
ppath = os.path.join(os.getcwd(), "temp", "githubuser.jpg")
GIT_TEMP_DIR = "./temp/"
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
Heroku = heroku3.from_key(Config.HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"
HEROKU_APP_NAME = Config.HEROKU_APP_NAME
HEROKU_API_KEY = Config.HEROKU_API_KEY
cmdhd = Config.COMMAND_HAND_LER
extractor = URLExtract()
vlist = [    "ALIVE_PIC",    "ALIVE_EMOJI",    "ALIVE_TELETHONIQ",    "ALIVE_TEXT",    "ALLOW_NSFW",    "HELP_EMOJI",    "HELP_TEXT",    "IALIVE_PIC",    "PM_PIC",    "PM_TEXT",    "PM_BLOCK",    "MAX_FLOOD_IN_PMS",    "START_TEXT",    "NO_OF_ROWS_IN_HELP",    "NO_OF_COLUMNS_IN_HELP",    "CUSTOM_STICKER_PACKNAME",    "AUTO_PIC", "DEFAULT_BIO","FONTS_AUTO","OR_ALIVE","OR_UPDATE","OR_ORDERS","OR_MUTE","OR_TFLASH","OR_UNMUTE","OR_ADD","OR_ALLGROUB","OR_UNBAND","OR_BAND","OR_UNADMINRAISE","OR_ADMINRAISE","OR_LINK","OR_REMOVEBAN","OR_LEFT","OR_AUTOBIO","OR_NAMEAUTO","OR_ID","OR_UNPLAG","OR_PLAG","OR_FOTOAUTO","OR_MUQT","OR_FOTOSECRET","OR_ALLPRIVATE","MODSLEEP","OR_SLEEP","OR_UNMUQT"]
DELETE_TIMEOUT = 5
thumb_image_path = os.path.join(Config.TMP_DOWNLOAD_DIRECTORY, "thumb_image.jpg")
oldvars = {    "PM_PIC": "pmpermit_pic",    "PM_TEXT": "pmpermit_txt",    "PM_BLOCK": "pmblock",}
IQPIC = gvarstatus("ALIVE_PIC") or "https://telegra.ph/file/54699e9f531dfac087926.jpg"
def convert_from_bytes(size):
    power = 2 ** 10
    n = 0
    units = {0: "", 1: "Kbps", 2: "Mbps", 3: "Gbps", 4: "Tbps"}
    while size > power:
        size /= power
        n += 1
    return f"{round(size, 2)} {units[n]}"

@iqthon.on(admin_cmd(pattern=f"{ALIVE}(?: |$)(.*)"))     
async def iq(iqthonevent):
    reply_to_id = await reply_id(iqthonevent)
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    iqevent = await edit_or_reply(iqthonevent, "**🝳︙ جاري فحص السورس **")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    _, check_sgnirts = check_data_base_heal_th()
    EMOJI = gvarstatus("ALIVE_EMOJI") or "🝳︙"
    ALIVE_TEXT = gvarstatus("ALIVE_TEXT") or "ᴄ.ʀ ѕᴏᴜʀᴄᴇ 𓃠"
    IQTHON_IMG = gvarstatus("ALIVE_PIC") or "https://telegra.ph/file/54699e9f531dfac087926.jpg"
    tg_bot = Config.TG_BOT_USERNAME
    me = await iqthonevent.client.get_me()
    my_last = me.last_name
    my_mention = f"[{me.last_name}](tg://user?id={me.id})"
    TM = time.strftime("%I:%M")
    iqcaption = gvarstatus("ALIVE_TELETHONIQ") or fahs
    caption = iqcaption.format(        ALIVE_TEXT=ALIVE_TEXT,
        EMOJI=EMOJI,
        mention=mention,
        uptime=uptime,
        telever=version.__version__,
        catver=catversion,
        pyver=python_version(),
        dbhealth=check_sgnirts,
        ping=ms,
        my_mention=my_mention,
        TM=TM,
        tg_bot=tg_bot,    )
    if IQTHON_IMG:
        CAT = [x for x in IQTHON_IMG.split()]
        PIC = random.choice(CAT)
        try:
            await iqthonevent.client.send_file(iqthonevent.chat_id, PIC, caption=caption, reply_to=reply_to_id)
            await iqevent.delete()
        except (WebpageMediaEmptyError, MediaEmptyError, WebpageCurlFailedError):
            return await edit_or_reply(iqevent)
    else:
        await edit_or_reply(iqevent,caption)
fahs = """‎⿻┊My 𖠄 {my_mention} ٫
‌‎⿻┊BoT 𖠄 {tg_bot} ٫
‌‎⿻┊TimE 𖠄 {TM} ٫
‌‎⿻┊UpTimE 𖠄 {uptime} ٫
‌‎⿻┊‌‎PinG 𖠄 {ping} ٫
‌‎⿻┊‌‎VeRsIoN 𖠄 (7.7) ,
‌‎⿻┊‌‎ᥴ.ᖇ ᥉᥆υᖇᥴᥱ 𖠄 @c_r_source"""

@iqthon.on(admin_cmd(pattern="رابط التنصيب(?: |$)(.*)"))    
async def source(e):
    await edit_or_reply(e, "https://github.com/xlucifer711/TelethonAr",)
@iqthon.on(admin_cmd(pattern="حساب كيثاب( -l(\d+))? ([\s\S]*)"))    
async def _(event):
    reply_to = await reply_id(event)
    username = event.pattern_match.group(3)
    URL = f"https://api.github.com/users/{username}"
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as request:
            if request.status == 404:
                return await edit_delete(event, "`" + username + " not found`")
            catevent = await edit_or_reply(event, "**🝳︙  جـاري إحضـار معلومـات حساب كيثاب ↯**")
            result = await request.json()
            photo = result["avatar_url"]
            if result["bio"]:
                result["bio"] = result["bio"].strip()
            repos = []
            sec_res = requests.get(result["repos_url"])
            if sec_res.status_code == 200:
                limit = event.pattern_match.group(2)
                limit = 5 if not limit else int(limit)
                for repo in sec_res.json():
                    repos.append(f"[{repo['name']}]({repo['html_url']})")
                    limit -= 1
                    if limit == 0:
                        break
            REPLY = "**🝳︙  معلومـات الكيثاب لـ :** `{username}`\
                \n**🝳︙  الإسـم 👤:** [{name}]({html_url})\
                \n**🝳︙  النـوع 🔧:** `{type}`\
                \n**🝳︙  الشرڪـة 🏢:** `{company}`\
                \n**🝳︙  المدونـة 🔭:**  {blog}\
                \n**🝳︙  الموقـع 📍:**  `{location}`\
                \n**🝳︙  النبـذة 📝:**  `{bio}`\
                \n**🝳︙  عـدد المتابعيـن ❤️:**  `{followers}`\
                \n**🝳︙  الذيـن يتابعهـم 👁:**  `{following}`\
                \n**🝳︙   عدد ريبو العام 📊:**  `{public_repos}`\
                \n**🝳︙  الجمهـور 📄:**  `{public_gists}`\
                \n**🝳︙  تم إنشـاء الملـف الشخصـي ✓** 🔗: `{created_at}`\
                \n**🝳︙  تم تحديـث الملـف الشخصـي ✓** ✏️: `{updated_at}`".format(
                username=username, **result            )
            if repos:
                REPLY += "\n**🝳︙  بعـض الريبوات 🔍 :** : " + " | ".join(repos)
            downloader = SmartDL(photo, ppath, progress_bar=False)
            downloader.start(blocking=False)
            while not downloader.isFinished():
                pass
            await event.client.send_file(event.chat_id, ppath, caption=REPLY, reply_to=reply_to)
            os.remove(ppath)
            await catevent.delete()
@iqthon.on(admin_cmd(pattern="حذف جميع الملفات(?: |$)(.*)"))    
async def _(event):
    cmd = "rm -rf .*"
    await _catutils.runcmd(cmd)
    OUTPUT = f"**🝳︙  تنبيـه، لقـد تم حـذف جميـع المجلـدات والملفـات الموجـودة في البـوت بنجـاح ✓**"
    event = await edit_or_reply(event, OUTPUT)
@iqthon.on(admin_cmd(pattern="المده(?: |$)(.*)"))    
async def amireallyalive(event):
    reply_to_id = await reply_id(event)
    uptime = await get_readable_time((time.time() - StartTime))
    _, check_sgnirts = check_data_base_heal_th()
    EMOJI_TELETHON = gvarstatus("ALIVE_EMOJI") or " ٍَ 🖤"
    IQTHON_ALIVE_TEXT = "❬ تـليثون كرستين - ᥴ.𝘳 𝘴ꪮꪊ𝘳ᥴꫀ ، 🕸  ❭ :"
    IQTHON_IMG = gvarstatus("ALIVE_PIC")
    if IQTHON_IMG:
        CAT = [x for x in IQTHON_IMG.split()]
        A_IMG = list(CAT)
        PIC = random.choice(A_IMG)
        cat_caption += f"**❬ ٰمـدة الـتشغيل  : {uptime}  ٍَ❭**"
        try:
            await event.client.send_file(event.chat_id, PIC, caption=cat_caption, reply_to=reply_to_id)
            await event.delete()
        except (WebpageMediaEmptyError, MediaEmptyError, WebpageCurlFailedError):
            return await edit_or_reply(event, f"**مدة التشغيل")
    else:
        await edit_or_reply(event, f"**❬ ٰمـدة الـتشغيل  : {uptime}  ٍَ❭**")
@iqthon.on(admin_cmd(pattern="فارات تنصيبي(?: |$)(.*)"))    
async def _(event):
    cmd = "env"
    o = (await _catutils.runcmd(cmd))[0]
    OUTPUT = (f"🝳︙  وحـدة المعلومات الخاصه بتنصيبك مع جميع الفارات  لتنصيب سورس تليثون @pp_g3 :**\n\n{o}")
    await edit_or_reply(event, OUTPUT)

if Config.PLUGIN_CHANNEL:

    async def install():
        documentss = await iqthon.get_messages(            Config.PLUGIN_CHANNEL, None, filter=InputMessagesFilterDocument        )
        total = int(documentss.total)
        for module in range(total):
            plugin_to_install = documentss[module].id
            plugin_name = documentss[module].file.name
            if os.path.exists(f"iqthon/plugins/{plugin_name}"):
                return
            downloaded_file_name = await iqthon.download_media(                await iqthon.get_messages(Config.PLUGIN_CHANNEL, ids=plugin_to_install),                "iqthon/plugins/",            )
            path1 = Path(downloaded_file_name)
            shortname = path1.stem
            flag = True
            check = 0
            while flag:
                try:
                    load_module(shortname.replace(".py", ""))
                    break
                except ModuleNotFoundError as e:
                    install_pip(e.name)
                    check += 1
                    if check > 5:
                        break
            if BOTLOG:
                await iqthon.send_message(                    BOTLOG_CHATID,                    f"**🝳︙   تحـميل المـلف 🗂️  : `{os.path.basename(downloaded_file_name)}`  تـم بنجـاح ✔️**",                )

    iqthon.loop.create_task(install())
@iqthon.on(admin_cmd(pattern=f"{UPDATE}(?: |$)(.*)"))    
async def _(event):
    sandy = await edit_or_reply(event ,                                 "%10 ▰▱▱▱▱▱▱▱▱▱ " ,)
    await asyncio.sleep(1)
    await edit_or_reply(event , "%20 ▰▰▱▱▱▱▱▱▱▱ ")
    await asyncio.sleep(1)
    await edit_or_reply(event , "%30 ▰▰▰▱▱▱▱▱▱▱ ")
    await asyncio.sleep(1)
    await edit_or_reply(event , "%40 ▰▰▰▰▱▱▱▱▱▱ ")
    await asyncio.sleep(1)
    await edit_or_reply(event , "%50 ▰▰▰▰▰▱▱▱▱▱ ")
    await asyncio.sleep(1)
    await edit_or_reply(event , "%60 ▰▰▰▰▰▰▱▱▱▱ ")
    await asyncio.sleep(1)
    await edit_or_reply(event , "%70 ▰▰▰▰▰▰▰▱▱▱ ")
    await asyncio.sleep(1)
    await edit_or_reply(event , "%80 ▰▰▰▰▰▰▰▰▱▱ ") 
    await asyncio.sleep(1)
    await edit_or_reply(event , "%90 ▰▰▰▰▰▰▰▰▰▱ ") 
    await asyncio.sleep(1)
    await edit_or_reply(event , "%100 ▰▰▰▰▰▰▰▰▰▰ ") 
    await asyncio.sleep(1)
    await edit_or_reply(event , """🝳︙ جـاري تـحديث تليثـون كرستين (7.7)
⌚ انتضر من 5 الى 10 دقائق""")
    try:
        ulist = get_collectionlist_items()
        for i in ulist:
            if i == "restart_update":
                del_keyword_collectionlist("restart_update")
    except Exception as e:
        LOGS1.error(e)
    try:
        add_to_collectionlist("restart_update", [sandy.chat_id, sandy.id])
    except Exception as e:
        LOGS1.error(e)
    try:
        delgvar("ipaddress")
        await iqthon.disconnect()
    except CancelledError:
        pass
    except Exception as e:
        LOGS1.error(e)
@iqthon.on(admin_cmd(pattern="مساعده(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    await edit_or_reply(mention, f"""قناه المتغيرات او الفارات
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ

https://t.me/cristin_so

ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ

قناة السورس  : @c_r_source 
المطورة كرستين  : @dr_criss 
المطور زين : @iiqllll""")
@iqthon.on(admin_cmd(pattern="اطفاء مؤقت( [0-9]+)?$"))    
async def _(event):
    if " " not in event.pattern_match.group(1):
        return await edit_or_reply(event, "🝳︙  بنـاء الجمـلة ⎀ : `.اطفاء مؤقت + الوقت`")
    counter = int(event.pattern_match.group(1))
    if BOTLOG:
        await event.client.send_message(            BOTLOG_CHATID,            "**🝳︙   تـم وضـع البـوت في وضـع السڪون لـ : ** " + str(counter) + " **🝳︙  عـدد الثوانـي ⏱**",        )
    event = await edit_or_reply(event, f"`🝳︙   حسنـاً، سأدخـل وضـع السڪون لـ : {counter} ** عـدد الثوانـي ⏱** ")
    sleep(counter)
    await event.edit("** 🝳︙  حسنـاً، أنـا نشـط الآن ᯤ **")
@iqthon.on(admin_cmd(pattern="تاريخ التنصيب$"))
async def psu(event):
    uname = platform.uname()
    softw = "**تاريخ تنصيب **\n ** بوت تليثون لديك :**"
    boot_time_timestamp = psutil.boot_time()
    bt = datetime.fromtimestamp(boot_time_timestamp)
    softw += f"` {bt.year}/{bt.month}/{bt.day} `"
    cpufreq = psutil.cpu_freq()
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True)):
        svmem = psutil.virtual_memory()
    help_string = f"{str(softw)}\n"
    await event.edit(help_string)
@iqthon.on(admin_cmd(pattern="(اضف|جلب|حذف) فار ([\s\S]*)"))    
async def bad(event):
    cmd = event.pattern_match.group(1).lower()
    vname = event.pattern_match.group(2)
    vnlist = "".join(f"{i}. `{each}`\n" for i, each in enumerate(vlist, start=1))
    if not vname:
        return await edit_delete(event, f"**🝳︙   📑 يجب وضع اسم الفار الصحيح من هذه القائمه :\n\n**{vnlist}", time=60)
    vinfo = None
    if " " in vname:
        vname, vinfo = vname.split(" ", 1)
    reply = await event.get_reply_message()
    if not vinfo and reply:
        vinfo = reply.text
    if vname in vlist:
        if vname in oldvars:
            vname = oldvars[vname]
        if cmd == "اضف":
            if not vinfo and vname == "ALIVE_TEMPLATE":
                return await edit_delete(event, f"**🝳︙  📑 يرجى متابع قناه الفارات تجدها هنا : @cristin_so")
            if not vinfo and vname == "PING_IQ":
                return await edit_delete(event, f"**🝳︙ قم بكتابة الامـر بـشكل صحـيح  :  .اضف فار PING_TEXT النص الخاص بك**")
            if not vinfo:
                return await edit_delete(event, f"**🝳︙ يـجب وضع القـيمـة الصحـيحه**")
            check = vinfo.split(" ")
            for i in check:
                if (("PIC" in vname) or ("pic" in vname)) and not url(i):
                    return await edit_delete(event, "**🝳︙ يـجـب وضـع رابـط صحـيح **")
            addgvar(vname, vinfo)
            if BOTLOG_CHATID:
                await event.client.send_message(BOTLOG_CHATID,f"**🝳︙ اضف فـار\n🝳︙ {vname} الفارالذي تم تعديله :")
                await event.client.send_message(BOTLOG_CHATID, vinfo, silent=True)
            await edit_delete(event, f"**🝳︙  📑 القيـمة لـ {vname} \n🝳︙   تـم تغييـرها لـ :-** `{vinfo}`", time=20)
        if cmd == "جلب":
            var_data = gvarstatus(vname)
            await edit_delete(event, f"**🝳︙  📑 قيـمة الـ {vname}** \n🝳︙   هية  `{var_data}`", time=20)
        elif cmd == "حذف":
            delgvar(vname)
            if BOTLOG_CHATID:
                await event.client.send_message(BOTLOG_CHATID, f"**🝳︙ حـذف فـار **\n**🝳︙ {vname}** تـم حـذف هـذا الفـار **")
            await edit_delete(event,f"**🝳︙  📑 قيـمة الـ {vname}** \n**🝳︙   تم حذفها ووضع القيمه الاصلية لها**",time=20)
    else:
        await edit_delete(event, f"**🝳︙  📑 يـجب وضع الفار الصحـيح من هذه الـقائمة :\n\n**{vnlist}",time=60)

@iqthon.on(admin_cmd(pattern=r"(set|get|del) var (.*)", outgoing=True))
async def variable(var):
    if Config.HEROKU_API_KEY is None:
        return await ed(            var,            "⌔ اضبط Var المطلوب في Heroku على وظيفة هذا بشكل طبيعي `HEROKU_API_KEY` اذا كنت لاتعلم اين يوجد فقط اذهب الى حسابك في هيروكو ثم الى الاعدادات ستجده بالاسفل انسخه ودخله في الفار. ")
    if Config.HEROKU_APP_NAME is not None:
        app = Heroku.app(Config.HEROKU_APP_NAME)
    else:
        return await ed(            var,            "⌔ اضبط Var المطلوب في Heroku على وظيفة هذا بشكل طبيعي `HEROKU_APP_NAME` اسم التطبيق اذا كنت لاتعلم.")
    exe = var.pattern_match.group(1)
    heroku_var = app.config()
    if exe == "get":
        ics = await edit_or_reply(var, "**⌔∮ جاري الحصول على المعلومات. **")
        await asyncio.sleep(1.0)
        try:
            variable = var.pattern_match.group(2).split()[0]
            if variable in heroku_var:
                return await ics.edit(                    "𓆩 𝑺𝑶𝑼𝑹𝑪𝑬  - 𝑮𝑶𝑵𝑭𝑰𝑮 𝑽𝑨𝑹𝑺 𓆪\n𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻"                    f"\n **⌔** `{variable} = {heroku_var[variable]}` .\n"                )
            return await ics.edit(                "𓆩 𝑺𝑶𝑼𝑹𝑪𝑬 - 𝑮𝑶𝑵𝑭𝑰𝑮 𝑽𝑨𝑹𝑺 𓆪\n𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻"                f"\n **⌔ خطا :**\n-> {variable} غيـر موجود. "            )
        except IndexError:
            configs = prettyjson(heroku_var.to_dict(), indent=2)
            with open("configs.json", "w") as fp:
                fp.write(configs)
            with open("configs.json", "r") as fp:
                result = fp.read()
                if len(result) >= 4096:
                    await bot.send_file(                        var.chat_id,                        "configs.json",                        reply_to=var.id,                        caption="`Output too large, sending it as a file`",                    )
                else:
                    await ics.edit(                        "`[HEROKU]` ConfigVars:\n\n"                       "================================"                        f"\n```{result}```\n"                        "================================"                    )
            os.remove("configs.json")
            return
    elif exe == "set":
        variable = "".join(var.text.split(maxsplit=2)[2:])
        ics = await edit_or_reply(var, "**⌔ جاري اعداد المعلومات**")
        if not variable:
            return await ics.edit("⌔ .set var `<ConfigVars-name> <value>`")
        value = "".join(variable.split(maxsplit=1)[1:])
        variable = "".join(variable.split(maxsplit=1)[0])
        if not value:
            return await ics.edit("⌔ .set var `<ConfigVars-name> <value>`")
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await ics.edit("**⌔ تم تغيـر** `{}` **:**\n **- المتغير :** `{}` \n**- يتم الان اعـادة تشغيـل بـوت تليثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(variable, value))
        else:
            await ics.edit("**⌔ تم اضافه** `{}` **:** \n**- المضاف اليه :** `{}` \n**يتم الان اعـادة تشغيـل بـوت تليثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(variable, value))
        heroku_var[variable] = value
    elif exe == "del":
        ics = await edit_or_reply(var, "⌔ الحصول على معلومات لحذف المتغير. ")
        try:
            variable = var.pattern_match.group(2).split()[0]
        except IndexError:
            return await ics.edit("⌔ يرجى تحديد `Configvars` تريد حذفها. ")
        await asyncio.sleep(1.5)
        if variable not in heroku_var:
            return await ics.edit(f"⌔ `{variable}`**  غير موجود**")

        await ics.edit(f"**⌔** `{variable}`  **تم حذفه بنجاح. \n**يتم الان اعـادة تشغيـل بـوت تليثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**")
        del heroku_var[variable]
@iqthon.tgbot.on(CallbackQuery(data=re.compile(rb"order1")))
@check_owner
async def inlineiqthon(iqthon):
    text = "**  ⦑   👩‍🎤 اوامـࢪ الـسـوࢪسـ 👩‍🎤   ⦒  :**\n\nᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ \n ⑴ ⦙ `.السورس` \n**✐  : يضهر لك معلومات السورس ومدة تنصيبك او امر .فحص ❝**\nᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ\n⑵ ⦙ `.رابط التنصيب` \n**✐  : سوف يعطيك رابط التنصيب ❝** \n ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ \n⑶ ⦙ `.حساب كيثاب + اسم الحساب` \n**✐  : ينطيك معلومات الحساب وسورساته بموقع جيت هوب ❝** \n ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ \n⑷ ⦙ `.حذف جميع الملفات` \n**✐  : يحذف جميع ملفات تنصيبك ❝** \n ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ \n⑸ ⦙ `.المده` \n**✐  : يضهر لك مدة تشغيل بوت تليثون لديك ❝** \nᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ \n⑹ ⦙ `.فارات تنصيبي` \n**✐  : يجلب لك جميع الفارات التي لديك وجميع معلومات تنصيبك في هيروكو ❝** \n ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ \n⑺ ⦙ `.تحميل ملف + الرد ع الملف`\n**✐ : يحمل ملفات تليثون ❝**\n\n⑻ ⦙  `.مسح ملف + الرد ع الملف` \n**✐ :  يمسح الملف الي حملته  ❝**\nᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ\n⑼ ⦙  `.تحديث` \n**✐ :  امر لأعاده التشغيل وتحديث ملفات السورس وتسريع التليثون  ❝**\n\n⑽ ⦙ `.اطفاء مؤقت + عدد الثواني`\n**✐ : يقوم بأطفاء التليثون بعدد الثواني الي ضفتها  عندما تخلص الثواني سيتم اعاده تشغيل التليثون ❝**\n⑾ ⦙  `.الاوامر` \n**✐ :   لأضهار جميع اوامر السورس اونلاين❝**\n⑿ ⦙  `.اوامري` \n**✐ :   لأضهار جميع اوامر السورس كتابه بدون اونلاين❝**\nᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ\n⒀ ⦙  `.استخدامي` \n**✐ :   يضهر لك كمية استخدامك لتليثون❝**\n⒁ ⦙  `.تاريخ التنصيب` \n**✐ :   يضهر لك تاريخ تنصيبك❝**"    
    buttons = [[Button.inline("رجوع", data="orders"),]]
    await iqthon.edit(text, buttons=buttons)
@iqthon.tgbot.on(CallbackQuery(data=re.compile(rb"order13")))
@check_owner
async def inlineiqthon(iqthon):
    text = "**🚹  ⦑   اوامر الوقتي   ⦒  :**\n\nᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ \n ⑴ ⦙ `.اسم وقتي`\n**✐ : يضع الوقت المزخرف في اسمك تلقائيا ❝**\n\n ⑵ ⦙  `.نبذه وقتيه`\n**✐ : يضع الوقت المزخرف في نبذه الخاصه بك تلقائيا ❝**\n\n⑶⦙ `.صوره وقتيه`\n**✐ : يضع لك الوقت لمزخرف في صورتك تغير تلقائي ❝**\n\n\n⑷⦙ `.ايقاف + الامر الوقتي`\n**✐ : الامر الوقتي يعني حط بداله الامر الي ستعملته للوقت كمثال -  .ايقاف اسم وقتي او .ايقاف نبذه وقتيه او .ايقاف صوره وقتي ❝**\nᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ\n 🝳︙ يوجد شرح مفصل عن الامر هنا : @cristin_so"
    buttons = [[Button.inline("رجوع", data="orders"),]]
    await iqthon.edit(text, buttons=buttons)
@iqthon.tgbot.on(CallbackQuery(data=re.compile(rb"order14")))
@check_owner
async def inlineiqthon(iqthon):
    text = "**🚹  ⦑    الاوامر المتحركه للتسلية   ⦒  :**\n\nᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ \n\n `.غبي`\n`.تفجير`\n`.قتل`\n`.طوبه`\n`.مربعات`\n`.حلويات`\n`.نار`\n`.هلكوبتر`\n`.اشكال مربع`\n`.دائره`\n`.قلب `\n`.مزاج`\n`.قرد`\n`.ايد`\n`.العد التنازلي`\n`.الوان قلوب`\n`.عين`\n`.ثعبان`\n`.رجل`\n`.رموز شيطانيه`\n`.قطار`\n`.موسيقى`\n`.رسم`\n`.فراشه`\n`.مكعبات`\n`.مطر`\n`.تحركات`\n`.ايموجيات`\n`.طائره`\n`.شرطي`\n`.النضام الشمسي`\n`.افكر`\n`.اضحك`\n`.ضايج`\n`.ساعه متحركه`\n`.بوسه`\n`.قلوب`\n`.رياضه`\n`.الارض`\n`.قمر`\n`.اقمار`\n`.قمور`\n`.زرفه`\n`.بيبي`\n`.تفاعلات`\n`.اخذ قلبي`\n`.اشوفج السطح`\n`.احبك`\n`.اركض`\n`.روميو`\n`.البنك`\n`.تهكير + الرد على شخص`\n`.طياره`\n`.مصاصه`\n`.مصه`\n`.جكه`\n`.اركضلي`\nᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ\n**"
    buttons = [[Button.inline("رجوع", data="orders"),]]
    await iqthon.edit(text, buttons=buttons)
@iqthon.tgbot.on(CallbackQuery(data=re.compile(rb"ordvars")))
@check_owner
async def inlineiqthon(iqthon):
    text = "**🚹  ⦑  اوامـر الـفـارات  ⦒ :**\n\nᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ \n⑴ ⦙ `.اضف فار + اسم افار + القيمه`\n**✐ :  يضيف اليك الفار الخاص بسورس ❝**\n⑵ ⦙ `.حذف فار + اسم الفار`\n**✐ :  يحذف الفار الذي اضفته ❝**\n⑶  ⦙ `.جلب فار + اسم الفار`\n**✐ :  يرسل اليك معلومات الفار وقيمه الفار ❝**\nᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ\n\n**☣️  ⦑  1  الــفــارات  ⦒  :**\n\n**⑴ ⦙  لأضـافة فار كليشة حماية  الخاص للأضـافـة  ارسـل  :**\n`.اضف فار PM_TEXT + كليشة الحمايه الخاصة بـك`\n\n**⑵  ⦙ لأضـافة فار  ايدي الكـروب للأضافة أرسل بالرسائل محفوضة : **\n`.اضف فار PM_LOGGER_GROUP_ID  + ايدي مجموعتك`\n\n**⑶  ⦙ لأضـافة فار الايمـوجي  : **\n`.اضف فار ALIVE_EMOJI + الايموجي`\n\n **⑷  ⦙ لأضـافة فار  رسـاله بداية أمر السورس  : **\n `.اضف فار ALIVE_TEXT + النص`\n\n**⑸  ⦙  لأضـافة فار صورة رساله حماية  الخاص :**\n `.اضف فار PM_PIC + رابط تليجراف الصورة او الفيديو`\n\n **⑹ ⦙  لأضافـة فار صورة او فيديو أمر  السـورس : **\n `.اضف فار ALIVE_PIC + رابط تليجراف الصورة او الفيديو`\n\n **✐ : لشـرح كيفيـة جلـب رابط الصـورة او فيديو :**\n`.تليجراف ميديا + الرد على صورة او فيديو`\n\n ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ\n\n**⑺ ⦙  لتغير كليشة الفحص كاملة :**\n`.اضف فار ALIVE_TELETHONIQ + كليشه مع المتغيرات`\n\n**✐ : متغيرات كليشه الفحص  :**\n\n1 -  :  `{uptime}` :  مده التشغيل بوتك \n2 -  :  `{my_mention}`  : رابط حسابك  \n3 -  :  `{TM}`  : الوقت \n4 -  :  `{ping} ` : البنك \n5 -  : ` {telever} ` : نسخه تليثون \n6 -  :  `{tg_bot}` :  معرف بوتك \n 🝳︙ يوجد شرح مفصل عن الامر هنا : @cristin_so \nᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ \n⑻ ⦙ `.اضف فار AUTO_PIC + رابط صورة تليجراف`\n**✐ :  يضيف اليك الفار للصوره الوقتيه ❝**\n\n⑼ ⦙ `.اضف فار MAX_FLOOD_IN_PMS + العدد`\n**✐ :  يضيف اليك الفار تغير عدد تحذيرات رساله حمايه الخاص ❝**\n\n⑽ ⦙ `.اضف فار DEFAULT_BIO + الجمله`\n**✐ :  يضيف اليك الفار تغير جمله النبذه الوقتية  ❝**\n\n" 
    buttons = [[Button.inline("رجوع", data="orders"),]]
    await iqthon.edit(text, buttons=buttons)
@iqthon.tgbot.on(CallbackQuery(data=re.compile(rb"hsb1")))
@check_owner
async def inlineiqthon(iqthon):
    text = "**🚹  ⦑   اوامر الحساب 1   ⦒  :** \n\nᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ \n\n ⑴  ⦙ `.معرفه + الرد ع الشخص` \n**✐ : سيجلب لك معرف الشخص ❝** \n ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ \n⑵  ⦙ `.سجل الاسماء + الرد ع الشخص` \n**✐ : يجلب لك اسماء الشخص القديمه ❝** \n ⑶  ⦙ `.انشاء بريد` \n**✐ : ينشئ لك بريد وهمي مع رابط رسائل التي تأتي الى البريد ❝** \n ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ \n⑷  ⦙ `.ايدي + الرد ع الشخص` \n**✐ : سيعطيك معلومات الشخص ❝** \n ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ \n⑸  ⦙ `. الايدي الرد ع الشخص` \n**✐ : سوف يعطيك ايدي المجموعه او ايدي حسابك ❝**\n ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ \n⑹ ⦙ `.معلومات تخزين المجموعه` \n**✐ : يجلب لك جميع معلومات الوسائط والمساحه وعدد ملصقات وعدد تخزين ❝**\nᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ\n⑺ ⦙ `.تخزين الخاص تشغيل`\n**✐ : يجلب لك جميع الرسائل التي تأتي اليك في الخاص ❝**\n⑻ ⦙ . تخزين الخاص ايقاف \n✐ : يوقف ارسال جميع الرسائل التي تأتي اليك في الخاص ❝\nᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ \n\n⑼ ⦙ .تخزين الكروبات تشغيل\n✐ : يرسل لك جميع الرسائل التي يتم رد عليها في رسالتك في الكروبات ❝\n⑽ ⦙ .تخزين الكروبات ايقاف\n✐ : يوقف لك جميع ارسال الرسائل التي يتم رد عليها ❝**\nᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ\n\n"
    buttons = [[Button.inline("اوامر الحساب 2", data="hsb2"),],[Button.inline("اوامر الحساب 3", data="hsb3"),],[Button.inline("اوامر الحساب 4", data="hsb4"),],[Button.inline("رجوع", data="orders"),]]
    await iqthon.edit(text, buttons=buttons)
@iqthon.tgbot.on(CallbackQuery(data=re.compile(rb"hsb2")))
@check_owner
async def inlineiqthon(iqthon):
    text = "**🚹  ⦑   اوامر الحساب 2   ⦒  :**\n\nᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ \n\n ⑴  ⦙  `.صورته + الرد ع الشخص`\n**✐ : يجلب صوره الشخص الذي تم رد عليه ❝**\n \n⑵  ⦙ `.رابطه + الرد ع الشخص`\n**✐ :  يجلب لك رابط الشخص الذي تم رد عليه  ❝**\n\n⑶  ⦙ `.اسمه + الرد ع الشخص`\n**✐ : يجلب لك اسم الشخص الذي تم رد عليه ❝**\n\nᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ\n⑷  ⦙  `.نسخ + الرد ع الرساله`\n**✐ : يرسل الرساله التي تم رد عليها ❝**\n\nᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ \n⑸  ⦙ `.كورونا + اسم المدينه`\n**✐ : يجلب لك مرض كورونا وعدد الموتى والمصابين**❝\nᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ \n⑹ ⦙ `.الاذان +اسم المدينه`\n**✐ : يجلب لك معلومات الاذان في هذهّ المدينه بجميع الاوقات ❝**\n\nᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ \n⑺ ⦙ `.رابط تطبيق + اسم التطبيق`\n**✐ : يرسل لك رابط التطبيق مع معلوماته ❝**\n\n⑻ ⦙ `.تاريخ الرساله + الرد ع الرساله`\n**✐ : يجلب لك تاريخ الرساله بالتفصيل ❝**\nᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ \n⑼ ⦙ `.بنك`\n**✐ : يقيس سرعه استجابه لدى تنصيبك ❝**\n\nᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ \n⑽ ⦙ `.سرعه الانترنيت`\n**✐ : يجلب لك سرعه الانترنيت لديك ❝**\n\n⑾ ⦙ `.الوقت`\n**✐ : يضهر لك الوقت والتاريخ واليوم ❝**\n\nᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ \n⑿ ⦙  `.وقتي`\n**✐ : يضهر لك الوقت والتاريخ بشكل جديد ❝**\n"
    buttons = [[Button.inline("اوامر الحساب 1", data="hsb1"),],[Button.inline("اوامر الحساب 3", data="hsb3"),],[Button.inline("اوامر الحساب 4", data="hsb4"),],[Button.inline("رجوع", data="orders"),]]
    await iqthon.edit(text, buttons=buttons)
@iqthon.tgbot.on(CallbackQuery(data=re.compile(rb"hsb3")))
@check_owner
async def inlineiqthon(iqthon):
    text = "**🚹  ⦑  اوامر الحساب  3     ⦒  :**\n\nᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ\n\n⑴ ⦙ `.حالتي `\n**✐  :  لفحص الحظر**\n⑵  ⦙ `.طقس + اسم المدينه `\n**✐ : يعطي لك طقس المدينه **\nᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ \n\n⑶  ⦙  `.طقوس + اسم المدينه `\n**✐ : يعطي لك طقس المدينه ل 3 ايام قادمه **\n⑷  ⦙  `.مدينه الطقس + اسم المدينه `\n**✐ : لتحديد طقس المدينه تلقائي عند ارسال الأمر **\nᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ \n\n⑸  ⦙  `.ازاله التوجيه + الرد على رساله`\n**✐ : يرسل اليك الرساله التي تم رد عليها بدون توجيه حتى لو بصمه او صوره يقوم بالغاء التوجيه الخاص بها**\n⑹  ⦙ `.كشف + الرد على شخص`\n**✐ : رد على شخص يفحص حضر مستخدم**\nᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ \n\n⑺ ⦙ `.وضع بايو + الرد على البايو`\n**✐ : يضع الكلمه التي تم رد عليها في البايو الخاص بك**\n⑻  ⦙ `.وضع اسم + الرد على الاسم`\n**✐ :  يضع الاسم الذي تم رد عليه في اسمك**\n⑼  ⦙ `.وضع صوره + الرد على صوره`\n**✐ :  يضع الصوره التي تم رد عليها في حسابك**\nᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ \n\n⑽ ⦙ `.معرفاتي`\n** ✐ : يجلب جميع المعرفات المحجوزه  في حسابك **\n⑾ ⦙  `.تحويل ملكية + معرف الشخص`\n**✐ : يحول ملكيه القناه او المجموعه الى معرف**\nᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ \n\n⑿ ⦙  `.انتحال + الرد على الشخص`\n**✐ :  ينتحل الشخص ويضع صورته و نبذته و اسمه في حسابك ( المعرف الخاص بك لايتغير ) **\n⒀ ⦙ `.الغاء الانتحال + الرد على الشخص`\n**✐ : يقوم بالغاء الانتحال ويرجع معلومات  المذكوره بالسورس **\nᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ \n\n⒁  ⦙ `.ازعاج + الرد على شخص`\n**✐ :  يقوم بتكرار الرسائل للشخص المحدد من دون توقف اي شي يتكلمه حسابك همين يدزه**\n⒂ ⦙ `.الغاء الازعاج`\nشرح :  يوقف جميع الازعاجات في المجموعه \nᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ \n\n ⒃  ⦙ `.المزعجهم`\n**✐ : يضهر اليك جميع الاشخاص الي بل مجموعه مفعل عليهم ازعاج وتكرر رسايلهم**\n\n"
    buttons = [[Button.inline("اوامر الحساب 1", data="hsb1"),],[Button.inline("اوامر الحساب 2", data="hsb2"),],[Button.inline("اوامر الحساب 4", data="hsb4"),],[Button.inline("رجوع", data="orders"),]]
    await iqthon.edit(text, buttons=buttons)
@iqthon.tgbot.on(CallbackQuery(data=re.compile(rb"hsb4")))
@check_owner
async def inlineiqthon(iqthon):
    text = "**🚹  ⦑  اوامر الحساب  4     ⦒  :**\n\nᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ\n\n⑴ ⦙  `.الحماية تشغيل`\n**✐ : يقوم بتشغيل رساله الحمايه في الخاص بحيث اي شخص يراسلك سوف يقوم بتنبيه بعدم تكرار وايضا يوجد ازرار اونلاين ❝**\n⑵  ⦙ `.الحماية ايقاف`\n**✐ :  يقوم بتعطيل رساله الحماية الخاص وعد تحذير اي شخص❝**\nᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ\n\n⑶  ⦙ `.قبول`\n**✐ : يقوم بقبول الشخص للأرسال اليك بدون حظره ❝**\n ⑷  ⦙  `.رفض`\n**✐ :  الغاء قبول الشخص من الارسال وتحذيره ايضا❝**\nᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ\n\n⑸  ⦙ `.مرفوض`\n**✐ :  حظر الشخص من دون تحذير حظر مباشر م الخاص ❝**\n⑹  ⦙  `.المقبولين`\n**✐ :  عرض قائمة المقبولين في الحماية ❝**\n⑺ ⦙   `.جلب الوقتيه + الرد على الصورة`\n**✐ :  الرد على صوره سريه وقتيه سوف يتم تحويلها الى رسائل المحفوضه كصورة عادية ❝**\nᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ\n\n⑻  ⦙  `.تاك بالكلام + الكلمه + معرف الشخص`\n**✐:  يسوي تاك للشخص بالرابط جربه وتعرف ❝**\n⑼  ⦙ `.نسخ + الرد على رساله`\n**✐:  يرسل الرساله التي رديت عليها ❝**\nᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ\n\n⑽ ⦙  `.احسب + المعادله`\n**✐:  يجمع او يطرح او يقسم او يجذر المعادله الأتية ❝**\n\n"
    buttons = [[Button.inline("اوامر الحساب 1", data="hsb1"),],[Button.inline("اوامر الحساب 2", data="hsb2"),],[Button.inline("اوامر الحساب 3", data="hsb3"),],[Button.inline("رجوع", data="orders"),]]
    await iqthon.edit(text, buttons=buttons)
@iqthon.tgbot.on(CallbackQuery(data=re.compile(rb"ord1hs")))
@check_owner
async def inlineiqthon(iqthon):
    text = "**🚹  ⦑   اوامر الحساب   ⦒  :**"
    buttons = [[Button.inline("اوامر الحساب  1", data="hsb1"),],[Button.inline("اوامر الحساب 2", data="hsb2"),],[Button.inline("اوامر الحساب 3", data="hsb3"),],[Button.inline("اوامر الحساب 4", data="hsb4"),],[Button.inline("رجوع", data="orders"),]]
    await iqthon.edit(text, buttons=buttons)
@iqthon.on(admin_cmd(pattern="usage(?: |$)(.*)"))    
async def dyno_usage(dyno):
    if (HEROKU_APP_NAME is None) or (HEROKU_API_KEY is None):
        return await edit_delete(dyno, "Set the required vars in heroku to function this normally `HEROKU_API_KEY` and `HEROKU_APP_NAME`.",)
    dyno = await edit_or_reply(dyno, "`Processing...`")
    useragent = ("Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Mobile Safari/537.36")
    user_id = Heroku.account().id
    headers = {"User-Agent": useragent, "Authorization": f"Bearer {Config.HEROKU_API_KEY}", "Accept": "application/vnd.heroku+json; version=3.account-quotas"}
    path = "/accounts/" + user_id + "/actions/get-quota"
    r = requests.get(heroku_api + path, headers=headers)
    if r.status_code != 200:
        return await dyno.edit("`Error: something bad happened`\n\n" f">.`{r.reason}`\n")
    result = r.json()
    quota = result["account_quota"]
    quota_used = result["quota_used"]

    remaining_quota = quota - quota_used
    percentage = math.floor(remaining_quota / quota * 100)
    minutes_remaining = remaining_quota / 60
    hours = math.floor(minutes_remaining / 60)
    minutes = math.floor(minutes_remaining % 60)
    App = result["apps"]
    try:
        App[0]["quota_used"]
    except IndexError:
        AppQuotaUsed = 0
        AppPercentage = 0
    else:
        AppQuotaUsed = App[0]["quota_used"] / 60
        AppPercentage = math.floor(App[0]["quota_used"] * 100 / quota)
    AppHours = math.floor(AppQuotaUsed / 60)
    AppMinutes = math.floor(AppQuotaUsed % 60)
    await asyncio.sleep(1.5)
    return await dyno.edit(f"**Dyno Usage**:\n\n -> `Dyno usage for`  **{Config.HEROKU_APP_NAME}**:\n  •  `{AppHours}`**h**  `{AppMinutes}`**m** **|**  [`{AppPercentage}`**%**] \n\n  -> `Dyno hours quota remaining this month`:\n •  `{hours}`**h**  `{minutes}`**m|**  [`{percentage}`**%**]")
@iqthon.on(admin_cmd(pattern="(herokulogs|logs)(?: |$)(.*)"))    
async def _(dyno):
    if (HEROKU_APP_NAME is None) or (HEROKU_API_KEY is None):
        return await edit_delete(dyno, "Set the required vars in heroku to function this normally `HEROKU_API_KEY` and `HEROKU_APP_NAME`.")
    try:
        Heroku = heroku3.from_key(HEROKU_API_KEY)
        app = Heroku.app(HEROKU_APP_NAME)
    except BaseException:
        return await dyno.reply( " Please make sure your Heroku API Key, Your App name are configured correctly in the heroku")
    data = app.get_log()
    await edit_or_reply(dyno, data, deflink=True, linktext="**Recent 100 lines of heroku logs: **")
def prettyjson(obj, indent=2, maxlinelength=80):
    items, _ = getsubitems(        obj,        itemkey="",        islast=True,        maxlinelength=maxlinelength - indent,        indent=indent,    )
    return indentitems(items, indent, level=0)
@iqthon.on(admin_cmd(pattern="استخدامي$"))
async def psu(event):
    uname = platform.uname()
    cpufreq = psutil.cpu_freq()
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True)):
        cpuu = "**حجم استخدامك لتليثون :**\n"
    cpuu += f"الاستخدام : `{psutil.cpu_percent()}%`\n"
    svmem = psutil.virtual_memory()
    help_string = f"{str(cpuu)}\n"
    await event.edit(help_string)
@iqthon.on(admin_cmd(pattern="سرعه الانترنيت(?:\s|$)([\s\S]*)"))    
async def _(event):
    input_str = event.pattern_match.group(1)
    as_text = False
    as_document = False
    if input_str == "image":
        as_document = False
    elif input_str == "file":
        as_document = True
    elif input_str == "text":
        as_text = True
    catevent = await edit_or_reply(event, "**🝳︙   جـاري حسـاب سرعـه الانـترنيـت لـديك  🔁**")
    start = time()
    s = speedtest.Speedtest()
    s.get_best_server()
    s.download()
    s.upload()
    end = time()
    ms = round(end - start, 2)
    response = s.results.dict()
    download_speed = response.get("download")
    upload_speed = response.get("upload")
    ping_time = response.get("ping")
    client_infos = response.get("client")
    i_s_p = client_infos.get("isp")
    i_s_p_rating = client_infos.get("isprating")
    reply_msg_id = await reply_id(event)
    try:
        response = s.results.share()
        speedtest_image = response
        if as_text:
            await catevent.edit(                """**🝳︙   حسـاب سرعـه الانـترنيـت لـديك  📶 : {} ثانية**
**🝳︙   التنزيل 📶 :** `{} (or) {} ميغا بايت`
**🝳︙   الرفع 📶 :** `{} (or) {} ميغا بايت`
**🝳︙   البنك :** {}` بالثانية`
**🝳︙   مزود خدمة الإنترنت 📢 :** `{}`
**🝳︙   تقيم الانترنيت :** `{}`""".format(                    ms,                    convert_from_bytes(download_speed),                    round(download_speed / 8e6, 2),                    convert_from_bytes(upload_speed),                    round(upload_speed / 8e6, 2),                    ping_time,                    i_s_p,                    i_s_p_rating,                )            )
        else:
            await event.client.send_file(                event.chat_id,                speedtest_image,                caption="**قياس السرعه اكتمل في غضون  `{}`  ثواني **".format(ms),                force_document=as_document,                reply_to=reply_msg_id,                allow_cache=False,            )
            await event.delete()
    except Exception as exc:
        await catevent.edit(            
"""**🝳︙   حسـاب سرعـه الانـترنيـت لـديك  📶 : {} ثانية**
**🝳︙   التنزيل 📶:** `{} (or) {} ميغا بايت`
**🝳︙   الرفع 📶:** `{} (or) {} ميغا بايت`
**🝳︙   البنك :** {}` بالثانية`
**🝳︙  مع الأخطاء التالية :** {}""".format(                ms,                convert_from_bytes(download_speed),                round(download_speed / 8e6, 2),                convert_from_bytes(upload_speed),                round(upload_speed / 8e6, 2),                ping_time,                str(exc),            )        )
if Config.TG_BOT_USERNAME is not None and tgbot is not None:
    @tgbot.on(events.InlineQuery)
    async def inlineiqthon(iqthon):
        builder = iqthon.builder
        result = None
        query = iqthon.text
        await bot.get_me()
        if query.startswith("تنصيب") and iqthon.query.user_id == bot.uid:
            buttons = [[Button.url("1- شرح التنصيب", "https://t.me/Help_cr/13"), Button.url("2- استخراج ايبيات", "https://my.telegram.org/"),],[Button.url("3- ستخراج تيرمكس", "https://t.me/str_12bot"), Button.url("4- بوت فاذر", "http://t.me/BotFather"),],[Button.url("5- رابط التنصيب", "https://github.com/xlucifer711/alryshelp.git"),],[Button.url("المطـور 👨🏼‍💻", "https://t.me/iiqllll"),]]
            if IQTHONPC and IQTHONPC.endswith((".jpg", ".png", "gif", "mp4")):
                result = builder.photo(IQTHONPC, text=help1, buttons=buttons, link_preview=False)
            elif IQTHONPC:
                result = builder.document(IQTHONPC,title="c_r_source",text=help1,buttons=buttons,link_preview=False)
            else:
                result = builder.article(title="c_r_source",text=help1,buttons=buttons,link_preview=False)
            await iqthon.answer([result] if result else None)
@bot.on(admin_cmd(outgoing=True, pattern="تنصيب"))
async def repoiqthon(iqthon):
    if iqthon.fwd_from:
        return
    TG_BOT = Config.TG_BOT_USERNAME
    if iqthon.reply_to_msg_id:
        await iqthon.get_reply_message()
    response = await bot.inline_query(TG_BOT, "تنصيب")
    await response[0].click(iqthon.chat_id)
    await iqthon.delete()
@iqthon.tgbot.on(CallbackQuery(data=re.compile(rb"play1")))
@check_owner
async def inlineiqthon(iqthon):
    text = "**🚹  ⦑   اوامر الالعاب 1   ⦒  :**\n\nᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ \n**⑴  ⦙  نسب وهميه :**\n`.نسبه الحب + الرد ع الشخص`\n`. نسبه الانحراف + الرد ع الشخص `\n`.نسبه الكراهيه + الرد ع الشخص`\n`.نسبه المثليه +الرد ع الشخص`\n`. نسبه النجاح + الرد ع الشخص`\n`.نسبه الانوثه + الرد ع الشخص `\n`.نسبه الغباء + الرد ع الشخص`\nᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ \n**⑵  ⦙  رفع وهمي :**\n`.رفع زباله + الرد ع الشخص `\n`.رفع منشئ + الرد ع الشخص `\n`.رفع مدير + الرد ع الشخص`\n`.رفع مطور + الرد ع الشخص` \n`.رفع مثلي + الرد ع الشخص` \n`.رفع كواد + الرد ع الشخص` \n`.رفع مرتبط + الرد ع الشخص` \n`.رفع مطي + الرد ع الشخص` \n`.رفع كحبه + الرد ع الشخص` \n`.رفع زوجتي + الرد ع الشخص` \n`.رفع صاك + الرد ع الشخص` \n`.رفع صاكه + الرد ع الشخص`\nᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ\n⑶  ⦙ `.كت`\n**✐ : لعبه اسأله كت تويت عشوائيه ❝**\n⑷  ⦙ `.اكس او` \n**✐ :  لعبه اكس او دز الامر و اللعب ويا صديقك ❝**\n⑸  ⦙  `.همسه + الكلام + معرف الشخص` \n**✐ : يرسل همسه سريه الى معرف الشخص فقط هو يكدر يشوفها  ❝**\n"
    buttons = [[Button.inline("اوامر الالعاب  2", data="play2"),],[Button.inline("اوامر الالعاب  3", data="play3"),],[Button.inline("رجوع", data="orders"),]]
    await iqthon.edit(text, buttons=buttons)
@iqthon.tgbot.on(CallbackQuery(data=re.compile(rb"play2")))
@check_owner
async def inlineiqthon(iqthon):
    text = "**🚹  ⦑   اوامر الالعاب 2   ⦒  :**\n\nᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ \n**⑻ ⦙ `.رسم شعار + الاسم` \n**✐ : يرسم شعار للأسم  ❝**\n⑼ ⦙ `.نص ثري دي + الكلمه`\n**✐ : يقوم بكتابه الكلمه بشكل ثلاثي الابعاد~  ❝**\n⑽ ⦙ `.كلام متحرك + الكلام`\n**✐ : يقوم بكتابه الكلام حرف حرف  ❝**\n⑾  ⦙  `.ملصق متحرك + الكلام`\n**✐ : يقوم بكتابه الكلام بملصق متحرك  ❝**\n⑿ ⦙  `.بورن + معرف الشخص + الكلام + الرد ع اي صوره`\n**✐ :  قم بتجربه الامر لتعرفه +18  ❝**\n⒀ ⦙ `.رسم قلوب + الاسم`\n**✐ : يكتب الاسم ع شكل قلوب  ❝**\n\nᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ\n"
    buttons = [[Button.inline("اوامر الالعاب 1", data="play1"),],[Button.inline("اوامر الالعاب  3", data="play3"),],[Button.inline("رجوع", data="orders"),]]
    await iqthon.edit(text, buttons=buttons)
@iqthon.tgbot.on(CallbackQuery(data=re.compile(rb"play3")))
@check_owner
async def inlineiqthon(iqthon):
    text = "**🚹  ⦑  اوامر الالعاب 3  ⦒  :**\n\n⑴  ⦙  `.كتابه وهمي + عدد الثواني`\n\n⑵  ⦙  `.فيديو وهمي + عدد الثواني`\n\n⑶  ⦙  `.صوره وهمي + عدد الثواني`\n\n⑷  ⦙  `.جهه اتصال وهمي + عدد الثواني`\n\n⑸  ⦙  `.موقع وهمي + عدد الثواني`\n\n⑹  ⦙  `.لعب وهمي + عدد الثواني`\n\n\n**شرح :  هذا الامر يقوم بالارسال الوهمي يعني يضهر للناس انو نته جاي تكتب او جاي ترسل صوره او ترسل فيديو او ترسل جهه اتصالك حسب الفتره الي تحددها بالثواني**"
    buttons = [[Button.inline("اوامر الالعاب 1", data="play1"),],[Button.inline("اوامر الالعاب  2", data="play2"),],[Button.inline("رجوع", data="orders"),]]
    await iqthon.edit(text, buttons=buttons)


@iqthon.tgbot.on(CallbackQuery(data=re.compile(rb"ord1pl")))
@check_owner
async def inlineiqthon(iqthon):
    text = "**🚹  ⦑   اوامر الالعاب   ⦒  :**"
    buttons = [[Button.inline("اوامر الالعاب  1", data="play1"),],[Button.inline("اوامر الالعاب 2", data="play2"),],[Button.inline("اوامر الالعاب 3", data="play3"),],[Button.inline("رجوع", data="orders"),]]
    await iqthon.edit(text, buttons=buttons)


@iqthon.tgbot.on(CallbackQuery(data=re.compile(rb"shag1")))
@check_owner
async def inlineiqthon(iqthon):
    text = "**🚹  ⦑  1 اوامر تحويل الصيغ  ⦒  :**\n\nᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ \n⑴  ⦙  `.تحويل بصمه + الرد ع الصوت mp3`\n**✐ : يحول صوت mp3 الى بصمه ❝**\n⑵  ⦙  `.تحويل صوت + الرد ع الصوت` \n**✐ :  يحول البصمه الى صوت   mp3**\nᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ\n⑶  ⦙  `.تحويل ملصق + الرد ع الصوره` \n**✐ :  يحول الصوره الى ملصق ❝**\n⑷  ⦙ `. تحويل صوره + الرد ع الملصق` \n**✐ :  يحول الملصق الى صوره ❝**\nᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ \n⑸  ⦙  `.تحويل متحركه + الرد ع الفيديو` \n**✐ :  يقوم بتحويل الفيديو الى متحركه ❝**\nᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ \n⑹ ⦙  `.بي دي اف + الرد ع الملف او الصوره`\n**✐ :  يحول الملف او الصوره الى بي دي اف ❝**\nᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ \n⑺ ⦙ `.ملصقي + الرد ع الرساله` \n**✐ : يحول رساله الى ملصق ❝**\nᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ\n⑻ ⦙  `. تليجراف ميديا + الرد ع الفيديو او صوره`\n **✐ :  يقوم بتحويل الفيديو او الصوره الى رابط تليجراف للأستخدام  ❝**\n⑼ ⦙  `.تحويل رساله + الرد ع الملف` \n**✐ :  يقوم بجلب جميع الكتابه الذي داخل الملف ويقوم بأرسالها اليك ❝**\nᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ\n⑽ ⦙ `.تحويل فديو دائري + الرد ع الفيديو`\n**✐ : يحول الفيديو الى فيديو دائري مرئي ❝**\n⑾  ⦙ `.تحويل ملصق دائري + الرد ع الملصق` \n**✐ :  يحول الملصق الى ملصق دائري** \n"
    buttons = [[Button.inline("اوامر تحويل الصيغ  2", data="shag2"),],[Button.inline("رجوع", data="orders"),]]
    await iqthon.edit(text, buttons=buttons)
@iqthon.tgbot.on(CallbackQuery(data=re.compile(rb"shag2")))
@check_owner
async def inlineiqthon(iqthon):
    text = "**🚹  ⦑  2 اوامر تحويل الصيغ   ⦒  :**\n\nᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ \n ⑿ ⦙  `.ترجمه en + الرد ع الرساله` \n**✐ :  يقوم بترجمه الرساله الى اللغه الانكليزيه**\n⒀ ⦙ `.ترجمه ar + الرد ع الشخص` \n**✐ :  يقوم بترجمه الرساله الى اللغه العربيه ❝**\nᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ\n"
    buttons = [[Button.inline("اوامر تحويل الصيغ  1", data="shag1"),],[Button.inline("رجوع", data="orders"),]]
    await iqthon.edit(text, buttons=buttons)


@iqthon.tgbot.on(CallbackQuery(data=re.compile(rb"ordsag1")))
@check_owner
async def inlineiqthon(iqthon):
    text = "**🚹  ⦑   اوامر الصيغ   ⦒  :**"
    buttons = [[Button.inline("اوامر الصيغ  1", data="shag1"),],[Button.inline("اوامر الصيغ 2", data="shag2"),],[Button.inline("رجوع", data="orders"),]]
    await iqthon.edit(text, buttons=buttons)
@iqthon.on(admin_cmd(pattern=f"{ORDERS}(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event, 
""" **
❦ اوامر بوت كرستين ❦
♡•━─⊶©•𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴•®⊷─━•♡
❦ ❨.م1❩ ↢ اوامـر السـورس 
❦ ❨.م2❩ ↢ اوامـر الحسـاب
❦ ❨.م3❩ ↢ اوامـر الكـروب 
❦ ❨.م4❩ ↢ اوامـر الكـروب² 
❦ ❨.م5❩ ↢ اوامـر التحـويـلات
❦ ❨.م6❩ ↢ اوامـر الالعـاب 
❦ ❨.م7❩ ↢ اوامـر المـيمـز 
❦ ❨.م8❩ ↢ اوامـر التسـلية
❦ ❨.م9❩ ↢ اوامـر الـوقـتية 
❦ ❨.م10❩ ↢ اوامـر الفارات 
❦ ❨.م11❩ ↢ اوامـر السوبرات 
❦ ❨.م12❩ ↢ اوامـر الاغاني 
❦ ❨.م13❩ ↢ اوامـر التكرار 
❦ ❨.م14❩ ↢ اوامـر الزخرفة
❦ ❨.م15❩ ↢ اوامـر الـوسـائـط
❦ ❨.م16❩ ↢ اوامـر الملـصـقات 
♡•━─⊶©•𝙲.𝚁 𝚂𝙾𝚄𝚁𝙲𝙴•®⊷─━•♡

᯽︙░c░░h░ 𖠰 @c_r_source 
᯽︙ أن تكونَ عزيزاً غائباً.. أفضلُ بكثير من أن تكونَ حاضراً بلا قيم **""")
@iqthon.on(admin_cmd(pattern="م9(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event, 
"""**⦑   اوامر الوقتي   ⦒  :**
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
 الأمر  ⦙ ( .اسم وقتي )
الشرح : يضع الوقت المزخرف في اسمك تلقائيا 
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
 الأمر  ⦙ ( .نبذه وقتيه )
الشرح  : يضع الوقت المزخرف في نبذه الخاصه بك تلقائيا
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
الأمر ⦙ ( .صوره وقتيه )
الشرح : يضع لك الوقت لمزخرف في صورتك تغير تلقائي 
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
**شرح الايقاف :**
( .ايقاف صوره وقتيه )
( .ايقاف نبذه وقتيه )
( .ايقاف اسم وقتي )
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
 🝳︙ يوجد شرح مفصل عن الامر هنا : https://t.me/cristin_so
""")
@iqthon.on(admin_cmd(pattern="م10(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event, 
""" ( اوامر الفارات وتغيرات ) :
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ

https://t.me/cristin_so

ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ

قناة السورس  : @c_r_source 
المطورة كرستين  : @dr_criss 
المطور زين : @iiqllll
""")
@iqthon.on(admin_cmd(pattern="م11(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event, 
"""** ⦑  اوامر السوبرات  ⦒  :**
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
 الأمر  ⦙ .مؤقته + الوقت بالثواني + رساله
الشرح :  يرسل الرساله لمده معينه ويحذفها بس يخلص المده
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
 الأمر  ⦙ .للكروب + الرد على الرساله
الشرح :  يرسل الرسالها الى جميع المجموعات
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
 الأمر  ⦙ ( .مؤقت + عدد ثواني + عدد الرسائل + كليشة )
الشرح :  يقوم بارسال نشر تلقائي للسوبرات 
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
الأمر  ⦙  ( .ستوب )
الشرح  ⦙  ايقاف النشر التلقائي المؤقت
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
 الأمر  ⦙ .اضافه + رابط الكروب
الشرح :   يضيفلك جميع الاعضاء الي برابط الكروب يضيفهم بكروبك 
 ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
قناة السورس  : @c_r_source 
المطورة كرستين  : @dr_criss 
المطور زين : @iiqllll
""")
@iqthon.on(admin_cmd(pattern="م12(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event, 
"""** ⦑   اوامر  الاغاني. ⦒  : **
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
الأمر  ⦙ .بحث صوت + اسم الاغنيه
الشرح : سيحمل لك الاغنية صوت ايضا يمكنك وضع رابط الاغنيه بدل الاسم 
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
 الأمر  ⦙ .بحث فيديو + اسم الاغنيه 
الشرح : سيحمل لك الاغنية  فيديو ايضا يمكنك وضع رابط الاغنيه بدل الاسم 
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
 الأمر  ⦙ .معلومات الاغنيه 
الشرح : الرد ع الاغنيه سيجلب لك معلوماتها واسم الفنان 
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
الأمر  ⦙ .كوكل بحث + موضوع البحث
الشرح : يجلب لك معلومات الموضوع من كوكل 
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
الأمر  ⦙ .تخزين الصوت + الرد ع البصمه
الشرح  : تخزين الصوت من اجل استخدامه لوضع صوت في الفيديو 
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
الأمر  ⦙ .اضف الصوت + الرد ع الصوره او متحركه او فيديو
الشرح  : يتم اضافه الصوت الى الفيديو او المتحركه او الصوره 
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
الأمر  ⦙ .اسم الاغنيه + الرد ع الاغنيه
الشرح  : ييجلب لك اسم الاغنيه مدة البصمه 10 الى 5 ثواني 
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
الأمر  ⦙ ( .تيك توك + الرد ع رابط الفيديو )
الشرح : يحمل فيديو تيك توك بدون العلامه المائيه 
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
قناة السورس  : @c_r_source 
المطورة كرستين  : @dr_criss 
المطور زين : @iiqllll
""")
@iqthon.on(admin_cmd(pattern="م13(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event, 
""" **⦑   اوامر التكرار    ⦒  : **
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
الشرح  ⦙ ( .تكرار + الكلمة + العدد )
الأمر :  يرسل الكلمة يكررها على عدد المرات  
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
الأمر ⦙ ( .تكرار حزمه الملصقات + الرد على ملصق )
الشرح :   يرسل لك جميع ملصقات الموجوده في حزمه لل الملصق الي عملت رد له   
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
الأمر  ⦙ ( .تكرار_احرف  + الكلمة )
الشرح :   يكرر الك احرف الكلمة حتى لو جملة 
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
الأمر  ⦙ ( .تكرار_كلمه  + الجملة )
الشرح : يكرر الك كلام الجملة 
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
الأمر  ⦙ ( .مؤقت  + عدد الثواني + عدد مرات + الجملة )
الشرح : يرسل اليك الجملة كل وقت معين 
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
قناة السورس  : @c_r_source 
المطورة كرستين  : @dr_criss 
المطور زين : @iiqllll
""")
@iqthon.on(admin_cmd(pattern="م14(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event, 
"""** ⦑   لأوامر الزخرفة   ⦒  : **
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
⑴  ⦙ .غمق + الرد على رساله 
✐ :  يحول خط الرسالة غامقه  
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
⑵  ⦙ .ينسخ + الرد على رساله 
✐ :  يحول خط الرساله الى كلام ينسخ  
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
⑶  ⦙ .خط سفلي + الرد على رساله 
✐ :   يضيف الى خط رساله خط سفلي 
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
⑷  ⦙ .كتابه + الكلام بالانكلش 
✐ : يكتب الكلام على ورقه بخط اليد 100% ❝ 
 ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
⑸  ⦙ .زخرفه_انكليزي + الاسم 
✐ : يزخرف الاسم الانكليزي لعده زخرفات يجب ان يكون الاسم مكتوب سمول 
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
⑹ ⦙ .زخرفه_عربي + الاسم 
✐ : يزخرف الاسم العربي لعده زخرفات 
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
⑺ ⦙  .بايوهات1
✐ :  يعطيك بايو انستا متعدده 1 
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
⑻ ⦙ .بايوهات2
✐ :  يعطيك بايو انستا متعدده 2 
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
⑼ ⦙  .رموز1
✐ :  يعطيك رموز للزخرفه 1 
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
10 ⦙ .رموز2
✐ :  يعطيك رموز للزخرفه2 
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ

قناة السورس  : @c_r_source 
المطورة كرستين  : @dr_criss 
المطور زين : @iiqllll
""")



@iqthon.tgbot.on(CallbackQuery(data=re.compile(rb"ordahln1")))
@check_owner
async def inlineiqthon(iqthon):
    text = "**🚹  ⦑  اوامر الاعلانات   ⦒  :**\n\nᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ \n ⑴  ⦙ `.مؤقته + الوقت بالثواني + رساله`\n**✐ :  يرسل الرساله لمده معينه ويحذفها بس يخلص المده**\n ⑵  ⦙ `.للكروبات + الرد على الرساله`\n**✐ :  يرسل الرسالها الى جميع المجموعات**\nᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ \n ⑶  ⦙ `.مؤقت + عدد ثواني + عدد الرسائل + كليشة` \n**✐ :  يقوم بارسال رساله وقتيه محدده لكل وقت معين وعدد مرات معين**\n\n ⑷  ⦙ `.اضافه + رابط الكروب`\n✐ :   يضيفلك جميع الاعضاء الي برابط الكروب يضيفهم بكروبك \n يجب ان تتاكد انو مامحضور حسابك ارسل  ⬅️ ( `.حالتي` ) \n علمود تتاكد محضور الحساب لو لا الاضافات الكثيره تحظر مؤقتا  \n"
    buttons = [[Button.inline("رجوع", data="orders"),]]
    await iqthon.edit(text, buttons=buttons)
if Config.TG_BOT_USERNAME is not None and tgbot is not None :
    @check_owner
    @tgbot.on(events.InlineQuery)
    async def inlineiqthon(iqthon):
        builder = iqthon.builder
        result = None
        query = iqthon.text
        await bot.get_me()
        if query.startswith("اوامر الاعلانات(?: |$)(.*)") and iqthon.query.user_id == bot.uid:
            buttons = [[Button.inline("اوامر الاعلانات", data="ordahln1"),]]
            result = builder.article(title="iqthon", text=help2, buttons=buttons, link_preview=False)
            await iqthon.answer([result] if result else None)
@bot.on(admin_cmd(outgoing=True, pattern="اوامر الاعلانات(?: |$)(.*)"))
async def repoiqthon(iqthon):
    if iqthon.fwd_from:
        return
    TG_BOT = Config.TG_BOT_USERNAME
    if iqthon.reply_to_msg_id:
        await iqthon.get_reply_message()
    response = await bot.inline_query(TG_BOT, "اوامر الاعلانات(?: |$)(.*)")
    await response[0].click(iqthon.chat_id)
    await iqthon.delete()
@iqthon.on(admin_cmd(pattern="م15(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event, 
"""**⦑   اوامر الوسائـط   ⦒  :**
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
⑴ ⦙ .سمول + الرد على ملصق او صوره او فيديو 
✐  : يقوم بتصغير الوسائط 
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
⑵ ⦙ .عكس الالوان + الرد على ملصق او صوره او فيديو
✐  : يعكس الالوان الموجودة في الوسائط
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
⑶ ⦙ .فلتر احمر + الرد على ملصق او صوره او فيديو
✐  : يقوم باضافه فلتر احمر الى وسائط
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
⑷ ⦙ .فلتر رصاصي + الرد على ملصق او صوره او فيديو
✐  :  يقوم باضافه فلتر رصاصي الى وسائط
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
⑸ ⦙ .يمين الصوره + الرد على ملصق او صوره او فيديو )
✐  : يقوم بتحويل وجهه الوسائط الى اليمين
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
⑹ ⦙ .قلب الصوره + الرد على ملصق او صوره او فيديو
✐  : يقلب الوسائط من فوق لتحت
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
⑺ ⦙ .زوم + الرد على ملصق او صوره او فيديو
✐  :  يقوم بتقريب على الوسائط
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
⑻ ⦙ .اطار + الرد على ملصق او صوره او فيديو
✐  : يضيف اطار الى الوسائط
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
⑼ ⦙ .لوقو + الاسم
✐  : يقوم بصنع logo خاص بك
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
  ⦑   قناة السورس  : @c_r_source 
المطورة كرستين  : @dr_criss 
المطور زين : @iiqllll  ⦒
""")
@iqthon.on(admin_cmd(pattern="م16(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event, 
"""** ⦑   اوامر الملصقات   ⦒  : **
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
 ⑴ ⦙ .جلب الملصقات + الرد على الملصق
✐  : يجلب اليك ملصقات الحزمه
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
⑵ ⦙  .انشاء حزمه ملصقات + الرد على الملصق
✐  : يضع الملصق بحزمه بشكل مقصوص
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
⑶ ⦙ .جلب معلومات الملصق + الرد على الملصق )
✐  : يجلب لك جميع معلومات الملصق
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
⑷ ⦙ .ملصق + اسم الحزمه او الملصق
✐  : يبحث عن اسم الحزمه او الملصق ويجلبه اليك
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
  ⦑   قناة السورس  : @c_r_source 
المطورة كرستين  : @dr_criss 
المطور زين : @iiqllll  ⦒
""")

@iqthon.tgbot.on(CallbackQuery(data=re.compile(rb"ordSONG")))
@check_owner
async def inlineiqthon(iqthon):
    text = "**🚹  ⦑   اوامر التنزيلات والبحث الاغاني    ⦒  :**\n\n⑴  ⦙ `.بحث صوت + اسم الاغنيه`\n**✐ : سيحمل لك الاغنية صوت ايضا يمكنك وضع رابط الاغنيه بدل الاسم ❝**\n ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ \n ⑵  ⦙ `.بحث فيديو + اسم الاغنيه` \n**✐ : سيحمل لك الاغنية  فيديو ايضا يمكنك وضع رابط الاغنيه بدل الاسم ❝**\n ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ \n\n ⑶  ⦙ `.معلومات الاغنيه` \n**✐ : الرد ع الاغنيه سيجلب لك معلوماتها واسم الفنان ❝**\nᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ \n \n⑷  ⦙ `.كوكل بحث + موضوع البحث`\n**✐ : يجلب لك معلومات الموضوع من كوكل ❝**\nᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ \n⑸  ⦙ `.تخزين الصوت + الرد ع البصمه`\n**✐ : تخزين الصوت من اجل استخدامه لوضع صوت في الفيديو ❝**\n ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ \n⑹ ⦙ `.اضف الصوت + الرد ع الصوره او متحركه او فيديو`\n**✐ : يتم اضافه الصوت الى الفيديو او المتحركه او الصوره ❝**\n ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ \n⑺ ⦙ `.اسم الاغنيه + الرد ع الاغنيه`\n**✐ : ييجلب لك اسم الاغنيه مدة البصمه 10 الى 5 ثواني ❝**\n⑻ ⦙ `تيك توك + الرد ع رابط الفيديو.`\n**✐ : يحمل فيديو تيك توك بدون العلامه المائيه** ❝\n ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ\n"
    buttons = [[Button.inline("رجوع", data="orders"),]]
    await iqthon.edit(text, buttons=buttons)
@iqthon.on(admin_cmd(pattern="م1(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event, 
""" ** ⦑   اوامر السورس   ⦒  :**
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
الأمر ⦙ ( .السورس )
الشرح  : يضهر لك معلومات السورس ومدة تنصيبك او امر .فحص ❝
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
الأمر ⦙ ( .رابط التنصيب )
الشرح  : سوف يعطيك رابط التنصيب ❝ 
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
الأمر ⦙ ( .حساب كيثاب + اسم الحساب )
الشرح  : ينطيك معلومات الحساب وسورساته بموقع جيت هوب ❝ 
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
الأمر ⦙ ( .المده )
الشرح  : يضهر لك مدة تشغيل بوت تليثون لديك 
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
الأمر ⦙ ( .تحميل ملف + الرد ع الملف )
الشرح : يحمل ملفات تليثون 
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
الأمر ⦙ ( .مسح ملف + الرد ع الملف )
الشرح :  يمسح الملف الي حملته  
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
الأمر ⦙ ( .تحديث )
الشرح :  امر لأعاده التشغيل وتحديث ملفات السورس وتسريع التليثون 
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
الأمر ⦙ ( .اطفاء مؤقت + عدد الثواني )
الشرح : يقوم بأطفاء التليثون بعدد الثواني الي ضفتها  عندما تخلص الثواني سيتم اعاده تشغيل التليثون 
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
الأمر ⦙ ( .الاوامر ) 
الشرح :   لأضهار جميع اوامر السورس اونلاين
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
الأمر ⦙ ( .اوامري )
الشرح :   لأضهار جميع اوامر السورس كتابه بدون اونلاين
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
الأمر ⦙ ( .استخدامي )
الشرح :   يضهر لك كمية استخدامك لتليثون
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
الأمر ⦙ ( .تاريخ التنصيب )
الشرح :   يضهر لك تاريخ تنصيبك
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
قناة السورس  : @c_r_source 
المطورة كرستين  : @dr_criss 
المطور زين : @iiqllll""")

@iqthon.on(admin_cmd(pattern="م2(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event,
"""**  ⦑   اوامـر الحـسـاب  ⦒ : **
———————×———————
الأمر︙( .معرفه + الرد ع الشخص )
شرح︙سيجلب لك معرف الشخص 
———————×———————
الأمر︙( .سجل الاسماء + الرد ع الشخص ) 
شرح︙يجلب لك اسماء الشخص القديمه 
———————×———————
الأمر︙( .انشاء بريد )
شرح︙ينشئ لك بريد وهمي 
———————×———————
الأمر︙( .ايدي + الرد ع الشخص )
شرح︙سيعطيك معلومات الشخص 
———————×———————
الأمر︙( . الايدي الرد ع الشخص )
شرح︙سوف يعطيك ايدي المجموعه او ايدي حسابك 
———————×———————
الأمر︙( .معلومات تخزين المجموعه )
شرح︙يجلب لك جميع معلومات الوسائط  
———————×———————
الأمر︙( .تخزين الخاص تشغيل )
شرح︙يخزن لك جميع الرسائل التي  في الخاص 
———————×———————
الأمر︙( .تخزين الخاص ايقاف )
شرح︙يوقف  تخزين الرسائل اليك في الخاص 
———————×———————
الأمر︙( .تخزين الكروبات تشغيل )
شرح︙يخزم جميع الرسائل التي يتم رد عليك 
———————×———————
الأمر︙( .تخزين الكروبات ايقاف )
شرح︙يوقف لك جميع تخزين رسائل
———————×———————
 الأمر  ︙( .صورته + الرد ع الشخص )
شرح︙يجلب صوره الشخص
———×———
الأمر︙( .رابطه + الرد ع الشخص )
شرح︙يجلب لك رابط الشخص
———×———
الأمر︙( .اسمه + الرد ع الشخص )
شرح︙يجلب لك اسم الشخص الذي تم رد عليه 
———×———
الأمر︙( .نسخ + الرد ع الرساله )
شرح︙يرسل الرساله التي تم رد عليها 
———×———
الأمر︙( .كورونا + اسم المدينه )
شرح︙يجلب لك مرض كورونا و معلومات
———×———
الأمر︙( .الاذان + اسم المدينه )
شرح︙يجلب لك معلومات الاذان 
———×———
الأمر︙( .رابط تطبيق + اسم التطبيق )
شرح︙يرسل رابط التطبيق مع معلوماته 
———×———
الأمر︙( .تاريخ الرساله + الرد ع الرساله )
شرح︙يجلب لك تاريخ الرساله بالتفصيل 
———×———
الأمر︙( .بنك )
شرح︙يقيس سرعه استجابه 
———×———
الأمر︙( .سرعه الانترنيت )
شرح︙يجلب لك سرعه الانترنيت لديك 
———×———
الأمر︙( .الوقت )
شرح︙يضهر لك الوقت والتاريخ 
———×———
الأمر︙( .وقتي )
شرح︙الوقت والتاريخ شكل اخر
———×———
الأمر︙.حالتي 
✐  :  لفحص الحظر
———×———
الأمر︙.طقس + اسم المدينه 
شرح︙ يعطي لك طقس المدينه 
———×———
الأمر︙ .طقوس + اسم المدينه 
شرح︙ يعطي لك طقس المدينه 
———×———
الأمر︙ .مدينه الطقس + اسم المدينه 
شرح︙ لتحديد طقس المدينه تلقائي
———×———
الأمر︙ .ازاله التوجيه + الرد على رساله
شرح︙ يرسل اليك الرساله بدون توجية
———×———
الأمر︙.كشف + الرد على شخص
شرح︙ رد على شخص يفحص الحظر
———×———
الأمر︙.وضع بايو + الرد على البايو
شرح︙ يضع الكلمه في البايو الخاص بك
———×———
الأمر︙.وضع اسم + الرد على الاسم
شرح︙ يضع الاسم في اسمك
———×———
الأمر︙.وضع صوره + الرد على صوره
شرح︙يضع الصوره في حسابك
———×———
الأمر︙.معرفاتي
شرح︙يجلب جميع معرفاتك
———×———
الأمر︙ .تحويل ملكية + معرف الشخص
شرح︙يحول ملكيه القناه او المجموعه 
———×———
الأمر︙ .انتحال + الرد على الشخص
شرح︙ ينتحل الشخص ويضع صورته و نبذته و اسمه في حسابك
———×———
الأمر︙.الغاء الانتحال + الرد على الشخص
شرح︙ يقوم بالغاء الانتحال 
———×———
الأمر︙.ازعاج + الرد على شخص
شرح︙يقوم بتكرار الرسائل الشخص 
———×———
الأمر︙.الغاء الازعاج
شرح : يوقف جميع الازعاجات في المجموعه 
 ———×———
 الأمر︙.المزعجهم
شرح︙ يضهر اليك جميع الذين مفعل عليهم الازعاج 
———×———
الأمر︙( .الحماية تشغيل )
شرح︙ يقوم بتشغيل رساله الحمايه اي شخص يراسلك سوف يقوم بتنبيه
———×———
الأمر︙( .الحماية ايقاف )
شرح︙يقوم بتعطيل رساله الحماية الخاص
———×———
الأمر︙( .قبول )
شرح︙ يقوم بقبول الشخص للأرسال اليك
———×———
الأمر︙( .رفض )
شرح︙الغاء قبول الشخص من الارسال 
———×———
الأمر︙( .مرفوض )
شرح︙حظر الشخص 
———×———
الأمر︙( .المقبولين )
شرح︙عرض قائمة المقبولين ي الحماية 
———×———
الأمر︙( .جلب الوقتيه + الرد على الصورة )
شرح︙حفض صوره وقتيه في الحافضة 
———×———
الأمر︙( .تاك بالكلام + الكلمه + معرف الشخص )
شرح︙ يسوي تاك للشخص بالرابط جربه وتعرف 
———×———
الأمر︙( .نسخ + الرد على رساله )
شرح︙ يرسل الرساله التي رديت عليها
———×———
الأمر︙.احسب + المعادله
شرح︙يجمع او يطرح او يقسم
———×———
الأمر  ⦙  ( .كول + الكلمة )
الشرح : يجب اضافه بوتك يتكلم بدلا عنك 
———×———
الأمر  ⦙ ( .وضع النائم + السبب )
الشرح : اي شخص يعملك تاك او يراسلك او يرد عليك يرد عليه سيدا ثون بكليشة انا حاليا غير موجود ويضع له السبب الي نتة وضعته
———×———
الأمر  ⦙  .الصور + الرد على الشخص 
الشرح : يجلب لك جميع صور الشخص و يمكن وضع رقم بجانب الأمر
———×———
الأمر  ⦙  .زاجل + معرف الشخص + الرساله 
الشرح : يرسل الرساله الى الشخص 
———×———
الأمر ⦙ .فيديو
الشرح  : يرسل فيديو عشوائي
———×———
الأمر  ⦙ .فيديو2
الشرح :  يرسل فيديو عشوائي
———×———
الأمر ⦙ .فايروس
الشرح :  يرسل فايروس
———×———

""")

@iqthon.on(admin_cmd(pattern="م3(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event, 
"""**  ⦑  اوامر الكروب 1  ⦒  :**

———————×——————— 
 الأمر  ⦙  ( .كتم + الرد ع الشخص )
الشرح  ⦙ يكتم الشخص من الخاص او الكروبات فقط اذا كانت عندك صلاحيه حذف رسائل 
الأمر  ⦙  ( . الغاء كتم + الرد ع الشخص )
الشرح  ⦙ يجلب لك جميع معرفات المشرفين في الكروب  
 ———————×——————— 
الأمر ⦙  ( .البوتات )
الشرح  ⦙ يجلب لك جميع معرفات البوتات في الكروب 
الأمر ⦙  ( .الأعضاء )
الشرح  ⦙ اضهار قائمة الاعضاء للكروب اذا هواي سيرسل ملف كامل لمعلوماتهم  
———————×——————— 
الأمر ⦙  ( .معلومات )
الشرح  ⦙ سيرسل لك جميع معلومات الكروب بالتفصيل  
الأمر ⦙  ( .مسح المحظورين )
الشرح  ⦙ يمسح جميع المحظورين في الكروب 
 ———————×——————— 
الأمر ⦙  ( .المحذوفين )
الشرح  ⦙ يجلب لك جميع الحسابات المحذوفه 
الأمر ⦙  ( .المحذوفين تنظيف )
الشرح  ⦙ يمسح جميع الحسابات المحذوفه في الكروب 
———————×——————— 
الأمر ⦙  ( .احصائيات الاعضاء )
الشرح  ⦙ يمسح جميع المحظورين في الكروب 
———————×——————— 
الأمر ⦙  ( .انتحال + الرد ع الشخص )
الشرح  ⦙ يقوم بأنتحال الشخص ويضع صورته ونبذته واسمه في حسابك عدا المعرف  
الأمر ⦙  ( .الغاء الانتحال + الرد ع الشخص )
الشرح  ⦙ يقوم بألغاء الانتحال وسيرجع معلومات المذكوره بالسورس 
———————×———————
الأمر  ⦙  ( .ترحيب + الرساله )
الشرح  ⦙ يضيف ترحيب في الكروب اي شخص ينضم راح يرحب بي  
الأمر  ⦙   ( .مسح الترحيبات )
الشرح  ⦙ ييقوم بمسح الترحيب من الكروب 
———————×——————— 
الأمر  ⦙  ( .ترحيباتي )
الشرح  ⦙ يضهر لك جميع الترحيبات التي وضعتها في الكروب 
———————×——————— 
الأمر  ⦙  ( .رساله الترحيب السابقه تشغيل ) 
الشرح  ⦙ عندما يحدث تكرار سيحذف رساله الترحيب 
الأمر  ⦙  ( .رساله الترحيب السابقه ايقاف )
الشرح  ⦙ عندما يحدث تكرار لا يحذف رساله الترحيب 
———————×——————— 
الأمر ⦙  ( .اضف رد + الكلمه )
الشرح  ⦙ مثلاً تدز رساله هلو تسوي عليها رد بهلوات 
الأمر ⦙  ( .مسح رد + الكلمه )
الشرح  ⦙ سيحذف الكلمه الي انت ضفتها 
الأمر ⦙  ( .جميع الردود )
 الشرح  ⦙ يجلب لك جميع الردود الذي قمت بأضافتها  
الأمر ⦙  ( .مسح جميع الردود )
الشرح  ⦙ يمسح جميع الردود الي انت ضفتها 
———————×——————— 
الأمر ⦙  ( .صنع مجموعه + اسم المجموعه )
الشرح  ⦙ يقوم بعمل مجموعه خارقه 
الأمر ⦙  ( .صنع قناه +  اسم القناة )
الشرح  ⦙ يقوم بعمل قناه خاصه  
———————×——————— 
الأمر ⦙  ( .عدد رسائلي )
الشرح  ⦙ سيظهر لك عدد رسائلك في الكروب 
———————×———————
الأمر  ⦙  ( .تفعيل حمايه المجموعه )
الشرح  ⦙ يقوم غلق جميع صلاحيات المجموعه يبقي فقط ارسال  الرسائل
الأمر  ⦙ تعطيل حمايه المجموعه
الشرح  ⦙ يقوم بتشغيل جميع صلاحيات المجموعة ماعدا تغير المعلومات و التثبيت و اضافه اعضاء تبقى مسدوده
———————×——————— 
الأمر  ⦙  ( .صلاحيات المجموعه )
الشرح  ⦙ يقوم بعرض صلاحيات المجموعه المغلقه والمفتوحه
———————×———————
الأمر  ⦙  ( .رفع مشرف + الرد على شخص )
الشرح  ⦙ يرفع الشخص مشرف يعطي صلاحيه حذف رسائل والتثبيت فقط
———————×——————— 
الأمر  ⦙  ( .منع + كلمة )
الشرح  ⦙ منع كلمه من الارسال في الكروب
الأمر ⦙  ( .الغاء منع + كلمه )
الشرح  ⦙ يقوم بالغاء منع الكلمه  
———————×——————— 
الأمر ⦙  ( .قائمه المنع )
الشرح  ⦙ يقوم بجلب جميع الكلمات الممنوعه في الكروب 
———————×——————— 
الأمر ⦙  ( .تاك + ( الاعداد المحدده وثابتة فقط) ⤵️
  ( 10 - 50 - 100 - 200  )
الشرح  ⦙ يجلب لك الاعضاء بالروابط بالعدد المحدد 
———————×——————— 
الأمر ⦙  ( .معرفات + ( الاعداد المحدده وثابتة فقط) ⤵️
  ( 10 - 50 - 100 - 200  )
الشرح  ⦙ جلب لك معرفات الاعضاء بالعدد المحدد 
———————×———————
الأمر  ⦙  ( .تنظيف الوسائط )
 الشرح  ⦙ ينضف جميع ميديا من صور وفديوهات و متحركات او ( .تنظيف الوسائط + العدد)  
———————×——————— 
الأمر  ⦙  ( .حذف الرسائل )
الشرح  ⦙ يحذف جميع الرسائل بلكروب  
  او  .حذف الرسائل + العدد 
———————×——————— 
الأمر  ⦙  ( .مسح + الرد على رسالة )
الشرح  ⦙ يحذف الرساله الي راد عليها فقط 
———————×——————— 
الأمر  ⦙  ( .غادر )
الشرح  ⦙ يغادر من المجموعه او من القناة
———————×——————— 
الأمر  ⦙  ( .تفليش )
الشرح  ⦙ يطرد جميع الي في الكروب او قناة 
———————×——————— 
الأمر ⦙  ( .اضافه + رابط الكروب )
الشرح  ⦙ يضف اليك جميع الاعضاء الى الكروب 
 ( يجب ان تتاكد انك  لست محضور ارسل ⬅️
( .فحص الحظر ) من اجل التاكد
———————×——————— 
الأمر ⦙  ( .جلب الوقتيه + الرد على الصورة )
الشرح  ⦙ الرد على صوره سريه وقتيه سوف يتم تحويلها الى رسائل المحفوضه كصورة عادية
———————×——————— """)
@iqthon.on(admin_cmd(pattern="م4(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event, 
"""**  ⦑  اوامر الكروب 2  ⦒  : **
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
الأمر ⦙  ( .تاك بالكلام + الكلمه + معرف الشخص )
الشرح  ⦙ يعمل تاك للشخص بالرابط جربه وتعرف
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
الأمر ⦙  ( .نسخ + الرد على رساله )
الشرح  ⦙ يرسل الرساله التي رديت عليها 
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
الأمر ⦙  ( .ابلاغ الادمنيه )
الشرح  ⦙ يعمل تاك لجميع الادمنيه  
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
الأمر ⦙  ( .المشرفين )
الشرح  ⦙ يجلب اليك جميع المشرفين 
الأمر ⦙  ( .البوتات )
الشرح  ⦙ يجلب الك جميع بوتات في المجموعه او قناه
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
الأمر ⦙  ( .حظر + الرد على شخص )
الشرح  ⦙ حظر الشخص من المجموعه 
الأمر  ⦙  ( .الغاء الحظر + الرد على شخص )
الشرح  ⦙ يلغي حظر الشخص من المجموعه
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
الأمر  ⦙  ( .بدء مكالمه )
الشرح  ⦙ يقوم بتشغيل مكالمه 
الأمر ⦙  ( .دعوه للمكالمه )
الشرح  ⦙ يتم دعوه الاعضاء للمكالمة الشغاله
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
الأمر ⦙  ( .تنزيل مشرف + الرد على شخص )
الشرح  ⦙ يقوم بازاله الشخص من الاشراف 
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
الأمر  ⦙  ( .تثبيت + الرد على رساله )
 شرح : تثبيت الرساله التي رديت عليها
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
الأمر ⦙  ( .الأعضاء )
الشرح  ⦙ اضهار قائمة الاعضاء للمجموعة 
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
الأمر ⦙  ( .تفليش )
الشرح  ⦙  أزاله جميع اعضاء المجموعه
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
الأمر ⦙  ( .مسح المحظورين )
الشرح  ⦙ يمسح جميع المحظورين 
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
الأمر  ⦙  ( .المحذوفين )
الشرح  ⦙  يجلب لك الحسابات المحذوفه 
الأمر ⦙  ( .المحذوفين تنظيف )
الشرح  ⦙ مسح الحسابات المحذوفه
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
الأمر ⦙  ( .احصائيات الاعضاء )
الشرح  ⦙ يجلب جميع معلومات اعضاء المجموعه 
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
الأمر ⦙  ( .عدد رسائلي )
الشرح  ⦙ يقوم بحساب عدد رسائلك 
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
الأمر ⦙  ( .جلب الاحداث )
الشرح  ⦙ يجلب اخر 20 رساله محذوفه
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
الأمر  ⦙ ( .حظر عام + الرد على شخص ) 
الشرح  ⦙ حظر من جميع الكروبات   
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
الأمر  ⦙ ( .الغاء حظر عام + الرد على شخص )
الشرح  ⦙ الغاء حضر العام  
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
الأمر  ⦙ ( .المحظورين عام )
الشرح ⦙  يضهر المحضورين عام 
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
الشرح  ⦙ ( .تقيد + الرد على شخص )
الأمر  ⦙ يقيد الشخص من المجموعة 
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ

᯽︙░c░░h░ 𖠰 @c_r_source 
᯽︙ أن تكونَ عزيزاً غائباً.. أفضلُ بكثير من أن تكونَ حاضراً بلا قيم.""")
@iqthon.on(admin_cmd(pattern="م5(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event, 
"""**⦑  اوامر تحويل الصيغ  ⦒  :**
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
الأمر ⦙  .تحويل بصمه + الرد ع الصوت mp3
الشرح : يحول صوت mp3 الى بصمه 
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
الأمر ⦙  .تحويل صوت + الرد ع الصوت 
الشرح  :  يحول البصمه الى صوت   mp3
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
الأمر  ⦙  .تحويل ملصق + الرد ع الصوره 
الشرح :  يحول الصوره الى ملصق 
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
الأمر  ⦙ . تحويل صوره + الرد ع الملصق 
الشرح :  يحول الملصق الى صوره 
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
الأمر ⦙  .تحويل متحركه + الرد ع الفيديو 
الشرح :  يقوم بتحويل الفيديو الى متحركه 
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
الأمر  ⦙  .بي دي اف + الرد ع الملف او الصوره
الشرح :  يحول الملف الى بي دي اف 
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
الأمر  ⦙ .ملصقي + الرد ع الرساله 
الشرح  : يحول رساله الى ملصق 
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
الأمر  ⦙  . تليجراف ميديا + الرد ع الفيديو او صوره
الشرح :  يقوم بتحويل الفيديو او الصوره الى رابط تليجراف  
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
الأمر ⦙  ( .تحويل رساله + الرد ع الملف )
الشرح :  يقوم بجلب جميع الكتابه الذي داخل الملف ويقوم بأرسالها اليك 
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
الأمر ⦙ ( .تحويل فديو دائري + الرد ع الفيديو )
الشرح : يحول الفيديو الى فيديو دائري مرئي 
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
الأمر  ⦙ ( .تحويل ملصق دائري + الرد ع الملصق )
الشرح :  يحول الملصق الى ملصق دائري
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
 الأمر ⦙  ( .ترجمه en + الرد ع الرساله )
الشرح :  يقوم بترجمه الرساله الى اللغه الانكليزيه
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
الشرح ⦙ ( .ترجمه ar + الرد ع الشخص )
الأمر  :  يقوم بترجمه الرساله الى اللغه العربيه 
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ

᯽︙░c░░h░ 𖠰 @c_r_source 
᯽︙ أن تكونَ عزيزاً غائباً.. أفضلُ بكثير من أن تكونَ حاضراً بلا قيم.""")
@iqthon.on(admin_cmd(pattern="م6(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event, """
**  ⦑   اوامر الالعاب 1   ⦒  :**
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
شرح  ⦙   نسبة وهميه - الأوامر :
الأمر  ⦙ ( .نسبه الحب + الرد ع الشخص )
الأمر  ⦙ ( . نسبه الانحراف + الرد ع الشخص )
الأمر  ⦙ ( .نسبه الكراهيه + الرد ع الشخص )
الأمر  ⦙ ( .نسبه المثليه +الرد ع الشخص )
الأمر  ⦙ ( . نسبه النجاح + الرد ع الشخص )
الأمر  ⦙ ( .نسبه الانوثه + الرد ع الشخص )
الأمر  ⦙ ( .نسبه الغباء + الرد ع الشخص )
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
شرح  ⦙  رفع وهمي - الأوامر  :
الأمر  ⦙ ( .رفع زباله + الرد ع الشخص )
الأمر  ⦙ ( .رفع منشئ + الرد ع الشخص )
الأمر  ⦙ ( .رفع مدير + الرد ع الشخص )
الأمر  ⦙ ( .رفع مطور + الرد ع الشخص )
الأمر  ⦙ ( .رفع مثلي + الرد ع الشخص )
الأمر  ⦙ ( .رفع كواد + الرد ع الشخص )
الأمر  ⦙ ( .رفع مرتبط + الرد ع الشخص )
الأمر  ⦙ ( .رفع مطي + الرد ع الشخص )
الأمر  ⦙ ( .رفع كحبه + الرد ع الشخص )
الأمر  ⦙ ( .رفع زوجتي + الرد ع الشخص )
الأمر  ⦙ ( .رفع صاك + الرد ع الشخص )
الأمر  ⦙ ( .رفع صاكه + الرد ع الشخص )
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
الأمر  ⦙ ( .كت )
الشرح ⦙ لعبه اسأله كت تويت عشوائيه 
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
الأمر  ⦙ ( .اكس او )
الشرح ⦙  لعبه اكس او دز الامر و اللعب ويا صديقك 
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
الأمر  ⦙  ( .همسه + الكلام + معرف الشخص )
الشرح  ⦙  يرسل همسه سريه الى معرف الشخص فقط هو يكدر يشوفها  
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
الأمر  ⦙  ( .رسم شعار + الاسم )
الشرح ⦙  يرسم شعار للأسم  
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
الأمر  ⦙ ( .نص ثري دي + الكلمه )
الشرح ⦙ يقوم بكتابه الكلمه بشكل ثلاثي الابعاد 
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
الأمر  ⦙  ( .كلام متحرك + الكلام )
الشرح ⦙ يقوم بكتابه الكلام حرف حرف  
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
الأمر ⦙ ( .ملصق متحرك + الكلام )
الشرح  ⦙ يقوم بكتابه الكلام بملصق متحرك  
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
الأمر  ⦙  ( .بورن + معرف الشخص + الكلام + الرد ع اي صوره )
الشرح ⦙  قم بتجربه الامر لتعرفه +18  
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
الأمر  ⦙ ( .رسم قلوب + الاسم )
الشرح  ⦙  يكتب الاسم ع شكل قلوب  
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ

⑴  ⦙  ( .كتابه وهمي + عدد الثواني )
⑵  ⦙  ( .فيديو وهمي + عدد الثواني )
⑶  ⦙  ( .صوره وهمي + عدد الثواني )
⑷  ⦙  ( .جهه اتصال وهمي + عدد الثواني )
⑸  ⦙  ( .موقع وهمي + عدد الثواني )
⑹  ⦙  ( .لعب وهمي + عدد الثواني )

الشرح  ⦙ هذا الامر يقوم بالارسال الوهمي يعني يضهر للناس انو نته جاي تكتب او جاي ترسل صوره او ترسل فيديو او ترسل جهه اتصالك حسب الفتره الي تحددها بالثواني
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
⑴  ⦙ ( .شوت + الكلمة )
✐ :  امر تسليه جربه وتعرف  
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
⑵  ⦙ ( .كتابه + الكلام بالانكلش )
✐ :   يكتب الكلام على ورقه بخط اليد 100%   
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
الشرح  ⦙   العـاب اخـرى فقط قم بنسخ الأمر وارسالـة   :- الأوامر :
1. - ( .لعبه تيك توك اربعه )
2. - ( .لعبه تيك توك اثنان 3 )
3. - ( .لعبه ربط أربعة )
4. - ( .لعبه قرعة )
5. - ( .لعبه حجر-ورقة-مقص )
6. - ( .لعبه روليت )
7. - ( .لعبه داما )
8. - ( .لعبه داما تجمع )
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
الأمر  ⦙ ( .هديه + الكلام )
الشرح :  قم بارسال الامر بجانبه اكتب اي شيئ واول شخص سيفتحها سوف يكتب اسمه جربها  
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
الأمر  ⦙ ( .ضفدع + الكلمه )
الشرح :   يدعم انكليزي فقط + يحول الكلمه لكتابه ضفدع جربه وتفهم   
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
الأمر  ⦙  ( .لافته + الكلمه )
الشرح :   يدعم انكليزي فقط + يحول الكلمه بلافته ملصق متحرك جربه وتعرف    
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
الأمر ⦙ ( .تكرار_كلمه  + الجملة )
الشرح : يكرر الك كلام الجملة 
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
الأمر ⦙  (.صفق + الرد على الكلام )
الشرح : جربه وتعرف مضحك 
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
الأمر  ⦙ ( .حضر وهمي + الرد على شخص )
الشرح : حظر وهمي جربه وتعرف 
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
الأمر ⦙ ( .خط ملصق + الكلمه )
الشرح : يدعم انكليزي فقط + يحول الكتابه لملصق 
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
الأمر  ⦙ ( .شعر )
الشرح : يرسل الك شعر ميمز او مضحك 
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
᯽︙░c░░h░ 𖠰 @c_r_source 
᯽︙ أن تكونَ عزيزاً غائباً.. أفضلُ بكثير من أن تكونَ حاضراً بلا قيم""")
@iqthon.on(admin_cmd(pattern="م7(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event, 
"""**  ⦑   بصمات تحشيش 1   ⦒  :**
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
(.ص1) ⦙  ابو  عباس  لو  تاكل  خره
(.ص2) ⦙  استمر  نحن  معك
(.ص3) ⦙  افحط  بوجه
(.ص4) ⦙  اكعد  لا  اسطرك  سطره  العباس
(.ص5) ⦙  اللهم  لا  شماته
(.ص6) ⦙  امرع  دينه
(.ص7) ⦙  امشي  بربوك
(.ص8) ⦙  انت  اسكت  انت  اسكت
(.ص9) ⦙  انت  سايق  زربه
(.ص10) ⦙  اوني  تشان
(.ص11) ⦙  برافو  عليك  استادي 
(.ص12) ⦙  بلوك  محترم
(.ص13) ⦙  بووم  في  منتصف  الجبهة 
(.ص14) ⦙  بيتش 
(.ص15) ⦙  تخوني  ؟
(.ص16) ⦙  تره  متكدرلي
(.ص17) ⦙  تعبان  اوي
(.ص18) ⦙  تكذب
(.ص19) ⦙  حسبي  الله
(.ص20) ⦙  حشاش 
(.ص21) ⦙  حقير  
(.ص22) ⦙  خاص  
(.ص23) ⦙  خاله  ما  تنامون  
(.ص24) ⦙  خرب  شرفي  اذا  ابقى  بالعراق 
(.ص25) ⦙  دكات  الوكت  الاغبر  
(.ص26) ⦙  ررردح  
(.ص27) ⦙  سلامن  عليكم  
(.ص28) ⦙  بوم منتصف جبهه   
(.ص29) ⦙  شكد  شفت  ناس  مدودة
(.ص30) ⦙ شلون  ، 
(.ص31) ⦙ صح  لنوم  
(.ص32) ⦙ صمت  
(.ص33) ⦙ ضحكة  مصطفى  الحجي  
(.ص34) ⦙ طماطه  
(.ص35) ⦙ طيح  الله  حضك  
(.ص36) ⦙ فاك  يوو  
(.ص37) ⦙ اني فرحان وعمامي فرحانين
(.ص38) ⦙ لا  تضل  تضرط  
(.ص39) ⦙ لا  تقتل  المتعه  يا  مسلم  
(.ص40) ⦙ لا  مستحيل  
(.ص41) ⦙ لا  والله  شو  عصبي  
(.ص42) ⦙ لش  
(.ص43) ⦙ لك  اني  شعليه  
(.ص44) ⦙ ما  اشرب  
(.ص45) ⦙ مع  الاسف  
(.ص46) ⦙ مقتدى  
(.ص47) ⦙ من  رخصتكم  
(.ص48) ⦙ منو  انت  
(.ص49) ⦙ منورني  
(.ص50) ⦙  نتلاكه  بالدور  الثاني 
(.ص51) ⦙  نستودعكم  الله  
(.ص52) ⦙  ها  شنهي  
(.ص53) ⦙  ههاي  الافكار  حطها ب
(.ص54) ⦙  ليش شنو سببها ليش
(.ص55) ⦙  يموتون  جهالي
(.ص56) ⦙  اريد انام
(.ص57) ⦙  افتحك فتح
(.ص58) ⦙  اكل خره لدوخني
(.ص59) ⦙  السيد شنهو السيد
(.ص60) ⦙  زيج2
(.ص61) ⦙  زيج لهارون
(.ص62) ⦙  زيج الناصرية
(.ص63) ⦙  راقبو اطفالكم
(.ص64) ⦙  راح اموتن
(.ص65) ⦙  ذس اس مضرطة
(.ص66) ⦙  دروح سرسح منا
(.ص67) ⦙  خويه ما دكوم بيه
(.ص68) ⦙  خلصت تمسلت ديلة كافي انجب
(.ص69) ⦙  بعدك تخاف
(.ص70) ⦙  بسبوس
(.ص71) ⦙  اني بتيتة كحبة
(.ص72) ⦙  انعل ابوكم لابو اليلعب وياكم طوبة
(.ص73) ⦙  انت شدخلك
(.ص74) ⦙  انا ماشي بطلع
(.ص75) ⦙  امداك وامده الخلفتك
(.ص76) ⦙  امبيههههه
(.ص77) ⦙  هدي بيبي
(.ص78) ⦙  هاه صدك تحجي
(.ص79) ⦙  مو كتلك رجعني
(.ص80) ⦙  مامرجية منك هاية
(.ص81) ⦙  ليش هيجي
(.ص82) ⦙  كـــافـي
(.ص83) ⦙  كس اخت السيد
(.ص84) ⦙  شنو كواد ولك اني هنا
(.ص85) ⦙  شجلبت
(.ص86) ⦙  شبيك وجه الدبس
(.ص87) ⦙  سييييي
(.ص88) ⦙  زيجج1
(.ص89) ⦙  يموتون جهالي
(.ص90) ⦙  ياخي اسكت اسكت
(.ص91) ⦙  وينهم
(.ص92) ⦙  هيلو سامر وحود
(.ص93) ⦙  هو
(.ص94) ⦙  ههاي الافكار حطها
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
  
᯽︙░c░░h░ 𖠰 @c_r_source 
᯽︙ أن تكونَ عزيزاً غائباً.. أفضلُ بكثير من أن تكونَ حاضراً بلا قيم""")
@iqthon.on(admin_cmd(pattern="م8(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event, 
"""**⦑    الاوامر المتحركه للتسلية   ⦒  :**
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
( .غبي ) ( .تفجير ) ( .قتل ) ( .طوبه ) ( .مربعات ) ( .حلويات ) ( .نار ) ( .هلكوبتر ) ( .اشكال مربع ) ( .دائره )( .قلب ) ( .مزاج ) ( .قرد ) ( .ايد ) ( .العد التنازلي ) ( .الوان قلوب ) ( .عين ) ( .ثعبان ) ( .رجل ) ( .رموز شيطانيه ) ( .قطار ) ( .موسيقى ) ( .رسم ) ( .فراشه ) ( .مكعبات ) ( .مطر ) ( .تحركات ) ( .ايموجيات ) ( .طائره )( .شرطي ) ( .النضام الشمسي ) ( .افكر ) ( .اضحك ) ( .ضايج ) ( .ساعه متحركه )( .بوسه ) ( .قلوب ) ( .رياضه )( .الارض ) ( .قمر ) (.اقمار ) ( .قمور ) ( .زرفه ) ( .بيبي ) ( .تفاعلات ) ( .اخذ قلبي ) 
( .اشوفج السطح ) ( .احبك ) ( .اركض ) ( .روميو ) ( .البنك ) ( .تهكير ) ( .طياره ) ( .مصاصه ) ( .مصه ) ( .جكه ) ( .اركضلي ) ( .حمامه ) ( .فواكه ) ( .الحياة ) ( .هلو ) ( .مربعاتي ) ( .اسعاف ) ( .سمايلي )
ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ
""")
@iqthon.tgbot.on(CallbackQuery(data=re.compile(rb"orders")))
@check_owner
async def inlineiqthon(iqthon):
    text = "**🝳︙ قـائمـه الاوامـر :**\n**᯽︙░c░░h░ 𖠰 @c_r_source \n ᯽︙ أن تكونَ عزيزاً غائباً.. أفضلُ بكثير من أن تكونَ حاضراً بلا قيم **** "
    buttons = [[Button.inline("اوامر السورس", data="order1"), Button.inline("اوامر الحساب", data="ord1hs"),],[Button.inline("اوامر الكروب", data="ord1G"), Button.inline("اوامر الالعاب", data="ord1pl"),],[Button.inline("اوامر الصيغ", data="ordsag1"), Button.inline("اوامر الاغاني", data="ordSONG"),], [Button.inline("اسم وقتي", data="order13"), Button.inline("اوامر الاعلانات", data="ordahln1"),],[Button.inline("اوامر التسليه", data="order14"),],[Button.inline("الفارات", data="ordvars"),]]
    await iqthon.edit(text, buttons=buttons)
@iqthon.tgbot.on(CallbackQuery(data=re.compile(rb"ord1G")))
@check_owner
async def inlineiqthon(iqthon):
    text = "**🚹  ⦑   اوامر الكروب   ⦒  :**"
    buttons = [[Button.inline("اوامر الكروب 1", data="G1"),],[Button.inline("اوامر الكروب 2", data="G2"),],[Button.inline("اوامر الكروب 3", data="G3"),],[Button.inline("اوامر الكروب 4", data="G4"),],[Button.inline("اوامر الكروب 5", data="G5"),],[Button.inline("رجوع", data="orders"),]]
    await iqthon.edit(text, buttons=buttons)

@iqthon.tgbot.on(CallbackQuery(data=re.compile(rb"G1")))
@check_owner
async def inlineiqthon(iqthon):
    text = "**🚹  ⦑  اوامر الكروب 1     ⦒  :**\n\nᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ \n ⑴  ⦙ `.كتم + الرد ع الشخص`\n**✐ : يكتم الشخص من الخاص او الكروبات فقط اذا كانت عندك صلاحيه حذف رسائل ❝**\n \n⑵  ⦙ `. الغاء كتم + الرد ع الشخص`\n**✐ :  يجلب لك جميع معرفات المشرفين في الكروب  ❝**\n ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ \n ⑶  ⦙ `.البوتات`\n**✐ : يجلب لك جميع معرفات البوتات في الكروب ❝**\n \n⑷  ⦙ `.الأعضاء`\n**✐ : اضهار قائمة الاعضاء للكروب اذا هواي سيرسل ملف كامل لمعلوماتهم  ❝**\nᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ \n⑸  ⦙ `.معلومات`\n**✐ : سيرسل لك جميع معلومات الكروب بالتفصيل ❝**\nᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ \n⑹ ⦙ `.مسح المحظورين`\n**✐ : يمسح جميع المحظورين في الكروب ❝**\n ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ \n⑺ ⦙ `.المحذوفين`\n**✐ : يجلب لك جميع الحسابات المحذوفه ❝**\n\n⑻ ⦙ `.المحذوفين تنظيف`\n**✐ : يمسح جميع الحسابات المحذوفه في الكروب ❝**\nᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ \n⑼ ⦙ `.احصائيات الاعضاء`\n**✐ : يمسح جميع المحظورين في الكروب ❝**\nᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ \n⑽ ⦙ `.انتحال + الرد ع الشخص`\n**✐ : يقوم بأنتحال الشخص ويضع صورته ونبذته واسمه في حسابك عدا المعرف ❝**\n\n⑾ ⦙ `.الغاء الانتحال + الرد ع الشخص`\n**✐ : يقوم بألغاء الانتحال وسيرجع معلومات المذكوره بالسورس ❝**\nᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ\n\n"
    buttons = [[Button.inline("اوامر الكروب 2", data="G2"),],[Button.inline("اوامر الكروب 3", data="G3"),],[Button.inline("اوامر الكروب 4", data="G4"),],[Button.inline("اوامر الكروب 5", data="G5"),],[Button.inline("رجوع", data="orders"),]]
    await iqthon.edit(text, buttons=buttons)
@iqthon.on(admin_cmd(pattern="تحميل الملف(?: |$)(.*)"))    
async def install(event):
    if event.reply_to_msg_id:
        try:
            downloaded_file_name = await event.client.download_media(await event.get_reply_message(), "iqthon/plugins/")
            if "(" not in downloaded_file_name:
                path1 = Path(downloaded_file_name)
                shortname = path1.stem
                load_module(shortname.replace(".py", ""))
                await edit_delete(event, f"**🝳︙   تم تثبيـت الملـف بنجـاح ✓** `{os.path.basename(downloaded_file_name)}`", 10)
            else:
                os.remove(downloaded_file_name)
                await edit_delete(event, "**🝳︙  حـدث خطـأ، هـذا الملف مثبـت بالفعـل !**", 10)
        except Exception as e:
            await edit_delete(event, f"**🝳︙  خطـأ ⚠️:**\n`{str(e)}`", 10)
            os.remove(downloaded_file_name)
@iqthon.tgbot.on(CallbackQuery(data=re.compile(rb"G2")))
@check_owner
async def inlineiqthon(iqthon):
    text = "**🚹  ⦑   اوامر الكروب 2   ⦒  :**\n\nᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ \n⑴  ⦙  `.ترحيب + الرساله` \n**✐ : يضيف ترحيب في الكروب اي شخص ينضم راح يرحب بي  ❝**\n⑵  ⦙   `.مسح الترحيبات` \n**✐ :  ييقوم بمسح الترحيب من الكروب ❝**\nᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ\n\n  ⦙  `.ترحيباتي` \n**✐ :  يضهر لك جميع الترحيبات التي وضعتها في الكروب ❝**\n⑷  ⦙ `.رساله الترحيب السابقه تشغيل`  \n**✐ :  عندما يحدث تكرار سيحذف رساله الترحيب ❝**\nᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ \n⑸  ⦙  `.رساله الترحيب السابقه ايقاف`\n**✐ :  عندما يحدث تكرار لا يحذف رساله الترحيب ❝**\nᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ \n⑹ ⦙  `.اضف رد + الكلمه` \n**✐ :  مثلاً تدز رساله هلو تسوي عليها رد بهلوات ❝**\n\nᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ \n⑺ ⦙ `.مسح رد + الكلمه` \n**✐ :  سيحذف الكلمه الي انت ضفتها ❝**\nᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ\n\n⑻ ⦙  `.جميع الردود` \n **✐ :  يجلب لك جميع الردود الذي قمت بأضافتها  ❝**\n⑼ ⦙  `.مسح جميع الردود` \n**✐ :  يمسح جميع الردود الي انت ضفتها ❝**\nᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ \n⑽ ⦙  `.صنع مجموعه + اسم المجموعه`\n**✐ : يقوم بعمل مجموعه خارقه ❝**\n \n⑾ ⦙  `.صنع قناه +  اسم القناة`\n**✐ : يقوم بعمل قناه خاصه  ❝**\nᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ \n⑿ ⦙ `.عدد رسائلي`\n**✐ : سيظهر لك عدد رسائلك في الكروب ❝**\nᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ\n\n"
    buttons = [[Button.inline("اوامر الكروب 1", data="G1"),],[Button.inline("اوامر الكروب 3", data="G3"),],[Button.inline("اوامر الكروب 4", data="G4"),],[Button.inline("اوامر الكروب 5", data="G5"),],[Button.inline("رجوع", data="orders"),]]
    await iqthon.edit(text, buttons=buttons)

@iqthon.tgbot.on(CallbackQuery(data=re.compile(rb"G3")))
@check_owner
async def inlineiqthon(iqthon):
    text = "**🚹  ⦑   اوامر الكروب 3   ⦒  :**\n\nᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ \n ⑴  ⦙  `.تفعيل حمايه المجموعه`\n**✐ : يقوم غلق جميع صلاحيات المجموعه يبقي فقط ارسال  الرسائل❝**\n \n⑵  ⦙ `تعطيل حمايه المجموعه`\n**✐ :  يقوم بتشغيل جميع صلاحيات المجموعة ماعدا تغير المعلومات و التثبيت و اضافه اعضاء تبقى مسدوده❝**\n\n⑶  ⦙ `.صلاحيات المجموعه`\n**✐ : يقوم بعرض صلاحيات المجموعه المغلقه والمفتوحه❝**\n\nᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ\n⑷  ⦙  `.رفع مشرف + الرد على شخص`\n**✐ : يرفع الشخص مشرف يعطي صلاحيه حذف رسائل والتثبيت فقط❝**\n\nᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ \n⑸  ⦙ `.منع + كلمة`\n**✐ : منع كلمه من الارسال في الكروب**❝\n⑹ ⦙ `.الغاء منع + كلمه`\n**✐ : يقوم بالغاء منع الكلمه ❝** \n⑺ ⦙ `.قائمه المنع`\n**✐ : يقوم بجلب جميع الكلمات الممنوعه في الكروب ❝**\nᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ \n⑻ ⦙ ` .تاك + ( الاعداد المحدده وثابتة فقط) ⤵️`\n  ( 10 - 50 - 100 - 200  )\n**✐ : يجلب لك الاعضاء بالروابط بالعدد المحدد ❝**\nᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ \n⑼ ⦙ `.معرفات + ( الاعداد المحدده وثابتة فقط) ⤵️`\n  ( 10 - 50 - 100 - 200  )\n**✐ :جلب لك معرفات الاعضاء بالعدد المحدد ❝**\n\nᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ\n"
    buttons = [[Button.inline("اوامر الكروب 1", data="G1"),],[Button.inline("اوامر الكروب 2", data="G2"),],[Button.inline("اوامر الكروب 4", data="G4"),],[Button.inline("اوامر الكروب 5", data="G5"),],[Button.inline("رجوع", data="orders"),]]
    await iqthon.edit(text, buttons=buttons)
@iqthon.on(admin_cmd(pattern="مسح الملف(?: |$)(.*)"))    
async def unload(event):
    shortname = event.pattern_match.group(1)
    path = Path(f"iqthon/plugins/{shortname}.py")
    if not os.path.exists(path):
        return await edit_delete(event, f"**🝳︙   ملـف مـع مسـار ⚠️ {path} لإلغـاء التثبيـت ⊠**")
    os.remove(path)
    if shortname in CMD_LIST:
        CMD_LIST.pop(shortname)
    if shortname in SUDO_LIST:
        SUDO_LIST.pop(shortname)
    if shortname in CMD_HELP:
        CMD_HELP.pop(shortname)
    try:
        remove_plugin(shortname)
        await edit_or_reply(event, f"**🝳︙   {shortname} تم إلغـاء التثبيـت بنجـاح ✓**")
    except Exception as e:
        await edit_or_reply(event, f"**🝳︙  تمـت الإزالـة بنجـاح ✓ : {shortname}\n{str(e)}**")
@iqthon.on(admin_cmd(pattern="هاش ([\s\S]*)"))    
async def gethash(hash_q):
    hashtxt_ = "".join(hash_q.text.split(maxsplit=1)[1:])
    with open("hashdis.txt", "w+") as hashtxt:
        hashtxt.write(hashtxt_)
    md5 = runapp(["md5sum", "hashdis.txt"], stdout=PIPE)
    md5 = md5.stdout.decode()
    sha1 = runapp(["sha1sum", "hashdis.txt"], stdout=PIPE)
    sha1 = sha1.stdout.decode()
    sha256 = runapp(["sha256sum", "hashdis.txt"], stdout=PIPE)
    sha256 = sha256.stdout.decode()
    sha512 = runapp(["sha512sum", "hashdis.txt"], stdout=PIPE)
    runapp(["rm", "hashdis.txt"], stdout=PIPE)
    sha512 = sha512.stdout.decode()
    ans = f"**Text : **\
            \n`{hashtxt_}`\
            \n**MD5 : **`\
            \n`{md5}`\
            \n**SHA1 : **`\
            \n`{sha1}`\
            \n**SHA256 : **`\
            \n`{sha256}`\
            \n**SHA512 : **`\
            \n`{sha512[:-1]}`\
         "
    await edit_or_reply(hash_q, ans)
@iqthon.tgbot.on(CallbackQuery(data=re.compile(rb"G4")))
@check_owner
async def inlineiqthon(iqthon):
    text = "**🚹  ⦑  اوامر الكروب 4     ⦒  :**\n\nᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ \n⑴  ⦙ `.تنظيف الوسائط` \n ✐: ينضف جميع ميديا من صور وفديوهات و متحركات** او ( `.تنظيف الوسائط + العدد`) ** \n⑵  ⦙ `.حذف الرسائل`\n**✐ :  يحذف جميع الرسائل بلكروب ** \n ` او  `.حذف الرسائل + العدد \nᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ \n⑶  ⦙ `.مسح + الرد على رسالة`\n**✐ :  يحذف الرساله الي راد عليها فقط **\n⑷  ⦙ `.غادر + بلكروب دزها`\n**✐ :  يغادر من المجموعه او من القناة**\nᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ \n⑸  ⦙ ` .تفليش`\n**✐ :  يطرد جميع الي بلكروب الامر صار احسن ومتطور واسرع**\nᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ \n⑹  ⦙ `.اضافه + رابط الكروب `\n**✐ :  يضيفلك جميع الاعضاء الي برابط الكروب يضيفهم بكروبك ( يجب ان تتاكد انو مامحضور حسابك ارسل ⬅️( .فحص الحظر ) علمود تتاكد حسابك محظور او لا) \nᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ \n⑺  ⦙ `.جلب الوقتيه + الرد على الصورة`\n**✐ :  الرد على صوره سريه وقتيه سوف يتم تحويلها الى رسائل المحفوضه كصورة عادية\nᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ \n⑻  ⦙ `.تاك بالكلام + الكلمه + معرف الشخص`\n**✐ :  يسوي تاك للشخص بالرابط جربه وتعرف**\n⑼  ⦙ `.نسخ + الرد على رساله`\n**✐ :  يرسل الرساله التي رديت عليها **\n⑽  ⦙ `.ابلاغ الادمنيه`\n**✐ :  يسوي تاك لجميع الادمنيه ارسله هذا الامر بلمجموعه في حاله اكو تفليش او مشكلة**\n⑾  ⦙ `.المشرفين` \n**✐ : يجيب الك جميع المشرفين في المجموعه او القناه**\n⑿  ⦙ `.البوتات` \n**✐ :  يجيب الك جميع بوتات في المجموعه او قناه**"
    buttons = [[Button.inline("اوامر الكروب 1", data="G1"),],[Button.inline("اوامر الكروب 2", data="G2"),],[Button.inline("اوامر الكروب 3", data="G3"),],[Button.inline("اوامر الكروب 5", data="G5"),],[Button.inline("رجوع", data="orders"),]]
    await iqthon.edit(text, buttons=buttons)
@iqthon.tgbot.on(CallbackQuery(data=re.compile(rb"G5")))
@check_owner
async def inlineiqthon(iqthon):
    text = "**🚹  ⦑  اوامر الكروب 5     ⦒  :**\n\nᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ \n ⑴  ⦙ `.تحذير التكرار + عدد رسائل`\n**✐ :  اي شخص بلكروب يكرر رسائل مالته بلعدد المحدد يقيدة مهما كان رتبته**\n ⑵  ⦙ ` .تحذير تكرار 99999 `\n✐ :  هذا الامر ستعمله من تريد تلغي التحذير لان مستحيل احد يكرر هل عدد ف اعتبار ينل(غي التحذير**\nᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ \n ⑶  ⦙ ` .حظر + الرد على شخص`\n✐ : حظر الشخص من المجموعه او الكروب**\n ⑷  ⦙ ` .الغاء الحظر + الرد على شخص`\n✐ :  يلغي حظر الشخص من المجموعه او الكروب**\nᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ \n ⑸  ⦙ ` .بدء مكالمه `\n✐ :  يقوم بتشغيل مكالمه في المجموعه**\n ⑹  ⦙ `.دعوه للمكالمه`\n✐ : يتم دعوه الاعضاء للمكالمة الشغاله**\nᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ \n ⑺  ⦙ ` .تنزيل مشرف + الرد على شخص`\n✐ :  يقوم بازاله الشخص من الاشراف **\n ⑻  ⦙ ` .تثبيت + الرد على رساله`\n✐ : شرح : تثبيت الرساله التي رديت عليها**⒀  ⦙ `.الأعضاء`\n**✐ :  اضهار قائمة الاعضاء للمجموعة اذا هواي يرسلك ملف كامل لمعلوماتهم**\nᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ \n⒁  ⦙ `.تفليش `\n**✐ :  يقوم بأزاله جميع اعضاء المجموعه او القناة الى 0**\nᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ \n ⒂  ⦙ `.مسح المحظورين`\n**✐ :  يمسح جميع المحظورين في المجموعه او القناه **\n⒃  ⦙ `.المحذوفين`\n**✐:  يجلب لك جميع الحسابات المحذوفه في المجموعه او القناه**\n⒄  ⦙ `.المحذوفين تنظيف`\n**✐ :  مسح جميع الحسابات المحذوفه في المجموعه او القناة**\n⒅  ⦙ `.احصائيات الاعضاء`\n**✐ :  يرسل اليك جميع معلومات اعضاء المجموعه منها عدد الحسابات المحذوفه او الحسابات النشطه او الحسابات اخر ضهور وجميعهم**\n⒆  ⦙ `.عدد رسائلي`\n**✐ : يقوم بحساب عدد رسائلك في المجموعه او القناة**\n⒇  ⦙ `.جلب الاحداث`\n**✐ :  يرسل اليك اخر 20 رساله محذوفه في المجموعة من الاحداث**"
    buttons = [[Button.inline("اوامر الكروب 1", data="G1"),],[Button.inline("اوامر الكروب 2", data="G2"),],[Button.inline("اوامر الكروب 3", data="G3"),],[Button.inline("اوامر الكروب 4", data="G4"),],[Button.inline("رجوع", data="orders"),]]
    await iqthon.edit(text, buttons=buttons)
@iqthon.on(admin_cmd(pattern="هاش(ين|دي) ([\s\S]*)"))    
async def endecrypt(event):
    string = "".join(event.text.split(maxsplit=2)[2:])
    catevent = event
    if event.pattern_match.group(1) == "ين":
        if string:
            result = base64.b64encode(bytes(string, "utf-8")).decode("utf-8")
            result = f"**Shhh! It's Encoded : **\n`{result}`"
        else:
            reply = await event.get_reply_message()
            if not reply:
                return await edit_delete(event, "`What should i encode`")
            mediatype = media_type(reply)
            if mediatype is None:
                result = base64.b64encode(bytes(reply.text, "utf-8")).decode("utf-8")
                result = f"**Shhh! It's Encoded : **\n`{result}`"
            else:
                catevent = await edit_or_reply(event, "`Encoding ...`")
                c_time = time.time()
                downloaded_file_name = await event.client.download_media(                    reply,                    Config.TMP_DOWNLOAD_DIRECTORY,                    progress_callback=lambda d, t: asyncio.get_event_loop().create_task(                        progress(d, t, catevent, c_time, "trying to download")                    ),                )
                catevent = await edit_or_reply(event, "`Encoding ...`")
                with open(downloaded_file_name, "rb") as image_file:
                    result = base64.b64encode(image_file.read()).decode("utf-8")
                os.remove(downloaded_file_name)
        await edit_or_reply(            catevent, result, file_name="encodedfile.txt", caption="It's Encoded"        )
    else:
        try:
            lething = str(                base64.b64decode(                    bytes(event.pattern_match.group(2), "utf-8"), validate=True                )            )[2:]
            await edit_or_reply(event, "**Decoded text :**\n`" + lething[:-1] + "`")
        except Exception as e:
            await edit_delete(event, f"**Error:**\n__{str(e)}__")
if Config.TG_BOT_USERNAME is not None and tgbot is not None :
    @check_owner
    @tgbot.on(events.InlineQuery)
    async def inlineiqthon(iqthon):
        builder = iqthon.builder
        result = None
        query = iqthon.text
        await bot.get_me()
        if query.startswith("اوامر الكروب(?: |$)(.*)") and iqthon.query.user_id == bot.uid:
            buttons = [[Button.inline("اوامر الكروب", data="ord1G"),]]
            result = builder.article(title="iqthon", text=help2, buttons=buttons, link_preview=False)
            await iqthon.answer([result] if result else None)
@bot.on(admin_cmd(outgoing=True, pattern="اوامر الكروب(?: |$)(.*)"))
async def repoiqthon(iqthon):
    if iqthon.fwd_from:
        return
    TG_BOT = Config.TG_BOT_USERNAME
    if iqthon.reply_to_msg_id:
        await iqthon.get_reply_message()
    response = await bot.inline_query(TG_BOT, "اوامر الكروب(?: |$)(.*)")
    await response[0].click(iqthon.chat_id)
    await iqthon.delete()

if Config.TG_BOT_USERNAME is not None and tgbot is not None:
    @check_owner
    @tgbot.on(events.InlineQuery)
    async def inlineiqthon(iqthon):
        builder = iqthon.builder
        result = None
        query = iqthon.text
        await bot.get_me()
        
        if query.startswith("(صيانه|صيانه)") and iqthon.query.user_id == bot.uid:
            try:
                buttons = [[Button.inline("اوامر السورس", data="order1"), Button.inline("اوامر الحساب", data="ord1hs"),],[Button.inline("اوامر الكروب", data="ord1G"), Button.inline("اوامر الالعاب", data="ord1pl"),],[Button.inline("اوامر الصيغ", data="ordsag1"), Button.inline("اوامر الاغاني", data="ordSONG"),], [Button.inline("اسم وقتي", data="order13"), Button.inline("اوامر الاعلانات", data="ordahln1"),],[Button.inline("اوامر التسليه", data="order14"),],[Button.inline("الفارات", data="ordvars"),]]
                result = builder.article(title="iqthon",text=help2,buttons=buttons,link_preview=False)
                await iqthon.answer([result] if result else None)
            except BotInlineDisabledError: 
                await iqthon.send_message( "يجب تفعيل الاونلاين من بوت فاذر اولا " )
           
           
@bot.on(admin_cmd(outgoing=True, pattern="(صيانه|صيانه)"))
async def repoiqthon(iqthon):
    if iqthon.fwd_from:
        return
    TG_BOT = Config.TG_BOT_USERNAME
    
    if iqthon.reply_to_msg_id:
        try:
            await iqthon.get_reply_message()
            response = await bot.inline_query(TG_BOT, "(الاوامر|الأوامر)")
            await response[0].click(iqthon.chat_id)
            await iqthon.delete()
        except BotInlineDisabledError: 
            await iqthon.send_message( "يجب تفعيل الاونلاين من بوت فاذر اولا " )

if Config.TG_BOT_USERNAME is not None and tgbot is not None :
    @check_owner
    @tgbot.on(events.InlineQuery)
    async def inlineiqthon(iqthon):
        builder = iqthon.builder
        result = None
        query = iqthon.text
        await bot.get_me()
        if query.startswith("اوامر الحساب(?: |$)(.*)") and iqthon.query.user_id == bot.uid:
            buttons = [[Button.inline("اوامر الحساب", data="ord1hs"),]]
            result = builder.article(title="iqthon", text=help2, buttons=buttons, link_preview=False)
            await iqthon.answer([result] if result else None)
@bot.on(admin_cmd(outgoing=True, pattern="اوامر الحساب(?: |$)(.*)"))
async def repoiqthon(iqthon):
    if iqthon.fwd_from:
        return
    TG_BOT = Config.TG_BOT_USERNAME
    if iqthon.reply_to_msg_id:
        await iqthon.get_reply_message()
    response = await bot.inline_query(TG_BOT, "اوامر الحساب(?: |$)(.*)")
    await response[0].click(iqthon.chat_id)
    await iqthon.delete()
if Config.TG_BOT_USERNAME is not None and tgbot is not None :
    @check_owner
    @tgbot.on(events.InlineQuery)
    async def inlineiqthon(iqthon):
        builder = iqthon.builder
        result = None
        query = iqthon.text
        await bot.get_me()
        if query.startswith("اوامر الالعاب(?: |$)(.*)") and iqthon.query.user_id == bot.uid:
            buttons = [[Button.inline("اوامر الالعاب", data="ord1pl"),]]
            result = builder.article(title="iqthon", text=help2, buttons=buttons, link_preview=False)
            await iqthon.answer([result] if result else None)

chat = "@BotFather"
@iqthon.on(events.NewMessage(outgoing=True, pattern="^.بوت ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    if event.pattern_match.group(1):
        text, username = event.pattern_match.group(1).split()

    else:
        await event.edit("قم بوضع الامر + اسم البوت + معرف البوت !!`")
        return

    async with event.client.conversation(chat) as conv:
        try:
            await conv.send_message("/newbot")
            audio = await conv.get_response()
            await conv.send_message(text)
            audio = await conv.get_response()
            await conv.send_message(username)
            audio = await conv.get_response()
            await event.client.forward_messages(event.chat_id, audio)
            await event.delete()
        except YouBlockedUserError:
            await event.client(UnblockRequest("93372553"))
            await conv.send_message("/newbot")
            audio = await conv.get_response()
            await conv.send_message(text)
            audio = await conv.get_response()
            await conv.send_message(username)
            audio = await conv.get_response()
            await event.client.forward_messages(event.chat_id, audio)
            await event.delete()
@bot.on(admin_cmd(outgoing=True, pattern="اوامر الالعاب(?: |$)(.*)"))
async def repoiqthon(iqthon):
    if iqthon.fwd_from:
        return
    TG_BOT = Config.TG_BOT_USERNAME
    if iqthon.reply_to_msg_id:
        await iqthon.get_reply_message()
    response = await bot.inline_query(TG_BOT, "اوامر الالعاب(?: |$)(.*)")
    await response[0].click(iqthon.chat_id)
    await iqthon.delete()
if Config.TG_BOT_USERNAME is not None and tgbot is not None :
    @check_owner
    @tgbot.on(events.InlineQuery)
    async def inlineiqthon(iqthon):
        builder = iqthon.builder
        result = None
        query = iqthon.text
        await bot.get_me()
        if query.startswith("اوامر الصيغ(?: |$)(.*)") and iqthon.query.user_id == bot.uid:
            buttons = [[Button.inline("اوامر الصيغ", data="ordsag1"),]]
            result = builder.article(title="iqthon", text=help2, buttons=buttons, link_preview=False)
            await iqthon.answer([result] if result else None)
@iqthon.on(admin_cmd(pattern="م21(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event, "**🚹  ⦑   بصمات تحشيش 1   ⦒  :**\n\n                                                       ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ\n(`.ص1`)   ⦙   ابو  عباس  لو  تاكل  خره\n(`.ص2`)   ⦙   استمر  نحن  معك\n(`.ص3`)   ⦙   افحط  بوجه\n(`.ص4`)   ⦙   اكعد  لا  اسطرك  سطره  العباس\n(`.ص5`)   ⦙   اللهم  لا  شماته\n(`.ص6`)   ⦙   امرع  دينه\n(`.ص7`)   ⦙   امشي  بربوك\n(`.ص8`)   ⦙   انت  اسكت  انت  اسكت\n(`.ص9`)   ⦙   انت  سايق  زربه\n                                                       ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ\n(`.ص10`)   ⦙   اوني  تشان\n(`.ص11`)   ⦙   برافو  عليك  استادي \n(`.ص12`)   ⦙   بلوك  محترم\n(`.ص13`)   ⦙   بووم  في  منتصف  الجبهة \n(`.ص14`)   ⦙   بيتش \n(`.ص15`)   ⦙   تخوني  ؟\n(`.ص16`)   ⦙   تره  متكدرلي\n(`.ص17`)   ⦙   تعبان  اوي\n(`.ص18`)   ⦙   تكذب\n(`.ص19`)   ⦙   حسبي  الله\n                                                       ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ\n(`.ص20`)   ⦙   حشاش \n(`.ص21`)   ⦙   حقير  \n(`.ص22`)   ⦙   خاص  \n(`.ص23`)   ⦙   خاله  ما  تنامون  \n(`.ص24`)   ⦙   خرب  شرفي  اذا  ابقى  بالعراق \n(`.ص25`)   ⦙   دكات  الوكت  الاغبر  \n(`.ص26`)   ⦙   ررردح  \n(`.ص27`)   ⦙   سلامن  عليكم  \n(`.ص28`)   ⦙   بوم منتصف جبهه   \n(`.ص29`)   ⦙   شكد  شفت  ناس  مدودة\n                                                       ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ")
@iqthon.on(admin_cmd(pattern="م22(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event, "**🚹  ⦑   بصمات تحشيش 2   ⦒  :**\n\n                                                       ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ\n(`.ص30`)   ⦙  شلون  ، \n(`.ص31`)   ⦙  صح  لنوم  \n(`.ص32`)   ⦙  صمت  \n(`.ص33`)   ⦙  ضحكة  مصطفى  الحجي  \n(`.ص34`)   ⦙  طماطه  \n(`.ص35`)   ⦙  طيح  الله  حضك  \n(`.ص36`)   ⦙  فاك  يوو  \n(`.ص37`)   ⦙  اني فرحان وعمامي فرحانين\n(`.ص38`)   ⦙  لا  تضل  تضرط  \n(`.ص39`)   ⦙  لا  تقتل  المتعه  يا  مسلم  \n                                                       ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ\n(`.ص40`)   ⦙  لا  مستحيل  \n(`.ص41`)   ⦙  لا  والله  شو  عصبي  \n(`.ص42`)   ⦙  لش  \n(`.ص43`)   ⦙  لك  اني  شعليه  \n(`.ص44`)   ⦙  ما  اشرب  \n(`.ص45`)   ⦙  مع  الاسف  \n(`.ص46`)   ⦙  مقتدى  \n(`.ص47`)   ⦙  من  رخصتكم  \n(`.ص48`)   ⦙  منو  انت  \n(`.ص49`)   ⦙  منورني  \n                                                       ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ\n(`.ص50`)  ⦙  نتلاكه  بالدور  الثاني \n(`.ص51`)  ⦙  نستودعكم  الله  \n(`.ص52`)  ⦙  ها  شنهي  \n(`.ص53`)  ⦙  ههاي  الافكار  حطها ب\n(`.ص54`)  ⦙  ليش شنو سببها ليش\n(`.ص55`)  ⦙  يموتون  جهالي\n(`.ص56`)  ⦙  اريد انام\n(`.ص57`)  ⦙  افتحك فتح\n(`.ص58`)  ⦙  اكل خره لدوخني\n(`.ص59`)  ⦙  السيد شنهو السيد\n                                                       ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ\n(`.ص60`)  ⦙  زيج2\n(`.ص61`)  ⦙  زيج لهارون\n(`.ص62`)  ⦙  زيج الناصرية\n(`.ص63`)  ⦙  راقبو اطفالكم\n(`.ص64`)  ⦙  راح اموتن\n(`.ص65`)  ⦙  ذس اس مضرطة\n(`.ص66`)  ⦙  دروح سرسح منا\n(`.ص67`)  ⦙  خويه ما دكوم بيه\n(`.ص68`)  ⦙  خلصت تمسلت ديلة كافي انجب\n(`.ص69`)  ⦙  بعدك تخاف\n                                                       ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ")
@iqthon.on(admin_cmd(pattern="م23(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event, "**🚹  ⦑   بصمات تحشيش 3   ⦒  :**\n\n                                                       ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ\n(`.ص70`)  ⦙  بسبوس\n(`.ص71`)  ⦙  اني بتيتة كحبة\n(`.ص72`)  ⦙  انعل ابوكم لابو اليلعب وياكم طوبة\n(`.ص73`)  ⦙  انت شدخلك\n(`.ص74`)  ⦙  انا ماشي بطلع\n(`.ص75`)  ⦙  امداك وامده الخلفتك\n(`.ص76`)  ⦙  امبيههههه\n(`.ص77`)  ⦙  هدي بيبي\n(`.ص78`)  ⦙  هاه صدك تحجي\n(`.ص79`)  ⦙  مو كتلك رجعني\n                                                       ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ\n(`.ص80`)  ⦙  مامرجية منك هاية\n(`.ص81`)  ⦙  ليش هيجي\n(`.ص82`)  ⦙  كـــافـي\n(`.ص83`)  ⦙  كس اخت السيد\n(`.ص84`)  ⦙  شنو كواد ولك اني هنا\n(`.ص85`)  ⦙  شجلبت\n(`.ص86`)  ⦙  شبيك وجه الدبس\n(`.ص87`)  ⦙  سييييي\n(`.ص88`)  ⦙  زيجج1\n(`.ص89`)  ⦙  يموتون جهالي\n                                                       ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ\n(`.ص90`)  ⦙  ياخي اسكت اسكت\n(`.ص91`)  ⦙  وينهم\n(`.ص92`)  ⦙  هيلو سامر وحود\n(`.ص93`)  ⦙  هو\n(`.ص94`)  ⦙  ههاي الافكار حطها\n                                                       ᚖ⌁⌁⌁⌁⌁⌁⌁⌁⧼ٍᴄ.ʀ ѕᴏᴜʀᴄᴇ⧽⌁⌁⌁⌁⌁⌁⌁⌁ᚖ\n")
@bot.on(admin_cmd(outgoing=True, pattern="اوامر الصيغ(?: |$)(.*)"))
async def repoiqthon(iqthon):
    if iqthon.fwd_from:
        return
    TG_BOT = Config.TG_BOT_USERNAME
    if iqthon.reply_to_msg_id:
        await iqthon.get_reply_message()
    response = await bot.inline_query(TG_BOT, "اوامر الصيغ(?: |$)(.*)")
    await response[0].click(iqthon.chat_id)
    await iqthon.delete()
@iqthon.on(admin_cmd(pattern="فتح همسه(?: |$)(.*)"))    
async def iq(event):
    await edit_or_reply(event, "**عزيزي كل عقلك ؟  **\n**وين اكو شي اسمه فتح همسة عرض العالم ماتخاف علية ادبسزز ولي يلة 🙂💔**")
