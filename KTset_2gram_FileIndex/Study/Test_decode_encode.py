#!/Python27/python
#-*- coding: utf-8 -*-

def getByte(v):
    return ' '.join(["%02X"%ord(b) for b in v])
# end def

s_utf='한글' # ED 95 9C EA B8 80 <type 'str'> (utf-8 encoded byte string)
s_UTF=s_utf.decode('utf-8') # D55C AE00 <type 'unicode'> (unicode)
s_euc=s_utf.decode('utf-8').encode('euc-kr') # C7 D1 B1 DB <type 'str'> (euc-kr encoded byte string)
s_EUC=s_euc.decode('euc-kr') # D55C AE00 <type 'unicode'> (unicode)

print getByte(s_utf),type(s_utf)
print getByte(s_UTF),type(s_UTF)
print getByte(s_euc),type(s_euc)
print getByte(s_EUC),type(s_EUC)