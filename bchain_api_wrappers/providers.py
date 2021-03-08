import nodes
import blockexplorers
import asyncio

PROVIDERS = {
    "BTC": [
        blockexplorers.BlockBookBased(url="https://btc1.trezor.io", coin="BTC"),
        blockexplorers.BlockBookBased(url="https://btc2.trezor.io", coin="BTC"),
        blockexplorers.BlockBookBased(url="https://btc3.trezor.io", coin="BTC"),
        blockexplorers.BlockBookBased(url="https://btc4.trezor.io", coin="BTC"),
        blockexplorers.BlockBookBased(url="https://btc5.trezor.io", coin="BTC"),
        blockexplorers.SoChainBased(url="https://sochain.com", coin="BTC"),
        blockexplorers.BitApsBased(url="https://bitaps.com", coin="BTC"),
        blockexplorers.BlockChairBased(url="https://api.blockchair.com/bitcoin", coin="BTC")
    ],
    "AYA": [
        blockexplorers.IquidusBased(url="https://explorer.aryacoin.io", coin="AYA"),
        blockexplorers.BlockBookBased(url="https://aya.polispay.com", coin="AYA")
    ],
    "ALGO": [
        blockexplorers.AlgoBased(url="https://api.algoexplorer.io", coin="ALGO"),
        blockexplorers.GoalSeekerBased(url="https://ms30v30mrj.execute-api.ca-central-1.amazonaws.com", coin="ALGO")
    ],
    "ADA": [
        blockexplorers.BlockChairBased(url="https://api.blockchair.com/cardano", coin="ADA"),
        blockexplorers.AdaGraphQLBased(url="https://explorer.cardano-mainnet.iohk.io/graphql", coin="ADA")
    ],
    "BSV": [
        blockexplorers.BlockChairBased(url="https://api.blockchair.com/bitcoin-sv", coin="BSV"),
        blockexplorers.WhatsOnChainBased(url="https://api.whatsonchain.com/v1/bsv/main", coin="BSV"),
        blockexplorers.TokenViewBased(url="https://grs.tokenview.com", coin="BSV")
    ],
    "TBSV": [
        blockexplorers.WhatsOnChainBased(url="https://api.whatsonchain.com/v1/bsv/test", coin="TBSV"),
    ],
    "BCH": [
        blockexplorers.BlockBookBased(url="https://bch1.trezor.io", coin="BCH"),
        blockexplorers.BlockBookBased(url="https://bch2.trezor.io", coin="BCH"),
        blockexplorers.BlockBookBased(url="https://bch3.trezor.io", coin="BCH"),
        blockexplorers.BlockBookBased(url="https://bch4.trezor.io", coin="BCH"),
        blockexplorers.BlockBookBased(url="https://bch5.trezor.io", coin="BCH"),
    ],
    "KMD": [
        blockexplorers.InsightBased(url="https://kmdexplorer.io/insight-api-komodo", coin="KMD"),
        blockexplorers.InsightBased(url="https://kmdexplorer.ru/insight-api-komodo", coin="KMD"),
    ],
    "DOGE": [
        blockexplorers.DogeChainBased(url="https://dogechain.info", coin="DOGE"),
    ],
    "CRM": [
        blockexplorers.IquidusBased(url="https://explorer.creamcoin.com", coin="CRM"),
    ],
    "DASH": [
        blockexplorers.InsightBased(url="https://explorer.dash.org/insight-api", coin="DASH"),
        blockexplorers.BlockChairBased(url="https://api.blockchair.com/dash", coin="DASH"),
    ],
    "GRS": [
        blockexplorers.InsightBased(url="https://groestlsight.groestlcoin.org/api", coin="GRS"),
        blockexplorers.TokenViewBased(url="https://grs.tokenview.com", coin="GRS"),
        blockexplorers.BlockChairBased(url="https://api.blockchair.com/groestlcoin", coin="GRS")
    ],
    "VTC": [
        blockexplorers.InsightBased(url="https://insight.vertcoin.org/insight-vtc-api", coin="VTC"),
        blockexplorers.TokenViewBased(url="https://vtc.tokenview.com", coin="VTC"),
    ],
    "YEC": [
        blockexplorers.ZChaINBased(url="https://yec-api.zcha.in/v2/mainnet", coin="YEC"),
    ],
    "DCR": [
        blockexplorers.DcrDataBased(url="https://explorer.dcrdata.org", coin="DCR"),
        blockexplorers.BlockBookBased(url="https://blockbook.decred.org:9161/", coin="DCR")
    ],
    "QTUM": [
        blockexplorers.InsightBased(url="https://explorer.qtum.org/insight-api", coin="QTUM"),
    ],
    "XZC": [
        blockexplorers.InsightBased(url="https://explorer.zcoin.io/api", coin="XZC"),
        blockexplorers.TokenViewBased(url="https://xzc.tokenview.com", coin="XZC"),
    ],
    "RVN": [
        blockexplorers.InsightBased(url="https://ravencoin.network/api", coin="RVN"),
    ],
    "LTC": [
        blockexplorers.BlockBookBased(url="https://ltc1.trezor.io", coin="LTC"),
        blockexplorers.BlockBookBased(url="https://ltc2.trezor.io", coin="LTC"),
        blockexplorers.BlockBookBased(url="https://ltc3.trezor.io", coin="LTC"),
        blockexplorers.BlockBookBased(url="https://ltc4.trezor.io", coin="LTC"),
        blockexplorers.BlockBookBased(url="https://ltc5.trezor.io", coin="LTC"),
    ],
    "DGB": [
        blockexplorers.InsightBased(url="https://digiexplorer.info/api", coin="DGB"),
        blockexplorers.TokenViewBased(url="https://dgb.tokenview.com", coin="DGB"),
    ],
    "ZEC": [
        blockexplorers.BlockBookBased(url="https://zec1.trezor.io", coin="ZEC"),
        blockexplorers.BlockBookBased(url="https://zec2.trezor.io", coin="ZEC"),
        blockexplorers.BlockBookBased(url="https://zec3.trezor.io", coin="ZEC"),
        blockexplorers.BlockBookBased(url="https://zec4.trezor.io", coin="ZEC"),
        blockexplorers.BlockBookBased(url="https://zec5.trezor.io", coin="ZEC"),
        blockexplorers.ZChaINBased(url="https://api.zcha.in/v2/mainnet", coin="ZEC"),
    ],
    "TZEC": [
        blockexplorers.SoChainBased(url="https://sochain.com", coin="TZEC"),
        blockexplorers.InsightBased(url="https://explorer.testnet.z.cash/api", coin="TZEC"),
    ],
    "TBTC": [
        blockexplorers.BlockStreamBased(url="https://BlockStream.info/testnet/api", coin="TBTC"),
    ],
    "NLG": [
        blockexplorers.TokenViewBased(url="https://nlg.tokenview.com", coin="NLG"),
    ],
    "BTG": [
        blockexplorers.InsightBased(url="https://explorer.bitcoingold.org/insight-api", coin="BTG"),
    ],
    "ETC": [
        blockexplorers.TokenViewBased(url="https://etc.tokenview.com", coin="ETC")
    ],
    "ETH": [
        blockexplorers.BlockChairBased(url="https://api.blockchair.com/ethereum", coin="ETH"),
        blockexplorers.EtherChainBased(url="https://EtherChain.org", coin="ETH")
    ],
    "ETH-ROPSTEN": [
        blockexplorers.BitApsBased(url="https://teth.bitaps.com", coin="ETH-ROPSTEN"),
    ],
    "ONT": [
        blockexplorers.OntBased(url="https://explorer.ont.io", coin="ONT"),
    ],
    "LSK": [
        blockexplorers.LskBased(url="https://explorer.lisk.io", coin="LSK"),
    ],
    "WAVES": [
        nodes.WavesBased(url="https://nodes.wavesnodes.com", coin="WAVES"),
    ],
    "SWAVES": [
        nodes.WavesBased(url="https://nodes-stagenet.wavesnodes.com", coin="SWAVES"),
    ],
    "FIO": [
        nodes.FioBased(url="https://fio.eu.eosamsterdam.net", coin="FIO"),
        nodes.FioBased(url="https://fio.eosphere.io", coin="FIO"),
    ],
    "OMNI": [
        blockexplorers.OmniApiBased(url="https://api.omniexplorer.info", coin="OMNI"),
    ],
    "RDD": [
        blockexplorers.InsightBased(url="https://live.reddcoin.com/api", coin="RDD"),
        blockexplorers.ProHashingBased(url="https://prohashing.com/explorerJson/getInfo?coin_name=Reddcoin",
                                       coin="RDD"),
    ],
    "ZEN": [
        blockexplorers.InsightBased(url="https://explorer.zensystem.io/api", coin="ZEN"),
        blockexplorers.InsightBased(url="https://explorer.horizen.global/api", coin="ZEN"),
    ],
    "XTZ": [
        blockexplorers.XtzBased(url="https://api.tzstats.com", coin="XTZ"),
    ],
    "XVG": [
        blockexplorers.XvgBased(url="https://vergeexplorer.com", coin="XVG"),
        blockexplorers.XvgBased(url="https://verge-blockchain.info", coin="XVG")
    ],
    "NANO": [
        blockexplorers.NanoCrawlerBased(url="https://api.nanocrawler.cc", coin="NANO"),
    ],
    "ATOM": [
        blockexplorers.CosmosStationBased(url="https://api.cosmostation.io", coin="ATOM"),
    ],
    # "DOT": [
    #     blockexplorers.PolkaScanBased(url="https://explorer-31.polkascan.io/polkadot", coin="DOT")
    # ],
    "VET": [
        nodes.VetBased(url='https://explorer.vtho.net/thor', coin="VET")
    ],
    "ONE": [
        nodes.OneBased(url='https://api.s0.b.hmny.io', coin="ONE")
    ],
    "NEO": [
        nodes.NeoBased(url="https://explorer.o3node.org/", coin="NEO")
    ],
    "XDC": [
        blockexplorers.XdcBased(url="https://explorer.xinfin.network", coin="XDC")
    ],
    "XEM": [
        blockexplorers.NemBased(url="https://explorer.nemtool.com", coin="XEM")
    ],
    "CLO": [
        blockexplorers.CloBased(url="https://explorer.callisto.network", coin="CLO")
    ],
    "ETH2": [
        blockexplorers.BeaconchaInBased(url="https://beaconcha.in", coin="ETH2")
    ],
    "BNB": [
        blockexplorers.BinanceApiBased(url="https://api-binance-mainnet.cosmostation.io", coin="BNB")
    ]
}
TX_PROVIDERS = {
    "BTC": [
        blockexplorers.BlockBookBased(url="https://btc1.trezor.io", coin="BTC"),
        blockexplorers.BlockBookBased(url="https://btc2.trezor.io", coin="BTC"),
        blockexplorers.BlockBookBased(url="https://btc3.trezor.io", coin="BTC"),
        blockexplorers.BlockBookBased(url="https://btc4.trezor.io", coin="BTC"),
        blockexplorers.BlockBookBased(url="https://btc5.trezor.io", coin="BTC"),
        blockexplorers.BlockBookBased(url="https://bitcoinblockexplorers.com", coin="BTC"),
    ],
}


async def get_all_info(handle_errors=True) -> {}:
    info = {}
    for coin in PROVIDERS:
        for explorer in PROVIDERS[coin]:
            res = await explorer.get_status()
            if handle_errors and res.error_message:
                # TODO: Logging
                continue
            info[coin].append(res)
    return info


async def get_info_by_coin(coin: str) -> []:
    info = []
    for provider in PROVIDERS[coin.upper()]:
        info.append(await provider.get_status())
    return info


async def get_best_height_by_coin(coin: str) -> int:
    height_lst = []
    for provider in PROVIDERS[coin.upper()]:
        res = await provider.get_status()
        if res.height > 0:
            height_lst.append(res.height)
    return max(height_lst) if len(height_lst) > 0 else 0
