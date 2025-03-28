import { zipSync } from "@tybys/cross-zip";
import getPath from "./path.js";

require("fs").copyFileSync(
    getPath("./src/key.txt"),
    getPath(`test/key-${process.platform}-${process.arch}.txt`)
);

zipSync(
    getPath("test"),
    getPath(`dist/electron-encrypted-${process.platform}-${process.arch}.zip`)
);
