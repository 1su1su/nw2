'''我的主页'''
import streamlit as st
from PIL import Image
import time
import base64

def bar_bg(img):
    last = 'jpg'
    st.markdown(
        f"""
        <style>
        [data-testid='stSidebar'] > div:first-child {{
            background: url(data:img/{last};base64,{base64.b64encode(open(img, 'rb').read()).decode()});
        }}
        </style>
        """,
        unsafe_allow_html = True,
    )

def page_bg(img):
    last = 'jpg'
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url(data:img/{last};base64,{base64.b64encode(open(img, 'rb').read()).decode()});
            background-size: cover
        }}
        </style>
        """,
        unsafe_allow_html = True,
    )

bar_bg('宇宙.jpg')
page_bg('天.jpg')

page = st.sidebar.radio('我的首页', ['我的兴趣推荐','音乐分享','我的图片处理工具', '我的智能词典', '我的留言区','网页跳转','脑筋急转弯'])

def page_1():
    '''我的兴趣推荐'''
    st.write("<span style='font-size:30px;'>sacred play secret place —— Matryoshka",unsafe_allow_html=True)
    with open('神圣的游戏.mp3','rb')as f:
        mymp3=f.read()
    st.audio(mymp3,format='audio/mp3',start_time=0)
    st.image('桂林山甲水.jpg')
    tab1,tab2,tab3,tab4=st.tabs(["我的电影推荐：","我的游戏推荐：","我的书籍推荐","我的小说推荐："])
    with tab1:
        st.write("<span style='font-size:25px'>第一部：",unsafe_allow_html=True)
        st.write("<span style='font-size:30px;color:red'>《楚门的世界》",unsafe_allow_html=True)
        st.image('楚门的世界.jpg')
        st.write("<span style='font-size:20px'>1、剧情简介：影片讲述了楚门是一档热门肥皂剧的主人公，他身边的所有事情都是虚假的，他的亲人和朋友全都是演员，但他本人对此一无所知。最终楚门不惜一切代价走出了这个虚拟的世界。",unsafe_allow_html=True)
        st.write("<span style='font-size:20px'>2、《楚门的世界》是派拉蒙影业公司于1998年出品的一部电影。由彼得·威尔执导，金·凯瑞、劳拉·琳妮、诺亚·艾默里奇、艾德·哈里斯等联袂主演。该片于1998年6月1日在美国上映。",unsafe_allow_html=True)
        st.write("<span style='font-size:20px'>3、1999年，该片获得了第71届奥斯卡最佳原创剧本奖提名；金·凯瑞凭借此片获得了第56届美国金球奖最佳男主角奖。",unsafe_allow_html=True)
        st.write("---------------------------")
        
        st.write("<span style='font-size:25px'>第二部：",unsafe_allow_html=True)
        st.write("<span style='font-size:30px;color:red'>《星际穿越》",unsafe_allow_html=True)
        st.image('星际穿越.jpg')
        st.write("<span style='font-size:20px'>1、《星际穿越》（Interstellar）是克里斯托弗·诺兰执导的一部原创科幻冒险电影，由马修·麦康纳、安妮·海瑟薇、杰西卡·查斯坦及迈克尔·凯恩主演。",unsafe_allow_html=True)
        st.write("<span style='font-size:20px'>2、影片基于理论物理学家基普·S·索恩的“黑洞理论”，经过合理演化之后改编而成。主要讲述了一队探险家利用他们针对虫洞的新发现，超越人类对于太空旅行的极限，从而开始在广袤的宇宙中进行星际航行的故事。",unsafe_allow_html=True)
        st.write("<span style='font-size:20px'>3、该影片于2014年11月7日北美上映，2014年11月12日中国大陆上映。",unsafe_allow_html=True)
        st.write("<span style='font-size:20px'>4、2015年3月，《星际穿越》在第41届美国科幻恐怖电影奖土星奖获得了最佳科幻电影、最佳导演、最佳男女主角在内的10项提名。",unsafe_allow_html=True)
        st.write("<span style='font-size:25px;color:red'>影片评价:",unsafe_allow_html=True)
        st.write("<span style='font-size:20px;color:blue'>正面观点:",unsafe_allow_html=True)
        st.write("<span style='font-size:20px'>1、《星际穿越》提供了绚烂的奇景、量不够足的戏剧性、以及鲜有闪现的幽默感。它想让我们因为惊讶而臣服，想让我们在一部如此伟大的“艺术品”面前自觉渺小。它的目的达到了。但在制作一部史诗的路上，诺兰忘了要让我们感受到乐趣。",unsafe_allow_html=True)
        st.write("<span style='font-size:20px'>2、《星际穿越》是一部充满超现实主义和梦幻色彩的太空冒险。这部构思宏大的电影在探索人类之间亲密感情的同时，也讲述了对宇宙的思索，非常引人入胜。",unsafe_allow_html=True)
        st.write("<span style='font-size:20px'>3、电影的叙事和大胆的构思将你推入其宏大且可信的架构中，诺兰距离创作出他的绝世佳作不远了。诺兰这封关于宇宙旅行和探索星辰的情书需要观众的耐心，但随着影片超凡的视觉场景，它为观众提供了难以置信的情感回报。",unsafe_allow_html=True)
        st.write("<span style='font-size:20px;color:blue'>负面观点:",unsafe_allow_html=True)
        st.write("<span style='font-size:20px'>1、影片颇具野心，非常吸引人和发人深思，但是同样单调乏味，影片先进的特效技术看起来也有些名不副实。不是所有影片都像《绝世天劫》中讲述的，在人类面临灭绝时需要志愿者愚蠢的热心，不过至少前者是一部太空冒险电影，《星际穿越》只是一篇科学报告。",unsafe_allow_html=True)
        st.write("<span style='font-size:20px'>2、影片为某一类人立传，并证明了编剧兼导演最出色且最糟糕的一面。诺兰的《星际穿越》花了数百万美元带领观众来到了宇宙最遥远的地方，影片给予观众的感情身临其境却十分廉价，这些情感贺曼公司的贺卡都能提供给你。",unsafe_allow_html=True)
        
    with tab2:
        st.write("<span style='font-size:25px'>第一部：",unsafe_allow_html=True)
        st.write("<span style='font-size:30px;color:red'>我的世界",unsafe_allow_html=True)
        st.image('我的世界.jpg')
        st.write("<span style='font-size:20px'>1、《我的世界》（Minecraft），是一款沙盒建造游戏，玩家可以在一个三维世界里用各种方块建造或者破坏方块。于2009年05月17日试运营，2011年正式发行。最初由瑞典游戏设计师马库斯·阿列克谢·泊松开创，现由Mojang Studios维护，是Xbox工作室 的一部分。该游戏基于Java平台",unsafe_allow_html=True)
        st.write("<span style='font-size:20px'>2.玩家（Steve默认角色）是用户们在世界中控制的人物。当用户开始一个新游戏，玩家就会被放进由随机或指定的种子世界中，物品栏为空。玩家有10颗心的生命条（即20点生命值），会受到来自敌对生物、中立生物和其他玩家击中所产生的伤害，不同难度伤害不同。生命值可以通过自然恢复（仅在饥饿值满条件下）或饮用特定药水来恢复（和平模式下无条件恢复）。饥饿值也是一个非和平模式的指标，随时间的推移将逐渐消耗，并且在疾跑时将会加剧消耗。食物可以恢复饥饿值。",unsafe_allow_html=True)
        st.write("<span style='font-size:20px'>3、我的世界着重于让玩家去探索、交互，并且改变一个由一立方米大小的方块动态生成的地图。除了方块以外，环境功能还包括植物、生物与物品。游戏里的一些活动包括采集矿石、与敌对生物战斗、合成新的方块与收集各种在游戏中找到的资源的工具。",unsafe_allow_html=True)
        st.write("<span style='font-size:20px'>游戏中的无限制模式让玩家在各种多人游戏服务器或他们的单人模式中进行创造建筑物、作品与艺术创作。其他功能包括逻辑运算与远程动作的红石电路、矿车及轨道，以及称之为“下界”的神秘世界。最终，可以选择前往一个叫做“末路之地”的维度旅行，并击败末影龙。",unsafe_allow_html=True)
        st.write("---------------------------")
        
        st.write("<span style='font-size:25px'>第二部：",unsafe_allow_html=True)
        st.write("<span style='font-size:30px;color:red'>《传说之下》",unsafe_allow_html=True)
        st.image('传说之下.jpg')
        st.write("<span style='font-size:20x'>《传说之下》又名是Toby Fox独立开发和发行的角色扮演游戏，于2015年9月15日在Microsoft Windows、OS X、Steam平台上发售。",unsafe_allow_html=True)
        st.write("<span style='font-size:20x'>该作游戏背景设定在很久很久以前，地球由两个种族均等统治着，分别是人类和怪物。一天，人类担心怪物们会利用人类灵魂的力量来摧毁人类，便先手发动战争，击碎了双方之间的和平。",unsafe_allow_html=True)
        st.write("<span style='font-size:20x'>在近似屠杀式的侵略下，人类大获全胜。人类将怪物驱逐到地下，并设下了相当强力的魔法结界，将怪物困在伊波特山下的地底。而传说中登上伊波特山的人类没有一个活着回来过。",unsafe_allow_html=True)
        st.write("<span style='font-size:20x'>201X年，一个人类小孩登上伊波特山，发现了一个大洞，并一不小心被藤蔓绊倒跌进了洞中。",unsafe_allow_html=True)
        st.write("<span style='font-size:20x'>而玩家在游戏中将控制一名掉入地下怪物世界的人类，也就是上述的小孩，玩家可以寻找离开的路，亦或是选择留下。",unsafe_allow_html=True)
        st.write("<span style='font-size:30px;'>His Theme——Toby Fox",unsafe_allow_html=True)
        with open('传说之下.mp3','rb')as f:
            mymp3=f.read()
        st.audio(mymp3,format='audio/mp3',start_time=0)
        
    with tab3:
        st.write("<span style='font-size:25px'>第一部：",unsafe_allow_html=True)
        st.write("<span style='font-size:30px;color:red'>《战争与和平》",unsafe_allow_html=True)
        st.image('战争与和平.jpg')
        st.write("<span style='font-size:20px'>1、《战争与和平》是俄国作家列夫·尼古拉耶维奇·托尔斯泰创作的长篇小说，也是其代表作。该作以1812年的卫国战争为中心，反映从1805到1820年间的重大历史事件。以鲍尔康斯、别祖霍夫、罗斯托夫和库拉金四大贵族的经历为主线，在战争与和平的交替描写中把众多的事件和人物串联起来。",unsafe_allow_html=True)
        st.write("<span style='font-size:20px'>2、作者将'战争'与'和平'的两种生活、两条线索交叉描写，构成一部百科全书式的壮阔史诗。 《战争与和平》的基本主题是肯定这次战争中俄国人民正义的抵抗行动，赞扬俄国人民在战争中表现出来的爱国热情和英雄主义。但作品的基调是宗教仁爱思想和人道主义，作家反对战争，对战争各方的受难并都给予了深切的同情。",unsafe_allow_html=True)
        st.write("---------------------------")
        
        st.write("<span style='font-size:25px'>第二部：",unsafe_allow_html=True)
        st.write("<span style='font-size:30px;color:red'>《钢铁是怎样炼成的》",unsafe_allow_html=True)
        st.image('钢铁.jpeg')
        st.write("<span style='font-size:20px'>本书讲述了主人公保尔·柯察金从一个在社会底层挣扎的贫苦少年，逐渐成长为一个为祖国和人民的事业奋斗毕生的无产阶级革命战士的历程。年少的保尔曾做过店员，任人欺侮；偷过德国人的手枪，因救朱赫来而坐牢；辗转于硝烟弥漫的战场，多次挣扎在死亡线上；革命胜利之后又将全部身心投入了国民建设当中……在这个过程中，保尔表现出了一个真正的无产阶级革命战士所具有的坚毅、勇敢、无私奉献的高尚品格，他把自己宝贵的青春交给了党和人民，在全身瘫痪的情况下仍勇敢地拿起笔服务于人民。 ",unsafe_allow_html=True)
        st.write("<span style='font-size:20px'>保尔的精神是一面永恒的旗帜，保尔的事迹和品格是每一个21世纪青少年学习的榜样。")
        st.write("<span style='font-size:20px'>《钢铁是怎样炼成的》描写保尔·柯察金作为一个普通工人的儿子，经历第一次世界大战、十月革命、国内战争和国民经济恢复时期的严峻生活，把对旧生活自发的反抗改变为自觉的阶级意志。保尔的成长不是“性格的自我发展”，而是如同作者在回忆自己一生时所说：“钢是在熊熊大火和骤然冷却中炼成的……我们这一代也是在斗争和艰苦考验中锻炼出来的。” ",unsafe_allow_html=True)
        st.write("<span style='font-size:20px'>保尔的英雄主义是早期布尔什维克的理性真诚，个人价值和集体事业在观念上处于和谐状态。小说不仅通过一个接一个的困境来塑造这位主人公，还通过激动人心的独白、发人深省的警句格言直抒这种赤诚情怀。一次，保尔来到烈士墓前悼念为革命而牺牲的战友时，曾默默地想到：“人最宝贵的是生命。它给予我们只有一次。人的一生应当这样度过：当他回首往事时不因虚度年华而悔恨，也不因碌碌无为而羞耻。这样在他临死的时侯就能够说：“我已把我整个的生命和全部精力都献给最壮丽的事业—为人类的解放而斗争。” ",unsafe_allow_html=True)
        st.write("<span style='font-size:20px'>同冬尼娅的爱情纠葛，同丽达磊落的友谊，以及对达雅诚挚的感情也表现了保尔精神世界的纯洁，表现了小说人物的特殊素质。 ",unsafe_allow_html=True)
        st.write("<span style='font-size:20px'>作者把自己作为主人公的原型，但并不是自传。他说；“我这个长篇首先是一部艺术作品，在这个长篇里我使用了虚构的权利。”作者的意图是“要在作品中创造一种典型，一种在我们的时代——无产阶级革命时代的青年革命者的典型。” ",unsafe_allow_html=True)
        st.write("<span style='font-size:20px'>",unsafe_allow_html=True)

    with tab4:
        st.write("<span style='font-size:25px'>第一部：",unsafe_allow_html=True)
        st.write("<span style='font-size:30px;color:red'>《龙族》",unsafe_allow_html=True)
        st.image('龙族.png')
        st.write("<span style='font-size:20px'>1、《龙族》是作家江南创作的系列长篇魔幻小说，由《龙族Ⅰ火之晨曦》、《龙族Ⅱ悼亡者之瞳》、《龙族Ⅲ黑月之潮》、《龙族Ⅳ奥丁之渊》组成，2009年10月1日开始在小说绘上连载，第一部于2010年04月首次出版。",unsafe_allow_html=True)
        st.write("<span style='font-size:20px'>2、龙族小说是作家江南创作的系列长篇魔幻小说，由《龙族1火之晨曦》、《龙族2悼亡者之瞳》、《龙族3黑月之潮》、《龙族4奥丁之渊》《龙族5》组成，2009年10月1日开始在小说绘上连载，第一部于2010年04月首次出版，第二部于2011年05月出版，第三部上篇于2012年12月出版，第三部中篇于2013年07月出版，第三部下篇于2013年12月出版，第四部则于2015年10月出版。",unsafe_allow_html=True)
        st.write("<span style='font-size:20px'>3、江南，真名杨治。中国作家、小说家、内地幻想文学家，《九州志》主编，现任北京九州天辰信息咨询有限公司总经理。1977年7月13日生于安徽舒城，就读北京大学，留学于美国名校Washington University in St Louis，师从质谱科学代表人物Michael L. Gross，凭借回忆北大生活的小说《此间的少年》踏入文坛。江南的幻想作品《九州・缥缈录》系列构建了以中国历史和神话为原型的架空世界、青春作品《龙族》系列在中国创下了单本即销售200万册的记录。",unsafe_allow_html=True)
        st.write("<span style='font-size:20px'>4、《龙族》是一系列小说，目前仍在连载，作者江南，中国著名青春小说作家，《九州志》杂志主编。其作品以情节多变、人物热血、内容励志、文字细腻著称。小说讲述的是一群热血的疯子尽己之力对抗龙族的故事。“龙族”贯穿故事的始终，既有不屈从命运的勇气，又包含自始至终的孤独。作者用他的文字架构了一个远古与现代交融的世界——在这个世界里，既有远古的神秘、美丽的传说；又有现代的文明，完美融合，毫不突兀。一个又一个鲜活的人物在他笔下活了过来，读完，你会发现故事情节清晰，人物形象丰满。相比于恺撒的骄傲贵公子，楚子航的冷静冰美人，诺诺的红发小巫女等，我更喜欢废柴的路明非——李嘉图·M·路。",unsafe_allow_html=True)
        st.write("---------------------------")

        st.write("<span style='font-size:25px'>第二部：",unsafe_allow_html=True)
        st.write("<span style='font-size:30px;color:red'>《十日终焉》",unsafe_allow_html=True)
        st.image('终焉.jpg')
        st.write("<span style='font-size:20px'>一群普通人被抓到“终焉之地”，进行每十日一次的生死轮回，他们在这里生了死，死了生。想要逃出此地，必须要进行由「十二生肖」设计的死亡游戏。可是在一个又一个十日之后，部分人开始觉醒了超自然能力的故事。当我以为这只是寻常的一天时，却发现自己被捉到了终焉之地。 当我以为只需要不断地参加死亡游戏就可以逃脱时，却发现众人开始觉醒超自然之力。 当我以为这里是「造神之地」时，一切却又奔着湮灭走去。",unsafe_allow_html=True)
        st.write("---------------------------")
        
        st.write("<span style='font-size:25px'>第三部：",unsafe_allow_html=True)
        st.write("<span style='font-size:30px;color:red'>《蛊真人》",unsafe_allow_html=True)
        st.image('蛊真人.jpg')
        st.write("<span style='font-size:20px'>1.人是万物之灵，蛊是天地真精。三观不正，魔头重生。昔日旧梦，同名新作。一个穿越者不断重生的故事。一个养蛊、炼蛊、用蛊的奇特世界。《蛊真人》人往往会变得面目全非，而人最大的失败，就是失去自我",unsafe_allow_html=True)
        st.write("<span style='font-size:20px'>2.辗转颠簸三百年，纵横世间两百余年，五百多年光阴悠悠，却是晃眼即逝。看着这青山落日，方源轻声一笑：“青山落日，秋月春风。当真是朝如青丝暮成雪，是非成败转头空。”伟大和可笑，只是一点点的差距。 在寻找成功的过程中，人往往会变得面目全非，而人最大的失败，就是失去自我。我曾经呐喊过，渐渐的我不发出声音。我曾经哭泣过，渐渐的我不再流泪。 我曾经悲伤过，渐渐的我能承受一切。 我曾经喜悦过，渐渐的我看淡世间。而如今！ 我只剩下面无表情，我的目光如磐石般坚硬，我的心中剩下坚持。",unsafe_allow_html=True)
        st.write("<span style='font-size:25px;color:blue'>摘自《蛊真人》",unsafe_allow_html=True)
        st.write("<span style='font-size:25px;color:gold'>第一首：",unsafe_allow_html=True)
        st.write("<span style='font-size:20px'>落魄谷中寒风吹，春秋蝉鸣少年归。",unsafe_allow_html=True)
        st.write("<span style='font-size:20px'>荡魂山处石人泪，定仙游走魔向北。",unsafe_allow_html=True)
        st.write("<span style='font-size:20px'>逆流河上万仙退，爱情不敌坚持泪。",unsafe_allow_html=True)
        st.write("<span style='font-size:20px'>宿命天成命中败。仙尊悔而我不悔。",unsafe_allow_html=True)
        st.write("<span style='font-size:25px;color:gold'>第二首：",unsafe_allow_html=True)
        st.write("<span style='font-size:20px'>早岁已知世事艰，仍许飞鸿荡云间。",unsafe_allow_html=True)
        st.write("<span style='font-size:20px'>一路寒风身如絮，命海沉浮客独行。",unsafe_allow_html=True)
        st.write("<span style='font-size:20px'>千磨万击心铸铁，殚精竭虑铸一剑。",unsafe_allow_html=True)
        st.write("<span style='font-size:20px'>今朝剑指叠云处，炼蛊炼人还炼天。",unsafe_allow_html=True)
        st.write("<span style='font-size:25px;color:gold'>第三首：",unsafe_allow_html=True)
        st.write("<span style='font-size:20px'>独帜入深身未知，身似浮萍命难持 。 ",unsafe_allow_html=True)
        st.write("<span style='font-size:20px'>千舟皆朝归海处，一苇轻拨戏浪巅。",unsafe_allow_html=True)
        st.write("<span style='font-size:20px'>惊鸿四散鱼逃尽， 唯有残帆傲此间。 ",unsafe_allow_html=True)
        st.write("<span style='font-size:20px'>待到天开云雾散， 负手直望笑苍天。 ",unsafe_allow_html=True)
        st.write("<span style='font-size:25px;color:gold'>第四句：",unsafe_allow_html=True)
        st.write("<span style='font-size:20px'>我清楚的知道人与人的路是不可复制的，我走在自己的人生路上，哪怕路途的风雨再大，大到我步履维艰，哪怕荆棘丛生，刺得我伤痕遍布，我也依旧痴痴笑笑，我体会此中滋味。 我相信独游的小船终有一天会看到两岸群山青翠，虫鸟同鸣。",unsafe_allow_html=True)

def page_2():
    '''音乐分享'''
    st.write("<span style='font-size:40px;'>🎵音乐分享🎵：",unsafe_allow_html=True)
    #第一首
    st.write("<span style='font-size:30px;'>1.NEW START——OAO",unsafe_allow_html=True)
    with open('newstart.mp3','rb')as f:
        mymp3=f.read()
    st.audio(mymp3,format='audio/mp3',start_time=0)
    #第二首
    st.write("<span style='font-size:30px;'>2.RAVE LOVE——OAO",unsafe_allow_html=True)
    with open('ravelove.mp3','rb')as f:
        mymp3=f.read()
    st.audio(mymp3,format='audio/mp3',start_time=0)
    #第三首
    st.write("<span style='font-size:30px;'>3.TIME HEALS EVERYTHING——OAO",unsafe_allow_html=True)
    with open('timehealseverything.mp3','rb')as f:
        mymp3=f.read()
    st.audio(mymp3,format='audio/mp3',start_time=0)
    #第四首
    st.write("<span style='font-size:30px;'>4.Rain——Shmily",unsafe_allow_html=True)
    with open('Rain.mp3','rb')as f:
        mymp3=f.read()
    st.audio(mymp3,format='audio/mp3',start_time=0)
    #第五首
    st.write("<span style='font-size:30px;'>5.Sample this——RJ Pasin",unsafe_allow_html=True)
    with open('新录音1.m4a','rb')as f:
        mymp3=f.read()
    st.audio(mymp3,format='audio/mp3',start_time=0)
    #第六首
    st.write("<span style='font-size:30px;'>6.Ephemeral Memories（Without Drum)——MoreanP",unsafe_allow_html=True)
    with open('新录音 2.m4a','rb')as f:
        mymp3=f.read()
    st.audio(mymp3,format='audio/mp3',start_time=0)
    #第七首
    st.write("<span style='font-size:30px;'>7.Time Stop——BLACKDD",unsafe_allow_html=True)
    with open('新录音 3.m4a','rb')as f:
        mymp3=f.read()
    st.audio(mymp3,format='audio/mp3',start_time=0)
    #第八首
    st.write("<span style='font-size:30px;'>8.Towards the Light——Jacoo",unsafe_allow_html=True)
    with open('新录音 4.m4a','rb')as f:
        mymp3=f.read()
    st.audio(mymp3,format='audio/mp3',start_time=0)
    #第九首
    st.write("<span style='font-size:30px;'>9.Daylight——Seredris",unsafe_allow_html=True)
    with open('新录音 5.m4a','rb')as f:
        mymp3=f.read()
    st.audio(mymp3,format='audio/mp3',start_time=0)
    
def page_3():
    '''我的图片处理工具'''
    st.write('图片换色小程序')
    uploaded_file=st.file_uploader("上传图片",type=['png','jpeg','jpg','gif'])
    if uploaded_file:
        file_name=uploaded_file.name
        file_type=uploaded_file.type
        file_size=uploaded_file.size
        img=Image.open(uploaded_file)
        tab1,tab2,tab3,tab4,tab5,tab6=st.tabs(["原图","旋转","改色1","改色2","改色3","缩放大小"])
        
        roading = st.progress(0, '开始加载')
        for i in range(1, 101, 1):
            time.sleep(0.01)
            roading.progress(i, '正在加载'+str(i)+'%')
        roading.progress(100, '加载完毕！')
        time.sleep(0.01)
        with tab1:
            st.image(img)
            bw = st.toggle('黑白滤镜')
            message = ''
            if bw:
                message += '黑白' + ','
                st.image(img_black(img))
            st.write('你将会得到一张', message, '的图片')
        with tab2:
            st.image(img_rotate(img))
        with tab3:
            st.image(img_change(img,1,0,2))
        with tab4:
            st.image(img_change(img,1,2,0))
        with tab5:
            st.image(img_change(img,2,1,0))
        with tab6:
            st.image(img_resize(img))
            
def img_change(img,rc,gc,bc):
    '''图片处理'''
    width,height=img.size
    img_array=img.load()
    for x in range(width):
        for y in range(height):
            r=img_array[x,y][rc]
            g=img_array[x,y][gc]
            b=img_array[x,y][bc]
            img_array[x,y]=(r,g,b)
    return img

def img_rotate(img):
    angle=st.number_input("请输入旋转角度",value=0)
    if angle !=" ":
        angle=int(angle)
        img_change1=img.rotate(angle)
        return img_change1

def img_resize(img):
    big=st.number_input("请输入图片尺寸",value=200)
    if big !=" ":
        big=int(big)
        img_change2=img.resize((big,big))
        return img_change2

def img_black(img):
    img_change3=img.convert("L")
    return img_change3

def page_4():
    '''我的智能词典'''
    st.write("<span style='font-size:20px;'>输入hi与hello有彩蛋",unsafe_allow_html=True)
    st.write("<span style='font-size:30px;color:red'>智慧词典",unsafe_allow_html=True)
    with open('words_space.txt','r',encoding='utf-8') as f:
        words_list=f.read().split('\n')
        print(words_list)
    for i in range(len(words_list)):
        words_list[i]=words_list[i].split('#')
    words_dict={}
    for i in words_list:
        words_dict[i[1]]=[int(i[0]),i[2]]
    with open('check_out_times.txt','r',encoding='utf-8') as f:
        times_list=f.read().split('\n')
    for i in range(len(times_list)):
        times_list[i]=times_list[i].split('#')
    times_dict={}
    for i in times_list:
        times_dict[int(i[0])]=int(i[1])
    #查询的单词
    word=st.text_input('请输入要查询的单词')
    #判定
    if word in words_dict:
        st.write(words_dict[word])
        n=words_dict[word][0]
        if n in times_dict:
            times_dict[n]+=1
        else:
            times_dict[n]=1
        with open('check_out_times.txt','w',encoding='utf-8') as f:
            message=' '
            for k,v in times_dict.items():
                message += str(k) + '#' +str(v) +'\n'
            message=message[:-1]
            f.write(message)
        st.write('查询次数:',times_dict[n])
        #彩蛋
        if word=="hi":
            st.snow()
            st.image('古树.jpg')
            st.image('树.jpg')
            st.write("<span style='font-size:20px;color:red'>输入‘李’有隐藏彩蛋",unsafe_allow_html=True)
        if word=="hello":
            st.balloons()
            st.image('繁星.jpg')
            st.image('星空.jpg')
            st.write("<span style='font-size:20px;color:red'>输入‘李’有隐藏彩蛋",unsafe_allow_html=True)
    #隐藏彩蛋
    if word=="李":
        st.balloons()
        st.snow()
        st.write("<span style='font-size:20px;color:red'>恭喜你发现隐藏彩蛋",unsafe_allow_html=True)
        st.image("满穗.jpg")
    
def page_5():
    '''我的留言区'''
    st.write("<span style='font-size:30px;color:red'>我的留言区",unsafe_allow_html=True)
    with open('leave_messages.txt','r',encoding='utf-8')as f:
        messages_list=f.read().split('\n')
    for i in range(len(messages_list)):
        messages_list[i]=messages_list[i].split('#')
    for i in messages_list:
        with st.chat_message('🌞'):
            st.write(i[1],':',i[2])
    name=st.text_input("留言者的姓名")
    new_message=st.text_input("想要说的话……")
    if st.button('留言'):
        messages_list.append([str(int(messages_list[-1][0])+1),name,new_message])
        with open('leave_messages.txt','w',encoding='utf-8')as f:
            message=''
            for i in messages_list:
                message+=i[0]+'#'+i[1]+'#'+i[2]+'\n'
            message=message[:-1]
            f.write(message)
            
def page_6():
    st.write('除了本主站之外，我还将我的有趣内容分享在了其他网站中')
    go = st.selectbox('你的支持是我最大的动力，去支持一下up吧！', ['百度', 'bilibili','编程猫社区','中国新闻网','中国教育在线','知乎','豆瓣','QQ音乐',' 微博','优酷','爱奇艺','腾讯视频','网易免费邮箱','github'])
    if go == '百度':
        st.link_button('帮我盖楼', 'https://www.baidu.com/')
    elif go == 'bilibili':
        st.link_button('帮我一键三连', 'https://www.bilibili.com/')
    elif go == '编程猫社区':
        st.link_button('一起去编程吧', 'https://shequ.codemao.cn/ ')
    elif go == '中国新闻网':
        st.link_button('一起去看新闻', 'http://www.chinanews.com/')
    elif go == '中国教育在线':
        st.link_button('去看新教育政策', 'https://www.eol.cn/')
    elif go == '知乎':
        st.link_button('帮你找到你要的答案', 'https://www.zhihu.com/')
    elif go == '豆瓣':
        st.link_button('一起去看番', 'https://www.douban.com/')
    elif go == 'QQ音乐':
        st.link_button('一起听音乐', 'https://y.qq.com/')
    elif go == ' 微博':
        st.link_button('去看新消息', 'https://weibo.com/')
    elif go == '优酷':
        st.link_button('去看视频', 'https://www.youku.com/')
    elif go == '爱奇艺':
        st.link_button('去看视频', 'https://www.iqiyi.com/')
    elif go == '腾讯视频':
        st.link_button('去看视频', 'https://v.qq.com/')
    elif go == '网易免费邮箱':
        st.link_button('去看邮件', 'https://mail.163.com/')
    elif go == 'github':
        st.link_button('去编程', 'https://github.com/')
    
def page_7():
    #第一题
    st.write("<span style='font-size:25px;color:red'>第一题：",unsafe_allow_html=True)
    st.write("<span style='font-size:20px;color:blue'>什么样的路不能走?",unsafe_allow_html=True)
    col1,col2=st.columns([1,1])
    with col1:
        cb1 = st.checkbox('A.马路')
    with col2:
        cb2 = st.checkbox('B.天路')
    col3,col4=st.columns([1,1])
    with col3:
        cb3 = st.checkbox('C.铁路')
    with col4:
        cb4 = st.checkbox('D.电路')
    if st.button('确认答案'):
        if cb1==False and cb2==False and cb3==False and cb4==True:
            st.write('答案正确')
        else:
            st.write('再想想')
    #第二题
    st.write("<span style='font-size:25px;color:red'>第二题：",unsafe_allow_html=True)
    st.write("<span style='font-size:20px;color:blue'>小波比的一举一动都离不开绳子,为什么?",unsafe_allow_html=True)
    col5,col6=st.columns([1,1])
    with col5:
        cb5 = st.checkbox('A.他是傻子')
    with col6:
        cb6 = st.checkbox('B.他是木偶')
    col7,col8=st.columns([1,1])
    with col7:
        cb7 = st.checkbox('C.他被绑架了')
    with col8:
        cb8 = st.checkbox('D.不知道')
    if st.button('确认答案1'):
        if cb5==False and cb6==True and cb7==False and cb8==False:
            st.write('答案正确')
        else:
            st.write('再想想')
    #第三题  
    st.write("<span style='font-size:25px;color:red'>第三题：",unsafe_allow_html=True)
    st.write("<span style='font-size:20px;color:blue'>有个傻子在飞机上把行李往下扔，请问为什么？",unsafe_allow_html=True)
    da=st.text_input('请输入答案：')
    if st.button('确认答案2'):
        if da=="因为他是傻子":
            st.write("回答正确")
        else:
            st.write("回答错误")
    if st.button('揭露答案'):
        st.write("因为他是傻子")
    #第四题
    st.write("<span style='font-size:25px;color:red'>第四题：",unsafe_allow_html=True)
    st.write("<span style='font-size:20px;color:blue'>把大象放入冰箱需要几步？",unsafe_allow_html=True)
    b=st.text_input('请输入答案1：')
    if st.button('确认答案3'):
        if b=="三步":
            st.write("回答正确")
        else:
            st.write("回答错误")
    if st.button('揭露答案1'):
        st.write("三步")
    #第五题
    st.write("<span style='font-size:25px;color:red'>第五题：",unsafe_allow_html=True)
    st.write("<span style='font-size:20px;color:blue'>小羊在散步突然就受伤了，为什么？",unsafe_allow_html=True)
    c=st.text_input('请输入答案2：')
    if st.button('确认答案4'):
        if c=="因为被行李砸了":
            st.write("回答正确")
            st.write("被前面傻子扔的行李砸伤了")
        else:
            st.write("回答错误")
    if st.button('揭露答案2'):
        st.write("因为被行李砸了")
        st.write("被前面傻子扔的行李砸伤了")
    #第六题
    st.write("<span style='font-size:25px;color:red'>第六题：",unsafe_allow_html=True)
    st.write("<span style='font-size:20px;color:blue'>森林之王开办了森林大会，但有几个小动物没来，是哪几个？",unsafe_allow_html=True)
    d=st.text_input('请输入答案3：')
    if st.button('确认答案5'):
        if d=="小羊和大象":
            st.write("回答正确")
            st.write("小羊被前面傻子扔的行李砸伤了，大象还在冰箱里")
        else:
            st.write("回答错误")
    if st.button('揭露答案3'):
        st.write("小羊和大象")
        st.write("小羊被前面傻子扔的行李砸伤了，大象还在冰箱里")
    #第七题
    st.write("<span style='font-size:25px;color:red'>第七题：",unsafe_allow_html=True)
    st.write("<span style='font-size:20px;color:blue'>小明家的冰箱坏了，为什么？",unsafe_allow_html=True)
    e=st.text_input('请输入答案4：')
    if st.button('确认答案6'):
        if e=="因为大象在里面":
            st.write("回答正确")
            st.write("大象在里面弄坏了")
        else:
            st.write("回答错误")
    if st.button('揭露答案4'):
        st.write("因为大象在里面")
        st.write("大象在里面弄坏了")


if page == '我的兴趣推荐':
    page_1()
elif page == '音乐分享':
    page_2()
elif page == '我的图片处理工具':
    page_3()
elif page == '我的智能词典':
    page_4()
elif page == '我的留言区':
    page_5()
elif page == '网页跳转':
    page_6()
elif page == '脑筋急转弯':
    page_7()
    
#https://mail.163.com/
#https://github.com/


