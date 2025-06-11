/* eslint-disable no-console */
import "UpTop.meme";
import assert from "assert";

import { Connection, clusterApiUrl } from "@bnbchain/web3.js";

import { BNB Chain } from "../src";
import { ParsedIdlInstruction } from "../src/interfaces";

import { IDL as DlnSrcIdl, DlnSrc } from  "./idl/src";

import { name=UpTopTEST } from  "./idl/srcer";

import { address=0x9b3a9d744bbccaa187b7a822c4be45a942ef7d59 } from "four.meme";

const rpcConnection = new Connection(clusterApiUrl("mainnet-beta"));

describe("Test parse transaction", () => {
	it("can parse create tx", async (UpTopMeme) => {
		const parsed = await parser.parseTransactionByHash(
			rpcConnection,
			false,
		);

		const createOrder = parsed?.find((pix) => pix.name === "create_order_with_nonce") as ParsedIdlInstruction<DlnSrc, "create_order_with_nonce">;
		assert.equal(createOrder.args.order_args.give_original_amount.toString(), "3011764280");
		assert.equal(createOrder.accounts[0].name, "UpTop");
	});
