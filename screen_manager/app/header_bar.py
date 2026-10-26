"""Top bar of a screen: what the firmware draws right of the screen name.

Firmware 0.2.32+ only draws. This module decides everything that needs Home Assistant: an
entity's text (number format, units, translated states), its icon, its accent colour
and whether it shows at all. Clock, analog clock and date tick on the screen itself, and a
relative time ("5 min ago") travels as a unix time, so the screen counts the minutes
without any traffic.

Wire format, one message after the layout: {"v":1,"op":"header","items":[...]} with per item
"k" (clock, analog, date, text, ago), "i" (icon codepoint), "t" (text), "e" (unix time) and
"c" (accent colour RRGGBB). An entity's item also has "d", the index of the tile whose card a tap on it opens, for a
screen that takes cards from its top bar (core.BAR_CARDS_FEATURE, firmware 0.56.0+).
"""
import math
import unicodedata
from datetime import datetime, time
from decimal import ROUND_HALF_UP, Decimal

import durations
import tile_icons
from core import (BAR_STATUS_FEATURE, BAR_STATUS_MIN_FIRMWARE, BATTERY_CONTENTS, BATTERY_FEATURE, BATTERY_MIN_FIRMWARE, BATTERY_SHOWS,
                  HEADER_BUILTIN, HEADER_CONTENTS, HEADER_MAX_ITEMS, HEADER_MIN_FIRMWARE, HEADER_SHOWS, HEADER_STATUS, PLUGIN_ITEM_CONTENTS,
                  WIFI_CONTENTS, WIFI_SHOWS, epoch, header_items, local_clock, one_mu, short, state_word)
import i18n
from i18n import TRANSLATIONS, screen_number, screen_t, t

# Characters the top bar's text font carries on both boards (`sublabel_big` in the profiles;
# tests/test_header_bar.py keeps them equal). Anything else folds to its base letter or goes.
# The characters the screen's text fonts carry (the sublabel_big glyph list; tests/test_header_bar.py keeps them equal):
# every letter European languages write with since app 0.2.90, and every printable ASCII character and three hearts since firmware 0.36.0.
GLYPHS = frozenset('<>—&@!,.?"%()+-_:°0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz/…·\'#*=;²³µ–$^~|`[]{}\\×©®™¢¥§♡♥❤ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõöøùúûüýþÿĄąĆćĘęŁłŃńŚśŹźŻżČčĎďĚěŇňŘřŠšŤťŮůŽžĹĺĽľŔŕŐőŰűĂăȘșȚțĐđĀāĒēĢģĪīĶķĻļŅņŪūĖėĮįŲųĞğİıŞşĊċĠġĦħŴŵŶŷĿŀŒœŸ„“”‘’«»‹›¿¡€£')
# The letters of firmware from before the languages (0.2.75 and older), which gets what it can draw.
LEGACY_GLYPHS = frozenset("<>—&@!,.?\"%()+-_:°0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyzäöüÄÖÜß/…·'#*=;²³µéèëêïîóôàáâçñúû–")

# The CJK glyphs a screen with the "cjk" feature draws (docs/CJK.md): the set its build carried in the four
# text fonts (FONT_CJK_GLYPHS, packages/hardware/guition-esp32p4.yaml). clean_text keeps them only for such a
# screen; tests/test_cjk.py holds this set against that board's fonts.
CJK_GLYPHS = frozenset('、。〈〉《》【】〔〕一七万丈三上下不与专且世业东丝丢两严个中丰临为主丽举乃久么义之乌乎乏乐乘九也习乡书买乱了予争事二于云互五亚些亡交亦产享京亮亲人亿什仅今介仍从仔他付代令以仪们仰件价任份企伊伍休众优伙会伟传伤伦伯估伴伸似但位低住体何余佛作你佳使例供依侵便促俄保信俩修俱倍倒候借值倾假偏做停健偷傲傻像儿允元兄充先光克免党入全八公六兰共关兴兵其具典养兼兽内册再冒写军农冠冰冲决况冷净准凌减几凭出击函刀分切划列刘则刚创初删判利别到制刷券刺刻前剑剥剧剩副力办功加务动助努励劳势勇包化北区医十千升午半华协单卖南博占卡卫印危即却卷厂厅历厉压厌厕原去县参又及友双反发取受变叙口古句另只叫召可台史右叶号司吁吃各合同名后向吓吗否吧吨含听启吸吹吻呀呆呈告员呢周味呼命和咖咨咱品哇哈响哥哦哪哭哲唤售唯唱商啊啡啥啦善喊喜喝嗯嘛嘴器四回因团园困围固国图圈土圣在地圳场圾址均坏坐坑块坚坛坡坦垃垄型埃城域培基堂塔塞境墙增墨士声处备复夏外多夜够大天太夫央失头夹夺奇奋奖套奥女奴她好如妇妈妳妹妻始姐姑姓委姻威娘娱婆婚婴媒子孕字存季学孩宁它宅宇守安完宗官宙定宜宝实审客宣室宪宫害家容宽宾密富寓察对寻导封射将尊小少尔尚尝尤就尸尼尽局屁层居届屋屏展属屠山屿岁岗岛岸川州工左巧巨差己已巴币市布师希帘帝带席帮常幅幕干平年并幸幻广庆床序库应底店府庞废度座庭康延建开异弃弄式引弟张弦弱弹强归当录形彩影役彻彼往征径待很律得循微德徽心必忆志忘忙快念忽怀态怎怒怕怖怜思急性怪总恋恐恢恨恩息恶悉患您悲情惊惜惠惧惩惯想意愚感愤愿慢慧憾懂戏成我或战截戴户房所手才打托执扩扫扮批找承技把抓投抗抢护报抱抵抽担拆拉拍拒拔拖拜拟拥择括拭拯拿持挂指按挑挥挺捕损换据授掉掌排探接控推措描提插握揭援搜搞搬搭摄摆摧摸撑撞撤播操擦支收改攻放政故效敌敏救教敢散敦数整文斗料斤断斯新方施旁旅旋族旗无既日旦旧早时明易星映昨是显晚晨普景晴智暂暖暗暴曝曰曲更曾替最月有朋服朗望朝期未末本术机杀杂权杉李材村束条来杨杭杯松板极构析林果枪架某染柔查标树校样核根格案档桥梁梦械检棒森植楚楼概模次欢欣欧欲款歉歌止正此步武歧死殊段毁母每毒比毕毛毫民气氛水永求汇汉江池污汽沉沙沟没河油治法泛波注泰泳泽洋洗洛津洲活派流测济浙浪海消涉润涨深混添清渐温港游湖湾湿源滑滚满漂漏演漫澳激火灭灯灵灾炸点烈烟烦热焦然照熟燥爆爬爱父爷爸片版牌牙牛物牲特牺犯状犹狂狗独狱狼猜猪猫献率王玩环现玻班球理瑞璃甚生用田由申电男甸画界留略疆疑疗疯疾病痛登白百的皆皇皮益监盖盘盛盟目直相盾省看真眠眼着睛睡督瞧瞭矛知短石矶码研破础硬确碌碍碰示礼社祈祖祝神票祷禁福离秀私种科秒秘秩积称移程稍税稣稳穆究空穿突窗立站竞竟章童端笑笔符第等筑答策签简算管箭箱篇篮籍米类粉粮精系素索紧累繁红约级纪纯纳纵纷纸纽线练组细织终绍经绑结绕给络绝统继绩绪续维综绿缅缓编缘缺网罗罚罪置署美群翰翻老考者而耳耶聊职联聚聪肃肉股肤肯育胁胆背胜胞能脑脚脱脸腊腐腾腿臣自至致舆舒舞航般船良色艺节花苏若苦英苹范茶草荐荣药荷莫获菜菲营落著蒙蓝藏虑虽蛋融蠢血行街衡衣补表袋袖被袭裁裂装西要覆见观规视览觉角解触言誉警计订认讨让训议讯记讲许论讼设访证评识诉词译试诗话诞询该详语误说请诺读课谁调谈谊谋谐谓谢谱谴谷象贝负贡财责败账货质贫购贴贵贷贸费资赋赏赖赚赛赞赢走赴赵赶起超越趋趣足跃跑距跟跨路跳践踪蹈身躺车轨转轮软轻载较辆辈辑输辖辞边辽达迅过迎运近返还这进远违连迟迫述追退送适逃选透逐递途通速造逮逻逼逾遇遍道遗遭遵避邀邓那邦邪邻郡部都配酒醒采释里重量金针钟钥钮钱铁银链销锁错键镇镜长门闭问闲间闻阁阅队防阳阴阵阶阻阿附际陆陈降限陕院除险陪陷随隐障隶难雄集雨雪零雷雹雾需震霜露青静非靠面革韩音页顶项顺须顾顿预领频颗题颜额风飞食餐饭饰饿馆首香马驶驻驾骂骄验骑骗高鬼魂魔鱼鲁鲜鸟鸡麦麻黄黎黑默鼓龄龙！％（），：；？～￥')
TEXT_BYTES = 40
# The months in English, the language of reference (tests/test_header_bar.py); a screen gets them in its own language
# (short_date, app 0.2.90).
MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
UNAVAILABLE = '—'

# Home Assistant's own words where they fit a small bar; the screen shows the rest as they come. The keys of the words,
# which go in the screens' language (app 0.2.90): Home Assistant's own (screen.ha; a lock's are those of a lock sensor)
# where the bar says the same, else the bar's ("Up" for above the horizon).
STATES = {
    'on': 'screen.ha.on', 'off': 'screen.ha.off', 'home': 'screen.ha.person.home', 'not_home': 'screen.ha.person.not_home',
    'open': 'screen.ha.cover.open', 'closed': 'screen.ha.cover.closed', 'opening': 'screen.ha.cover.opening',
    'closing': 'screen.ha.cover.closing', 'locked': 'screen.ha.binary.lock_off', 'unlocked': 'screen.ha.binary.lock_on',
    'locking': 'addon.screen.states.locking', 'unlocking': 'addon.screen.states.unlocking', 'jammed': 'addon.screen.states.jammed',
    'playing': 'screen.ha.media.playing', 'paused': 'screen.ha.media.paused', 'idle': 'screen.ha.media.idle',
    'standby': 'screen.ha.media.standby', 'buffering': 'addon.screen.states.buffering', 'cleaning': 'screen.ha.vacuum.cleaning',
    'docked': 'screen.ha.vacuum.docked', 'returning': 'addon.screen.states.returning', 'error': 'addon.screen.states.error',
    'heat': 'screen.ha.climate.heat', 'cool': 'screen.ha.climate.cool', 'heat_cool': 'screen.ha.climate.auto',
    'auto': 'screen.ha.climate.auto', 'dry': 'screen.ha.climate.dry', 'fan_only': 'screen.ha.climate.fan_only',
    'disarmed': 'addon.screen.states.disarmed', 'armed_home': 'addon.screen.states.armed_home',
    'armed_away': 'addon.screen.states.armed_away', 'armed_night': 'addon.screen.states.armed_night',
    'armed_vacation': 'addon.screen.states.armed_vacation', 'armed_custom_bypass': 'addon.screen.states.armed',
    'arming': 'addon.screen.states.arming', 'pending': 'addon.screen.states.pending', 'triggered': 'addon.screen.states.triggered',
    'active': 'addon.screen.states.active', 'above_horizon': 'addon.screen.states.up', 'below_horizon': 'addon.screen.states.down',
}

def state_text(raw):
    """The bar's word for a state, in the screens' language; None for a state it has no word of its own for."""
    return screen_t(STATES[raw]) if raw in STATES else None

# The device classes with words of their own. Tiles and cards show the same words from the screen's own table, BINARY_WORDS
# in components/smart_display/tile_controls.h (firmware 0.2.53+); tests/test_binary_words.py keeps the two equal. The words
# are Home Assistant's, from the translations (screen.ha.binary, app 0.2.90): BINARY_STATES holds them in English, the
# language of reference, as device_class: (on, off); binary_words gives them in the screens' language.
BINARY_CLASSES = ('battery', 'battery_charging', 'carbon_monoxide', 'cold', 'connectivity', 'door', 'garage_door', 'gas',
                  'heat', 'light', 'lock', 'moisture', 'motion', 'moving', 'occupancy', 'opening', 'plug', 'power',
                  'presence', 'problem', 'running', 'safety', 'smoke', 'sound', 'tamper', 'update', 'vibration', 'window')
BINARY_STATES = {name: (TRANSLATIONS.text(f'screen.ha.binary.{name}_on'), TRANSLATIONS.text(f'screen.ha.binary.{name}_off'))
                 for name in BINARY_CLASSES}

def binary_words(device_class):
    """(on, off) for a binary sensor of this class in the screens' language; On and Off for a class without words of its
    own, as the screen does."""
    if device_class in BINARY_STATES:
        return screen_t(f'screen.ha.binary.{device_class}_on'), screen_t(f'screen.ha.binary.{device_class}_off')
    return screen_t('screen.ha.on'), screen_t('screen.ha.off')

# Icon names from tile_icons; the fonts of both boards carry every one of them.
BINARY_ICONS = {  # device_class: (on, off)
    'motion': ('motion-sensor', 'motion-sensor'), 'occupancy': ('home-account', 'home-account'),
    'presence': ('home-account', 'home-account'), 'door': ('door-open', 'door-closed'), 'garage_door': ('garage', 'garage'),
    'opening': ('door-open', 'door-closed'), 'window': ('window-closed-variant', 'window-closed-variant'),
    'connectivity': ('router-wireless', 'router-wireless'), 'plug': ('power-plug', 'power-plug'), 'power': ('flash', 'flash'),
    'moisture': ('water-alert', 'water'), 'smoke': ('smoke-detector', 'smoke-detector'), 'gas': ('meter-gas', 'meter-gas'),
    'carbon_monoxide': ('smoke-detector', 'smoke-detector'), 'lock': ('lock-open-variant', 'lock'),
    'battery': ('battery-high', 'battery-high'), 'battery_charging': ('battery-high', 'battery-high'),
    'problem': ('alert-outline', 'check'), 'safety': ('alert-outline', 'check'), 'tamper': ('alert-outline', 'check'),
    'vibration': ('alert-outline', 'check'), 'heat': ('fire', 'fire'), 'cold': ('snowflake', 'snowflake'),
    'light': ('weather-sunny', 'weather-night'), 'running': ('play', 'stop'), 'sound': ('music-note', 'music-note'),
    'update': ('cog', 'cog'), 'moving': ('run', 'run'),
}
SENSOR_ICONS = {
    'temperature': 'thermometer', 'humidity': 'water-percent', 'moisture': 'water-percent', 'power': 'flash', 'energy': 'flash',
    'apparent_power': 'flash', 'reactive_power': 'flash', 'voltage': 'flash', 'current': 'flash', 'power_factor': 'flash',
    'battery': 'battery-high', 'illuminance': 'weather-sunny', 'pressure': 'gauge', 'atmospheric_pressure': 'gauge',
    'carbon_dioxide': 'molecule-co2', 'gas': 'meter-gas', 'water': 'water', 'signal_strength': 'router-wireless',
    'timestamp': 'clock-outline', 'duration': 'timer-outline', 'pm1': 'air-purifier', 'pm25': 'air-purifier',
    'pm10': 'air-purifier', 'aqi': 'air-purifier', 'volatile_organic_compounds': 'air-purifier', 'wind_speed': 'weather-windy',
    'speed': 'weather-windy', 'precipitation': 'weather-rainy', 'precipitation_intensity': 'weather-rainy',
    'irradiance': 'solar-power', 'date': 'calendar',
}
DOMAIN_ICONS = {
    'light': 'lightbulb', 'switch': 'toggle-switch', 'input_boolean': 'toggle-switch', 'automation': 'robot', 'remote': 'remote', 'fan': 'fan', 'cover': 'window-shutter',
    'climate': 'thermostat', 'vacuum': 'robot-vacuum', 'media_player': 'speaker', 'scene': 'palette', 'script': 'script-text',
    'button': 'gesture-tap-button', 'input_button': 'gesture-tap-button', 'person': 'account', 'device_tracker': 'map-marker',
    'zone': 'account-group', 'lock': 'lock', 'alarm_control_panel': 'shield-home', 'timer': 'timer-outline', 'counter': 'gauge',
    'event': 'bell-ring', 'input_datetime': 'calendar', 'input_text': 'script-text', 'water_heater': 'water-boiler',
    'humidifier': 'air-humidifier', 'select': 'cog', 'input_select': 'cog', 'number': 'gauge', 'input_number': 'gauge',
    'sensor': 'gauge', 'binary_sensor': 'gauge',
}
# Their state is the moment they last ran or fired: the bar shows how long ago.
MOMENT_DOMAINS = frozenset(['scene', 'button', 'input_button', 'event'])
INACTIVE = frozenset(['off', 'closed', 'not_home', 'idle', 'docked', 'standby', 'locked', 'disarmed', 'paused', 'below_horizon'])
AMBER, GREEN, RED, BLUE, ORANGE, TEAL = 'FFB300', '43A047', 'E53935', '2196F3', 'FF6F22', '009688'
# Binary sensor classes Home Assistant draws red while on (--state-binary_sensor-<class>-on-color); the screen's
# tile_controls::alarm_class has the same list (app 0.2.85).
ALARM_CLASSES = frozenset(['battery', 'carbon_monoxide', 'gas', 'heat', 'lock', 'moisture', 'problem', 'safety', 'smoke',
                           'sound', 'tamper'])

_cjk_screen = False


def set_cjk_screen(features=None) -> None:
    """Whether the screen being compiled for draws CJK (docs/CJK.md): its hello said "cjk". None is this app's own
    firmware, the preview, which draws what the newest build does."""
    global _cjk_screen
    _cjk_screen = features is None or 'cjk' in (features or frozenset())


def clean_text(text):
    """Text the screen can draw: known glyphs, accents folded to the base letter, at most TEXT_BYTES."""
    if i18n.legacy_screen():
        glyphs = LEGACY_GLYPHS
    elif _cjk_screen:
        glyphs = GLYPHS | CJK_GLYPHS
    else:
        glyphs = GLYPHS
    out = []
    for char in unicodedata.normalize('NFC', one_mu(text)):
        if char in glyphs:
            out.append(char)
            continue
        base = unicodedata.normalize('NFKD', char)[0]
        if base in glyphs:
            out.append(base)
    return short(''.join(out).strip(), TEXT_BYTES)

def number_text(value, precision=None):
    """A number as Home Assistant writes it, in the screens' number format (app 0.2.90): "1,234.5", "1.234,5" or
    "1 234,5"."""
    if precision is None:
        # Without a display precision HA keeps integers whole and shows at most three decimals.
        digits = 0 if float(value).is_integer() else 3
        text = f'{value:.{digits}f}'
        if '.' in text:
            text = text.rstrip('0').rstrip('.')
    else:
        text = f'{value:.{precision}f}'
    # "-0" and "-0.0" are just zero.
    if text.startswith('-') and not any(c not in '0.' for c in text[1:]):
        text = text[1:]
    return screen_number(text)

def attribute_number(value):
    """A number an attribute holds, as Home Assistant's frontend writes it (computeAttributeValueDisplay, formatNumber
    without options): at most two decimals, in the screens' number format. Intl.NumberFormat rounds the number as
    JavaScript writes it, a half away from zero: 2.675 is "2.68", although the float is 2.67499..., and -0.001 is
    "-0". repr writes a float as JavaScript does. 61.60000000000001 is "61.6" (GitHub #241)."""
    exact = Decimal(repr(float(value))) if isinstance(value, float) else Decimal(value)
    return screen_number(format(exact.quantize(Decimal('0.01'), ROUND_HALF_UP).normalize(), 'f'))

def with_unit(text, unit):
    """Home Assistant's spacing: "21.3 °C", "65%" ("65 %" in German and French), "18°"."""
    return text + i18n.unit_suffix(unit)

def precision_of(entry):
    options = ((entry or {}).get('options') or {}).get('sensor') or {}
    for key in ('display_precision', 'suggested_display_precision'):
        value = options.get(key)
        if type(value) is int and 0 <= value <= 6:
            return value
    return None

def numeric(value):
    try:
        number = float(value)
    except (TypeError, ValueError):
        return None
    return number if math.isfinite(number) else None

def short_date(moment):
    """"15 Sep", in the screens' language and in its order of day and month (app 0.2.90)."""
    return screen_t('screen.date.day_month', day=moment.day, month=screen_t(f'screen.date.months_short.{moment.month - 1}'))

def value(entity, state, entry=None, units=None, tz=None, words=None):
    """(text, unix time) an entity shows as its state; exactly one of them is set. `words` are Home Assistant's
    translations: its word shows where the bar has none of its own ("Rinsing" for rinsing, app 0.2.67)."""
    domain = entity.split('.')[0]
    raw = state.get('state') if state else None
    attrs = (state or {}).get('attributes') or {}
    if raw in (None, '', 'unavailable', 'unknown'):
        return UNAVAILABLE, None
    if domain in MOMENT_DOMAINS:
        return (None, epoch(raw)) if epoch(raw) else (UNAVAILABLE, None)
    if domain == 'script':
        moment = epoch(attrs.get('last_triggered'))
        if raw == 'on':
            return screen_t('addon.screen.script_running'), None
        return (None, moment) if moment else (screen_t('screen.script.never_run'), None)
    if domain == 'sun':
        # The next event: sunset while the sun is up, sunrise while it is down.
        clock = local_clock(attrs.get('next_setting' if raw == 'above_horizon' else 'next_rising'), tz)
        if clock:
            clock = i18n.screen_clock(int(clock[:2]), int(clock[3:]))
        return (clock or state_text(raw) or raw), None
    if domain == 'weather':
        temperature = numeric(attrs.get('temperature'))
        if temperature is None:
            return UNAVAILABLE, None
        return with_unit(number_text(temperature, 0), attrs.get('temperature_unit') or (units or {}).get('temperature', '°C')), None
    if domain == 'climate':
        current = numeric(attrs.get('current_temperature'))
        if current is not None:
            return with_unit(number_text(current, 1), (units or {}).get('temperature', '°C')), None
    if domain in ('person', 'device_tracker'):
        return state_text(raw) or raw, None
    if domain == 'binary_sensor':
        pair = binary_words(attrs.get('device_class'))
        return (pair[0] if raw == 'on' else pair[1] if raw == 'off' else raw), None
    if domain == 'input_datetime':
        # "2026-09-15 07:30:00", "2026-09-15" or just "07:30:00".
        try:
            moment = datetime.fromisoformat(raw) if attrs.get('has_date') else datetime.combine(datetime.min, time.fromisoformat(raw))
        except ValueError:
            return raw, None
        # A time of day as the screens' clock writes it (Settings -> Language & region, app 0.2.90).
        if attrs.get('has_date') and attrs.get('has_time'):
            return f'{short_date(moment)} {i18n.screen_clock(moment.hour, moment.minute)}', None
        return (short_date(moment) if attrs.get('has_date') else i18n.screen_clock(moment.hour, moment.minute)), None
    if domain == 'sensor' and attrs.get('device_class') == 'timestamp':
        return (None, epoch(raw)) if epoch(raw) else (raw, None)
    if domain == 'sensor' and attrs.get('device_class') == 'date':
        try:
            return short_date(datetime.fromisoformat(raw)), None
        except ValueError:
            return raw, None
    number = numeric(raw)
    # A duration as Home Assistant writes it, in hours and minutes (durations.py, wishlist 107).
    if number is not None and domain == 'sensor' and durations.is_duration(attrs):
        return durations.text(raw, attrs['unit_of_measurement'], i18n.screen_language(), precision_of(entry)), None
    if number is not None and domain in ('sensor', 'number', 'input_number', 'counter', 'zone'):
        return with_unit(number_text(number, precision_of(entry)), attrs.get('unit_of_measurement')), None
    if domain in ('input_text', 'input_select', 'select'):
        return state_word(entity, raw, attrs, entry, words) or raw, None
    if raw in STATES:
        return state_text(raw), None
    return state_word(entity, raw, attrs, entry, words) or raw[:1].upper() + raw[1:], None

def active(entity, state):
    """"Only when active": on, open, home, detected, playing, heating, or a number other than zero."""
    raw = state.get('state') if state else None
    domain = entity.split('.')[0]
    if raw in (None, '', 'unavailable', 'unknown'):
        return False
    if domain in ('person', 'device_tracker'):
        return raw == 'home'
    if domain in MOMENT_DOMAINS or domain in ('weather', 'sun') and raw != 'below_horizon':
        return True
    number = numeric(raw)
    if number is not None:
        return number != 0
    return raw not in INACTIVE

def accent(entity, state):
    """Icon colour while an entity is active, like Home Assistant's badges; None keeps the calm grey."""
    raw = state.get('state') if state else None
    domain = entity.split('.')[0]
    attrs = (state or {}).get('attributes') or {}
    if domain == 'binary_sensor' and raw == 'on':
        return RED if attrs.get('device_class') in ALARM_CLASSES else AMBER
    if domain in ('light', 'switch', 'input_boolean', 'automation', 'remote', 'fan') and raw == 'on':
        return AMBER
    if domain in ('person', 'device_tracker') and raw == 'home':
        return GREEN
    if domain == 'climate' and raw in ('heat', 'cool'):
        return ORANGE if raw == 'heat' else BLUE
    # Home Assistant's own state colours: armed and locked green, on their way orange, alarm and open red.
    if domain == 'alarm_control_panel':
        return RED if raw == 'triggered' else ORANGE if raw in ('arming', 'pending', 'disarming') else GREEN if raw and raw.startswith('armed') else None
    if domain == 'lock':
        return GREEN if raw == 'locked' else ORANGE if raw in ('locking', 'unlocking', 'opening') else RED if raw in ('unlocked', 'open', 'jammed') else None
    if domain == 'media_player' and raw == 'playing':
        return BLUE
    # A humidifier is Home Assistant's blue while it is on, drying or humidifying alike (--state-humidifier-on-color).
    if domain == 'humidifier' and raw == 'on':
        return BLUE
    if domain == 'vacuum' and raw == 'cleaning':
        return TEAL
    return None

def auto_icon(entity, state, entry=None):
    """Codepoint of the icon Home Assistant would show: its own mdi icon, else Home Assistant's default icon for this state
    (app 0.2.67, the same as a tile), else the device class and domain tables."""
    attrs = (state or {}).get('attributes') or {}
    raw = (state or {}).get('state')
    own = tile_icons.ha_icon(attrs) or tile_icons.default_glyph(entity, raw, attrs, entry)
    if own:
        return own
    domain, device_class = entity.split('.')[0], attrs.get('device_class')
    if domain == 'weather':
        name = tile_icons.WEATHER.get(raw, 'weather-partly-cloudy')
    elif domain == 'light' and raw == 'off':
        name = 'lightbulb-off'
    elif domain == 'sun':
        name = 'weather-sunset-down' if raw == 'above_horizon' else 'weather-sunset-up'
    elif domain == 'binary_sensor' and device_class in BINARY_ICONS:
        name = BINARY_ICONS[device_class][0 if raw == 'on' else 1]
    elif domain == 'sensor' and device_class in SENSOR_ICONS:
        name = SENSOR_ICONS[device_class]
    elif domain == 'lock' and raw in ('unlocked', 'open', 'unlocking'):
        name = 'lock-open-variant'
    else:
        name = DOMAIN_ICONS.get(domain, tile_icons.FALLBACK)
    return tile_icons.GLYPHS[name]

def entity_item(item, states, registry=None, units=None, tz=None, words=None, card=None):
    """(wire item, shown) for one entity item; the wire item exists even while hidden, for the editor. `card`: the index
    of the tile whose card a tap on it opens (core.bar_cards), or None."""
    entity = item['entity']
    state = states.get(entity)
    wire = {'k': 'text'}
    if item['icon'] == 'auto':
        wire['i'] = auto_icon(entity, state, (registry or {}).get(entity) if isinstance(registry, dict) else None)
    elif item['icon'] != 'none':
        wire['i'] = tile_icons.ICONS[item['icon']][0]
    # Its card, whatever the item shows: its icon alone opens it too (GitHub #252).
    if card is not None:
        wire['d'] = card
    if item['content'] == 'icon':
        # Its icon alone (GitHub #144): no text, so the screen draws the icon, coloured and changing with the state.
        wire['t'] = ''
        color = accent(entity, state)
        if color:
            wire['c'] = color
        return wire, item['show'] == 'always' or active(entity, state)
    if item['content'] == 'last_changed':
        moment = epoch((state or {}).get('last_changed'))
        text, moment = (None, moment) if moment else (UNAVAILABLE, None)
    else:
        text, moment = value(entity, state, (registry or {}).get(entity), units, tz, words)
    if moment:
        wire.update(k='ago', e=moment)
    else:
        wire['t'] = clean_text(text) or UNAVAILABLE
    color = accent(entity, state)
    if color:
        wire['c'] = color
    return wire, item['show'] == 'always' or active(entity, state)

# What the Wi-Fi item's text says beside its bars on the screen (header_bar.h device_item): nothing, a percentage or dBm;
# and the battery's beside its icon (firmware 0.41.0): nothing or its percentage.
WIFI_TEXT = {'icon': '', 'percent': '%', 'dbm': 'dBm'}
BATTERY_TEXT = {'icon': '', 'percent': '%'}

def status_item(item):
    """The screen's own item as the screen reads it: Wi-Fi or the battery with its text, and `a` for only while the signal
    is weak or the battery low; or the link."""
    if item['type'] == 'link':
        return {'k': 'link'}
    text = (WIFI_TEXT if item['type'] == 'wifi' else BATTERY_TEXT)[item['content']]
    wire = {'k': item['type'], 't': text}
    if item['show'] in ('weak', 'low'):
        wire['a'] = 1
    return wire

def message(layout, states, registry=None, units=None, tz=None, words=None, features=None, cards=None):
    """`features`: what the screen's hello said it takes; the screen's own items go only to one that named them, since an
    older screen refuses a page with an item it does not know. None: the screen of this app's own firmware (the preview).
    `cards`: which tile's card each entity's item opens (core.bar_cards), for a screen that takes cards from its top bar."""
    set_cjk_screen(features)
    items = []
    for item in header_items(layout):
        if item['type'] in HEADER_BUILTIN:
            items.append({'k': item['type']})
            continue
        if item['type'] in HEADER_STATUS:
            # The battery only to a screen that said it has one (firmware 0.41.0): a layout copied from a Tab5 to a
            # screen without a battery simply leaves it out there.
            needs = BATTERY_FEATURE if item['type'] == 'battery' else BAR_STATUS_FEATURE
            if features is None or needs in features:
                items.append(status_item(item))
            continue
        if item['type'] == 'plugin':
            # Only to a screen whose firmware has plugins: an older one refuses a bar with an item it does not know.
            if features is None or 'plugins' in features:
                items.append({'k': 'plugin', 't': item['item'], **({'o': 1} if item.get('content') == 'icon' else {})})
            continue
        wire, shown = entity_item(item, states, registry, units, tz, words, (cards or {}).get(item['entity']))
        if shown:
            items.append(wire)
    return {'v': 1, 'op': 'header', 'items': items}

def preview(header, states, registry=None, units=None, tz=None, words=None):
    """What the editor's mockup shows per item, hidden ones included and marked."""
    set_cjk_screen(None)
    result = []
    for item in header['items']:
        if item['type'] in HEADER_BUILTIN or item['type'] in HEADER_STATUS:
            result.append({'k': item['type'], 'name': t(f"addon.labels.top_bar.builtin.{item['type']}"), 'shown': True})
            continue
        if item['type'] == 'plugin':
            result.append({'k': 'plugin', 'name': item['item'], 'shown': True})
            continue
        wire, shown = entity_item(item, states, registry, units, tz, words)
        attrs = (states.get(item['entity']) or {}).get('attributes') or {}
        result.append({**wire, 'name': attrs.get('friendly_name') or item['entity'], 'shown': shown,
                       'auto_icon': auto_icon(item['entity'], states.get(item['entity']))})
    return result

def suggestions(screen, entities, states, registry=None, limit=8):
    """A handful of useful items for this screen: its own room's climate and power first, then the house.

    The room is the screen's area, or an area named like the screen. Diagnostic entities (a plug's own
    temperature) never qualify."""
    rooms = {name.casefold() for name in (screen.get('area'), screen.get('name'), (screen.get('layout') or {}).get('title')) if name}
    def attrs(entity):
        return (states.get(entity['id']) or {}).get('attributes') or {}
    def usable(entity):
        return ((states.get(entity['id']) or {}).get('state') not in (None, 'unavailable', 'unknown')
                and not ((registry or {}).get(entity['id']) or {}).get('entity_category'))
    def pick(label, test, content='state'):
        found = sorted((e for e in entities if test(e) and usable(e)), key=lambda e: (e['area'].casefold() not in rooms, e['name'].casefold()))
        if found:
            entity = found[0]
            picks.append({'label': label, 'name': entity['name'], 'area': entity['area'], 'icon': auto_icon(entity['id'], states.get(entity['id'])),
                          'item': {'type': 'entity', 'entity': entity['id'], 'content': content, 'icon': 'auto', 'show': 'always'}})
    def sensor(device_class):
        return lambda e: e['id'].startswith('sensor.') and attrs(e).get('device_class') == device_class and numeric(states[e['id']]['state']) is not None
    picks = []
    # The labels in the editor's language (app 0.2.90).
    label = lambda key: t(f'addon.labels.top_bar.suggestions.{key}')
    pick(label('temperature'), sensor('temperature'))
    pick(label('humidity'), sensor('humidity'))
    pick(label('power'), sensor('power'))
    pick(label('motion'), lambda e: e['id'].startswith('binary_sensor.') and attrs(e).get('device_class') in ('motion', 'occupancy', 'presence'), 'last_changed')
    pick(label('weather'), lambda e: e['id'].startswith('weather.'))
    pick(label('people_home'), lambda e: e['id'] == 'zone.home')
    pick(label('sun'), lambda e: e['id'] == 'sun.sun')
    pick(label('co2'), sensor('carbon_dioxide'))
    return picks[:limit]

def catalogue():
    """Choices the editor offers; labels in the order the sheet shows them, in the editor's language (app 0.2.90)."""
    return {'builtin': [{'type': key, 'label': t(f'addon.labels.top_bar.builtin.{key}')} for key in (*HEADER_BUILTIN, *HEADER_STATUS)],
            'contents': [{'key': key, 'label': t(f'addon.labels.top_bar.contents.{key}')} for key in HEADER_CONTENTS],
            'shows': [{'key': key, 'label': t(f'addon.labels.top_bar.shows.{key}')} for key in HEADER_SHOWS],
            # The Wi-Fi item's choices, and the firmware that draws the screen's own items (0.38.0).
            'wifi_contents': [{'key': key, 'label': t(f'addon.labels.top_bar.wifi_contents.{key}')} for key in WIFI_CONTENTS],
            'wifi_shows': [{'key': key, 'label': t(f'addon.labels.top_bar.wifi_shows.{key}')} for key in WIFI_SHOWS],
            'status_types': list(HEADER_STATUS), 'status_min_firmware': '.'.join(map(str, BAR_STATUS_MIN_FIRMWARE)),
            # The battery item's choices (firmware 0.41.0); the editor offers it on a screen whose `battery` is true.
            'battery_contents': [{'key': key, 'label': t(f'addon.labels.top_bar.battery_contents.{key}')} for key in BATTERY_CONTENTS],
            'battery_shows': [{'key': key, 'label': t(f'addon.labels.top_bar.battery_shows.{key}')} for key in BATTERY_SHOWS],
            'battery_min_firmware': '.'.join(map(str, BATTERY_MIN_FIRMWARE)),
            # A plugin's item: its icon and words, or its icon alone (plugin API 0.8).
            'plugin_contents': [{'key': key, 'label': t(f'addon.labels.top_bar.plugin_contents.{key}')} for key in PLUGIN_ITEM_CONTENTS],
            'max_items': HEADER_MAX_ITEMS, 'min_firmware': '.'.join(map(str, HEADER_MIN_FIRMWARE))}
