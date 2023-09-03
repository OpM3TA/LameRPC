import json
import requests 
from requests.auth import HTTPBasicAuth   
import pprint

#rpc_user='escrow'
#rpc_password='password'
#url = "http://127.0.0.1:19991"


"""
JSONRPC Client class meant for communicating with Electrum.
"""
class JSONRPC_CLIENT:
    #TRUTH_VALUES = ["True", "true","TRUE"]
    #FALSE_VALUES = ["False", "false"]
    """
   Setup the rpc server info, including creds.
    """
    def __init__(self, rpc_host:str, rpc_port:int, rpc_user:str, rpc_pass:str):
        self.RPC_URL=f'{rpc_host}:{rpc_port}'
        self.RPC_AUTH=HTTPBasicAuth(rpc_user,rpc_pass)
    
    """
    Update RPC Auth, in case for example you setconfig, rpcpassword, lol.
    """
    def UpdateAuth(self, rpc_user:str, rpc_pass:str):
        self.RPC_AUTH=HTTPBasicAuth(rpc_user,rpc_pass)
        """
        Update rpc server host:port
        Yes you could just call constructor again, or..not :)
        """
    def UpdateServer(self, rpc_host:str, rpc_port:int):
         self.RPC_URL=f'{rpc_host}:{rpc_port}'


    class RPCMSG:
        """
        Build RPC message for electrum. 
        Basically only changes method (command)
        and params, which can be things like a btc addy
        or empty list by default
        """
        def __init__(self,rpc_method='help', rpc_params=[]):
            self.RPC_METHOD=rpc_method
            self.RPC_PARAMS=rpc_params

        """
        Headers required for electrums jsonrpc
        No reason to ever modify.
        Same for the..um..whatever tf the rest is for the rpc request.
        """
        RPC_HEADERS = {'content-type': "application/json", 'cache-control': "no-cache"}
        __JSONRPC = {"jsonrpc":"2.0","id":"curltext"}


        def __str__(self):
            return json.dumps({**self.__JSONRPC, "method":self.RPC_METHOD, "params": self.RPC_PARAMS})
        """
        get_dump literally just calls the __str__ function,
        no diff than someone doing like str(class).
        fuck off.
        """
        def get_dump(self):
            return self.__str__()

        """
            Setup commands manually, or I'll have some pre-set ones too.
            read_pass = provider.RPCMSG("getconfig",["rpcpassword"])
        """
    def SendRPC(self, payload:RPCMSG):
        response = requests.request("POST", 
                                self.RPC_URL, 
                                data = str(payload), 
                                headers = payload.RPC_HEADERS,
                                auth=self.RPC_AUTH)
        return response


    """
    Start of simple/easy access commands.
    """

    """
    I've started doing it inline, hope thats fine.
    Why create useless variables when I'm just returning
    the values?

    Setconfig command.
    ex: setconfig(["rpcpassword", "new_password123"])
    """


    def SetConfig(self, params:list):
         return self.SendRPC(self.RPCMSG("setconfig", params))
    def GetConfig(self, params:list):
        return self.SendRPC(self.RPCMSG("getconfig", params))
    # Sets RPC password
    def SetRPCPassword(self, new_pass:str):
        return self.SetConfig(["rpcpassword", new_pass])
    # Returns current RPC password
    def GetRPCPassword(self):
        return self.GetConfig(["rpcpassword"]).json()["result"]
        # Probably better ways to parse and error check in future.
        # But right now this is chill.
    def ValidateAddress(self, btcaddr:str):
        return self.SendRPC(self.RPCMSG("validateaddress",[btcaddr])).json()["result"]
