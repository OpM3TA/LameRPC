from rpc_service import *


"""
I'm gonna rant a little here, I'm fuckin confused,
is the username used to communicate with electrum just the wallet name? Or is that just in my instance,
because I'm simple minded as fuck. I'm actually really confused about this but lets let it slide, point is yeah, uh whatever.
"""
# Replace info below with your info and port. You can find this out in electrum (prob by other means) but by using
# the python console and getconfig("rpcuser") then getconfig("rpcport") or whatever

provider = JSONRPC_CLIENT("http://127.0.0.1", 19991, "user","password")
resp = provider.ValidateAddress("blahblahblahblah")
print(resp)

"""
Theres a couple more commands I've preset, I'll continue working on it personally but wont upload.
But for anyone that comes across here are current commands:
SetConfig
GetConfig
SetRPCPassword
GetRPCPassword
ValidateAddress

Anything other than those will need to be construction from RPCMSG or whatever, but its basic 
and just commands with params and its what is behind the scenes of the previous commands
so just look at them as a reference for doing more or something.
"""

