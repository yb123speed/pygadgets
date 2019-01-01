#coding=utf-8
from random import choice
from time import sleep

two_chars_words = "朱砂 天下 杀伐 人家 韶华 风华 繁华 血染 墨染 白衣 素衣 嫁衣 倾城 孤城 空城 旧城 旧人 伊人 心疼 春风 古琴 无情 迷离 奈何 断弦 焚尽 散乱 陌路 乱世 笑靥 浅笑 明眸 轻叹 烟火 一生 三生 浮生 桃花 梨花 落花 烟花 离殇 情殇 爱殇 剑殇 灼伤 仓皇 匆忙 陌上 清商 焚香 墨香 微凉 断肠 痴狂 凄凉 黄梁 未央 成双 无恙 虚妄 凝霜 洛阳 长安 江南 忘川 千年 纸伞 烟雨 回眸 公子 红尘 红颜 红衣 红豆 红线 青丝 青史 青冢 白发 白首 白骨 黄土 黄泉 碧落 紫陌 浅唱 寂灭 无声 邂逅 流年 落寂 叙述 唯爱 晨曦 回忆 错落 迷茫 恬静 默诺 余音 情殇 背殇 落幕 黯然 拾忆 独寂 透彻 水影 浅陌 无垠 似水 流年 深音 铭记 迷遇 暖光 蘩藜 尘宵 磬音 黯伤 醉生 沉静 寂冷".split(" ")

four_chars_words = "情深缘浅 情深不寿 莫失莫忘 阴阳相隔 如花美眷 似水流年 眉目如画 曲终人散 繁华落尽 不诉离殇 一世长安 半世烟尘 落梅似雪 冷月花魂 平湖秋月 蝶恋忆回 秋水伊人 断桥残雪 风动铃心 伊人已逝 望断秋水 似水流年 如花美眷 落晚芳菲 沧山映水 上善若水 匠心独运 倾国倾城 天香国色 浑然一体 如梦如幻 风华绝代 繁华落尽 寂寞如烟 独坐如莲 清风有情 明月可鉴 落花有情 流水可懂 流星有情 星空可睹 红颜有梦 陌上花开 弦断花落 似水流年 物是人非 昔云楚楚 紫燕悠悠 在水一方 雪殇若兮 燕笑语兮 清风扶柳 夕颜若雪 笑若扶风 凭兰秋思 素兮饶眉 雨夜聆风 月舞神殇 似水流年 此去经年 烟雨平生 宛如红袖 飞泉鸣玉 曾经沧海 谁堪共语 古道西风 流荆默望 往事如烟 静水流深 相濡以沫 笑靥如花 花开堪折 浮生若梦 情非得已 思绪万千 豆寇年华 地老天荒 曲终人散 沧海桑田 柒指流年 灯火阑珊 与子偕老 过眼云烟 生如夏花 尘埃落定 彼岸流年 莫矢莫忘".split(" ")

sentence_model = "xx，xx，xx了xx。 xxxx，xxxx，不过是一场xxxx。 你说xxxx，我说xxxx，最后不过xxxx。 xx，xx，许我一场xxxx。 一x一x一xx，半x半x半xx。 你说xxxxxxxx，后来xxxxxxxx。 xxxx，xxxx，终不敌xxxx。 xx，xxxx，xx，xxxx。 用我xxxx，换你xxxx。".split(" ")

def get_sentence():
    model = choice(sentence_model)
    while "xxxx" in model:
        model = model.replace("xxxx", choice(four_chars_words), 1)
    while "xx" in model:
        model = model.replace("xx", choice(two_chars_words), 1)
    while "x" in model:
        x = choice([0, 3])
        model = model.replace("x", choice(two_chars_words)[x:x+3], 1)
    print(model)

while True:
    get_sentence()
    sleep(1)