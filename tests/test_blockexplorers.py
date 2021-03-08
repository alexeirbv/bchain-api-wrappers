import aiounittest
from bchain_api_wrappers.base.models import ServiceStatus
from bchain_api_wrappers.blockexplorers import *


class TestAdapter(aiounittest.AsyncTestCase):
    async def test_ada_graphql(self):
        adapter = AdaGraphQLBased(url="https://adaapi.guarda.co", coin="ada")
        status = await adapter.get_status()
        assert isinstance(status, ServiceStatus)
        assert status.height > 0

    async def test_yoroi_backend(self):
        adapter = AdaYoroiBackendBased(url="https://ada-backend.guarda.co", coin="ada")
        status = await adapter.get_status()
        assert isinstance(status, ServiceStatus)
        assert status.height > 0

    async def test_algo_explorer(self):
        adapter = AlgoBased(url="https://api.algoexplorer.io", coin="algo")
        status = await adapter.get_status()
        assert isinstance(status, ServiceStatus)
        assert status.height > 0

    async def test_beaconchain_explorer(self):
        adapter = BeaconchaInBased(url="https://beaconcha.in", coin="eth2")
        status = await adapter.get_status()
        assert isinstance(status, ServiceStatus)
        assert status.height > 0

    async def test_binance_api(self):
        adapter = BinanceApiBased(url="https://api-binance-mainnet.cosmostation.io", coin="bnb")
        status = await adapter.get_status()
        assert isinstance(status, ServiceStatus)
        assert status.height > 0

    async def test_bit_aps_explorer(self):
        adapter = BitApsBased(url="https://teth.bitaps.com", coin="eth-ropsten")
        status = await adapter.get_status()
        assert isinstance(status, ServiceStatus)
        assert status.height > 0

    async def test_bitcoin_com_explorer(self):
        adapter = BitcoinComBased(url="https://explorer.api.bitcoin.com/bch", coin="bch")
        status = await adapter.get_status()
        assert isinstance(status, ServiceStatus)
        assert status.height > 0

    async def test_bitcore_insight_explorer(self):
        adapter = BitcoreBased(url="https://xvginsight.guarda.co", coin="xvg")
        status = await adapter.get_status()
        assert isinstance(status, ServiceStatus)
        assert status.height > 0

    async def test_blockbook_explorer(self):
        adapter = BlockBookBased(url="https://bitcoinblockexplorers.com/", coin="btc")
        status = await adapter.get_status()
        assert isinstance(status, ServiceStatus)
        assert status.height > 0

    async def test_blockchair_explorer(self):
        adapter = BlockChairBased(url="https://api.blockchair.com/cardano", coin="ada")
        status = await adapter.get_status()
        assert isinstance(status, ServiceStatus)
        assert status.height > 0

    async def test_blockstream_explorer(self):
        adapter = BlockStreamBased(url="https://BlockStream.info/testnet/api", coin="TBTC")
        status = await adapter.get_status()
        assert isinstance(status, ServiceStatus)
        assert status.height > 0

    async def test_chainz_explorer(self):
        adapter = ChainZBased(url="https://chainz.cryptoid.info/btc", coin="btc")
        status = await adapter.get_status()
        assert isinstance(status, ServiceStatus)
        assert status.height > 0

    async def test_clo_explorer(self):
        adapter = CloBased(url="https://explorer.callisto.network", coin="clo")
        status = await adapter.get_status()
        assert isinstance(status, ServiceStatus)
        assert status.height > 0

    async def test_cosmos_cli(self):
        adapter = CosmosCliBased(url="https://cosmos.guarda.co", coin="atom")
        status = await adapter.get_status()
        assert isinstance(status, ServiceStatus)
        assert status.height > 0

    async def test_cosmos_station_explorer(self):
        adapter = CosmosStationBased(url="https://api.cosmostation.io", coin="atom")
        status = await adapter.get_status()
        assert isinstance(status, ServiceStatus)
        assert status.height > 0

    async def test_dcr_data_explorer(self):
        adapter = DcrDataBased(url="https://explorer.dcrdata.org", coin="dcr")
        status = await adapter.get_status()
        assert isinstance(status, ServiceStatus)
        assert status.height > 0

    async def test_dogechain_explorer(self):
        adapter = DogeChainBased(url="https://dogechain.info", coin="doge")
        status = await adapter.get_status()
        assert isinstance(status, ServiceStatus)
        assert status.height > 0

    async def test_etherchain_explorer(self):
        adapter = EtherChainBased(url="https://etherchain.org", coin="ETH")
        status = await adapter.get_status()
        assert isinstance(status, ServiceStatus)
        assert status.height > 0

    async def test_insight_explorer(self):
        adapter = InsightBased("https://explorer.bitcoingold.org/insight-api", coin="BTG")
        status = await adapter.get_status()
        assert isinstance(status, ServiceStatus)
        assert status.height > 0

    async def test_iquidus_explorer(self):
        adapter = IquidusBased(url="https://explorer.aryacoin.io", coin="AYA")
        status = await adapter.get_status()
        assert isinstance(status, ServiceStatus)
        assert status.height > 0

    async def test_lisk_explorer(self):
        adapter = LskBased(url="https://explorer.lisk.io", coin="LSK")
        status = await adapter.get_status()
        assert isinstance(status, ServiceStatus)
        assert status.height > 0

    async def test_nanocrawler_explorer(self):
        adapter = NanoCrawlerBased(url="https://api.nanocrawler.cc", coin="NANO")
        status = await adapter.get_status()
        assert isinstance(status, ServiceStatus)
        assert status.height > 0

    async def test_omni_api_explorer(self):
        adapter = OmniApiBased(url="https://api.omniexplorer.info", coin="OMNI")
        status = await adapter.get_status()
        assert isinstance(status, ServiceStatus)
        assert status.height > 0

    async def test_ontology_explorer(self):
        adapter = OntBased(url="https://explorer.ont.io", coin="ONT")
        status = await adapter.get_status()
        assert isinstance(status, ServiceStatus)
        assert status.height > 0

    # async def test_polkascan_explorer(self):
    #     adapter = PolkaScan(url="https://explorer-31.polkascan.io/polkadot", coin="DOT")
    #     status = await adapter.get_status()
    #     print(status)
    #     assert isinstance(status, ServiceStatus)
    #     assert status.height > 0

    async def test_prohashing_explorer(self):
        adapter = ProHashingBased(url="https://prohashing.com/explorerJson/getInfo?coin_name=Reddcoin", coin="RDD")
        status = await adapter.get_status()
        assert isinstance(status, ServiceStatus)
        assert status.height > 0

    async def test_so_chain_explorer(self):
        adapter = SoChainBased(url="https://sochain.com", coin="TZEC")
        status = await adapter.get_status()
        assert isinstance(status, ServiceStatus)
        assert status.height > 0

    async def test_subscan_explorer(self):
        adapter = SubscanBased(url="https://polkadot.subscan.io", coin="DOT")
        status = await adapter.get_status()
        assert isinstance(status, ServiceStatus)
        assert status.height > 0

    async def test_tokenview_explorer(self):
        adapter = TokenViewBased(url="https://grs.tokenview.com", coin="GRS")
        status = await adapter.get_status()
        assert isinstance(status, ServiceStatus)
        assert status.height > 0

    async def test_verge_explorer(self):
        adapter = XvgBased(url="https://vergeexplorer.com", coin="XVG")
        status = await adapter.get_status()
        assert isinstance(status, ServiceStatus)
        assert status.height > 0

    async def test_whatsonchain_explorer(self):
        adapter = WhatsOnChainBased(url="https://api.whatsonchain.com/v1/bsv/main", coin="BSV")
        status = await adapter.get_status()
        assert isinstance(status, ServiceStatus)
        assert status.height > 0

    async def test_xdc_explorer(self):
        adapter = XdcBased(url="https://explorer.xinfin.network", coin="XDC")
        status = await adapter.get_status()
        assert isinstance(status, ServiceStatus)
        assert status.height > 0

    async def test_xem_explorer(self):
        adapter = NemBased(url="https://explorer.nemtool.com", coin="XEM")
        status = await adapter.get_status()
        assert isinstance(status, ServiceStatus)
        assert status.height > 0

    async def test_xtz_explorer(self):
        adapter = XtzBased(url="https://api.tzstats.com", coin="XTZ", is_provider=True)
        status = await adapter.get_status()
        assert isinstance(status, ServiceStatus)
        assert status.height > 0

    async def test_zchain_explorer(self):
        adapter = ZChaINBased(url="https://yec-api.zcha.in/v2/mainnet", coin="YEC")
        status = await adapter.get_status()
        assert isinstance(status, ServiceStatus)
        assert status.height > 0

    async def test_goalseeker_based(self):
        adapter = GoalSeekerBased(url="https://ms30v30mrj.execute-api.ca-central-1.amazonaws.com", coin="ALGO")
        status = await adapter.get_status()
        print(status)
        assert isinstance(status, ServiceStatus)
        assert status.height > 0

    async def test_tokenview_based(self):
        adapter = TokenViewBased(url="https://neo.tokenview.com", coin="NEO")
        status = await adapter.get_status()
        print(status)
        assert isinstance(status, ServiceStatus)
        assert status.height > 0


    # async def test_etherchain_explorer(self):
    #     adapter = DcrData(url="https://dogechain.info", coin="doge")
    #     status = await adapter.get_status()
    #     assert isinstance(status, ServiceStatus)
    #     assert status.height > 0
