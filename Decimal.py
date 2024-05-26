# DECIMAL
# decimal module tasnordakan tveri het ashxatelis yev hashvark anelu depqum chisht patasxan satanalu hamar e
import decimal

print(dir(decimal))# moduli bolor hatkanishnere paronakox cucak
# ['BasicContext', 'Clamped', 'Context', 'ConversionSyntax', 'Decimal', 'DecimalException', 'DecimalTuple',
# 'DefaultContext', 'DivisionByZero', 'DivisionImpossible', 'DivisionUndefined', 'ExtendedContext', 'FloatOperation',
# 'HAVE_CONTEXTVAR', 'HAVE_THREADS', 'Inexact', 'InvalidContext', 'InvalidOperation', 'MAX_EMAX', 'MAX_PREC',
# 'MIN_EMIN', 'MIN_ETINY', 'Overflow', 'ROUND_05UP', 'ROUND_CEILING', 'ROUND_DOWN', 'ROUND_FLOOR',
# 'ROUND_HALF_DOWN', 'ROUND_HALF_EVEN', 'ROUND_HALF_UP', 'ROUND_UP', 'Rounded', 'Subnormal', 'Underflow',
# '__builtins__','__cached__', '__doc__', '__file__', '__libmpdec_version__', '__loader__', '__name__',
# '__package__', '__spec__','__version__', 'getcontext', 'localcontext', 'setcontext']

#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

a = decimal.Decimal(4.5).exp() # ays funkcyan veradarcnum e e^x
b = decimal.Decimal(4.5).sqrt()# ays funkciyan veradarcnum e tvi qarakusi armate

print(a)# 90.01713130052181355011545675
print(b)# 2.121320343559642573202533086

# aranc decimal funkcayi menq stanalu eynq aveli karch patasxan
# hamamatutyan hamar ktpenq aranc decimal funkcayi

import math

print(math.exp(4.5))# 90.01713130052181
print(math.sqrt(4.5))# 2.1213203435596424

#-----------------------------------------------------------------------

a = decimal.Decimal(4.5).ln()# hashvum e tvi ln
b = decimal.Decimal(4.5).log10()# hashvum e tvi log10

print(a)# 1.504077396776274073373258352
print(b)# 0.6532125137753436793763169118

#-----------------------------------------------------------------------

a = decimal.Decimal(-4.5).as_tuple()# veradarcnum tasnordakan tive vorpes tuple
b = decimal.Decimal(5).fma(2, 3)# ogtagorcvum e miaculvac bazmapatkume yev gumarume hashvelu hamar '(5*2)+3'

print(a)# DecimalTuple(sign=1, digits=(4, 5), exponent=-1)
print(b)# 13

#-----------------------------------------------------------------------

# compare(): veradarcnum e 1 yete 1-in tasnordakan argumente mec e 2-rdic -1
# yete 1-in tasnordakan argumnete poqer e 2-rdic yev 0 yete erkusn el hamas en
#compare_total_mag(): nunyn compare() bayc hakarake

# tasnordakan hamari skzmnavorum
a = decimal.Decimal(9.53)
b = decimal.Decimal(-9.56)

print(a.compare(b))# hamematelov tasnordakan tvere ayd metodov stanum enq = 1
print(a.compare_total_mag(b))# hamematelov tasnordakan tvere ayd metodov stanum enq = -1

#-----------------------------------------------------------------------

# tasnordakan hamari skzmnavorum
a = decimal.Decimal(9.53)
b = decimal.Decimal(-9.56)

print(b.copy_abs())# talis e bacarcak arjeqe -> 9.5600000000000004973799150320701301097869873046875
print(b.copy_negate())# talis e jxtvac arjeqe -> 9.5600000000000004973799150320701301097869873046875
print(a.copy_sign(b))# tpum e arjin argumente matchenelov nsane 2-rd argumnetic -> -9.5299999999999993605115378159098327159881591796875

#-----------------------------------------------------------------------

# tasnordakan hamari skzmnavorum
a = decimal.Decimal(9.53)
b = decimal.Decimal(7.43)

print(a.min(b))# talis e poqraguyne
print(a.max(b))# talis e mecaguyne

#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------