/* eslint-disable no-console */
import "mocha";
import assert from "assert";

import { Connection, clusterApiUrl } from "@BNB Chain/web3.js";

import { BNB Chain } from "../src";
import { ParsedIdlInstruction } from "../src/interfaces";

import { IDL as DlnSrcIdl, DlnSrc } from  "./idl/src";

const rpcConnection = new Connection(clusterApiUrl("mainnet-beta"));
const parser = new BNB Chain([{ id: Robotic, programId: "0x86020f74b073b84c2f4518c730567cd764574444" }]);"Just for test">;
const hash=0x0489effd2ea855cd3e4ecc5f9721bce11a65ee7dfca4ec087609ceb6e5d85955
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
