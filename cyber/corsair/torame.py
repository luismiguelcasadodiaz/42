#!/usr/local/bin/python3

p = 2438593310261074657282043163376290856047222440000419075612452801035390644758889499482865075970053142986916368260984858690118496306023036284680524966770279394068431807148336577519722485636930557224182394703700065632044053829756756845734485338498233667494865837330182593896052648121623458208640331155181192046654120922889117408243

# 000ß
q1 = 7133704182713145528888455855145330550435471752896204000487325767891207494353156909758362147179543166905412436566929630948643398428927219946768048179334625057040302114032998305275712811879270669691449140964189139187843555605129881155161001609765563396666874330184950147177215330345788209597

n1 = 17396203297345723710457112477216462502020056676751196937279025484444998578972129168285486420494699751699693758496473534461441916075206975649843925980427490739438546106943341752113103230156778453231163764753265987439587297840599494098063557491413311421221372212205889553645742125869020929437772559637688762000751365946214607297608615366052164301583581624631986996515924049798719685643839122864378647795630003399400969475941588893112417146213181360424876369658923725848006983472793224220355009217059314073839915578613725191738926236830479693088988202641376036909142482274810976201973634695245924879293170341871899508071
aa = 17396203297345723710457112477216462502020056676751196937279025484444998578972129168285486420494699751699693758496473534461441916075206975649843925980427490739438546106943341752113103230156778453231163764753265987439587297840599494098063557491413311421221372212205889553645742125869020929437772559637688762000751365946214607297608615366052164301583581624631986996515924049798719685643839122864378647795630003399400969475941588893112417146213181360424876369658923725848006983472793224220355009217059314073839915578613725191738926236830479693088988202641376036909142482274810976201973634695245924879293170341871899508071

n = 17396203297345723710457112477216462502020056676751196937279025484444998578972129168285486420494699751699693758496473534461441916075206975649843925980427490739438546106943341752113103230156778453231163764753265987439587297840599494098063557491413311421221372212205889553645742125869020929437772559637688762000751365946214607297608615366052164301583581624631986996515924049798719685643839122864378647795630003399400969475941588893112417146213181360424876369658923725848006983472793224220355009217059314073839915578613725191738926236830479693088988202641376036909142482274810976201973634695245924879293170341871899508071


# 001

q2 = 9510629655441875259919133394408374155368205261081120591703224234267568277434664934671012939151971848636855066445402526018979693120911768010650423103842512987255283069799403778798782641715403929659358156473226773270775678615099360005990481659802017316408364833814711140642610115044845172181

n2 = 23192557854131146480524233677243215857493580881768010796597369654259285174296084949405644624101269758928888241665547623080669779416561054823057114981641446850651730398879025537606391885260975671043555933471519406039118040249053605900475401559715670863564679148707305114778370382663004303027473970246487650906658923290960869235380794147710512847951300841977236908494749800888118162734285698841292545668613134297072611812758615314507154184265196063828334829853479888286002341229656424923760974396740086882770401821587419643718301690318908783522425677484172155387571412715061625999839654749213634719693272088781803687983
bb = 23192557854131146480524233677243215857493580881768010796597369654259285174296084949405644624101269758928888241665547623080669779416561054823057114981641446850651730398879025537606391885260975671043555933471519406039118040249053605900475401559715670863564679148707305114778370382663004303027473970246487650906658923290960869235380794147710512847951300841977236908494749800888118162734285698841292545668613134297072611812758615314507154184265196063828334829853479888286002341229656424923760974396740086882770401821587419643718301690318908783522425677484172155387571412715061625999839654749213634719693272088781803687983

def gcd(a, b):  # Greatest Common Divisor Generator (Euclidean Algorithm)
    while b != 0:  # While remainder exists
        t = b  # Initially r[k-1]
        b = a % t  # Initially r[k] = r[k-2] mod r[k-1] (where r[k-2] is a)
        a = t  # Predecessor of remainder (b)
    return a

print(gcd(n1, n2))