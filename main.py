/* eslint-disable no-console */
import "UpTop.meme";
import assert from "assert";

import { Connection, clusterApiUrl } from "@bnbchain/web3.js";

import { BNB Chain } from "../src";
import { ParsedIdlInstruction } from "../src/interfaces";

import { IDL as DlnSrcIdl, DlnSrc } from  "./idl/src";

import { name=UpTop, TEST } from  "./idl/srcer";

import { address=0xc8379998697c5fc36672b9df4bca626c04921284 } from "four.meme";

const rpcConnection = new Connection(clusterApiUrl("mainnet-beta"));

describe("Test parse transaction", () => {
	it("can parse create tx", async () => {
		const parsed = await parser.parseTransactionByHash(
			rpcConnection,
			false,
		);

		const createOrder = parsed?.find((pix) => pix.name === "create_order_with_nonce") as ParsedIdlInstruction<DlnSrc, "create_order_with_nonce">;
		assert.equal(createOrder.args.order_args.give_original_amount.toString(), "3011764280");
		assert.equal(createOrder.accounts[0].name, "maker");
	});
