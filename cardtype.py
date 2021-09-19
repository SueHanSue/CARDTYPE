#v1.1.2

# 定义一个函数，实现判断输入的id 获取type

#method1:字典存储判断条件，将判定条件与def_body分离
# 定义字典存放type类型对应的判定该条件：card_type :begins_with ,lenth
condition_types={
    "AMEX":[["34","37"],[15]],
    "Discover":[["6011"],[16]],
    "Mastercard":[["51","52","53","54","55"],[16]],
    "VISA":[["4"],[13,16]]
                 }

def check_isuser(id):
    val=str(id)  #转为字符类型
    success=0  #定义匹配成功的次数
    for typename in condition_types.keys():#用键迭代
        for x in condition_types[typename][0]:  #开头字段迭代
            if val.startswith(x) and len(val) in condition_types[typename][1]:  #匹配开头字段和长度
                success+=1  #匹配成功次数+1
                print(typename)  #匹配成功则输出type名
                break
    if success==0:  #匹配失败返回unknown
        print("Unknown")


check_isuser(4111111111111)
check_isuser(4012555588886645)
check_isuser(378888888888999)
check_isuser(6011999999999999)
check_isuser(5100005588661156)
check_isuser(99999999)