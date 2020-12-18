import os

class Connector:
    def __init__(self):
        self.run_list = os.popen("iwctl device list").read().split(' ')

        self.interface = "".join([i for i in self.run_list if i.startswith('w')])

        self.net_list = os.popen(f"iwctl station {self.interface} get-networks").read()

        self.connected_network = os.popen(r"iwctl station wlan0 show | grep -oP 'Connected network\s+\K\w+'").read()

        self.known_networks = os.popen("iwctl known-networks list").read()
    
    def check_connection(self):
        if self.connected_network != "":
            return True, ssid
        else:
            return False, None


    def connect(self, ssid, psk=None):
        if self.connected_network in self.known_networks:
            os.popen(f"iwctl station {self.interface} connect {ssid}")

        else:
            if psk:
                conn = os.popen(f"iwctl --passphrase '{psk}' station {self.interface} connect '{ssid}'").read()
                print(f"Network: {ssid}, PSK: {psk}")
                if conn == "Operation failed":
                    return False
                else:
                    return True

            else: 
                os.popen(f"iwctl station {self.interface} connect '{ssid}'")
                print(f"Netowrk: {ssid}, Interface: ", self.interface)
                return True

    def disconnect(self):
        os.popen(f"iwctl station {self.interface} disconnect")
        return True


    def forget(self, ssid):
        os.popen(f"iwctl known-networks {ssid} forget")
        return True




