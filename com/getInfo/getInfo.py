# -*- coding: utf-8 -*-
__author__ = 'yuegang'

import re

titleList = [
    "Grabtaxi公司融资3.5亿美元",
    "他趣完成B轮8500万融资 年底挂牌新三板",
    "在这个羞羞的行业里 他趣完成了B轮8500万融资",
    "上药云健康获11亿元 A轮融资",
    "摄影O2O平台美时美刻A轮融资1.2亿",
    "英国领先票据平台获得600万英镑A轮融资",
    "增强现实眼镜castAR完成1500万美元A轮融资",
    "易试互动完成B轮融资 中国文化产业投资基金投资",
    "易试互动宣布完成8000万元B轮融资",
    "自媒体“酒业家”完成5000万元Pre-A轮融资",
    "杰西卡·阿尔芭拥有的Honest完成一亿美元D轮融资",
    "客服平台Udesk完成3000万元A+轮融资",
    "物流配货平台运满满获C轮融资 云峰基金领投",
    "情趣电商“他趣”获8500万B轮融资 年底挂牌新三板",
    "8.17投融资日报：酒店哥哥获2000万美元B轮融资",


]

contentList = [
    "深圳晚报讯（记者 王卫东）东南亚领先的打车应用Grabtaxi宣布完成3.5亿美元的融资，寇图资本、中投和滴滴快的为本轮投资者。据GrabTaxi方面相关负责人介绍，本轮融资资金主要用于快速将出租车产品的成功经验复制到私家车和摩托车等新产品上，以及进一步投入技术研发和延展建设各地的研发中心。",
    "网易科技讯 8月19日消息，两性健康平台他趣宣布完成B轮8500万元融资，投资方为中信建投、鼎锋资产、深圳前海高晟融信股权投资有限公司和A轮投资方达晨创投，此外，创始人黄天财透露，将于今年年底正式挂牌新三板，相关手续已经变更完成。",
    "凤凰科技讯 8月19日消息，成人用品电商他趣今天宣布，已经完成B轮融资8500万，投资方包括中信建投，鼎峰资产，达晨创投以及高晟融信。其中达晨创投参与了他趣的A轮5000万融资。另外，沟通会上他趣还透露，去年底已经启动了新三板挂牌计划，预计今年将在新三板挂牌。",
    "8月18日晚，上海医药(22.02 +1.06%,咨询)集团股份有限公司（601607.SH，下称“上海医药”）发布公告，宣布旗下上海医药大健康云商股份有限公司（下称“上药云健康”）完成来自上海医药、北京京东世纪贸易有限公司（JD.NASDAQ，下称“京东”）以及北京和谐成长投资中心（有限合伙）（下称“IDG资本”）等方面的A轮融资，融资总额达11.12亿元。",
    "美时美刻在创立之初就得到众多互联网及投资领域大佬的力捧。它在天使轮即获得58同城CEO姚劲波、黑马会秘书长杨守斌、酷我科技CEO雷鸣、分享投资创始合伙人崔欣欣、学大教育CEO金鑫等的共同投资。",
    "摘要：英国票据P2P平台MarketInvoice最近获得了A轮融资。新资金将被用于开拓市场。网贷之家译 英国伦敦的P2P网贷平台MarketInvoice最近完成了价值600万英镑的A轮融资。MarketInvoice上线于2011年，在2013年和2014年实现盈利。在4年的运营过程中，平台总共撮合了4.75亿英镑的贷款。这家创业公司的创始人团队是来自雷曼兄弟、高盛集团等著名投行的前银行家和咨询师，因此这家企业在选择融资时机方面做得非常老练。",
    "专注于游戏的初创公司castAR周三宣布，它已经完成了A轮融资，规模为1500万美元。本轮融资的领投方是Android联合创始人安迪·鲁宾（Andy Rubin）在今年早些时候创立的专注于硬件的孵化器风投Playground Global Ventures。",
    "近日，易试互动宣布获得八千万元B轮融资，本次投资方为中国文化产业投资基金。",
    "国内互动新媒体公司易试互动8月18日下午宣布获得8000万元人民币的B轮融资，投资方为中国文化产业投资基金。",
    "7月27日，餐饮O2O自媒体微信公号“餐饮老板内参”宣布完成2000万元Pre-A轮融资，本轮融资由狮享家新媒体基金领投。至此，餐饮老板内参估值或已达1亿元。",
    "600万美元种子资金来说是非常高的回报。Honest最近的这轮融资由新投资者GladeBrookCapitalPartners公司领投。其他参投方包括联博基金以及现有投资者富达管理研究公司、威灵顿管理公司和机构风险合伙公司。",
    "而对于本轮融资，Udesk方面并未透露更多融资细节。",
    "腾讯科技讯（相欣）8月19日消息，物流配货平台“运满满”今日宣布获得数亿元人民币C轮融资，具体融资金额不详，且腾讯科技无法证实融资真实性。本轮融资由马云(微博)旗下云锋基金领投，上一轮投资方红杉资本、光速安振此轮继续跟投。",
    "两性健康平台他趣宣布完成B轮8500万元融资，投资方为中信建投、鼎锋资产、深圳前海高晟融信股权投资有限公司和A轮投资方达晨创投，此外，创始人黄天财透露，将于今年年底正式挂牌新三板，相关手续已经完成。",
    "1. 会场搜索预订平台“酒店哥哥”获经纬创投参投2000万美元B轮融资 2. 提供医生上门出诊服务，Dispatch Health 获 360 万美元融资 2. 居家养老O2O平台“陪爸妈”完成e袋洗千万元融资  3. 汽车后市场O2O平台“好胎屋”完成上海羽时资本领投1亿元A轮融资 4. 跨境电商“拉拉米”获搜于特领投5000万元A轮融资 5. 陌生人互助社区“有我”完成千万美元天使轮融资"

]

#前期处理，去掉引用报头

def preProcess(str):
    patt = re.compile(u".*[：:](.*)")
    temp = re.findall(patt, str)
    if temp:
        str = temp[0]
    return str

#获得融资级别
def getRankInfo(str):
    patt = re.compile(u"^.*([ABCD]|天使|A\+|Pre-A|pre-A)轮")
    ret = re.findall(patt, str)
    rank = ""
    if ret:
        rank = ret[0]
    return rank

#获得融资金额
def getMoneyInfo(str):
    patt = re.compile(u"^.*([ABCD]轮|天使轮|A\+轮|Pre-[ABCD]轮|pre-[ABCD]轮|(最近)?(获得|完成|融资)|[已]?获[得]?|[已]?完成|到资|融资|融资总额为)([\$￥]?[0-9\.]+.*[万亿元镑]|[近数]?[一二两三四五六七八九]?[十百千]?[万亿][美英]?[元镑]?)")
    ret = re.findall(patt, str)
    money = ""
    if ret:
        money = ret[0][3]
    return money

#获得公司名称
def getCompanyInfo(str):
    patt = re.compile(u"^(.+?)([ABCD]\+?轮融资|天使轮融资|[已]?获[得]?|[已]?完成|(正式)?宣布(到资|完成)|到资|融资|最近(获|完成))")
    ret = re.findall(patt, str)
    company = ""
    if ret:
        company = ret[0][0]
        company = company.split(' ')[-1]
        company, number = re.subn(u".*?(拥有的|创立|电商|平台|网站|软件)", "", company)
        company, number = re.subn(u"(公司)", "", company)
        temp = re.findall(u"“(.+)”", company)
        if temp:
            company = temp[0]
        return company

#获得投资方
def getInvestorInfo(str):
    patterns = []
    patterns.append(re.compile(u"().*?[，。].*?[本这]轮(投资|融资)由(.+?领投[，。].+?跟投)[,。]"))
    patterns.append(re.compile(u"().*?[，。].*?[本这]轮(投资|融资)由(.+?领投[，。](其他投资者包括|其他投资者为|其他参投方包括|其他参投方为).+?)[，。]"))
    patterns.append(re.compile(u"().*?[，。].*?[本这]轮(投资|融资)由(.+?领投)[，。]"))
    patterns.append(re.compile(u"()().*?[，。](.+)为.*?投资者"))
    patterns.append(re.compile(u".*?[，。].*?(投资方)(是|为|包括)(.+?、.+?)[，。]"))
    patterns.append(re.compile(u".*?[，。].*?(投资方)(是|为|包括)(.+?，.+?)[。]"))
    patterns.append(re.compile(u".*?[，。].*?(投资方)(是|为|包括)(.+?)[，。]"))
    patterns.append(re.compile(u".*?[，。].*?(领投方)(是|为)(.+?)[，。]"))
    patterns.append(re.compile(u"().*?[，。].*?(完成)?来自(.+?)[等几各]?(方面|家)的.*?([ABCD]轮|天使轮|A\+轮|Pre-[ABCD]轮)"))
    for patt in patterns:
        ret = re.findall(patt, str)
        if ret != []:
            break
    investor = ""
    if ret:
        investor = ret[0][2]
    investor, number = re.subn(u"（.+?）", "", investor)
    investor, number = re.subn(u"[,，。、  ]|和|及|以及", " ", investor)
    investor, number = re.subn(u"领投|跟投|其他投资者包括|其他投资者为|其他参投方包括|其他参投方为", "", investor)
    investor = investor.split(" ")
    return investor

def getMultiCompanies(str):
    patt = re.compile(u"(.+?)(获|[ABCD]\+?轮融资|天使轮融资|[已]?获[得]?|[已]?完成|(正式)?宣布(到资|完成)|到资|融资|最近(获|完成))")
    rets = re.findall(patt, str)
    # print len(rets)
    companies = []
    for ret in rets:
        company = ret[0]
        # print company
        company, number = re.subn(u"[，。]", " ", company)
        company = company.split(' ')[-1]
        company, number = re.subn(u".*?(拥有的|创立|电商|平台|网站|软件)", "", company)
        company, number = re.subn(u"(公司)", "", company)
        temp = re.findall(u"“(.+)”", company)
        if temp:
            company = temp[0]
        companies.append(company)
    return companies

def multiJudge(str):
    companies = getMultiCompanies(str)
    if len(companies) <= 1:
        return False
    mark = 0
    company = companies[0]
    for temp in companies:
        if temp != company:
            mark += 1
    if mark > 0:
        return True
    else:
        return False

def getMultiInfo(title = "", content = ""):
    companies = getMultiCompanies(content)
    for company in companies:
        # print company
        positions = re.finditer(company, content)
        for objTemp in positions:
            pos = objTemp.start()


def getSingleInfo(title = "", content = ""):
    #前期处理，去掉引用报头
    title = preProcess(title)

    rank = company = money = investor = ''

    #获得融资级别
    rank = getRankInfo(title)
    if rank == "":
        rank = getRankInfo(content)

    #获得融资金额
    money = getMoneyInfo(title)
    if money == "":
        money = getMoneyInfo(content)

    #获得公司名称
    company = getCompanyInfo(title)
    if company == "":
        company = getCompanyInfo(content)

    #获得投资者信息
    investor = getInvestorInfo(content)

    rs = {"company": company, "money": money, "rank": rank, "investor": investor}
    return rs

def getInfo(title = "", content = ""):
    ret = []
    if not multiJudge(content):
        temp = getSingleInfo(title, content)
        return temp
    else:
        return ret

if __name__ == "__main__":
    for i in range(len(titleList)):
        title = titleList[i].decode("utf-8")
        content = contentList[i].decode("utf-8")
        multiJudge(content)
        print "title: ", title, "\n", "content: ", content
        financeInfo = getSingleInfo(title, content)
        for key, value in financeInfo.items():
            print key, value
        print "*****************************############################*********************************\n"

