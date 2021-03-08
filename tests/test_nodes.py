import aiounittest
from base.models import ServiceStatus
from nodes import *


class TestAdapter(aiounittest.AsyncTestCase):
    async def test_algo_node(self):
        adapter = AlgoBased(url="https://algonode.guarda.com", coin="ALGO")
        status = await adapter.get_status()
        assert isinstance(status, ServiceStatus)
        assert status.height > 0

    # async def test_bitcoind_based(self):
    #     adapter = BtcBased(url="https://btc.guarda.co", coin="BTC", credentials=("guarda", "PLEASE_FILL"))
    #     status = await adapter.get_status()
    #     assert isinstance(status, ServiceStatus)
    #     assert status.height > 0

    async def test_cosmos_node(self):
        adapter = AtomBased(url="https://cosmos.guarda.co", coin="BTC")
        status = await adapter.get_status()
        print(status)
        assert isinstance(status, ServiceStatus)
        assert status.height > 0

    async def test_dot_node(self):
        adapter = DotBased(url="https://dotnode.guarda.co", coin="DOT")
        status = await adapter.get_status()
        assert isinstance(status, ServiceStatus)
        assert status.height > 0

    async def test_eth2_node(self):
        adapter = Eth2PrysmBased(url="https://eth2node.guarda.com", coin="DOT")
        status = await adapter.get_status()
        assert isinstance(status, ServiceStatus)
        assert status.height > 0

    async def test_fio_node(self):
        adapter = FioBased(url="https://fio.guarda.co", coin="FIO")
        status = await adapter.get_status()
        assert isinstance(status, ServiceStatus)
        assert status.height > 0

    async def test_geth_based(self):
        adapter = EthGethBased(url="https://eth.guarda.co", coin="ETH")
        status = await adapter.get_status()
        print(status)
        assert isinstance(status, ServiceStatus)
        assert status.height > 0

    async def test_lsk_node(self):
        adapter = LskBased(url="https://lsk.guarda.co", coin="LSK")
        status = await adapter.get_status()
        print(status)
        assert isinstance(status, ServiceStatus)
        assert status.height > 0

    # TODO: Resolve lag
    # async def test_nano_node(self):
    #     adapter = NanoNode(url="https://nano.guarda.co", coin="NANO")
    #     status = await adapter.get_status()
    #     print(status)
    #     assert isinstance(status, ServiceStatus)
    #     assert status.height > 0

    async def test_neo_node(self):
        adapter = NeoBased(url="https://neo.guarda.co", coin="NEO")
        status = await adapter.get_status()
        assert isinstance(status, ServiceStatus)
        assert status.height > 0

    async def test_one_node(self):
        adapter = OneBased(url="https://api.s0.t.hmny.io", coin="ONE")
        status = await adapter.get_status()
        assert isinstance(status, ServiceStatus)
        assert status.height > 0

    async def test_ontology_node(self):
        adapter = OntBased(url="https://ont.guarda.co", coin="ONT")
        status = await adapter.get_status()
        assert isinstance(status, ServiceStatus)
        assert status.height > 0

    async def test_vechain_node(self):
        adapter = VetBased(url="https://vet.guarda.co", coin="VET")
        status = await adapter.get_status()
        assert isinstance(status, ServiceStatus)
        assert status.height > 0

    async def test_waves_node(self):
        adapter = WavesBased(url="https://waves.guarda.co", coin="WAVES")
        status = await adapter.get_status()
        assert isinstance(status, ServiceStatus)
        assert status.height > 0

    async def test_nem_node(self):
        adapter = NemBased(url="https://nemnode.guarda.co", coin="NEM")
        status = await adapter.get_status()
        assert isinstance(status, ServiceStatus)
        assert status.height > 0

    async def test_xtz_node(self):
        adapter = XtzBased(url="https://xtz.guarda.co", coin="XTZ")
        status = await adapter.get_status()
        assert isinstance(status, ServiceStatus)
        assert status.height > 0
