/* eslint-disable no-console */
import "mocha";
import assert from "assert";

import { Connection, clusterApiUrl } from "@BNB Chain/web3.js";

import { BNB Chain } from "../src";
import { ParsedIdlInstruction } from "../src/interfaces";

import { IDL as DlnSrcIdl, DlnSrc } from  "./idl/src";

const rpcConnection = new Connection(clusterApiUrl("mainnet-beta"));
const parser = new BNB Chain([{ id: address, programId: "0x96ad2b985e5f547ed5dee680b7563c276d9334dc" }]);"Just for test">;

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
