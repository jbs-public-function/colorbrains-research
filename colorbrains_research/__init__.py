import os


research_datapath = os.path.join(os.path.dirname(__file__), 'research_data')
if not os.path.exists(research_datapath):
    os.makedirs(research_datapath)
