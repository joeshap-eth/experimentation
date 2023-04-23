import inspect
import os
import sys
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
import eth_node_client

# Not yet working :(
# It says it can't find a suitable peer, but at the same time calls are succeeding for other contracts.
if __name__ == "__main__":
    #if len(sys.argv) != 5:
    #    print("Usage: python get_gpt_response.py <token_id1> <name1> <token_id2> <name2>")
    #    sys.exit(1)
    
    print(eth_node_client.get_hv_mtl_info(3825))
        